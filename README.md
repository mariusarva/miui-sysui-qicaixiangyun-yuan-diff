# 七彩祥云_圆 · MIUI 系统界面组件改包审计

> MIUI 系统界面组件（`miui.systemui.plugin`，版本 18.3.2.57.0）原版与「七彩祥云_圆」改包的全量差异分析。
> 结论全部来自 apktool 3.0.3 解码态 + 方法级归一化 diff + 资源集合对比，`scripts/` 可一键复现。

## 0. 对象

| 项 | 原版 | 改版 |
|---|---|---|
| 文件 | `系统界面组件_18.3.2.57.0_anti.apk` | `七彩祥云_圆.apk` |
| 大小 | 25,620,643 B | 29,627,322 B（+15.6%） |
| MD5 | `d2b3c19222952f34f62c207313522df5` | `85a361a6709815b3aa902f46eb9a149f` |
| SHA-256 | `b8698eac10f1cf2f760a94588879ae23664087f1e2504f65163eee66d3224538` | `e690ee47e22a9c73bb39a881dc865220e1b6967de938bf9c7697beae446e3ab1` |
| dex | `classes.dex` + `classes2.dex` | 多一个 **`classes3.dex`**（437 类） |
| 类总数 | 14,398 | 14,924 |
| AndroidManifest.xml | — | **字节级无改动** |
| 签名 | `META-INF/CERT.RSA` / `CERT.SF` / `MANIFEST.MF` | 三件套大小与 CRC 完全一致，证书 SHA-256 相同 → **未重签** |

> 注：改版 dex 已变而 `META-INF` 三件套未变，说明该包不走 V1 摘要校验（或运行环境已放行），这是系统界面组件改包的常见处理；实际加载以装机验证为准。

> 两份 APK 本体随仓库提供：[原版 `系统界面组件_18.3.2.57.0_anti.apk`](apk/系统界面组件_18.3.2.57.0_anti.apk) · [改版 `七彩祥云_圆.apk`](apk/七彩祥云_圆.apk)。

## 1. 结论速览

改包在保留原版全部功能与签名的基础上，做了 7 组改动：

1. **整套 iOS 风格控制中心 / 电源菜单**：`com.kashi.ios` 311 类 + `com.kashi.mpager` 21 类 + `miui.systemui.controlcenter.ModsCenter` 75 类，全部装入新增的 `classes3.dex`；`MiuiGlobalActionsDialog` 单类注入 155 个方法与 2072 条指令。
2. **控制中心分组磁贴 / 自由布局**：`CCGroupContainer`、`CCGroupPanel`、`CCTileButton`、`CCNewTileCardView`、`FreeLayout`、`LandscapeLayout`、`NewGridLayoutManager`、`ShapePreviewDrawable`、`VolumeSlim`、`MediaProgressView`。
3. **自定义 QS 磁贴体系**：`AllinOneButton` 41 类（2×2 快捷开关）+ `miui.systemui.quicksettings` 25 类（应用磁贴/调光/折叠/常亮/LSPosed/5G/电源/重启/护眼）+ `QSListController` 整套 `qsFold*` 折叠逻辑。
4. **音量 / 亮度面板玻璃圆角**：`brightness_panel_slider_radius` 24→90dp、`miui_volume_bg_radius` 18→30dp 等一批 dimens；`ModsCenter.KashiVolume.touch`、`VolumePanelViewController$KashiRelayout`、`RoundRectFrameLayout`（`KashiRR` 日志）注入。
5. **媒体 / MiPlay 面板重构**：`PlayingStatus`、`MiPlayVolumeBar`、`QSControlMiPlayDetailHeader`、`MiPlaySeekBar`、6 个 `*_big` 布局、`ios_music_pause/wave.json` Lottie 动画。
6. **大屏 / 横屏适配**：`values-land`、`values-sw340dp`、`values/layouts.xml` 布局别名。
7. **视觉资源换皮**：51 个 drawable 重绘（滑块图标 pathData 胶囊化 + `fillAlpha` 1.0→0.65）、iOS 蓝 `#32ade6`、QS 卡片背景改透明、媒体进度条着色器改粉紫光晕、旋转动画幅度 180°→0°。

