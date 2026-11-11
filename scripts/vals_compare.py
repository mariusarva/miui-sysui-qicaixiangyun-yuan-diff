#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
apktool 解码态资源集合对比。

values*/*.xml 用 (type,name)->value 映射比较，规避 apktool XML 顺序噪声；
颜色做 6/8 位归一化、尺寸做 24.0dp==24dp 归一化；
非 values 资源（layout / drawable / animator）按集合统计并抽取自定义 View 标签变化。
输出 res_summary.md。

用法：先跑 run_diff.sh，再 python3 vals_compare.py
"""
import os, re, collections

BASE = os.environ.get("DIFF_BASE") or os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RO = os.path.join(BASE, "dec_orig", "res")
RM = os.path.join(BASE, "dec_mod", "res")

TAG = re.compile(
    r'<(dimen|color|string|integer|bool|item|id|fraction|drawable|attr|style|'
    r'string-array|integer-array|array|plurals)\s+name="([^"]+)"([^>]*?)(?:>(.*?)</\1>|/>)',
    re.S)
VIEW = re.compile(r'<([A-Za-z_][\w.$]*)\s')


def colnorm(v):
    v = v.strip()
    m = re.fullmatch(r"#([0-9a-fA-F]{6})", v)
    if m:
        return "#" + m.group(1).lower()
    m = re.fullmatch(r"#ff([0-9a-fA-F]{6})", v, re.I)
    if m:
        return "#" + m.group(1).lower()
    # 复合值（array 等）：apktool 把 #ffRRGGBB 格式化成 #RRGGBB，属噪声
    v = re.sub(r"#ff([0-9a-fA-F]{6})", r"#\1", v, flags=re.I)
    v = re.sub(r"\s+", " ", v).strip()
    return v


def numnorm(v):
    v = v.strip()
    m = re.fullmatch(r"(-?\d+)\.0+(dp|sp|px|dip|in|mm|pt|%)", v)
    return (m.group(1) + m.group(2)) if m else v


def parse(p):
    d = {}
    try:
        txt = open(p, encoding="utf-8", errors="replace").read()
    except OSError:
        return d
    for m in TAG.finditer(txt):
        typ, name, inner = m.group(1), m.group(2), m.group(4) or ""
        val = re.sub(r"<[^>]+>", " ", inner).strip()
        d[(typ, name)] = val
    return d


def walk(root):
    out = {}
    for dp, dn, fn in os.walk(root):
        for f in fn:
            rel = os.path.relpath(os.path.join(dp, f), root)
            if rel.startswith("values") and f.endswith(".xml"):
                out[rel] = parse(os.path.join(root, rel))
    return out


def txt_lines(p):
    try:
        return [x.strip() for x in open(os.path.join(BASE, p), encoding="utf-8") if x.strip()]
    except OSError:
        return []


def views(rel, root):
    try:
        t = open(os.path.join(root, rel), encoding="utf-8", errors="replace").read()
    except OSError:
        return set()
    return set(m.group(1) for m in VIEW.finditer(t))


def main():
    a, b = walk(RO), walk(RM)
    files = sorted(set(a) | set(b))
    total_add = total_del = total_chg = 0
    rows = []
    for rel in files:
        A, B = a.get(rel, {}), b.get(rel, {})
        added = {k: v for k, v in B.items() if k not in A}
        removed = {k: v for k, v in A.items() if k not in B}
        changed = {k: (A[k], B[k]) for k in set(A) & set(B)
                   if colnorm(numnorm(A[k])) != colnorm(numnorm(B[k]))}
        total_add += len(added)
        total_del += len(removed)
        total_chg += len(changed)
        if added or removed or changed:
            rows.append((rel, len(A), len(B), added, removed, changed))

    res_new = txt_lines("rdiff/res_new.txt")
    res_del = txt_lines("rdiff/res_del.txt")
    res_mod = txt_lines("rdiff/res_mod.txt")

    def group(lst):
        return collections.Counter(x.split("/")[0] for x in lst)

    out = os.path.join(BASE, "res_summary.md")
    with open(out, "w", encoding="utf-8") as w:
        w.write("# 资源层差异（集合对比）\n\n")
        w.write("| 项 | 数量 |\n|---|---|\n")
        w.write("| values 文件 | %d |\n" % len(files))
        w.write("| 新增资源键 | %d |\n| 删除资源键 | %d |\n| 值变化键 | %d |\n" %
                (total_add, total_del, total_chg))
        w.write("| res 新增文件 | %d |\n| res 删除文件 | %d |\n| res 修改文件 | %d |\n\n" %
                (len(res_new), len(res_del), len(res_mod)))

        w.write("## 非 values 资源按目录\n\n")
        w.write("| 目录 | 新增 | 删除 | 修改 |\n|---|---|---|---|\n")
        gn, gd, gm = group(res_new), group(res_del), group(res_mod)
        for k in sorted(set(gn) | set(gd) | set(gm)):
            w.write("| `%s` | %d | %d | %d |\n" % (k, gn[k], gd[k], gm[k]))

        w.write("\n## values 值变化明细（归一化后）\n\n")
        w.write("| 文件 | 类型 | 名称 | 原版 | 改版 |\n|---|---|---|---|---|\n")
        for rel, na, nb, added, removed, changed in rows:
            for (typ, name), (va, vb) in sorted(changed.items()):
                w.write("| `%s` | %s | `%s` | `%s` | `%s` |\n" %
                        (rel, typ, name, va[:60], vb[:60]))

        w.write("\n## values 新增键（按类型统计）\n\n")
        ca = collections.Counter()
        for rel, na, nb, added, removed, changed in rows:
            for (typ, name) in added:
                ca[typ] += 1
        w.write("| 类型 | 数量 |\n|---|---|\n")
        for k, v in ca.most_common():
            w.write("| %s | %d |\n" % (k, v))
        w.write("\n<details><summary>新增键明细</summary>\n\n")
        for rel, na, nb, added, removed, changed in rows:
            if added:
                w.write("\n**`%s`**\n\n" % rel)
                for (typ, name), v in sorted(added.items()):
                    w.write("- %s `%s` = `%s`\n" % (typ, name, v[:60]))
        w.write("\n</details>\n")

        w.write("\n## values 删除键\n\n")
        for rel, na, nb, added, removed, changed in rows:
            for (typ, name), v in sorted(removed.items()):
                w.write("- `%s` %s `%s` = `%s`\n" % (rel, typ, name, v[:60]))

        w.write("\n## layout 改动里的自定义 View 标签变化\n\n")
        for rel in res_mod:
            if rel.startswith("layout") and rel.endswith(".xml"):
                va, vb = views(rel, RO), views(rel, RM)
                add, rm = sorted(vb - va), sorted(va - vb)
                if add or rm:
                    w.write("- `%s`\n" % rel)
                    for x in add:
                        w.write("    + `%s`\n" % x)
                    for x in rm:
                        w.write("    - `%s`\n" % x)

        w.write("\n## res 新增文件清单\n\n")
        for x in res_new:
            w.write("- `%s`\n" % x)
        w.write("\n## res 删除文件清单\n\n")
        for x in res_del:
            w.write("- `%s`\n" % x)
        w.write("\n## res 修改文件清单\n\n")
        for x in res_mod:
            w.write("- `%s`\n" % x)

    print("wrote", out)
    print("values files=%d +%d -%d ~%d ; res +%d -%d ~%d" %
          (len(files), total_add, total_del, total_chg,
           len(res_new), len(res_del), len(res_mod)))
    print("res groups:", dict(group(res_mod).most_common(8)))


if __name__ == "__main__":
    main()
