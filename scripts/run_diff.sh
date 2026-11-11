#!/bin/sh
# 全量对比入口：apktool 解码 + 类/资源清单
#
# 用法：
#   export APK_ORIG="/path/原版.apk"
#   export APK_MOD="/path/改版.apk"
#   bash scripts/run_diff.sh
#
# 工作目录默认是脚本所在目录的上一级，可用 DIFF_BASE 覆盖。
set -u
SELF_DIR=$(cd "$(dirname "$0")" && pwd)
W=${DIFF_BASE:-$(dirname "$SELF_DIR")}
ORIG=${APK_ORIG:?请设置 APK_ORIG}
MOD=${APK_MOD:?请设置 APK_MOD}

cd "$W" || exit 1
mkdir -p rdiff
export JAVA_OPTS="-Xmx3500m"

echo "[1/4] decode ORIG"
apktool d -f -o dec_orig "$ORIG" > apktool_orig.log 2>&1 || echo "WARN orig rc=$?"
echo "[2/4] decode MOD"
apktool d -f -o dec_mod "$MOD" > apktool_mod.log 2>&1 || echo "WARN mod rc=$?"

echo "[3/4] smali lists"
(cd dec_orig && find smali* -name '*.smali' | sort) > orig_smali.list
(cd dec_mod && find smali* -name '*.smali' | sort) > mod_smali.list
comm -13 orig_smali.list mod_smali.list > new_classes.txt
comm -23 orig_smali.list mod_smali.list > del_classes.txt
comm -12 orig_smali.list mod_smali.list | while read f; do
  cmp -s "dec_orig/$f" "dec_mod/$f" || echo "$f"
done > differ_classes.txt

echo "[4/4] res lists"
(cd dec_orig/res && find . -type f | sed 's|^\./||' | sort) > rdiff/orig.list
(cd dec_mod/res && find . -type f | sed 's|^\./||' | sort) > rdiff/mod.list
comm -13 rdiff/orig.list rdiff/mod.list > rdiff/res_new.txt
comm -23 rdiff/orig.list rdiff/mod.list > rdiff/res_del.txt
comm -12 rdiff/orig.list rdiff/mod.list | while read f; do
  cmp -s "dec_orig/res/$f" "dec_mod/res/$f" || echo "$f"
done > rdiff/res_mod.txt
diff -u dec_orig/AndroidManifest.xml dec_mod/AndroidManifest.xml > rdiff/manifest.diff || true
diff -u dec_orig/apktool.yml dec_mod/apktool.yml > rdiff/apktool_yml.diff || true

echo "DONE"
wc -l new_classes.txt del_classes.txt differ_classes.txt \
      rdiff/res_new.txt rdiff/res_del.txt rdiff/res_mod.txt