## 2. 规模数据

| 层 | 指标 | 数值 |
|---|---|---|
| ZIP | 条目 | 3,776 → 3,849 |
| ZIP | 新增 / 删除 / 内容变化 | 75 / 2 / 75 |
| 代码 | 新增类 / 删除类 | **527** / 1（dex 间迁移，非功能删除） |
| 代码 | 内容不同类 / 归一化后真实改动 | 202 / **69** |
| 代码 | 新增方法 / 删除方法 / 改动方法 | 188 / 2 / 177 |
| 代码 | 新增字段 / 删除字段 | 31 / 12 |
| 资源 | res 新增 / 删除 / 修改 | 72 / 3 / 79 |
| 资源 | values 新增键 / 删除键 / 值变化 | 57 / 1 / 54 |

## 3. 新增 527 类的分布

| 位置 | 包 | 类数 | 用途 |
|---|---|---|---|
| `classes3.dex` | `com.kashi.ios` | 311 | iOS 风格控制中心/电源菜单/媒体页/音量页/装饰 |
| `classes3.dex` | `com.kashi.mpager` | 21 | 媒体分页器（`KashiMediaPager`、`KashiLocalSession`） |
| `classes3.dex` | `miui.systemui.controlcenter.ModsCenter` | 75 | 分组磁贴、自由布局、音量细条、媒体进度 |
| `classes3.dex` | `miui.systemui.controlcenter.xd` | 12 | 纹理磁贴、咖啡因磁贴（`KashiTexture`） |
| `classes3.dex` | `miui.systemui.controlcenter.panel` | 4 | 面板适配 |
| `classes3.dex` | `miui.systemui.quicksettings` | 6 | 磁贴入口/ID |
| `classes3.dex` | `com.android.systemui.miui.globalactions` | 8 | `KashiIosPowerH` / `KashiIosPowerLink` 桥接 |
| `classes2.dex` | `AllinOneButton` | 41 | 2×2 快捷开关（飞行/蓝牙/数据/手电/定位/热点/互传/静音/NFC/勿扰/旋转/WiFi） |
| `classes2.dex` | `miui.systemui.quicksettings` | 25 | 应用磁贴、调光、折叠、常亮、LSPosed、5G、电源、重启、护眼 |
| `classes2.dex` | 控制中心编辑/折叠 | 8 | `CardTileConfigHelper`、`EditButtonController$*`、`EditButtonHeaderEntry`、`PowerHeaderEntry` |
| `classes.dex` | `android.widget` | 6 | `NAImageViewOnClickApp`、`PlayingStatus`、`PowerMenu` |
| `classes.dex` | `bg.mods.plugin.5GSwitch` | 5 | 5G 开关磁贴插件 |
| `classes.dex` | `miui.systemui` / `com.android.systemui` | 5 | `QsFoldNoOp`、`QsFoldRefresh`、`MiPlayKeyMargin`、`KashiRelayout`、灵动岛内部类 |

## 4. 改动最重的类

