#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
方法级归一化 smali diff（apktool 解码态）

剔除 dex 重编译噪声：nop / .source / .line / .registers / .locals /
寄存器重编号 / 标签重命名 / const-string-jumbo / 字段静态初值。
输出 code_summary.md：真实改动类、新增/删除/改动方法、新增字段、注入调用热点。

用法：先跑 run_diff.sh，再 python3 analyze_methods.py
"""
import os, re, collections

BASE = os.environ.get("DIFF_BASE") or os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ORIG = os.path.join(BASE, "dec_orig")
MOD = os.path.join(BASE, "dec_mod")

CALL = re.compile(r"invoke-[\w/]+.*?L([\w/$]+);->([\w$<>]+)")


def norm(s):
    s = s.strip()
    if not s or s == "nop":
        return ""
    if s.startswith((".source ", ".line ", ".prologue", ".registers", ".locals")):
        return ""
    if s.startswith(".field "):
        s = re.sub(r"\s*=\s*(null|false|true|0x0|-?\d+(\.\d+)?[a-zA-Z]*)$", "", s)
    s = s.replace("const-string/jumbo", "const-string")
    s = re.sub(r"\b[vp]\d+\b", "R", s)
    s = re.sub(r":[A-Za-z0-9_$-]+", ":L", s)
    return s


def parse(path):
    methods, fields, cur, body = {}, [], None, []
    with open(path, encoding="utf-8", errors="replace") as f:
        for line in f:
            s = line.strip()
            if s.startswith(".field "):
                n = norm(s)
                if n:
                    fields.append(n)
            if s.startswith(".method "):
                cur, body = s[8:].strip(), []
            elif s == ".end method":
                if cur is not None:
                    methods[cur] = body
                cur = None
            elif cur is not None:
                n = norm(s)
                if n:
                    body.append(n)
    return methods, fields


def lines(p):
    return [x.strip() for x in open(p, encoding="utf-8") if x.strip()]


def main():
    differ = lines(os.path.join(BASE, "differ_classes.txt"))
    newc = lines(os.path.join(BASE, "new_classes.txt"))
    delc = lines(os.path.join(BASE, "del_classes.txt"))
    new_m, del_m, chg_m, new_f, del_f, real = [], [], [], [], [], []
    hot_calls = collections.Counter()

    for c in differ:
        mo, fo = parse(os.path.join(ORIG, c))
        mm, fm = parse(os.path.join(MOD, c))
        add = sorted(set(mm) - set(mo))
        rm = sorted(set(mo) - set(mm))
        fo_s, fm_s = set(fo), set(fm)
        nf = sorted(fm_s - fo_s)
        df = sorted(fo_s - fm_s)
        chg = []
        for k in sorted(set(mo) & set(mm)):
            if mo[k] != mm[k]:
                added = [x for x in mm[k] if x not in mo[k]]
                chg.append((k, len(added), added))
                for x in added:
                    m = CALL.search(x)
                    if m:
                        hot_calls[m.group(1) + "->" + m.group(2)] += 1
        for k in add:
            new_m.append((c, k))
        for k in rm:
            del_m.append((c, k))
        for item in chg:
            chg_m.append((c,) + item)
        for f in nf:
            new_f.append((c, f))
        for f in df:
            del_f.append((c, f))
        if add or rm or chg or nf or df:
            real.append((c, len(add), len(rm), len(chg), len(nf), len(df),
                         sum(x[1] for x in chg)))

    groups = collections.Counter()
    for c in newc:
        parts = c.split("/")
        key = "/".join(parts[:2]) if len(parts) > 2 else parts[0]
        groups[key] += 1

    out = os.path.join(BASE, "code_summary.md")
    with open(out, "w", encoding="utf-8") as w:
        w.write("# smali 方法级归一化差异\n\n")
        w.write("| 项 | 数量 |\n|---|---|\n")
        w.write("| 内容不同的类 | %d |\n" % len(differ))
        w.write("| 归一化后仍有真实改动 | %d |\n" % len(real))
        w.write("| 新增类 | %d |\n| 删除类 | %d |\n" % (len(newc), len(delc)))
        w.write("| 新增方法 | %d |\n| 删除方法 | %d |\n| 改动方法 | %d |\n" %
                (len(new_m), len(del_m), len(chg_m)))
        w.write("| 新增字段 | %d |\n| 删除字段 | %d |\n\n" % (len(new_f), len(del_f)))

        w.write("## 真实改动类（按改动量排序）\n\n")
        w.write("| 类 | +方法 | -方法 | ~方法 | +字段 | -字段 | +指令 |\n|---|---|---|---|---|---|---|\n")
        for r in sorted(real, key=lambda x: -(x[3] + x[6])):
            w.write("| `%s` | %d | %d | %d | %d | %d | %d |\n" % r)

        w.write("\n## 新增类分组\n\n| 顶层包 | 数量 |\n|---|---|\n")
        for k, v in groups.most_common():
            w.write("| `%s` | %d |\n" % (k, v))

        w.write("\n## 注入调用热点（改动方法里新增的 invoke）\n\n| 调用 | 次数 |\n|---|---|\n")
        for k, v in hot_calls.most_common(40):
            w.write("| `%s` | %d |\n" % (k, v))

        w.write("\n## 新增方法明细\n\n")
        for c, k in new_m:
            w.write("- `%s` :: `%s`\n" % (c, k))
        w.write("\n## 删除方法明细\n\n")
        for c, k in del_m:
            w.write("- `%s` :: `%s`\n" % (c, k))
        w.write("\n## 新增字段明细\n\n")
        for c, f in new_f:
            w.write("- `%s` :: `%s`\n" % (c, f))
        w.write("\n## 改动方法明细（按新增指令数）\n\n")
        for c, k, n, a in sorted(chg_m, key=lambda x: -x[2]):
            w.write("### `%s` :: `%s` (+%d)\n\n" % (c, k, n))
            for x in a[:8]:
                w.write("    `%s`\n" % x)
            w.write("\n")
        w.write("\n## 新增类清单\n\n")
        for c in newc:
            w.write("- `%s`\n" % c)

    print("wrote", out)
    print("differ=%d real=%d new=%d del=%d +m=%d -m=%d ~m=%d +f=%d -f=%d" %
          (len(differ), len(real), len(newc), len(delc), len(new_m),
           len(del_m), len(chg_m), len(new_f), len(del_f)))
    print("top groups:", groups.most_common(12))
    print("top calls:", hot_calls.most_common(15))


if __name__ == "__main__":
    main()