| 类 | +方法 | ~方法 | +指令 | 要点 |
|---|---|---|---|---|
| `MiuiGlobalActionsDialog` | 155 | 48 | 2072 | iOS 电源菜单：`KashiIosPowerLink.attach(SliderView)`、滑动重启/关机/Recovery/Fastboot/静音/重启系统界面 |
| `QSListController` | 22 | 8 | 56 | 整套 `qsFold*` 折叠：`qsFoldTarget="fold_tile"`、`Settings.System:qs_fold_collapsed` |
| `LocalMiuiQSTilePlugin` | 0 | 4 | 43 | 注册 `AppTiles`、`DimTile`、`LsposedTile`、`KeepScreenTile`、`SunTile` 等 |
| `MainPanelAdapter` | 0 | 1 | 36 | `distributeContent` → `qsFoldSyncOrientation` |
| `BrightnessPanelSliderDelegate` | 0 | 7 | 27 | `applyMaterialBackground` → `MiBackgroundStyle` 玻璃材质 |
| `EditButtonController` | 2 | 5 | 28 | 编辑面板、卡片长按菜单、重启入口 |
| `MediaPanelDelegate` | 0 | 4 | 26 | 媒体面板接入 |
| `BrightnessPanelTilesDelegate` | 0 | 4 | 23 | 亮度面板磁贴 |
| `QSTileItemIconView` | 0 | 3 | 24 | 磁贴图标着色（sun/dim/keep_screen 等） |
| `QSCardItemIconView` | 0 | 1 | 20 | 卡片图标着色 |
| `TimerItem` | 0 | 1 | 19 | 音量定时器玻璃背景（`getDEFAULT_GLASS_TOKEN` + `GradientDrawable(0x52808080)`） |
| `CompactQSListController` | 0 | 6 | 13 | 紧凑列表同步折叠 |
| `SecondaryPanelRouter` | 0 | 6 | 12 | 二级面板路由 |
| `BrightnessPanelAnimator` | 0 | 1 | 17 | 亮度面板颜色合成 |
| `QSControlMiPlayDetailHeader` | 0 | 3 | 14 | MiPlay 头部 |
| `VolumeColumn` | 0 | 3 | 13 | 音量列颜色过渡 |
| `QSControlMiPlayDetailContent` | 0 | 2 | 12 | MiPlay 内容页 |

完整 69 个真实改动类见 [`docs/01-代码层.md`](docs/01-代码层.md)。

## 5. 资源关键值

### 5.1 圆角 / 尺寸（`values/dimens.xml`）

| 资源 | 原版 | 改版 |
|---|---|---|
| `brightness_panel_slider_radius` | 24dp | **90dp** |
| `brightness_panel_slider_height_large/small` | 195 / 176dp | **300dp** |
| `brightness_panel_slider_width_large/small` | 88.81 / 80.15dp | **110dp** |
| `brightness_panel_slider_icon_size_large/small` | 34.78 / 31.39dp | **60dp** |
| `brightness_panel_slider_icon_margin_bottom_*` | 21.12 / 19.06dp | **350dp** |
| `brightness_panel_toggle_slider_margin_top_large` | 44dp | 134dp |
| `control_center_brightness_volume_panel_content_height_vertical` | 403dp | **600dp** |
| `control_center_detail_max_height` | 500dp | 575dp |
| `miui_volume_bg_radius` | 18dp | **30dp** |
| `miui_volume_timer_corner_radius` | 20dp | 30dp |
| `miui_volume_countdown_radius` | 20.5dp | 30.5dp |
| `o3_miui_volume_radius` | 20dp | 30dp |
| `island_icon_radius` | 4.56dp | **90dp** |
| `big_island_min_width` | 108dp | 138dp |
| `mask_size` / `mask_size_big` | 72 / 84dp | 64dp |
| `media_player_cover_radius` | 10dp | 15dp |
| `slider_height` / `slider_width` | 338 / 84dp | 290 / 70dp |
| `slider_border_width` | 1.2dp | 1.5dp |

### 5.2 大屏覆盖（`values-sw340dp/dimens.xml`）

| 资源 | 原版 | 改版 |
|---|---|---|
| `control_center_universal_corner_radius` | 24dp | 48dp |
| `detail_panel_background_corner_radius` | 36dp | 50dp |
| `media_player_cover_size` | 42dp | 55dp |
| `qs_tile_item_icon_bitmap_size` | 30dp | 38dp |
| `qs_tile_item_icon_inner_size` | 34dp | 38dp |
| `toggle_slider_icon_size` | 34dp | 38dp |
| `slider_margin_end` | 160dp | 120dp |

### 5.3 颜色

| 资源 | 原版 | 改版 | 说明 |
|---|---|---|---|
| `qs_icon_enabled_color` | `#3482ff` | **`#32ade6`** | iOS 系统蓝 |
| `toggle_slider_volume_icon_color` | `#3482ff` | `#32ade6` | 同上 |
| `qs_paper_mode_icon_enabled_color` | `#ff9f05` | `#1dcd3a` | 护眼绿 |
| `miplay_recycler_view_thumb_color` | `#26ffffff` | `#00000000` | 缩略图底透明 |
| `values-night/…thumb_color` | `#298c93b0` | `#00000000` | 夜间同样透明 |

### 5.4 默认磁贴排列（`values/arrays.xml`）

| 数组 | 原版 | 改版 |
|---|---|---|
| `compact_tiles` | bt, airplane, mute, flashlight | **rotation, screenrecordertile** |
| `card_style_tiles_mobile` | wifi, cell | airplane, cell, vowifi1, vowifi1 |

### 5.5 新增文案（8 条）

`kashi_ios_pw_off` 滑动关机 · `kashi_ios_pw_restart` 滑动重启 · `kashi_ios_pw_recovery` 滑动进入 Recovery · `kashi_ios_pw_fastboot` 滑动进入 Fastboot · `kashi_ios_pw_sysui` 滑动重启系统界面 · `kashi_ios_pw_mute` 滑动静音 · `kashi_ios_pw_unmute` 滑动取消静音 · `mcool_new_tiles_section` 新增磁贴区

## 6. 布局改动

| 布局 | 改动 |
|---|---|
| `device_controls_entry.xml` | 容器改 157×157dp；新增 4 个 `AllinOneButton`（飞行/数据/WiFi/蓝牙，各 56dp）；原 `entry_icon`、`entry_title` 改 `invisible` |
| `main_panel_customize_header.xml` | 新增 `android.widget.NAImageViewOnClickApp`（`reboot` 图标，`nabilaba_toapp="com.systemui.restart"`）与 `android.widget.PowerMenu`（`power_menu` 图标，`stateListAnimator=power_press`） |
| `qs_customize_button.xml` | 新增 `QuietButton` / `NfcButton` / `MuteButton`（各 40dp）；原文字按钮改为 157×68dp 空文本 |
| `security_footer.xml` | 整条高度 0、margin 0；新增 4 个 `alpha=0` 装饰图标（heart / music / network / mainpage） |
| `miplay_entrance_view.xml` | `ControlCenterMiPlayView` → `QSControlMiPlayDetailHeader` + `MiPlayVolumeBar` + `PlayingStatus` + `UnPressableRelativeLayout` |
| `miplay_view.xml` | `MiPlayView` → `CardView` + `ConstraintLayout` + `MarqueeTextView` + `MediaTimeTextView` + `MiPlaySeekBar` |
| `media_player_view.xml` | 新增 `ImageView` |
| `qs_control_detail_*` | SeekBar 高度、`progressBarMode=high`、margin 调整 |
| 新增 6 个 `*_big.xml` | MiPlay 横屏/大屏布局（`miplay_detail_device_item_land_big`、`qs_control_detail_miplay_*_big` 等） |

## 7. 资源文件

- **新增 72**：22 个 `ic_qs_*` / 电源菜单矢量（`ic_airplane_on/off`、`ic_bootloader`、`ic_recovery`、`ic_mask_*`、`ic_qs_5g_tile`、`ic_qs_perf_on/off`、`ic_qs_power_tile`、`ic_qs_restart_tile`、`ic_qs_saver_on/off`、`ic_qs_sun_tile` 等）+ 42 个 `blackscreen/*.xml` 状态矢量（开关 on/off/semi、`background_on_*`、`power`/`power_menu`/`power_press`/`reboot`、装饰 `heart`/`music`/`network`/`mainpage`/`dots`/`edit_add`）+ 2 个 `$ic_media_*` + 6 个 `_big` 布局 + 2 个 Lottie（`ios_music_pause.json`、`ios_music_wave.json`）。
- **删除 3**：`ic_device_center_item_background_default.xml`（被同名 `.png` 取代）、`ic_reboot_small.xml`、`ic_shutdown_small.xml`。
- **修改 79**：drawable 51、layout 13、values 7、drawable-anydpi 2、animator 1、raw 1、values-land 1、values-night 1。
- 51 个 drawable 里最典型的是滑块动画图标：`pathData` 由多段贝塞尔重写为圆角胶囊（`M…L…C…Z`），`fillAlpha` 由 `1.0` 统一降到 `0.65`；`qs_background_enabled.xml` 的 `solid` 由 `?qsEnableColor` 改为 `#00000000`；`ic_qs_scanner.xml` 的 viewport 由 35 放大到 200 并整体重绘。
- 媒体进度条着色器 `raw/music_player_tracker.frag` 不是纯格式化：新增 `verticalScale` 参数、`glowRange` 1.5→3.0、进度主体改为粉紫色 `vec3(0.91, 0.71, 0.85)` 并与光晕 `alphaBlend`。
- `animator/sysui_anim_rotation_1step_560e.xml` 的 `valueTo` 由 `180` 改为 `0`（旋转动画幅度归零）。
- `apktool.yml` 的 `doNotCompress` 新增 7 个 `ic_qs_*`（perf/power/restart/restartlauncher/saver 系列）。

## 8. 噪声与判定口径

- **202 个「内容不同」类里 133 个是重编译噪声**，归一化（去 `nop`/`.source`/`.line`/`.registers`、寄存器重编号、标签重命名、`const-string/jumbo`、字段静态初值）后只剩 69 个真实改动。
- `values/arrays.xml` 里的 `#ffXXXXXX → #XXXXXX` 是 apktool 对 8 位颜色的格式化，不是改色；已按颜色 token 归一剔除。
- `public.xml` 的 ID 后移是新增资源后的正常位移，不是逻辑改动。
- 删除的 `DynamicIslandAnimationDelegate$…$1` 实际是从 `classes2.dex` 迁到 `classes.dex`（同名文件两处一增一删），不是功能删除。
- `androidx` / `miuix` / `kotlin` 等第三方库类的 ±1 指令差异全部判为噪声。

## 9. 复现

```bash
# 依赖：apktool 3.0.3、python3
export APK_ORIG="/path/系统界面组件_18.3.2.57.0_anti.apk"
export APK_MOD="/path/七彩祥云_圆.apk"
bash scripts/run_diff.sh          # apktool 解码 + 类/资源清单
python3 scripts/analyze_methods.py  # 方法级归一化 diff → code_summary.md
python3 scripts/vals_compare.py     # 资源集合对比 → res_summary.md
python3 scripts/zipdiff.py "$APK_ORIG" "$APK_MOD"  # ZIP 条目级对比
```

脚本默认把工作目录放在自身所在目录的上一级，可用 `DIFF_BASE` 覆盖。

## 10. 文件结构

```
README.md                 本报告
apk/                      审计对象（原版 + 改版 APK）
docs/01-代码层.md          新增类分组、69 个真实改动类全表、方法/字段明细、注入热点
docs/02-资源层.md          values 值变化全表、新增键、res 文件清单、layout/drawable 明细
docs/03-复现与口径.md      脚本说明、噪声判定、验证清单
scripts/                  复现脚本（run_diff.sh / analyze_methods.py / vals_compare.py / zipdiff.py）
data/                     本次实测原始清单（new_classes / differ_classes / code_summary / res_summary / zip_layer / rdiff）
```

## 11. 免责

本仓库只做差异审计与复现记录，不包含原版或改版 APK 本体，也不提供任何安装方式。系统界面组件属系统分区应用，改动与安装风险自负。
