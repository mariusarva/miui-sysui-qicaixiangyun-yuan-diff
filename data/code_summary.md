# smali 方法级归一化差异

| 项 | 数量 |
|---|---|
| 内容不同的类 | 202 |
| 归一化后仍有真实改动 | 69 |
| 新增类 | 527 |
| 删除类 | 1 |
| 新增方法 | 188 |
| 删除方法 | 2 |
| 改动方法 | 177 |
| 新增字段 | 31 |
| 删除字段 | 12 |

## 真实改动类（按改动量排序）

| 类 | +方法 | -方法 | ~方法 | +字段 | -字段 | +指令 |
|---|---|---|---|---|---|---|
| `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` | 155 | 0 | 48 | 6 | 5 | 2072 |
| `smali_classes2/miui/systemui/controlcenter/panel/main/qs/QSListController.smali` | 22 | 0 | 8 | 13 | 1 | 56 |
| `smali_classes2/miui/systemui/quicksettings/LocalMiuiQSTilePlugin.smali` | 0 | 0 | 4 | 0 | 0 | 43 |
| `smali_classes2/miui/systemui/controlcenter/panel/main/recyclerview/MainPanelAdapter.smali` | 0 | 0 | 1 | 0 | 0 | 36 |
| `smali_classes2/miui/systemui/controlcenter/panel/secondary/brightness/BrightnessPanelSliderDelegate.smali` | 0 | 0 | 7 | 0 | 0 | 27 |
| `smali_classes2/miui/systemui/controlcenter/panel/main/qs/EditButtonController.smali` | 2 | 0 | 5 | 3 | 1 | 28 |
| `smali_classes2/miui/systemui/controlcenter/panel/secondary/media/MediaPanelDelegate.smali` | 0 | 0 | 4 | 0 | 0 | 26 |
| `smali_classes2/miui/systemui/controlcenter/panel/secondary/brightness/BrightnessPanelTilesDelegate.smali` | 0 | 1 | 4 | 0 | 0 | 23 |
| `smali_classes2/miui/systemui/controlcenter/qs/tileview/QSTileItemIconView.smali` | 0 | 0 | 3 | 1 | 0 | 24 |
| `smali_classes2/miui/systemui/controlcenter/qs/tileview/QSCardItemIconView.smali` | 0 | 0 | 1 | 0 | 0 | 20 |
| `smali/com/android/systemui/miui/volume/TimerItem.smali` | 0 | 0 | 1 | 0 | 0 | 19 |
| `smali_classes2/miui/systemui/controlcenter/panel/main/qs/CompactQSListController.smali` | 0 | 0 | 6 | 0 | 0 | 13 |
| `smali_classes2/miui/systemui/controlcenter/panel/SecondaryPanelRouter.smali` | 0 | 0 | 6 | 0 | 0 | 12 |
| `smali_classes2/miui/systemui/controlcenter/panel/secondary/brightness/BrightnessPanelAnimator.smali` | 0 | 0 | 1 | 0 | 0 | 17 |
| `smali/com/android/systemui/QSControlMiPlayDetailHeader.smali` | 0 | 0 | 3 | 0 | 0 | 14 |
| `smali/com/android/systemui/miui/volume/VolumeColumn.smali` | 0 | 0 | 3 | 0 | 0 | 13 |
| `smali/com/android/systemui/QSControlMiPlayDetailContent.smali` | 0 | 0 | 2 | 0 | 0 | 12 |
| `smali_classes2/miui/systemui/controlcenter/panel/main/devicecontrol/DeviceControlsEntryController.smali` | 0 | 0 | 5 | 0 | 0 | 8 |
| `smali_classes2/miui/systemui/controlcenter/panel/secondary/detail/DetailPanelTilesDelegate.smali` | 0 | 0 | 1 | 0 | 0 | 12 |
| `smali/com/android/systemui/QSControlMiPlayDetailContent$Adapter2.smali` | 0 | 0 | 1 | 0 | 0 | 8 |
| `smali/com/android/systemui/miui/volume/VolumePanelViewController.smali` | 3 | 1 | 4 | 0 | 0 | 4 |
| `smali_classes2/miui/systemui/controlcenter/panel/secondary/detail/DetailPanelDelegate.smali` | 0 | 0 | 4 | 3 | 3 | 4 |
| `smali/com/android/systemui/miui/volume/MiuiVolumeDialogView.smali` | 0 | 0 | 1 | 0 | 0 | 6 |
| `smali_classes2/miui/systemui/controlcenter/qs/customize/TileQueryHelper.smali` | 0 | 0 | 1 | 0 | 0 | 6 |
| `smali_classes2/miui/systemui/controlcenter/utils/MiuiQSHostCompat.smali` | 0 | 0 | 1 | 0 | 0 | 6 |
| `smali/com/android/systemui/miui/volume/MiuiRingerModeLayout$RingerButtonHelper.smali` | 0 | 0 | 1 | 0 | 0 | 5 |
| `smali_classes2/miui/systemui/controlcenter/panel/main/MainPanelTouchController.smali` | 1 | 0 | 2 | 1 | 0 | 4 |
| `smali_classes2/miui/systemui/controlcenter/panel/main/qs/QSRecord$longClickAction$1.smali` | 0 | 0 | 1 | 0 | 0 | 5 |
| `smali_classes2/miui/systemui/controlcenter/qs/tileview/QSCardItemView.smali` | 0 | 0 | 2 | 0 | 0 | 4 |
| `smali_classes2/miui/systemui/util/MiuiColorBlendToken.smali` | 0 | 0 | 1 | 0 | 0 | 5 |
| `smali/com/android/systemui/QSControlMiPlayDetailContentSupportLand.smali` | 0 | 0 | 2 | 0 | 0 | 3 |
| `smali_classes2/miui/systemui/controlcenter/panel/main/MainPanelModeController.smali` | 0 | 0 | 1 | 0 | 0 | 4 |
| `smali_classes2/miui/systemui/controlcenter/panel/main/header/MainPanelHeaderController$expandCallback$1.smali` | 0 | 0 | 1 | 0 | 0 | 4 |
| `smali_classes2/miui/systemui/util/ThemeUtils.smali` | 0 | 0 | 3 | 0 | 0 | 2 |
| `smali_classes2/miui/systemui/controlcenter/panel/main/media/MediaPlayerController.smali` | 0 | 0 | 3 | 0 | 0 | 1 |
| `smali_classes2/miui/systemui/controlcenter/panel/main/qs/QSCardsController.smali` | 0 | 0 | 2 | 0 | 0 | 2 |
| `smali_classes2/miui/systemui/controlcenter/panel/main/volume/VolumeSliderController.smali` | 0 | 0 | 2 | 0 | 0 | 2 |
| `smali_classes2/miui/systemui/controlcenter/panel/secondary/volume/VolumePanelController.smali` | 2 | 0 | 1 | 0 | 0 | 3 |
| `smali_classes2/miui/systemui/controlcenter/panel/secondary/volume/VolumePanelDelegate.smali` | 0 | 0 | 2 | 0 | 0 | 2 |
| `smali_classes2/miui/systemui/controlcenter/qs/QSController$compactTileSpecs$2.smali` | 0 | 0 | 1 | 0 | 0 | 3 |
| `smali_classes2/miui/systemui/util/MiBackgroundStyle.smali` | 0 | 0 | 1 | 0 | 0 | 3 |
| `smali/com/android/systemui/MiPlayExtentionsKt.smali` | 0 | 0 | 2 | 0 | 0 | 1 |
| `smali/com/android/systemui/miplay/material/MiPlayMaterialTokensKt$devicesItemUnSelectedToken$2.smali` | 0 | 0 | 1 | 0 | 0 | 2 |
| `smali_classes2/miui/systemui/controlcenter/panel/main/security/SecurityFooterController.smali` | 0 | 0 | 2 | 0 | 0 | 1 |
| `smali_classes2/miui/systemui/controlcenter/qs/tileview/QSTileItemView.smali` | 0 | 0 | 1 | 1 | 0 | 2 |
| `smali_classes2/miui/systemui/flashlight/NotificationManager.smali` | 0 | 0 | 1 | 0 | 0 | 2 |
| `smali_classes2/miui/systemui/quicksettings/soundeffect/DolbyAtomsSoundEffectTile.smali` | 0 | 0 | 1 | 0 | 0 | 2 |
| `smali/com/android/systemui/QSControlMiPlayDetailHeader$addObservers$2.smali` | 0 | 0 | 1 | 0 | 0 | 1 |
| `smali/com/android/systemui/miui/volume/RoundRectFrameLayout.smali` | 1 | 0 | 1 | 0 | 0 | 1 |
| `smali/miui/systemui/controlcenter/material/ControlCenterMaterialTokens$editButtonToken$2.smali` | 0 | 0 | 1 | 0 | 0 | 1 |
| `smali_classes2/miui/systemui/controlcenter/panel/main/brightness/BrightnessSliderController.smali` | 0 | 0 | 1 | 0 | 0 | 1 |
| `smali_classes2/miui/systemui/controlcenter/panel/main/header/MessageHeaderController$Msg$showConfig$1.smali` | 0 | 0 | 1 | 0 | 0 | 1 |
| `smali_classes2/miui/systemui/controlcenter/panel/main/media/MediaPlayerController$MediaPlayerViewHolder.smali` | 0 | 0 | 1 | 0 | 0 | 1 |
| `smali_classes2/miui/systemui/controlcenter/qs/QSController.smali` | 0 | 0 | 1 | 1 | 0 | 1 |
| `smali_classes2/miui/systemui/devicecenter/DeviceCenterController.smali` | 0 | 0 | 1 | 0 | 0 | 1 |
| `smali/com/android/systemui/miplay/material/MiPlayMaterialTokensKt$devicesItemSelectedToken$2.smali` | 0 | 0 | 1 | 0 | 0 | 0 |
| `smali/com/android/systemui/miui/volume/MiuiVolumeDialogMotion.smali` | 0 | 0 | 1 | 0 | 0 | 0 |
| `smali_classes2/miui/systemui/controlcenter/panel/main/MainPanelContentDistributor.smali` | 0 | 0 | 1 | 0 | 0 | 0 |
| `smali_classes2/miui/systemui/controlcenter/panel/main/qs/QSRecord.smali` | 0 | 0 | 1 | 0 | 0 | 0 |
| `smali_classes2/miui/systemui/controlcenter/panel/main/qs/WordlessModeController.smali` | 0 | 0 | 1 | 0 | 0 | 0 |
| `smali_classes2/miui/systemui/controlcenter/panel/main/recyclerview/ToggleSliderViewHolder.smali` | 0 | 0 | 1 | 0 | 0 | 0 |
| `smali_classes2/miui/systemui/controlcenter/panel/secondary/media/MediaPanelAnimator.smali` | 0 | 0 | 1 | 0 | 0 | 0 |
| `smali_classes2/miui/systemui/controlcenter/widget/VerticalSeekBar.smali` | 0 | 0 | 1 | 0 | 0 | 0 |
| `smali_classes2/miui/systemui/controlcenter/windowview/ControlCenterWindowViewImpl.smali` | 0 | 0 | 1 | 0 | 0 | 0 |
| `smali_classes2/miui/systemui/dynamicisland/window/DynamicIslandWindowView.smali` | 0 | 0 | 1 | 0 | 0 | 0 |
| `smali/com/xiaomi/onetrack/f/a.smali` | 0 | 0 | 0 | 1 | 1 | 0 |
| `smali_classes2/miui/systemui/controlcenter/panel/main/header/MessageHeaderController.smali` | 0 | 0 | 0 | 1 | 1 | 0 |
| `smali_classes2/miui/systemui/controlcenter/panel/main/qs/QSItemViewHolder.smali` | 1 | 0 | 0 | 0 | 0 | 0 |
| `smali_classes2/miui/systemui/controlcenter/panel/secondary/brightness/BrightnessPanelController.smali` | 1 | 0 | 0 | 0 | 0 | 0 |

## 新增类分组

| 顶层包 | 数量 |
|---|---|
| `smali_classes3/com` | 340 |
| `smali_classes3/miui` | 97 |
| `smali_classes2/AllinOneButton` | 41 |
| `smali_classes2/miui` | 33 |
| `smali/android` | 6 |
| `smali/bg` | 5 |
| `smali/miui` | 3 |
| `smali/com` | 2 |

## 注入调用热点（改动方法里新增的 invoke）

| 调用 | 次数 |
|---|---|
| `com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog->cu` | 108 |
| `com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog->cz` | 57 |
| `com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog->al` | 36 |
| `com/android/systemui/miui/globalactions/e->bs` | 30 |
| `com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog->r` | 21 |
| `java/lang/StringBuilder->append` | 16 |
| `com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog->ef` | 15 |
| `miui/systemui/controlcenter/panel/main/recyclerview/c->w` | 13 |
| `com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog->dr` | 12 |
| `com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog->ai` | 12 |
| `com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog->aq` | 10 |
| `com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog->fa` | 10 |
| `com/android/systemui/miui/globalactions/e->ep` | 9 |
| `com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog->m` | 8 |
| `com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog->et` | 7 |
| `com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog->n` | 7 |
| `miui/systemui/controlcenter/panel/main/qs/EditButtonHeaderEntry->hideNow` | 6 |
| `miui/systemui/controlcenter/panel/main/qs/PowerHeaderEntry->hideNow` | 6 |
| `java/lang/StringBuilder-><init>` | 6 |
| `android/view/View->getResources` | 5 |
| `com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog->cv` | 5 |
| `com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog->ce` | 5 |
| `miui/systemui/controlcenter/xd/b->cm` | 5 |
| `com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog->ca` | 5 |
| `com/kashi/ios/e->bi` | 5 |
| `miui/systemui/util/MiuiColorBlendToken->getCC_TILE_DEFAULT_BLEND_COLORS` | 5 |
| `miui/systemui/controlcenter/panel/main/g->au` | 4 |
| `com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog->ch` | 4 |
| `com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog->bq` | 4 |
| `miui/systemui/controlcenter/xd/d->j` | 4 |
| `com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog->df` | 4 |
| `com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog->ev` | 4 |
| `com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog->dq` | 4 |
| `com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog->cx` | 4 |
| `com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog->dw` | 4 |
| `com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog->bo` | 4 |
| `miui/systemui/quicksettings/g->dz` | 4 |
| `com/kashi/ios/f->c` | 4 |
| `miui/systemui/controlcenter/xd/a->ee` | 4 |
| `com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog->ad` | 4 |

## 新增方法明细

- `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `public static aa(Ljava/lang/Object;Ljava/lang/Object;)V`
- `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `public static ab(Ljava/lang/Object;)Landroid/content/BroadcastReceiver;`
- `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `public static ac(ILjava/lang/Object;Ljava/lang/Object;)V`
- `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `public static ad(Ljava/lang/Object;)Lcom/android/systemui/plugins/GlobalActions$GlobalActionsManager;`
- `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `public static ae(Ljava/lang/Object;Z)V`
- `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `public static af()I`
- `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `public static ag()I`
- `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `public static ah(Ljava/lang/Object;Ljava/lang/Object;Z)V`
- `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `public static ai(Ljava/lang/Object;)Landroid/widget/FrameLayout;`
- `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `public static aj()Landroid/view/animation/Interpolator;`
- `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `public static ak()Landroid/os/Handler;`
- `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `public static al()[S`
- `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `public static am(Ljava/lang/Object;Ljava/lang/Object;)Z`
- `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `public static an()I`
- `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `public static ao(Ljava/lang/Object;)Z`
- `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `public static ap()I`
- `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `public static aq()Z`
- `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `public static ar(Ljava/lang/Object;III)Ljava/lang/String;`
- `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `public static as()Z`
- `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `public static at(Ljava/lang/Object;)V`
- `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `public static au(Ljava/lang/Object;Ljava/lang/Object;Z)I`
- `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `public static av()I`
- `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `public static aw(Ljava/lang/Object;)V`
- `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `public static ax(Ljava/lang/Object;)Z`
- `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `public static ay()Lmiui/systemui/util/DeviceStateManagerCompat;`
- `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `public static az(Ljava/lang/Object;)V`
- `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `public static ba()Z`
- `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `public static bb(Ljava/lang/Object;FZ)V`
- `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `public static bc()I`
- `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `public static bd(Ljava/lang/Object;)V`
- `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `public static be(Ljava/lang/Object;)V`
- `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `public static bf(Ljava/lang/Object;III)Ljava/lang/String;`
- `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `public static bg(Ljava/lang/Object;Ljava/lang/Object;)V`
- `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `public static bh()I`
- `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `public static bi(Ljava/lang/Object;)V`
- `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `public static bj(Ljava/lang/Object;Ljava/lang/Object;)Z`
- `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `public static bk(Ljava/lang/Object;)I`
- `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `public static bl()Z`
- `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `public static bm()I`
- `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `public static bn(Ljava/lang/Object;)Ljava/lang/String;`
- `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `public static bo(Ljava/lang/Object;III)Ljava/lang/String;`
- `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `public static bp()I`
- `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `public static bq(Ljava/lang/Object;)I`
- `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `public static br()I`
- `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `public static bs()I`
- `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `public static bt(ILjava/lang/Object;Ljava/lang/Object;)V`
- `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `public static bu(Ljava/lang/Object;Ljava/lang/Object;FII)V`
- `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `public static bv(Ljava/lang/Object;Ljava/lang/Object;)V`
- `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `public static bw(Ljava/lang/Object;)Ljava/lang/Object;`
- `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `public static bx(Ljava/lang/Object;III)Ljava/lang/String;`
- `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `public static by()Lmiui/systemui/util/CommonUtils;`
- `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `public static bz(Ljava/lang/Object;III)Ljava/lang/String;`
- `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `public static ca(Ljava/lang/Object;III)Ljava/lang/String;`
- `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `public static cb(Ljava/lang/Object;Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;`
- `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `public static cc(Ljava/lang/Object;)Ljava/lang/Object;`
- `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `public static cd(Ljava/lang/Object;I)V`
- `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `public static ce(Ljava/lang/Object;)Landroid/app/Dialog;`
- `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `public static cf()I`
- `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `public static cg(Ljava/lang/Object;)V`
- `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `public static ch()Z`
- `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `public static ci()I`
- `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `public static cj()I`
- `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `public static ck(Ljava/lang/Object;)Z`
- `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `public static cl(Ljava/lang/Object;)Landroid/content/Context;`
- `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `public static cm()I`
- `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `public static cn()I`
- `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `public static co(Ljava/lang/Object;)V`
- `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `public static cp()I`
- `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `public static cq(Ljava/lang/Object;III)Ljava/lang/String;`
- `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `public static cr(Ljava/lang/Object;III)Ljava/lang/String;`
- `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `public static cs(Ljava/lang/Object;)V`
- `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `public static ct(Ljava/lang/Object;FFZ)V`
- `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `public static cu(Ljava/lang/Object;)I`
- `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `public static cv(Ljava/lang/Object;)Landroid/view/Window;`
- `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `public static cw(Ljava/lang/Object;Ljava/lang/Object;Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;`
- `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `public static cx(Ljava/lang/Object;)Z`
- `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `public static cy(Ljava/lang/Object;)I`
- `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `public static cz(Ljava/lang/Object;)Landroid/content/Context;`
- `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `public static da()I`
- `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `public static db(Ljava/lang/Object;Ljava/lang/Object;Ljava/lang/Object;)V`
- `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `public static dc(Ljava/lang/Object;III)Ljava/lang/String;`
- `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `public static dd()I`
- `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `public static de(Ljava/lang/Object;)V`
- `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `public static df(Ljava/lang/Object;)Landroid/util/DisplayMetrics;`
- `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `public static dg(Ljava/lang/Object;)V`
- `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `public static dh(Ljava/lang/Object;)Z`
- `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `public static di(Ljava/lang/Object;)V`
- `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `public static dj(Ljava/lang/Object;I)V`
- `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `public static dk(Ljava/lang/Object;I)[I`
- `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `public static dl(Ljava/lang/Object;)Z`
- `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `public static dm(Ljava/lang/Object;)V`
- `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `public static dn(Ljava/lang/Object;ILjava/lang/Object;II)Lcom/android/systemui/miui/globalactions/BorderDrawable;`
- `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `public static do(Ljava/lang/Object;Ljava/lang/Object;Z)V`
- `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `public static dp(Ljava/lang/Object;Ljava/lang/Object;)V`
- `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `public static dq(Ljava/lang/Object;III)Ljava/lang/String;`
- `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `public static dr(Ljava/lang/Object;)Landroid/widget/FrameLayout;`
- `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `public static ds()I`
- `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `public static dt()I`
- `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `public static du(Ljava/lang/Object;III)Ljava/lang/String;`
- `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `public static dv(Ljava/lang/Object;Z)V`
- `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `public static dw(Ljava/lang/Object;III)Ljava/lang/String;`
- `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `public static dx(Ljava/lang/Object;)Z`
- `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `public static dy(Ljava/lang/Object;)Ljava/lang/Boolean;`
- `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `public static dz(Ljava/lang/Object;)V`
- `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `public static ea()I`
- `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `public static eb(Ljava/lang/Object;)F`
- `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `public static ec()I`
- `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `public static ed(Ljava/lang/Object;)V`
- `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `public static ee(Ljava/lang/Object;Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;`
- `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `public static ef(Ljava/lang/Object;)Landroid/widget/TextView;`
- `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `public static eg(Ljava/lang/Object;Ljava/lang/Object;Ljava/lang/Object;)V`
- `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `public static eh(Ljava/lang/Object;)Z`
- `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `public static ei(Ljava/lang/Object;)F`
- `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `public static ej()I`
- `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `public static ek(Ljava/lang/Object;)Z`
- `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `public static el()I`
- `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `public static em(Ljava/lang/Object;)J`
- `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `public static en(Ljava/lang/Object;III)Ljava/lang/String;`
- `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `public static eo(Ljava/lang/Object;III)Ljava/lang/String;`
- `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `public static ep(Ljava/lang/Object;)Z`
- `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `public static eq()I`
- `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `public static er(Ljava/lang/Object;Ljava/lang/Object;Z)V`
- `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `public static es(Ljava/lang/Object;)Ljava/lang/Object;`
- `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `public static et(Ljava/lang/Object;)Landroid/widget/Button;`
- `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `public static eu(Ljava/lang/Object;Ljava/lang/Object;)V`
- `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `public static ev()I`
- `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `public static ew()Z`
- `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `public static ex()[Ljava/lang/String;`
- `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `public static ey(Ljava/lang/Object;)V`
- `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `public static ez(Ljava/lang/Object;III)Ljava/lang/String;`
- `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `public static fa()Ljava/lang/String;`
- `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `public static fb()I`
- `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `public static fc(Ljava/lang/Object;Z)V`
- `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `public static fd()I`
- `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `public static fe()Z`
- `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `public static ff()I`
- `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `public static fg(Ljava/lang/Object;)Z`
- `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `public static i(Ljava/lang/Object;Ljava/lang/Object;)V`
- `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `public static j(Ljava/lang/Object;)V`
- `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `public static k(Ljava/lang/Object;FFILjava/lang/Object;)Landroid/animation/ObjectAnimator;`
- `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `public static l(Ljava/lang/Object;)Ljava/lang/String;`
- `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `public static m(Ljava/lang/Object;)Landroid/widget/Button;`
- `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `public static n(I)I`
- `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `public static o()I`
- `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `public static p(Z)V`
- `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `public static q(Ljava/lang/Object;)Landroid/view/WindowManager$LayoutParams;`
- `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `public static r(Ljava/lang/Object;)Lcom/android/systemui/miui/globalactions/SliderView;`
- `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `public static s(Ljava/lang/Object;)Z`
- `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `public static t(Ljava/lang/Object;)Z`
- `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `public static u(Ljava/lang/Object;)Z`
- `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `public static v(Ljava/lang/Object;)Z`
- `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `public static w(Ljava/lang/Object;Ljava/lang/Object;)Z`
- `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `public static x(Ljava/lang/Object;Ljava/lang/Object;)V`
- `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `public static y(Ljava/lang/Object;)I`
- `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `public static z(Z)Z`
- `smali/com/android/systemui/miui/volume/RoundRectFrameLayout.smali` :: `public draw(Landroid/graphics/Canvas;)V`
- `smali/com/android/systemui/miui/volume/VolumePanelViewController.smali` :: `public onMaterialModeChanged()V`
- `smali/com/android/systemui/miui/volume/VolumePanelViewController.smali` :: `public vsEnter()V`
- `smali/com/android/systemui/miui/volume/VolumePanelViewController.smali` :: `public vsKey(I)V`
- `smali_classes2/miui/systemui/controlcenter/panel/main/MainPanelTouchController.smali` :: `public static final isEditPanelShowing()Z`
- `smali_classes2/miui/systemui/controlcenter/panel/main/qs/EditButtonController.smali` :: `public final dismissEditPanel()V`
- `smali_classes2/miui/systemui/controlcenter/panel/main/qs/EditButtonController.smali` :: `public final isEditPanelShowing()Z`
- `smali_classes2/miui/systemui/controlcenter/panel/main/qs/QSItemViewHolder.smali` :: `public setHideLabel(Z)V`
- `smali_classes2/miui/systemui/controlcenter/panel/main/qs/QSListController.smali` :: `private static mcoolBuildEditList(Lmiui/systemui/controlcenter/panel/main/qs/QSListController;Ljava/util/ArrayList;)V`
- `smali_classes2/miui/systemui/controlcenter/panel/main/qs/QSListController.smali` :: `private static mcoolIsNewSpec(Ljava/lang/String;)Z`
- `smali_classes2/miui/systemui/controlcenter/panel/main/qs/QSListController.smali` :: `public final qsFoldApplyInstance()V`
- `smali_classes2/miui/systemui/controlcenter/panel/main/qs/QSListController.smali` :: `public final qsFoldLimitedList()Ljava/util/List;`
- `smali_classes2/miui/systemui/controlcenter/panel/main/qs/QSListController.smali` :: `public final qsFoldNotify()V`
- `smali_classes2/miui/systemui/controlcenter/panel/main/qs/QSListController.smali` :: `public static qsFoldApplyRv(Landroidx/recyclerview/widget/RecyclerView;Landroid/view/View;)V`
- `smali_classes2/miui/systemui/controlcenter/panel/main/qs/QSListController.smali` :: `public static qsFoldApplyView(Landroid/view/View;)V`
- `smali_classes2/miui/systemui/controlcenter/panel/main/qs/QSListController.smali` :: `public static qsFoldDecorate(Lmiui/systemui/controlcenter/panel/main/recyclerview/MainPanelItemViewHolder;Lmiui/systemui/controlcenter/panel/main/recyclerview/MainPanelListItem;)V`
- `smali_classes2/miui/systemui/controlcenter/panel/main/qs/QSListController.smali` :: `public static qsFoldDecorateView(Landroid/view/View;)V`
- `smali_classes2/miui/systemui/controlcenter/panel/main/qs/QSListController.smali` :: `public static qsFoldDispatch()V`
- `smali_classes2/miui/systemui/controlcenter/panel/main/qs/QSListController.smali` :: `public static qsFoldFilterList(Ljava/util/List;Z)Z`
- `smali_classes2/miui/systemui/controlcenter/panel/main/qs/QSListController.smali` :: `public static qsFoldHandleClick(Lmiui/systemui/controlcenter/panel/main/MainPanelController$Mode;Ljava/lang/String;)Z`
- `smali_classes2/miui/systemui/controlcenter/panel/main/qs/QSListController.smali` :: `public static qsFoldIndexOf(Ljava/util/List;)I`
- `smali_classes2/miui/systemui/controlcenter/panel/main/qs/QSListController.smali` :: `public static qsFoldIsTarget(Ljava/lang/String;)Z`
- `smali_classes2/miui/systemui/controlcenter/panel/main/qs/QSListController.smali` :: `public static qsFoldRemoveRecords(Ljava/util/List;)V`
- `smali_classes2/miui/systemui/controlcenter/panel/main/qs/QSListController.smali` :: `public static qsFoldSetCollapsed(Z)V`
- `smali_classes2/miui/systemui/controlcenter/panel/main/qs/QSListController.smali` :: `public static qsFoldSyncOrientation(Z)V`
- `smali_classes2/miui/systemui/controlcenter/panel/main/qs/QSListController.smali` :: `public static qsFoldToggle()V`
- `smali_classes2/miui/systemui/controlcenter/panel/main/qs/QSListController.smali` :: `public static qsFoldToggle2()V`
- `smali_classes2/miui/systemui/controlcenter/panel/main/qs/QSListController.smali` :: `public static qsFoldToggle3()V`
- `smali_classes2/miui/systemui/controlcenter/panel/main/qs/QSListController.smali` :: `public static qsFoldToggle4()V`
- `smali_classes2/miui/systemui/controlcenter/panel/main/qs/QSListController.smali` :: `public static qsFoldTrimList(Ljava/util/List;)Ljava/util/ArrayList;`
- `smali_classes2/miui/systemui/controlcenter/panel/secondary/brightness/BrightnessPanelController.smali` :: `public getContentBgMaterialToken()Lmiui/systemui/ui/material/MaterialToken;`
- `smali_classes2/miui/systemui/controlcenter/panel/secondary/volume/VolumePanelController.smali` :: `public getContentBgMaterialToken()Lmiui/systemui/ui/material/MaterialToken;`
- `smali_classes2/miui/systemui/controlcenter/panel/secondary/volume/VolumePanelController.smali` :: `public onMaterialModeChanged(Lmiui/systemui/util/MaterialMode;)V`

## 删除方法明细

- `smali/com/android/systemui/miui/volume/VolumePanelViewController.smali` :: `private onMaterialModeChanged()V`
- `smali_classes2/miui/systemui/controlcenter/panel/secondary/brightness/BrightnessPanelTilesDelegate.smali` :: `public preheatForShow()V`

## 新增字段明细

- `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `.field private static final KEYGUARD_DISMISS_MESSAGE:L/lang/String;`
- `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `.field private static final KEY_TALKBACK:L/lang/String;`
- `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `.field private static final SYSTEM_DIALOG_REASON_GLOBAL_ACTIONS:L/lang/String;`
- `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `.field private static final SYSTEM_DIALOG_REASON_KEY:L/lang/String;`
- `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `.field private static final TAG:L/lang/String;`
- `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `.field private static final short:[S`
- `smali/com/xiaomi/onetrack/f/a.smali` :: `.field private static f:L`
- `smali_classes2/miui/systemui/controlcenter/panel/main/MainPanelTouchController.smali` :: `.field public static editPanelOverlay:L/view/View;`
- `smali_classes2/miui/systemui/controlcenter/panel/main/header/MessageHeaderController.smali` :: `.field private static final HIDE_DELAY:L = 0x0L`
- `smali_classes2/miui/systemui/controlcenter/panel/main/qs/EditButtonController.smali` :: `.field private cardLongClickListener:L/systemui/controlcenter/panel/main/qs/EditButtonController$cardLongClickListener$1;`
- `smali_classes2/miui/systemui/controlcenter/panel/main/qs/EditButtonController.smali` :: `.field public final mainPanelController:L/a;`
- `smali_classes2/miui/systemui/controlcenter/panel/main/qs/EditButtonController.smali` :: `.field public static sEditClick:L/jvm/functions/Function1;`
- `smali_classes2/miui/systemui/controlcenter/panel/main/qs/QSListController.smali` :: `.field private final mcoolNewDivider:L/systemui/controlcenter/panel/main/qs/QSListController$EditModeDividerTextItem;`
- `smali_classes2/miui/systemui/controlcenter/panel/main/qs/QSListController.smali` :: `.field private static final MIN_TILE_COUNT:L`
- `smali_classes2/miui/systemui/controlcenter/panel/main/qs/QSListController.smali` :: `.field public static qsFoldAdapter:L/lang/Object;`
- `smali_classes2/miui/systemui/controlcenter/panel/main/qs/QSListController.smali` :: `.field public static qsFoldAnchor:L/systemui/controlcenter/panel/main/qs/QSListController;`
- `smali_classes2/miui/systemui/controlcenter/panel/main/qs/QSListController.smali` :: `.field public static qsFoldAnchorCard:L/lang/Object;`
- `smali_classes2/miui/systemui/controlcenter/panel/main/qs/QSListController.smali` :: `.field public static qsFoldCollapsed:L`
- `smali_classes2/miui/systemui/controlcenter/panel/main/qs/QSListController.smali` :: `.field public static qsFoldHost:L/lang/Object;`
- `smali_classes2/miui/systemui/controlcenter/panel/main/qs/QSListController.smali` :: `.field public static qsFoldLand:L`
- `smali_classes2/miui/systemui/controlcenter/panel/main/qs/QSListController.smali` :: `.field public static qsFoldRv:L/lang/Object;`
- `smali_classes2/miui/systemui/controlcenter/panel/main/qs/QSListController.smali` :: `.field public static qsFoldSaved:L`
- `smali_classes2/miui/systemui/controlcenter/panel/main/qs/QSListController.smali` :: `.field public static qsFoldSeen:L`
- `smali_classes2/miui/systemui/controlcenter/panel/main/qs/QSListController.smali` :: `.field public static qsFoldSyncInit:L`
- `smali_classes2/miui/systemui/controlcenter/panel/main/qs/QSListController.smali` :: `.field public static qsFoldTarget:L/lang/String; = "fold_tile"`
- `smali_classes2/miui/systemui/controlcenter/panel/secondary/detail/DetailPanelDelegate.smali` :: `.field public detailAdapter:L/android/systemui/plugins/qs/DetailAdapter;`
- `smali_classes2/miui/systemui/controlcenter/panel/secondary/detail/DetailPanelDelegate.smali` :: `.field public final activityStarter:L/android/systemui/plugins/ActivityStarter;`
- `smali_classes2/miui/systemui/controlcenter/panel/secondary/detail/DetailPanelDelegate.smali` :: `.field public final cellAnimator:L/systemui/controlcenter/panel/secondary/detail/DetailPanelCellAnimator;`
- `smali_classes2/miui/systemui/controlcenter/qs/QSController.smali` :: `.field public static sInstance:L/systemui/controlcenter/qs/QSController;`
- `smali_classes2/miui/systemui/controlcenter/qs/tileview/QSTileItemIconView.smali` :: `.field private dolbyTileIconColor:L`
- `smali_classes2/miui/systemui/controlcenter/qs/tileview/QSTileItemView.smali` :: `.field public forceHideLabel:L`

## 改动方法明细（按新增指令数）

### `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `static constructor <clinit>()V` (+985)

    `const R, 0x317`
    `new-array R, R, [S`
    `fill-array-data R, :L`
    `sput-object R, Lcom/android/systemui/miui/globalactions/MiuiGlobalActionsDialog;->short:[S`
    `invoke-static/range {}, Lcom/android/systemui/miui/globalactions/MiuiGlobalActionsDialog;->al()[S`
    `const R, 0xdd02`
    `invoke-static/range {}, Lmiui/systemui/controlcenter/panel/main/recyclerview/a;->bg()Ljava/lang/String;`
    `invoke-static/range {R .. R}, Lcom/android/systemui/miui/globalactions/MiuiGlobalActionsDialog;->cu(Ljava/lang/Object;)I`

### `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `private initViews()V` (+165)

    `move-object/from16 R, R`
    `invoke-static {R}, Lcom/android/systemui/miui/globalactions/MiuiGlobalActionsDialog;->cz(Ljava/lang/Object;)Landroid/content/Context;`
    `invoke-static {R, R}, Lcom/android/systemui/miui/globalactions/e;->v(Ljava/lang/Object;Z)V`
    `invoke-static {R}, Lcom/android/systemui/miui/globalactions/MiuiGlobalActionsDialog;->dr(Ljava/lang/Object;)Landroid/widget/FrameLayout;`
    `invoke-static {R, R}, Lmiui/systemui/controlcenter/panel/main/recyclerview/c;->cd(Ljava/lang/Object;Z)V`
    `invoke-static {R}, Lcom/android/systemui/miui/globalactions/MiuiGlobalActionsDialog;->cz(Ljava/lang/Object;)Landroid/content/Context;`
    `invoke-static {R}, Lcom/android/systemui/miui/globalactions/MiuiGlobalActionsDialog;->cz(Ljava/lang/Object;)Landroid/content/Context;`
    `invoke-static {}, Lcom/android/systemui/miui/globalactions/MiuiGlobalActionsDialog;->eq()I`

### `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `public showDialog()V` (+101)

    `move-object/from16 R, R`
    `invoke-static {R}, Lcom/android/systemui/miui/globalactions/MiuiGlobalActionsDialog;->ad(Ljava/lang/Object;)Lcom/android/systemui/plugins/GlobalActions$GlobalActionsManager;`
    `invoke-static {R}, Lcom/android/systemui/miui/globalactions/MiuiGlobalActionsDialog;->dg(Ljava/lang/Object;)V`
    `invoke-static {R}, Lcom/android/systemui/miui/globalactions/MiuiGlobalActionsDialog;->cz(Ljava/lang/Object;)Landroid/content/Context;`
    `invoke-static {R}, Lmiui/systemui/controlcenter/xd/d;->aj(Ljava/lang/Object;)Landroid/content/ContentResolver;`
    `invoke-static/range {}, Lcom/android/systemui/miui/globalactions/MiuiGlobalActionsDialog;->al()[S`
    `const R, 0x1aa440`
    `invoke-static/range {}, Lcom/android/systemui/miui/globalactions/g;->dg()Ljava/lang/String;`

### `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `public action(IZ)V` (+86)

    `move/from16 R, R`
    `move/from16 R, R`
    `move-object/from16 R, R`
    `invoke-static {}, Lcom/android/systemui/miui/globalactions/MiuiGlobalActionsDialog;->fa()Ljava/lang/String;`
    `invoke-static/range {}, Lcom/android/systemui/miui/globalactions/MiuiGlobalActionsDialog;->al()[S`
    `const R, 0x1aacd6`
    `invoke-static/range {}, Lmiui/systemui/quicksettings/f;->w()Ljava/lang/String;`
    `invoke-static/range {R .. R}, Lcom/android/systemui/miui/globalactions/MiuiGlobalActionsDialog;->cu(Ljava/lang/Object;)I`

### `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `public onConfigChanged(Landroid/content/res/Configuration;)V` (+60)

    `move-object/from16 R, R`
    `move-object/from16 R, R`
    `invoke-static {}, Lcom/android/systemui/miui/globalactions/MiuiGlobalActionsDialog;->fa()Ljava/lang/String;`
    `invoke-static/range {}, Lcom/android/systemui/miui/globalactions/MiuiGlobalActionsDialog;->al()[S`
    `const R, 0x1aa7f7`
    `invoke-static/range {}, Lcom/android/systemui/miui/globalactions/d;->bw()Ljava/lang/String;`
    `invoke-static/range {R .. R}, Lcom/android/systemui/miui/globalactions/MiuiGlobalActionsDialog;->cu(Ljava/lang/Object;)I`
    `xor-int R, R, R`

### `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `private createWindowParams()Landroid/view/WindowManager$LayoutParams;` (+58)

    `move-object/from16 R, R`
    `invoke-static {R}, Lcom/android/systemui/miui/globalactions/MiuiGlobalActionsDialog;->cv(Ljava/lang/Object;)Landroid/view/Window;`
    `invoke-static {R}, Lcom/android/systemui/miui/globalactions/d;->p(Ljava/lang/Object;)Landroid/view/WindowManager$LayoutParams;`
    `invoke-static {R}, Lcom/android/systemui/miui/globalactions/MiuiGlobalActionsDialog;->cv(Ljava/lang/Object;)Landroid/view/Window;`
    `invoke-static {R, R}, Lmiui/systemui/controlcenter/panel/main/g;->bz(Ljava/lang/Object;Ljava/lang/Object;)V`
    `invoke-static {R}, Lcom/android/systemui/miui/globalactions/MiuiGlobalActionsDialog;->cv(Ljava/lang/Object;)Landroid/view/Window;`
    `invoke-static {R, R}, Lcom/android/systemui/miui/globalactions/f;->u(Ljava/lang/Object;I)V`
    `invoke-static {R}, Lmiui/systemui/controlcenter/xd/a;->v(Ljava/lang/Object;)I`

### `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `private isEnableTalkBack(Landroid/content/Context;)Z` (+55)

    `move-object/from16 R, R`
    `move-object/from16 R, R`
    `invoke-static {R}, Lmiui/systemui/controlcenter/xd/d;->aj(Ljava/lang/Object;)Landroid/content/ContentResolver;`
    `invoke-static/range {}, Lcom/android/systemui/miui/globalactions/MiuiGlobalActionsDialog;->al()[S`
    `const R, 0x1acb1a`
    `invoke-static/range {}, Lmiui/systemui/controlcenter/panel/main/recyclerview/a;->bv()Ljava/lang/String;`
    `invoke-static/range {R .. R}, Lcom/android/systemui/miui/globalactions/MiuiGlobalActionsDialog;->cu(Ljava/lang/Object;)I`
    `xor-int R, R, R`

### `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `private computeButtonMarginBottom(Landroid/widget/Button;Z)I` (+46)

    `move/from16 R, R`
    `move-object/from16 R, R`
    `move-object/from16 R, R`
    `invoke-static {R}, Lcom/android/systemui/miui/globalactions/MiuiGlobalActionsDialog;->cz(Ljava/lang/Object;)Landroid/content/Context;`
    `invoke-static {R}, Lcom/android/systemui/miui/globalactions/e;->bs(Ljava/lang/Object;)Landroid/content/res/Resources;`
    `invoke-static {}, Lcom/android/systemui/miui/globalactions/MiuiGlobalActionsDialog;->ec()I`
    `invoke-static {R, R}, Lmiui/systemui/controlcenter/panel/main/recyclerview/c;->w(Ljava/lang/Object;I)I`
    `invoke-static {R}, Lcom/android/systemui/miui/globalactions/MiuiGlobalActionsDialog;->cz(Ljava/lang/Object;)Landroid/content/Context;`

### `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `private dismiss(I)V` (+39)

    `move/from16 R, R`
    `move-object/from16 R, R`
    `invoke-static {R}, Lcom/android/systemui/miui/globalactions/MiuiGlobalActionsDialog;->r(Ljava/lang/Object;)Lcom/android/systemui/miui/globalactions/SliderView;`
    `move-result-object R`
    `invoke-static {R}, Lcom/android/systemui/miui/globalactions/MiuiGlobalActionsDialog;->s(Ljava/lang/Object;)Z`
    `invoke-static {R}, Lcom/android/systemui/miui/globalactions/MiuiGlobalActionsDialog;->ax(Ljava/lang/Object;)Z`
    `invoke-static {}, Lcom/android/systemui/miui/globalactions/MiuiGlobalActionsDialog;->fa()Ljava/lang/String;`
    `move-result-object R`

### `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `private dismissKeyguardThenExecute(Ljava/lang/Runnable;)V` (+39)

    `move-object/from16 R, R`
    `move-object/from16 R, R`
    `invoke-static {}, Lcom/android/systemui/miui/globalactions/g;->ao()Landroid/view/IWindowManager;`
    `invoke-static {R}, Lmiui/systemui/controlcenter/xd/c;->bc(Ljava/lang/Object;)Z`
    `invoke-static/range {}, Lcom/android/systemui/miui/globalactions/MiuiGlobalActionsDialog;->al()[S`
    `const R, 0x1aa3df`
    `invoke-static/range {}, Lmiui/systemui/controlcenter/xd/b;->dg()Ljava/lang/String;`
    `invoke-static {R}, Lcom/android/systemui/miui/globalactions/MiuiGlobalActionsDialog;->cu(Ljava/lang/Object;)I`

### `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `private setViewAttr(Landroid/widget/TextView;FII)V` (+36)

    `move/from16 R, R`
    `move/from16 R, R`
    `move/from16 R, R`
    `move-object/from16 R, R`
    `move-object/from16 R, R`
    `invoke-static {R, R}, Lmiui/systemui/controlcenter/xd/d;->cp(Ljava/lang/Object;F)V`
    `invoke-static {R}, Lcom/android/systemui/miui/globalactions/MiuiGlobalActionsDialog;->cz(Ljava/lang/Object;)Landroid/content/Context;`
    `invoke-static {R}, Lcom/android/systemui/miui/globalactions/e;->bs(Ljava/lang/Object;)Landroid/content/res/Resources;`

### `smali_classes2/miui/systemui/controlcenter/panel/main/recyclerview/MainPanelAdapter.smali` :: `private final distributeContent(Z)V` (+36)

    `iget-object R, R, Lmiui/systemui/controlcenter/panel/main/recyclerview/MainPanelAdapter;->context:L/content/Context;`
    `invoke-virtual {R}, Landroid/content/Context;->getDisplay()Landroid/view/Display;`
    `const/4 R, -0x1`
    `invoke-virtual {R}, Landroid/view/Display;->getRotation()I`
    `const/4 R, 0x1`
    `if-ne R, R, :L`
    `const/4 R, 0x1`
    `const/4 R, 0x3`

### `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `public constructor <init>(Landroid/content/Context;Landroid/content/Context;Lcom/android/systemui/plugins/GlobalActions$GlobalActionsManager;)V` (+35)

    `move-object/from16 R, R`
    `move-object/from16 R, R`
    `move-object/from16 R, R`
    `move-object/from16 R, R`
    `invoke-static {}, Lmiui/systemui/controlcenter/panel/main/recyclerview/a;->dq()Ljava/lang/String;`
    `invoke-static {R, R}, Lmiui/systemui/controlcenter/panel/main/recyclerview/a;->af(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;`
    `invoke-static/range {}, Lcom/android/systemui/miui/globalactions/MiuiGlobalActionsDialog;->al()[S`
    `const R, 0x1ac6bf`

### `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `private addAlarmTextView()V` (+34)

    `move-object/from16 R, R`
    `invoke-static {R}, Lcom/android/systemui/miui/globalactions/MiuiGlobalActionsDialog;->cz(Ljava/lang/Object;)Landroid/content/Context;`
    `invoke-static {R}, Lcom/android/systemui/miui/globalactions/MiuiGlobalActionsDialog;->cz(Ljava/lang/Object;)Landroid/content/Context;`
    `invoke-static {R}, Lcom/android/systemui/miui/globalactions/MiuiGlobalActionsDialog;->bn(Ljava/lang/Object;)Ljava/lang/String;`
    `invoke-static {R}, Lcom/android/systemui/miui/globalactions/MiuiGlobalActionsDialog;->cz(Ljava/lang/Object;)Landroid/content/Context;`
    `invoke-static {R}, Lcom/android/systemui/miui/globalactions/MiuiGlobalActionsDialog;->l(Ljava/lang/Object;)Ljava/lang/String;`
    `invoke-static {R}, Lcom/android/systemui/miui/globalactions/MiuiGlobalActionsDialog;->ef(Ljava/lang/Object;)Landroid/widget/TextView;`
    `invoke-static {R, R}, Lmiui/systemui/quicksettings/e;->c(Ljava/lang/Object;Ljava/lang/Object;)V`

### `smali_classes2/miui/systemui/quicksettings/LocalMiuiQSTilePlugin.smali` :: `private initAllMiuiTilesPlugin()V` (+29)

    `invoke-static {R, R, R}, Lmiui/systemui/quicksettings/AppTiles;->registerAll(Landroid/content/Context;Landroid/content/Context;Ljava/util/HashMap;)V`
    `.catchall {:L .. :L} :L`
    `new-instance R, Lmiui/systemui/quicksettings/DimTile;`
    `invoke-direct {R, R, R}, Lmiui/systemui/quicksettings/DimTile;-><init>(Landroid/content/Context;Landroid/content/Context;)V`
    `invoke-virtual {R}, Lmiui/systemui/quicksettings/DimTile;->getTileSpec()Ljava/lang/String;`
    `new-instance R, Lmiui/systemui/quicksettings/LsposedTile;`
    `const-string R, "lsposed_tile"`
    `invoke-direct {R, R, R, R}, Lmiui/systemui/quicksettings/LsposedTile;-><init>(Landroid/content/Context;Landroid/content/Context;Ljava/lang/String;)V`

### `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `private createAlphaAnimator(FFILandroid/view/View;)Landroid/animation/ObjectAnimator;` (+27)

    `move-object/from16 R, R`
    `move/from16 R, R`
    `move/from16 R, R`
    `move/from16 R, R`
    `move-object/from16 R, R`
    `invoke-static/range {}, Lcom/android/systemui/miui/globalactions/MiuiGlobalActionsDialog;->al()[S`
    `const R, 0xdbb8`
    `invoke-static/range {}, Lcom/kashi/mpager/a;->k()Ljava/lang/String;`

### `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `private updateFoldState(Z)V` (+26)

    `move/from16 R, R`
    `move-object/from16 R, R`
    `invoke-static {}, Lcom/android/systemui/miui/globalactions/MiuiGlobalActionsDialog;->fa()Ljava/lang/String;`
    `invoke-static/range {}, Lcom/android/systemui/miui/globalactions/MiuiGlobalActionsDialog;->al()[S`
    `const R, 0x1aa415`
    `invoke-static/range {}, Lmiui/systemui/controlcenter/panel/main/recyclerview/a;->c()Ljava/lang/String;`
    `invoke-static/range {R .. R}, Lcom/android/systemui/miui/globalactions/MiuiGlobalActionsDialog;->cu(Ljava/lang/Object;)I`
    `xor-int R, R, R`

### `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `private isMoveTouch(Landroid/view/MotionEvent;)Z` (+25)

    `move-object/from16 R, R`
    `move-object/from16 R, R`
    `invoke-static {R}, Lmiui/systemui/quicksettings/e;->da(Ljava/lang/Object;)I`
    `invoke-static {R}, Lcom/android/systemui/miui/globalactions/MiuiGlobalActionsDialog;->ei(Ljava/lang/Object;)F`
    `invoke-static {R}, Lcom/kashi/ios/e;->bi(Ljava/lang/Object;)F`
    `invoke-static {R}, Lcom/android/systemui/miui/globalactions/MiuiGlobalActionsDialog;->eb(Ljava/lang/Object;)F`
    `invoke-static {R}, Lcom/android/systemui/miui/globalactions/e;->q(F)F`
    `invoke-static {R}, Lcom/kashi/ios/e;->bi(Ljava/lang/Object;)F`

### `smali_classes2/miui/systemui/controlcenter/panel/main/qs/QSListController.smali` :: `private final distributeTiles(Z)V` (+25)

    `goto/16 :L`
    `goto/16 :L`
    `invoke-virtual {R}, Lmiui/systemui/controlcenter/qs/QSController;->getCardStyleTileSpecs()Ljava/util/List;`
    `const-string R, "ccbig"`
    `invoke-direct {R}, Ljava/lang/StringBuilder;-><init>()V`
    `const-string R, "flaglist n="`
    `invoke-virtual {R, R}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;`
    `invoke-interface {R}, Ljava/util/List;->size()I`

### `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `private setButtonAttr(Landroid/widget/Button;Z)V` (+24)

    `move/from16 R, R`
    `move-object/from16 R, R`
    `move-object/from16 R, R`
    `invoke-static {R}, Lcom/android/systemui/miui/globalactions/MiuiGlobalActionsDialog;->cz(Ljava/lang/Object;)Landroid/content/Context;`
    `invoke-static {R}, Lcom/android/systemui/miui/globalactions/e;->bs(Ljava/lang/Object;)Landroid/content/res/Resources;`
    `invoke-static {}, Lcom/android/systemui/miui/globalactions/MiuiGlobalActionsDialog;->bp()I`
    `invoke-static {R, R}, Lmiui/systemui/controlcenter/panel/main/recyclerview/c;->w(Ljava/lang/Object;I)I`
    `invoke-static {R}, Lcom/android/systemui/miui/globalactions/MiuiGlobalActionsDialog;->cz(Ljava/lang/Object;)Landroid/content/Context;`

### `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `private updateTinyScreenSliderViewLp(Landroid/widget/FrameLayout$LayoutParams;)V` (+22)

    `move-object/from16 R, R`
    `move-object/from16 R, R`
    `invoke-static {R}, Lcom/android/systemui/miui/globalactions/MiuiGlobalActionsDialog;->cz(Ljava/lang/Object;)Landroid/content/Context;`
    `invoke-static {R}, Lmiui/systemui/controlcenter/xd/a;->ee(Ljava/lang/Object;)Landroid/view/Display;`
    `invoke-static {R}, Lcom/android/systemui/miui/globalactions/MiuiGlobalActionsDialog;->t(Ljava/lang/Object;)Z`
    `invoke-static {R}, Lcom/android/systemui/miui/globalactions/MiuiGlobalActionsDialog;->cz(Ljava/lang/Object;)Landroid/content/Context;`
    `invoke-static {R}, Lcom/android/systemui/miui/globalactions/e;->bs(Ljava/lang/Object;)Landroid/content/res/Resources;`
    `invoke-static {}, Lcom/android/systemui/miui/globalactions/MiuiGlobalActionsDialog;->ev()I`

### `smali_classes2/miui/systemui/controlcenter/panel/main/qs/EditButtonController.smali` :: `public onBindViewHolder()V` (+22)

    `invoke-virtual {R}, Landroid/view/View;->getParent()Landroid/view/ViewParent;`
    `instance-of R, R, Landroid/view/ViewGroup;`
    `check-cast R, Landroid/view/ViewGroup;`
    `const R, 0x7f0a0269`
    `invoke-virtual {R, R}, Landroid/view/ViewGroup;->findViewById(I)Landroid/view/View;`
    `if-nez R, :L`
    `move-object R, R`
    `sput-object R, Lmiui/systemui/controlcenter/panel/main/qs/EditButtonController;->sEditClick:L/jvm/functions/Function1;`

### `smali_classes2/miui/systemui/controlcenter/qs/tileview/QSTileItemIconView.smali` :: `private final drawableTint(Lcom/android/systemui/plugins/qs/QSTile$State;Landroid/graphics/drawable/Drawable;)V` (+21)

    `const-string R, "sun_tile"`
    `if-ne R, R, :L`
    `const/4 R, -0x1`
    `const-string R, "keep_screen"`
    `if-ne R, R, :L`
    `const/4 R, -0x1`
    `const-string R, "dim_tile"`
    `if-ne R, R, :L`

### `smali_classes2/miui/systemui/controlcenter/qs/tileview/QSCardItemIconView.smali` :: `public setIcon(Lcom/android/systemui/plugins/qs/QSTile$State;Z)V` (+20)

    `goto/16 :L`
    `goto/16 :L`
    `const-string R, "mute"`
    `const R, -0xb0c1`
    `goto/16 :L`
    `const-string R, "flashlight"`
    `const R, -0x60fb`
    `goto/16 :L`

### `smali/com/android/systemui/miui/volume/TimerItem.smali` :: `public updateTimerSeekbar()V` (+19)

    `const/4 R, 0x0`
    `invoke-virtual {R, R}, Landroid/view/View;->setBackground(Landroid/graphics/drawable/Drawable;)V`
    `sget-object R, Lmiui/systemui/util/MiBackgroundStyle;->INSTANCE:L/systemui/util/MiBackgroundStyle;`
    `invoke-virtual {R}, Lmiui/systemui/util/MiBackgroundStyle;->getDEFAULT_GLASS_TOKEN()Lmiui/systemui/util/BionicsToken;`
    `invoke-static {R, R, R, R}, Lcom/android/systemui/miui/volume/Util;->setMiViewBackgroundStyle(Landroid/view/View;ILmiuix/theme/token/ColorBlendToken;Lmiui/systemui/util/BionicsToken;)V`
    `new-instance R, Landroid/graphics/drawable/GradientDrawable;`
    `invoke-direct {R}, Landroid/graphics/drawable/GradientDrawable;-><init>()V`
    `const R, 0x52808080`

### `smali_classes2/miui/systemui/controlcenter/panel/secondary/brightness/BrightnessPanelAnimator.smali` :: `public frameCallback()V` (+17)

    `const R, -0x1`
    `invoke-virtual/range {R .. R}, Lmiui/systemui/controlcenter/panel/secondary/SecondaryPanelAnimatorBase;->isCollapsing()Z`
    `const R, 0x42c00000    # 96.0f`
    `const/high16 R, 0x437f0000    # 255.0f`
    `const R, 0x437a0000    # 250.0f`
    `const/high16 R, 0x437f0000    # 255.0f`
    `shl-int/lit8 R, R, 0x8`
    `or-int/2addr R, R`

### `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `private updateButtonBottomMargins()V` (+15)

    `move-object/from16 R, R`
    `invoke-static {}, Lcom/android/systemui/miui/globalactions/MiuiGlobalActionsDialog;->aq()Z`
    `invoke-static {}, Lcom/android/systemui/miui/globalactions/MiuiGlobalActionsDialog;->ch()Z`
    `invoke-static {R}, Lcom/android/systemui/miui/globalactions/MiuiGlobalActionsDialog;->et(Ljava/lang/Object;)Landroid/widget/Button;`
    `invoke-static {R, R, R}, Lcom/android/systemui/miui/globalactions/MiuiGlobalActionsDialog;->au(Ljava/lang/Object;Ljava/lang/Object;Z)I`
    `invoke-static {R}, Lcom/android/systemui/miui/globalactions/MiuiGlobalActionsDialog;->et(Ljava/lang/Object;)Landroid/widget/Button;`
    `invoke-static {R}, Lcom/android/systemui/miui/globalactions/h;->ba(Ljava/lang/Object;)Landroid/view/ViewGroup$LayoutParams;`
    `invoke-static {R}, Lcom/android/systemui/miui/globalactions/MiuiGlobalActionsDialog;->et(Ljava/lang/Object;)Landroid/widget/Button;`

### `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `public sliderViewDismiss()V` (+15)

    `move-object/from16 R, R`
    `invoke-static {R}, Lcom/android/systemui/miui/globalactions/MiuiGlobalActionsDialog;->ce(Ljava/lang/Object;)Landroid/app/Dialog;`
    `move-result-object R`
    `invoke-static {R}, Lcom/android/systemui/miui/globalactions/g;->du(Ljava/lang/Object;)Z`
    `invoke-static {R}, Lcom/android/systemui/miui/globalactions/MiuiGlobalActionsDialog;->ce(Ljava/lang/Object;)Landroid/app/Dialog;`
    `move-result-object R`
    `invoke-static {R}, Lmiui/systemui/controlcenter/panel/main/recyclerview/b;->eh(Ljava/lang/Object;)V`
    `invoke-static {R}, Lcom/android/systemui/miui/globalactions/MiuiGlobalActionsDialog;->cz(Ljava/lang/Object;)Landroid/content/Context;`

### `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `private computeFlipTinyAlarmTextWidth()I` (+14)

    `move-object/from16 R, R`
    `invoke-static {R}, Lcom/android/systemui/miui/globalactions/MiuiGlobalActionsDialog;->cz(Ljava/lang/Object;)Landroid/content/Context;`
    `invoke-static {R}, Lcom/android/systemui/miui/globalactions/e;->bs(Ljava/lang/Object;)Landroid/content/res/Resources;`
    `invoke-static {}, Lcom/android/systemui/miui/globalactions/MiuiGlobalActionsDialog;->ev()I`
    `invoke-static {R}, Lcom/android/systemui/miui/globalactions/MiuiGlobalActionsDialog;->n(I)I`
    `invoke-static {R, R}, Lmiui/systemui/controlcenter/panel/main/recyclerview/c;->w(Ljava/lang/Object;I)I`
    `invoke-static {R}, Lcom/android/systemui/miui/globalactions/MiuiGlobalActionsDialog;->cz(Ljava/lang/Object;)Landroid/content/Context;`
    `invoke-static {R}, Lcom/android/systemui/miui/globalactions/e;->bs(Ljava/lang/Object;)Landroid/content/res/Resources;`

### `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `public textViewAlphaAnimator(Z)V` (+14)

    `move/from16 R, R`
    `move-object/from16 R, R`
    `invoke-static {R}, Lcom/android/systemui/miui/globalactions/MiuiGlobalActionsDialog;->ef(Ljava/lang/Object;)Landroid/widget/TextView;`
    `invoke-static {R, R, R, R, R}, Lcom/android/systemui/miui/globalactions/MiuiGlobalActionsDialog;->k(Ljava/lang/Object;FFILjava/lang/Object;)Landroid/animation/ObjectAnimator;`
    `invoke-static {R, R}, Lcom/kashi/ios/f;->ao(Ljava/lang/Object;Ljava/lang/Object;)V`
    `invoke-static {}, Lcom/android/systemui/miui/globalactions/MiuiGlobalActionsDialog;->fe()Z`
    `invoke-static {R}, Lcom/android/systemui/miui/globalactions/MiuiGlobalActionsDialog;->m(Ljava/lang/Object;)Landroid/widget/Button;`
    `invoke-static {R, R, R, R, R}, Lcom/android/systemui/miui/globalactions/MiuiGlobalActionsDialog;->k(Ljava/lang/Object;FFILjava/lang/Object;)Landroid/animation/ObjectAnimator;`

### `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `private addEmergencyCallButton()V` (+13)

    `move-object/from16 R, R`
    `invoke-static {R}, Lcom/android/systemui/miui/globalactions/MiuiGlobalActionsDialog;->cz(Ljava/lang/Object;)Landroid/content/Context;`
    `invoke-static {R}, Lcom/android/systemui/miui/globalactions/MiuiGlobalActionsDialog;->cz(Ljava/lang/Object;)Landroid/content/Context;`
    `invoke-static {R}, Lcom/android/systemui/miui/globalactions/e;->bs(Ljava/lang/Object;)Landroid/content/res/Resources;`
    `invoke-static {}, Lcom/android/systemui/miui/globalactions/MiuiGlobalActionsDialog;->bs()I`
    `invoke-static {R, R}, Lmiui/systemui/controlcenter/panel/main/g;->au(Ljava/lang/Object;I)Ljava/lang/String;`
    `invoke-static {R, R}, Lcom/android/systemui/miui/globalactions/e;->dp(Ljava/lang/Object;Ljava/lang/Object;)V`
    `invoke-static {}, Lcom/android/systemui/miui/globalactions/MiuiGlobalActionsDialog;->aq()Z`

### `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `private initDialog()V` (+13)

    `move-object/from16 R, R`
    `invoke-static {R}, Lcom/android/systemui/miui/globalactions/MiuiGlobalActionsDialog;->cz(Ljava/lang/Object;)Landroid/content/Context;`
    `invoke-static {}, Lcom/android/systemui/miui/globalactions/MiuiGlobalActionsDialog;->fd()I`
    `invoke-static {R}, Lmiui/systemui/controlcenter/xd/c;->by(Ljava/lang/Object;)Landroid/view/Window;`
    `invoke-static {R, R}, Lmiui/systemui/quicksettings/g;->ca(Ljava/lang/Object;I)Z`
    `invoke-static {R}, Lcom/android/systemui/miui/globalactions/MiuiGlobalActionsDialog;->cx(Ljava/lang/Object;)Z`
    `invoke-static {}, Lcom/android/systemui/miui/globalactions/MiuiGlobalActionsDialog;->aq()Z`
    `invoke-static {R}, Lcom/android/systemui/miui/globalactions/MiuiGlobalActionsDialog;->bi(Ljava/lang/Object;)V`

### `smali_classes2/miui/systemui/controlcenter/panel/main/qs/QSListController.smali` :: `public getListItems()Ljava/util/List;` (+13)

    `invoke-static {R, R}, Lmiui/systemui/controlcenter/panel/main/qs/QSListController;->mcoolBuildEditList(Lmiui/systemui/controlcenter/panel/main/qs/QSListController;Ljava/util/ArrayList;)V`
    `sput-object R, Lmiui/systemui/controlcenter/panel/main/qs/QSListController;->qsFoldHost:L/lang/Object;`
    `sget-boolean R, Lmiui/systemui/controlcenter/panel/main/qs/QSListController;->qsFoldSeen:L`
    `sput-boolean R, Lmiui/systemui/controlcenter/panel/main/qs/QSListController;->qsFoldSeen:L`
    `invoke-virtual {R}, Lmiui/systemui/util/ViewController;->getContext()Landroid/content/Context;`
    `invoke-virtual {R}, Landroid/content/Context;->getContentResolver()Landroid/content/ContentResolver;`
    `const-string R, "qs_fold_collapsed"`
    `const/4 R, 0x0`

### `smali_classes2/miui/systemui/controlcenter/panel/secondary/brightness/BrightnessPanelTilesDelegate.smali` :: `private final addQSTileItemView(Ljava/lang/String;)V` (+13)

    `sget R, Lmiui/systemui/controlcenter/R$id;->tile_label:L`
    `invoke-virtual {R, R}, Landroid/widget/FrameLayout;->findViewById(I)Landroid/view/View;`
    `invoke-virtual {R, R}, Landroid/view/View;->setVisibility(I)V`
    `invoke-virtual {R, R}, Landroid/view/View;->setAlpha(F)V`
    `invoke-virtual {R}, Landroid/view/View;->getResources()Landroid/content/res/Resources;`
    `sget R, Lmiui/systemui/controlcenter/R$dimen;->control_center_universal_1_row_with_margin_size:L`
    `invoke-virtual {R, R}, Landroid/content/res/Resources;->getDimensionPixelSize(I)I`
    `invoke-virtual {R}, Landroid/view/View;->getResources()Landroid/content/res/Resources;`

### `smali/com/android/systemui/QSControlMiPlayDetailContent.smali` :: `public onFinishInflate()V` (+12)

    `invoke-virtual {R}, Landroid/view/View;->getLayoutParams()Landroid/view/ViewGroup$LayoutParams;`
    `iget R, R, Landroid/view/ViewGroup$LayoutParams;->width:L`
    `if-lez R, :L`
    `:L`
    `invoke-virtual {R}, Landroid/view/View;->getLayoutParams()Landroid/view/ViewGroup$LayoutParams;`
    `iget R, R, Landroid/view/ViewGroup$LayoutParams;->width:L`
    `if-lez R, :L`
    `invoke-virtual {R, R}, Landroid/view/ViewGroup;->setClipChildren(Z)V`

### `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `private addSystemUpdateButton()V` (+12)

    `move-object/from16 R, R`
    `invoke-static {R}, Lcom/android/systemui/miui/globalactions/MiuiGlobalActionsDialog;->cz(Ljava/lang/Object;)Landroid/content/Context;`
    `invoke-static {R}, Lcom/android/systemui/miui/globalactions/MiuiGlobalActionsDialog;->cz(Ljava/lang/Object;)Landroid/content/Context;`
    `invoke-static {R}, Lcom/android/systemui/miui/globalactions/e;->bs(Ljava/lang/Object;)Landroid/content/res/Resources;`
    `invoke-static {}, Lcom/android/systemui/miui/globalactions/MiuiGlobalActionsDialog;->cp()I`
    `move-result R`
    `invoke-static {R, R}, Lmiui/systemui/controlcenter/panel/main/g;->au(Ljava/lang/Object;I)Ljava/lang/String;`
    `invoke-static {R, R}, Lcom/android/systemui/miui/globalactions/e;->dp(Ljava/lang/Object;Ljava/lang/Object;)V`

### `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `private applyTextLayout(Landroid/view/View;Landroid/widget/FrameLayout$LayoutParams;)V` (+12)

    `move-object/from16 R, R`
    `move-object/from16 R, R`
    `move-object/from16 R, R`
    `invoke-static {R}, Lcom/android/systemui/miui/globalactions/MiuiGlobalActionsDialog;->dh(Ljava/lang/Object;)Z`
    `invoke-static {R}, Lcom/android/systemui/miui/globalactions/MiuiGlobalActionsDialog;->fg(Ljava/lang/Object;)Z`
    `invoke-static {R}, Lcom/android/systemui/miui/globalactions/MiuiGlobalActionsDialog;->cz(Ljava/lang/Object;)Landroid/content/Context;`
    `invoke-static {R}, Lcom/android/systemui/miui/globalactions/e;->bs(Ljava/lang/Object;)Landroid/content/res/Resources;`
    `invoke-static {}, Lcom/android/systemui/miui/globalactions/MiuiGlobalActionsDialog;->ej()I`

### `smali_classes2/miui/systemui/controlcenter/panel/secondary/detail/DetailPanelTilesDelegate.smali` :: `private final createTiles()V` (+12)

    `invoke-virtual {R, R}, Ljava/util/HashMap;->containsKey(Ljava/lang/Object;)Z`
    `if-nez R, :L`
    `const-string R, "wifi"`
    `invoke-virtual {R, R}, Ljava/util/HashMap;->containsKey(Ljava/lang/Object;)Z`
    `if-nez R, :L`
    `const-string R, "wifi"`
    `const-string R, "cell"`
    `invoke-virtual {R, R}, Ljava/util/HashMap;->containsKey(Ljava/lang/Object;)Z`

### `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `private computeFlipTinyButtonMargin()I` (+11)

    `move-object/from16 R, R`
    `invoke-static {R}, Lcom/android/systemui/miui/globalactions/MiuiGlobalActionsDialog;->bq(Ljava/lang/Object;)I`
    `invoke-static {R}, Lcom/android/systemui/miui/globalactions/MiuiGlobalActionsDialog;->cz(Ljava/lang/Object;)Landroid/content/Context;`
    `invoke-static {R}, Lcom/android/systemui/miui/globalactions/e;->bs(Ljava/lang/Object;)Landroid/content/res/Resources;`
    `invoke-static {}, Lcom/android/systemui/miui/globalactions/MiuiGlobalActionsDialog;->ev()I`
    `invoke-static {R}, Lcom/android/systemui/miui/globalactions/MiuiGlobalActionsDialog;->n(I)I`
    `invoke-static {R, R}, Lcom/android/systemui/miui/globalactions/e;->ep(Ljava/lang/Object;I)F`
    `invoke-static {R}, Lcom/android/systemui/miui/globalactions/MiuiGlobalActionsDialog;->cz(Ljava/lang/Object;)Landroid/content/Context;`

### `smali_classes2/miui/systemui/controlcenter/panel/main/qs/QSListController.smali` :: `public createViewHolder(Landroid/view/ViewGroup;I)Lmiui/systemui/controlcenter/panel/main/recyclerview/MainPanelItemViewHolder;` (+11)

    `const/16 R, 0x8e1`
    `iput-boolean R, R, Lmiui/systemui/controlcenter/qs/tileview/QSTileItemView;->forceHideLabel:L`
    `invoke-static {R, R, R}, Lmiui/systemui/controlcenter/databinding/QsCardItemViewBinding;->inflate(Landroid/view/LayoutInflater;Landroid/view/ViewGroup;Z)Lmiui/systemui/controlcenter/databinding/QsCardItemViewBinding;`
    `invoke-virtual {R}, Lmiui/systemui/controlcenter/databinding/QsCardItemViewBinding;->getRoot()Lmiui/systemui/controlcenter/qs/tileview/QSCardItemView;`
    `new-instance R, Lmiui/systemui/controlcenter/qs/tileview/QSCardItemIconView;`
    `invoke-virtual {R}, Landroid/widget/LinearLayout;->getContext()Landroid/content/Context;`
    `const/4 R, 0x4`
    `invoke-direct/range {R .. R}, Lmiui/systemui/controlcenter/qs/tileview/QSCardItemIconView;-><init>(Landroid/content/Context;Landroid/content/Context;Landroid/util/AttributeSet;ILkotlin/jvm/internal/DefaultConstructorMarker;)V`

### `smali_classes2/miui/systemui/controlcenter/panel/secondary/media/MediaPanelDelegate.smali` :: `public final getListView()Lmiuix/recyclerview/widget/RecyclerView;` (+11)

    `invoke-virtual {R}, Lmiui/systemui/util/ViewController;->getContext()Landroid/content/Context;`
    `move-result-object R`
    `invoke-virtual {R}, Landroid/content/Context;->getResources()Landroid/content/res/Resources;`
    `move-result-object R`
    `invoke-virtual {R}, Landroid/content/res/Resources;->getConfiguration()Landroid/content/res/Configuration;`
    `move-result-object R`
    `iget R, R, Landroid/content/res/Configuration;->orientation:L`
    `const/4 R, 0x2`

### `smali/com/android/systemui/QSControlMiPlayDetailHeader.smali` :: `public final updateSize()V` (+10)

    `invoke-virtual {R}, Landroid/widget/LinearLayout;->getParent()Landroid/view/ViewParent;`
    `instance-of R, R, Landroid/view/View;`
    `check-cast R, Landroid/view/View;`
    `invoke-virtual {R}, Landroid/view/View;->getId()I`
    `const R, 0x7f0a0604`
    `if-ne R, R, :L`
    `const R, 0x7f070c37`
    `goto :L`

### `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `private computeAlarmTextWidth()I` (+10)

    `move-object/from16 R, R`
    `invoke-static {}, Lcom/android/systemui/miui/globalactions/MiuiGlobalActionsDialog;->aq()Z`
    `invoke-static {R}, Lcom/android/systemui/miui/globalactions/MiuiGlobalActionsDialog;->y(Ljava/lang/Object;)I`
    `invoke-static {R}, Lcom/android/systemui/miui/globalactions/MiuiGlobalActionsDialog;->dh(Ljava/lang/Object;)Z`
    `invoke-static {R}, Lcom/android/systemui/miui/globalactions/MiuiGlobalActionsDialog;->fg(Ljava/lang/Object;)Z`
    `invoke-static {R}, Lcom/android/systemui/miui/globalactions/MiuiGlobalActionsDialog;->bq(Ljava/lang/Object;)I`
    `invoke-static {R}, Lcom/android/systemui/miui/globalactions/MiuiGlobalActionsDialog;->cz(Ljava/lang/Object;)Landroid/content/Context;`
    `invoke-static {R}, Lcom/android/systemui/miui/globalactions/e;->bs(Ljava/lang/Object;)Landroid/content/res/Resources;`

### `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `public destroy()V` (+10)

    `move-object/from16 R, R`
    `invoke-static {}, Lcom/android/systemui/miui/globalactions/MiuiGlobalActionsDialog;->bl()Z`
    `invoke-static {}, Lcom/android/systemui/miui/globalactions/MiuiGlobalActionsDialog;->as()Z`
    `invoke-static {R}, Lcom/android/systemui/miui/globalactions/MiuiGlobalActionsDialog;->cc(Ljava/lang/Object;)Ljava/lang/Object;`
    `move-result-object R`
    `invoke-static {}, Lcom/android/systemui/miui/globalactions/MiuiGlobalActionsDialog;->ay()Lmiui/systemui/util/DeviceStateManagerCompat;`
    `move-result-object R`
    `invoke-static {R}, Lcom/android/systemui/miui/globalactions/MiuiGlobalActionsDialog;->es(Ljava/lang/Object;)Ljava/lang/Object;`

### `smali_classes2/miui/systemui/controlcenter/panel/secondary/brightness/BrightnessPanelSliderDelegate.smali` :: `private final applyMaterialBackground()V` (+10)

    `invoke-virtual {R}, Lmiui/systemui/controlcenter/panel/secondary/brightness/BrightnessPanelSliderDelegate;->getVProgressBg()Lmiui/systemui/widget/View;`
    `invoke-virtual {R}, Lmiui/systemui/controlcenter/panel/secondary/brightness/BrightnessPanelSliderDelegate;->getVProgressBg()Lmiui/systemui/widget/View;`
    `invoke-virtual {R}, Lmiui/systemui/util/MiuiColorBlendToken;->getCC_TILE_DEFAULT_BLEND_COLORS()Lmiuix/theme/token/ColorBlendToken;`
    `const/4 R, 0x2`
    `invoke-static {R, R, R, R, R}, Lmiui/systemui/util/MiBackgroundStyle;->setMiBackgroundStyle$default(Landroid/view/View;Lmiuix/theme/token/ColorBlendToken;Lmiui/systemui/util/BionicsToken;ILjava/lang/Object;)V`
    `invoke-virtual {R}, Lmiui/systemui/controlcenter/panel/secondary/brightness/BrightnessPanelSliderDelegate;->getVProgress()Lmiui/systemui/widget/View;`
    `invoke-virtual {R}, Lmiui/systemui/util/MiuiColorBlendToken;->getCC_SLIDER_GLASS_BLEND_COLORS()Lmiuix/theme/token/ColorBlendToken;`
    `goto :L`

### `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `private updateTinyScreenButtonLp(Landroid/widget/FrameLayout$LayoutParams;)V` (+9)

    `move-object/from16 R, R`
    `move-object/from16 R, R`
    `invoke-static {R}, Lcom/android/systemui/miui/globalactions/MiuiGlobalActionsDialog;->bk(Ljava/lang/Object;)I`
    `invoke-static {R}, Lcom/android/systemui/miui/globalactions/MiuiGlobalActionsDialog;->cz(Ljava/lang/Object;)Landroid/content/Context;`
    `invoke-static {R}, Lmiui/systemui/controlcenter/xd/a;->ee(Ljava/lang/Object;)Landroid/view/Display;`
    `invoke-static {R}, Lcom/android/systemui/miui/globalactions/MiuiGlobalActionsDialog;->t(Ljava/lang/Object;)Z`
    `invoke-static {R}, Lcom/android/systemui/miui/globalactions/MiuiGlobalActionsDialog;->cz(Ljava/lang/Object;)Landroid/content/Context;`
    `invoke-static {R}, Lmiui/systemui/controlcenter/xd/a;->ee(Ljava/lang/Object;)Landroid/view/Display;`

### `smali/com/android/systemui/QSControlMiPlayDetailContent$Adapter2.smali` :: `public onCreateViewHolder(Landroid/view/ViewGroup;I)Landroidx/recyclerview/widget/RecyclerView$ViewHolder;` (+8)

    `invoke-virtual {R}, Landroid/view/View;->getResources()Landroid/content/res/Resources;`
    `invoke-virtual {R}, Landroid/content/res/Resources;->getConfiguration()Landroid/content/res/Configuration;`
    `iget R, R, Landroid/content/res/Configuration;->orientation:L`
    `instance-of R, R, Lcom/android/systemui/QSControlMiPlayDetailContentSupportLand;`
    `const R, 0x7f0d0231`
    `invoke-virtual {R}, Landroid/view/View;->getId()I`
    `const R, 0x7f0a0604`
    `const R, 0x7f0d022f`

### `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `private updateMargin(Landroid/view/View;Z)V` (+8)

    `move/from16 R, R`
    `move-object/from16 R, R`
    `move-object/from16 R, R`
    `invoke-static {R}, Lcom/kashi/mpager/a;->bw(Ljava/lang/Object;)Landroid/view/ViewGroup$LayoutParams;`
    `invoke-static {R, R, R}, Lcom/android/systemui/miui/globalactions/MiuiGlobalActionsDialog;->db(Ljava/lang/Object;Ljava/lang/Object;Ljava/lang/Object;)V`
    `invoke-static {R, R}, Lcom/android/systemui/miui/globalactions/MiuiGlobalActionsDialog;->i(Ljava/lang/Object;Ljava/lang/Object;)V`
    `invoke-static {R}, Lcom/android/systemui/miui/globalactions/MiuiGlobalActionsDialog;->ai(Ljava/lang/Object;)Landroid/widget/FrameLayout;`
    `invoke-static {R, R, R}, Lmiui/systemui/controlcenter/panel/main/recyclerview/b;->be(Ljava/lang/Object;Ljava/lang/Object;Ljava/lang/Object;)V`

### `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `private updateTinyScreenViewLp(Landroid/view/View;Z)V` (+8)

    `move/from16 R, R`
    `move-object/from16 R, R`
    `move-object/from16 R, R`
    `invoke-static {R}, Lcom/kashi/mpager/a;->bw(Ljava/lang/Object;)Landroid/view/ViewGroup$LayoutParams;`
    `invoke-static {R, R}, Lcom/android/systemui/miui/globalactions/MiuiGlobalActionsDialog;->bg(Ljava/lang/Object;Ljava/lang/Object;)V`
    `invoke-static {R, R}, Lcom/android/systemui/miui/globalactions/MiuiGlobalActionsDialog;->x(Ljava/lang/Object;Ljava/lang/Object;)V`
    `invoke-static {R}, Lcom/android/systemui/miui/globalactions/MiuiGlobalActionsDialog;->ai(Ljava/lang/Object;)Landroid/widget/FrameLayout;`
    `invoke-static {R, R, R}, Lmiui/systemui/controlcenter/panel/main/recyclerview/b;->be(Ljava/lang/Object;Ljava/lang/Object;Ljava/lang/Object;)V`

### `smali_classes2/miui/systemui/controlcenter/panel/secondary/brightness/BrightnessPanelTilesDelegate.smali` :: `private final updateSize(I)V` (+8)

    `invoke-virtual {R}, Landroid/widget/FrameLayout;->getLayoutParams()Landroid/view/ViewGroup$LayoutParams;`
    `invoke-virtual {R}, Landroid/view/View;->getResources()Landroid/content/res/Resources;`
    `sget R, Lmiui/systemui/controlcenter/R$dimen;->control_center_universal_1_row_with_margin_size:L`
    `invoke-virtual {R}, Landroid/view/View;->getResources()Landroid/content/res/Resources;`
    `sget R, Lmiui/systemui/controlcenter/R$dimen;->qs_tile_item_label_height:L`
    `add-int/2addr R, R`
    `iput R, R, Landroid/view/ViewGroup$LayoutParams;->height:L`
    `invoke-virtual {R, R}, Landroid/view/View;->setLayoutParams(Landroid/view/ViewGroup$LayoutParams;)V`

### `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `private isWideFoldLandscape()Z` (+7)

    `move-object/from16 R, R`
    `invoke-static {}, Lcom/android/systemui/miui/globalactions/MiuiGlobalActionsDialog;->ba()Z`
    `invoke-static {}, Lcom/android/systemui/miui/globalactions/MiuiGlobalActionsDialog;->by()Lmiui/systemui/util/CommonUtils;`
    `move-result-object R`
    `invoke-static {R}, Lcom/android/systemui/miui/globalactions/MiuiGlobalActionsDialog;->cz(Ljava/lang/Object;)Landroid/content/Context;`
    `move-result-object R`
    `invoke-static {R, R}, Lcom/android/systemui/miui/globalactions/MiuiGlobalActionsDialog;->w(Ljava/lang/Object;Ljava/lang/Object;)Z`

### `smali_classes2/miui/systemui/controlcenter/panel/main/qs/CompactQSListController.smali` :: `public onBindViewHolder(Lmiui/systemui/controlcenter/panel/main/recyclerview/MainPanelItemViewHolder;Lmiui/systemui/controlcenter/panel/main/recyclerview/MainPanelListItem;)V` (+7)

    `move-object R, R`
    `instance-of R, R, Lmiui/systemui/controlcenter/panel/main/qs/QSItemViewHolder;`
    `if-eqz R, :L`
    `check-cast R, Lmiui/systemui/controlcenter/panel/main/qs/QSItemViewHolder;`
    `const/4 R, 0x1`
    `invoke-virtual {R, R}, Lmiui/systemui/controlcenter/panel/main/qs/QSItemViewHolder;->setHideLabel(Z)V`
    `:L`

### `smali_classes2/miui/systemui/controlcenter/panel/secondary/brightness/BrightnessPanelSliderDelegate.smali` :: `public final setOutlineRadius(F)V` (+7)

    `invoke-virtual {R}, Lmiui/systemui/controlcenter/panel/secondary/brightness/BrightnessPanelSliderDelegate;->getVProgressBg()Lmiui/systemui/widget/View;`
    `if-eqz R, :L`
    `invoke-virtual {R}, Landroid/view/View;->getBackground()Landroid/graphics/drawable/Drawable;`
    `instance-of R, R, Landroid/graphics/drawable/GradientDrawable;`
    `if-eqz R, :L`
    `check-cast R, Landroid/graphics/drawable/GradientDrawable;`
    `invoke-virtual {R, R}, Landroid/graphics/drawable/GradientDrawable;->setCornerRadius(F)V`

### `smali_classes2/miui/systemui/controlcenter/panel/secondary/media/MediaPanelDelegate.smali` :: `private final initView()V` (+7)

    `iget R, R, Landroid/util/DisplayMetrics;->widthPixels:L`
    `iget R, R, Landroid/util/DisplayMetrics;->heightPixels:L`
    `if-le R, R, :L`
    `invoke-static {R}, Landroid/view/LayoutInflater;->from(Landroid/content/Context;)Landroid/view/LayoutInflater;`
    `const R, 0x7f0d022a`
    `invoke-virtual {R, R, R}, Landroid/view/LayoutInflater;->inflate(ILandroid/view/ViewGroup;)Landroid/view/View;`
    `invoke-direct {R}, Lmiui/systemui/controlcenter/panel/secondary/media/MediaPanelDelegate;->updateSize()V`

### `smali_classes2/miui/systemui/controlcenter/panel/secondary/media/MediaPanelDelegate.smali` :: `private final updateSize()V` (+7)

    `invoke-virtual {R}, Landroid/content/res/Resources;->getDisplayMetrics()Landroid/util/DisplayMetrics;`
    `iget R, R, Landroid/util/DisplayMetrics;->widthPixels:L`
    `iget R, R, Landroid/util/DisplayMetrics;->heightPixels:L`
    `if-gt R, R, :L`
    `const R, 0x7f070c37`
    `goto :L`
    `const R, 0x7f070c3a`

### `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `private provideDisplayMetrics()Landroid/util/DisplayMetrics;` (+6)

    `move-object/from16 R, R`
    `invoke-static {R}, Lcom/android/systemui/miui/globalactions/MiuiGlobalActionsDialog;->cz(Ljava/lang/Object;)Landroid/content/Context;`
    `invoke-static {}, Lmiui/systemui/controlcenter/panel/main/recyclerview/a;->dq()Ljava/lang/String;`
    `invoke-static {R, R}, Lmiui/systemui/controlcenter/panel/main/recyclerview/a;->af(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;`
    `invoke-static {R}, Lmiui/systemui/quicksettings/g;->ed(Ljava/lang/Object;)Landroid/view/Display;`
    `invoke-static {R, R}, Lmiui/systemui/quicksettings/f;->ah(Ljava/lang/Object;Ljava/lang/Object;)V`

### `smali/com/android/systemui/miui/volume/MiuiVolumeDialogView.smali` :: `public dispatchTouchEvent(Landroid/view/MotionEvent;)Z` (+6)

    `invoke-static {R, R}, Lmiui/systemui/controlcenter/ModsCenter/KashiVolume;->touch(Landroid/view/View;Landroid/view/MotionEvent;)V`
    `invoke-static {R, R}, Lmiui/systemui/controlcenter/ModsCenter/VolumeSlim;->onTouch(Landroid/view/View;Landroid/view/MotionEvent;)Z`
    `if-eqz R, :L`
    `const/4 R, 0x1`
    `:L`
    `invoke-super {R, R}, Lcom/android/systemui/miui/volume/widget/ExpandCollapseLinearLayout;->dispatchTouchEvent(Landroid/view/MotionEvent;)Z`

### `smali/com/android/systemui/miui/volume/VolumeColumn.smali` :: `public final setSliderBlendColor(Z)V` (+6)

    `sget-object R, Lmiui/systemui/util/MiuiColorBlendToken;->INSTANCE:L/systemui/util/MiuiColorBlendToken;`
    `invoke-virtual {R}, Lmiui/systemui/util/MiuiColorBlendToken;->getCC_TILE_DEFAULT_BLEND_COLORS()Lmiuix/theme/token/ColorBlendToken;`
    `invoke-virtual {R, R}, Landroid/view/View;->setBackground(Landroid/graphics/drawable/Drawable;)V`
    `invoke-virtual {R}, Lmiui/systemui/util/MiBackgroundStyle;->getDEFAULT_GLASS_TOKEN()Lmiui/systemui/util/BionicsToken;`
    `sget-object R, Lmiui/systemui/util/MiuiColorBlendToken;->INSTANCE:L/systemui/util/MiuiColorBlendToken;`
    `invoke-virtual {R}, Lmiui/systemui/util/MiuiColorBlendToken;->getCC_TILE_DEFAULT_BLEND_COLORS()Lmiuix/theme/token/ColorBlendToken;`

### `smali_classes2/miui/systemui/controlcenter/panel/main/devicecontrol/DeviceControlsEntryController.smali` :: `public available(Z)Z` (+6)

    `iget-object R, R, Lmiui/systemui/controlcenter/panel/main/devicecontrol/DeviceControlsEntryController;->mainPanelModeController:L/a;`
    `invoke-interface {R}, LE0/a;->get()Ljava/lang/Object;`
    `check-cast R, Lmiui/systemui/controlcenter/panel/main/MainPanelModeController;`
    `invoke-virtual {R}, Lmiui/systemui/controlcenter/panel/main/MainPanelModeController;->getMode()Lmiui/systemui/controlcenter/panel/main/MainPanelController$Mode;`
    `sget-object R, Lmiui/systemui/controlcenter/panel/main/MainPanelController$Mode;->EDIT:L/systemui/controlcenter/panel/main/MainPanelController$Mode;`
    `if-eq R, R, :L`

### `smali_classes2/miui/systemui/controlcenter/qs/customize/TileQueryHelper.smali` :: `public constructor <init>(Landroid/content/Context;Lmiui/systemui/util/SystemUIResourcesHelper;Landroid/content/Context;Lmiui/systemui/util/concurrency/DelayableExecutor;LE0/a;Lcom/android/systemui/plugins/miui/qs/MiuiQSHost;Lcom/android/systemui/settings/UserTracker;)V` (+6)

    `new-instance R, Ljava/lang/StringBuilder;`
    `invoke-direct {R}, Ljava/lang/StringBuilder;-><init>()V`
    `invoke-virtual {R, R}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;`
    `const-string R, ",5g_tile,restartsysui,fold_tile"`
    `invoke-virtual {R, R}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;`
    `invoke-virtual {R}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;`

### `smali_classes2/miui/systemui/controlcenter/utils/MiuiQSHostCompat.smali` :: `public final getStockTilesCompat(Lcom/android/systemui/plugins/miui/qs/MiuiQSHost;)Ljava/lang/String;` (+6)

    `new-instance R, Ljava/lang/StringBuilder;`
    `invoke-direct {R}, Ljava/lang/StringBuilder;-><init>()V`
    `invoke-virtual {R, R}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;`
    `const-string R, ",5g_tile,restartsysui,fold_tile,dim_tile,sun_tile,power_tile,restartlauncher,app_tile_add,keep_screen,lsposed_tile"`
    `invoke-virtual {R, R}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;`
    `invoke-virtual {R}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;`

### `smali_classes2/miui/systemui/quicksettings/LocalMiuiQSTilePlugin.smali` :: `public getDefaultTileWithOrder()Ljava/lang/String;` (+6)

    `new-instance R, Ljava/lang/StringBuilder;`
    `invoke-direct {R}, Ljava/lang/StringBuilder;-><init>()V`
    `invoke-virtual {R, R}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;`
    `const-string R, ",lsposed_tile"`
    `invoke-virtual {R, R}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;`
    `invoke-virtual {R}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;`

### `smali_classes2/miui/systemui/quicksettings/LocalMiuiQSTilePlugin.smali` :: `public getStockTileWithOrder()Ljava/lang/String;` (+6)

    `new-instance R, Ljava/lang/StringBuilder;`
    `invoke-direct {R}, Ljava/lang/StringBuilder;-><init>()V`
    `invoke-virtual {R, R}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;`
    `const-string R, ",lsposed_tile"`
    `invoke-virtual {R, R}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;`
    `invoke-virtual {R}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;`

### `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `private applySliderGravity(Landroid/widget/FrameLayout$LayoutParams;)V` (+5)

    `move-object/from16 R, R`
    `move-object/from16 R, R`
    `invoke-static {R}, Lcom/android/systemui/miui/globalactions/MiuiGlobalActionsDialog;->dh(Ljava/lang/Object;)Z`
    `invoke-static {R}, Lcom/android/systemui/miui/globalactions/MiuiGlobalActionsDialog;->fg(Ljava/lang/Object;)Z`
    `invoke-static {R}, Lcom/android/systemui/miui/globalactions/MiuiGlobalActionsDialog;->bq(Ljava/lang/Object;)I`

### `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `private isLargeMuiltDisplay()Z` (+5)

    `move-object/from16 R, R`
    `invoke-static {R}, Lcom/android/systemui/miui/globalactions/MiuiGlobalActionsDialog;->cz(Ljava/lang/Object;)Landroid/content/Context;`
    `move-result-object R`
    `invoke-static {R}, Lcom/android/systemui/miui/globalactions/MiuiGlobalActionsDialog;->v(Ljava/lang/Object;)Z`
    `invoke-static {}, Lcom/android/systemui/miui/globalactions/MiuiGlobalActionsDialog;->bl()Z`

### `smali/com/android/systemui/miui/volume/MiuiRingerModeLayout$RingerButtonHelper.smali` :: `private applyExpandedStyle()V` (+5)

    `const/4 R, 0x1`
    `sget-object R, Lmiui/systemui/util/MiBackgroundStyle;->INSTANCE:L/systemui/util/MiBackgroundStyle;`
    `invoke-virtual {R}, Lmiui/systemui/util/MiBackgroundStyle;->getDEFAULT_GLASS_TOKEN()Lmiui/systemui/util/BionicsToken;`
    `const/4 R, 0x1`
    `invoke-static {R, R, R, R}, Lcom/android/systemui/miui/volume/Util;->setMiViewBackgroundStyle(Landroid/view/View;ILmiuix/theme/token/ColorBlendToken;Lmiui/systemui/util/BionicsToken;)V`

### `smali_classes2/miui/systemui/controlcenter/panel/main/qs/QSRecord$longClickAction$1.smali` :: `public final invoke(Landroid/view/View;)Ljava/lang/Boolean;` (+5)

    `invoke-static {R, R}, Lmiui/systemui/controlcenter/panel/main/qs/QSListController;->qsFoldHandleClick(Lmiui/systemui/controlcenter/panel/main/MainPanelController$Mode;Ljava/lang/String;)Z`
    `invoke-virtual {R}, Landroid/content/Context;->getContentResolver()Landroid/content/ContentResolver;`
    `const-string R, "qs_fold_collapsed"`
    `sget-boolean R, Lmiui/systemui/controlcenter/panel/main/qs/QSListController;->qsFoldCollapsed:L`
    `invoke-static {R, R, R}, Landroid/provider/Settings$System;->putInt(Landroid/content/ContentResolver;Ljava/lang/String;I)Z`

### `smali_classes2/miui/systemui/controlcenter/panel/secondary/brightness/BrightnessPanelSliderDelegate.smali` :: `public prepareShow(Lmiui/systemui/controlcenter/panel/secondary/BrightnessPanelParams;)V` (+5)

    `invoke-virtual {R}, Lmiui/systemui/util/ViewController;->getContext()Landroid/content/Context;`
    `invoke-static {R}, Lmiui/systemui/controlcenter/utils/ControlCenterUtils;->getBackgroundMaterialOpenedWithoutSuperPower(Landroid/content/Context;)Z`
    `if-eqz R, :L`
    `invoke-direct {R}, Lmiui/systemui/controlcenter/panel/secondary/brightness/BrightnessPanelSliderDelegate;->applyMaterialBackground()V`
    `:L`

### `smali_classes2/miui/systemui/util/MiuiColorBlendToken.smali` :: `static constructor <clinit>()V` (+5)

    `const/16 R, -0x4de3`
    `const R, -0xcd521a`
    `const R, -0x171718`
    `const R, -0x1`
    `const R, -0xcd521a`

### `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `private updateScreenSize()V` (+4)

    `move-object/from16 R, R`
    `invoke-static {R}, Lcom/android/systemui/miui/globalactions/MiuiGlobalActionsDialog;->df(Ljava/lang/Object;)Landroid/util/DisplayMetrics;`
    `invoke-static {R}, Lmiui/systemui/controlcenter/panel/main/recyclerview/b;->cb(Ljava/lang/Object;)I`
    `move-result R`

### `smali/com/android/systemui/miui/volume/VolumeColumn.smali` :: `public final onMaterialModeChanged()V` (+4)

    `invoke-virtual {R}, Lcom/android/systemui/miui/volume/VolumeColumn;->isExpanded()Z`
    `move-result R`
    `xor-int/lit8 R, R, 0x1`
    `invoke-virtual {R, R}, Lcom/android/systemui/miui/volume/VolumeColumn;->setSliderBlendColor(Z)V`

### `smali_classes2/miui/systemui/controlcenter/panel/main/MainPanelModeController.smali` :: `private final set_mode(Lmiui/systemui/controlcenter/panel/main/MainPanelController$Mode;)V` (+4)

    `invoke-static {}, Lmiui/systemui/controlcenter/panel/main/qs/EditButtonHeaderEntry;->hideNow()V`
    `invoke-static {}, Lmiui/systemui/controlcenter/panel/main/qs/PowerHeaderEntry;->hideNow()V`
    `invoke-static {}, Lmiui/systemui/controlcenter/panel/main/qs/EditButtonHeaderEntry;->showBack()V`
    `invoke-static {}, Lmiui/systemui/controlcenter/panel/main/qs/PowerHeaderEntry;->showBack()V`

### `smali_classes2/miui/systemui/controlcenter/panel/main/header/MainPanelHeaderController$expandCallback$1.smali` :: `public onAppearanceChanged(ZZ)V` (+4)

    `invoke-static {}, Lmiui/systemui/controlcenter/panel/main/qs/EditButtonHeaderEntry;->showAnim()V`
    `invoke-static {}, Lmiui/systemui/controlcenter/panel/main/qs/PowerHeaderEntry;->showAnim()V`
    `invoke-static {}, Lmiui/systemui/controlcenter/panel/main/qs/EditButtonHeaderEntry;->hideAnim()V`
    `invoke-static {}, Lmiui/systemui/controlcenter/panel/main/qs/PowerHeaderEntry;->hideAnim()V`

### `smali_classes2/miui/systemui/controlcenter/panel/main/qs/EditButtonController.smali` :: `public onStop()V` (+4)

    `iget-object R, R, Lmiui/systemui/controlcenter/panel/main/qs/EditButtonController;->cardLongClickListener:L/systemui/controlcenter/panel/main/qs/EditButtonController$cardLongClickListener$1;`
    `if-eqz R, :L`
    `invoke-virtual {R}, Lmiui/systemui/controlcenter/panel/main/qs/EditButtonController$cardLongClickListener$1;->dismissNow()V`
    `:L`

### `smali/com/android/systemui/QSControlMiPlayDetailHeader.smali` :: `public final onOrientationChanged(I)V` (+3)

    `const R, 0x7f070c38`
    `const R, 0x7f070c38`
    `const R, 0x7f070c38`

### `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `private isLargeFoldExceptWideFold()Z` (+3)

    `move-object/from16 R, R`
    `invoke-static {R}, Lcom/android/systemui/miui/globalactions/MiuiGlobalActionsDialog;->cx(Ljava/lang/Object;)Z`
    `invoke-static {}, Lcom/android/systemui/miui/globalactions/MiuiGlobalActionsDialog;->ba()Z`

### `smali/com/android/systemui/miui/volume/VolumeColumn.smali` :: `private final setRadius(Z)V` (+3)

    `move-object R, R`
    `invoke-static {R}, Lcom/kashi/ios/IosLook;->columnReset(Ljava/lang/Object;)V`
    `invoke-static {R}, Lmiui/systemui/controlcenter/ModsCenter/VolumeSlim;->kashiColumnReset(Ljava/lang/Object;)V`

### `smali_classes2/miui/systemui/controlcenter/panel/main/MainPanelTouchController.smali` :: `public onInterceptTouchEvent(Landroid/view/MotionEvent;)Z` (+3)

    `invoke-static {}, Lmiui/systemui/controlcenter/panel/main/MainPanelTouchController;->isEditPanelShowing()Z`
    `invoke-static {R}, Lmiui/systemui/controlcenter/panel/main/qs/EditButtonHeaderEntry;->hit(Landroid/view/MotionEvent;)Z`
    `invoke-static {R}, Lmiui/systemui/controlcenter/panel/main/qs/PowerHeaderEntry;->hit(Landroid/view/MotionEvent;)Z`

### `smali_classes2/miui/systemui/controlcenter/panel/secondary/brightness/BrightnessPanelSliderDelegate.smali` :: `private final updateIconProgress(Z)V` (+3)

    `const R, -0x1`
    `invoke-static {R}, Landroid/content/res/ColorStateList;->valueOf(I)Landroid/content/res/ColorStateList;`
    `invoke-virtual {R, R}, Landroid/widget/ImageView;->setImageTintList(Landroid/content/res/ColorStateList;)V`

### `smali_classes2/miui/systemui/controlcenter/panel/secondary/volume/VolumePanelController.smali` :: `public prepareShow(Lmiui/systemui/controlcenter/panel/secondary/VolumePanelParams;)Z` (+3)

    `invoke-virtual {R}, Lmiui/systemui/controlcenter/panel/secondary/volume/VolumePanelController;->getDelegate()Lmiui/systemui/controlcenter/panel/secondary/volume/VolumePanelDelegate;`
    `move-result-object R`
    `invoke-virtual {R}, Lmiui/systemui/controlcenter/panel/secondary/volume/VolumePanelDelegate;->onMaterialModeChanged()V`

### `smali_classes2/miui/systemui/controlcenter/qs/QSController$compactTileSpecs$2.smali` :: `public final invoke()Ljava/util/List;` (+3)

    `invoke-virtual {R}, Lmiui/systemui/controlcenter/qs/QSController;->getContext()Landroid/content/Context;`
    `invoke-virtual {R}, Landroid/content/Context;->getResources()Landroid/content/res/Resources;`
    `const R, 0x7f030010`

### `smali_classes2/miui/systemui/controlcenter/qs/tileview/QSCardItemView.smali` :: `public onBindViewHolder(Lmiui/systemui/controlcenter/panel/main/qs/QSRecord;)V` (+3)

    `const/4 R, 0x4`
    `invoke-virtual {R, R}, Landroid/widget/LinearLayout;->setVisibility(I)V`
    `invoke-virtual {R, R}, Landroid/widget/LinearLayout;->setVisibility(I)V`

### `smali_classes2/miui/systemui/util/MiBackgroundStyle.smali` :: `static constructor <clinit>()V` (+3)

    `const R, 0x3f7ae148    # 0.98f`
    `const R, 0x3df5c28f    # 0.12f`
    `const R, 0x3f028f5`

### `smali/com/android/systemui/QSControlMiPlayDetailContentSupportLand.smali` :: `private final resetUILayout()V` (+2)

    `const R, 0x7f070c39`
    `const R, 0x7f070c3b`

### `smali/com/android/systemui/miplay/material/MiPlayMaterialTokensKt$devicesItemUnSelectedToken$2.smali` :: `public final invoke()Lmiui/systemui/ui/material/MaterialToken;` (+2)

    `const R, 0x106000d`
    `const R, 0x106000d`

### `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `private launchSystemUpdater()V` (+2)

    `move-object/from16 R, R`
    `invoke-static {R, R}, Lcom/android/systemui/miui/globalactions/MiuiGlobalActionsDialog;->bv(Ljava/lang/Object;Ljava/lang/Object;)V`

### `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `private synthetic lambda$new$0(Ljava/lang/Boolean;)V` (+2)

    `invoke-static {R}, Lcom/android/systemui/miui/globalactions/f;->cr(Ljava/lang/Object;)Z`
    `invoke-static {R, R}, Lcom/android/systemui/miui/globalactions/MiuiGlobalActionsDialog;->ae(Ljava/lang/Object;Z)V`

### `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `public static bridge synthetic b(Lcom/android/systemui/miui/globalactions/MiuiGlobalActionsDialog;)Landroid/content/Context;` (+2)

    `invoke-static {R}, Lcom/android/systemui/miui/globalactions/MiuiGlobalActionsDialog;->cz(Ljava/lang/Object;)Landroid/content/Context;`
    `move-result-object R`

### `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `public static bridge synthetic c(Lcom/android/systemui/miui/globalactions/MiuiGlobalActionsDialog;)Landroid/content/Context;` (+2)

    `invoke-static {R}, Lcom/android/systemui/miui/globalactions/MiuiGlobalActionsDialog;->cl(Ljava/lang/Object;)Landroid/content/Context;`
    `move-result-object R`

### `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `public static bridge synthetic h()Ljava/lang/String;` (+2)

    `invoke-static {}, Lcom/android/systemui/miui/globalactions/MiuiGlobalActionsDialog;->fa()Ljava/lang/String;`
    `move-result-object R`

### `smali_classes2/miui/systemui/controlcenter/panel/SecondaryPanelRouter.smali` :: `public final routeToBrightnessPanel(Lmiui/systemui/controlcenter/panel/secondary/BrightnessPanelParams;)V` (+2)

    `invoke-static {}, Lmiui/systemui/controlcenter/panel/main/qs/EditButtonHeaderEntry;->hideNow()V`
    `invoke-static {}, Lmiui/systemui/controlcenter/panel/main/qs/PowerHeaderEntry;->hideNow()V`

### `smali_classes2/miui/systemui/controlcenter/panel/SecondaryPanelRouter.smali` :: `public final routeToCustomize(Lmiui/systemui/controlcenter/customize/CustomizeAdapter;)V` (+2)

    `invoke-static {}, Lmiui/systemui/controlcenter/panel/main/qs/EditButtonHeaderEntry;->hideNow()V`
    `invoke-static {}, Lmiui/systemui/controlcenter/panel/main/qs/PowerHeaderEntry;->hideNow()V`

### `smali_classes2/miui/systemui/controlcenter/panel/SecondaryPanelRouter.smali` :: `public final routeToDetail(Lmiui/systemui/controlcenter/panel/secondary/DetailPanelParams;)V` (+2)

    `invoke-static {}, Lmiui/systemui/controlcenter/panel/main/qs/EditButtonHeaderEntry;->hideNow()V`
    `invoke-static {}, Lmiui/systemui/controlcenter/panel/main/qs/PowerHeaderEntry;->hideNow()V`

### `smali_classes2/miui/systemui/controlcenter/panel/SecondaryPanelRouter.smali` :: `public final routeToMain()V` (+2)

    `invoke-static {}, Lmiui/systemui/controlcenter/panel/main/qs/EditButtonHeaderEntry;->showBack()V`
    `invoke-static {}, Lmiui/systemui/controlcenter/panel/main/qs/PowerHeaderEntry;->showBack()V`

### `smali_classes2/miui/systemui/controlcenter/panel/SecondaryPanelRouter.smali` :: `public final routeToMediaPanel(Lmiui/systemui/controlcenter/panel/secondary/MediaPanelParams;)V` (+2)

    `invoke-static {}, Lmiui/systemui/controlcenter/panel/main/qs/EditButtonHeaderEntry;->hideNow()V`
    `invoke-static {}, Lmiui/systemui/controlcenter/panel/main/qs/PowerHeaderEntry;->hideNow()V`

### `smali_classes2/miui/systemui/controlcenter/panel/SecondaryPanelRouter.smali` :: `public final routeToVolumePanel(Lmiui/systemui/controlcenter/panel/secondary/VolumePanelParams;)V` (+2)

    `invoke-static {}, Lmiui/systemui/controlcenter/panel/main/qs/EditButtonHeaderEntry;->hideNow()V`
    `invoke-static {}, Lmiui/systemui/controlcenter/panel/main/qs/PowerHeaderEntry;->hideNow()V`

### `smali_classes2/miui/systemui/controlcenter/panel/main/qs/CompactQSListController.smali` :: `public available(Z)Z` (+2)

    `sget-object R, Lmiui/systemui/controlcenter/panel/main/MainPanelController$Mode;->EDIT:L/systemui/controlcenter/panel/main/MainPanelController$Mode;`
    `xor-int/lit8 R, R, 0x1`

### `smali_classes2/miui/systemui/controlcenter/panel/main/qs/CompactQSListController.smali` :: `public createViewHolder(Landroid/view/ViewGroup;I)Lmiui/systemui/controlcenter/panel/main/recyclerview/MainPanelItemViewHolder;` (+2)

    `const/4 R, 0x1`
    `iput-boolean R, R, Lmiui/systemui/controlcenter/qs/tileview/QSTileItemView;->forceHideLabel:L`

### `smali_classes2/miui/systemui/controlcenter/panel/main/qs/QSListController.smali` :: `public constructor <init>(Lmiui/systemui/controlcenter/windowview/ControlCenterWindowViewImpl;Landroid/content/Context;LE0/a;Lcom/android/systemui/plugins/miui/qs/MiuiQSHost;LE0/a;LE0/a;Lmiui/systemui/controlcenter/panel/main/qs/QSRecord$Factory;Lmiui/systemui/controlcenter/qs/customize/TileQueryHelper;Lmiui/systemui/util/concurrency/DelayableExecutor;Landroid/os/Handler;Landroid/os/Handler;Lmiui/systemui/controlcenter/panel/main/qs/QSCardsController;Lmiui/systemui/controlcenter/panel/main/qs/QSItemViewHolder$Factory;LE0/a;Lmiui/systemui/broadcast/BroadcastDispatcher;Ljava/util/concurrent/Executor;)V` (+2)

    `const R, 0x7f1203e0`
    `iput-object R, R, Lmiui/systemui/controlcenter/panel/main/qs/QSListController;->mcoolNewDivider:L/systemui/controlcenter/panel/main/qs/QSListController$EditModeDividerTextItem;`

### `smali_classes2/miui/systemui/controlcenter/panel/main/qs/QSListController.smali` :: `public onBindViewHolder(Lmiui/systemui/controlcenter/panel/main/recyclerview/MainPanelItemViewHolder;Lmiui/systemui/controlcenter/panel/main/recyclerview/MainPanelListItem;)V` (+2)

    `move-object R, R`
    `invoke-virtual {R, R}, Lmiui/systemui/controlcenter/panel/main/qs/QSItemViewHolder;->setHideLabel(Z)V`

### `smali_classes2/miui/systemui/controlcenter/qs/tileview/QSTileItemIconView.smali` :: `private final updateColor()V` (+2)

    `const R, -0x76aa36`
    `iput R, R, Lmiui/systemui/controlcenter/qs/tileview/QSTileItemIconView;->dolbyTileIconColor:L`

### `smali_classes2/miui/systemui/controlcenter/qs/tileview/QSTileItemView.smali` :: `private final getShowLabel()Z` (+2)

    `iget-boolean R, R, Lmiui/systemui/controlcenter/qs/tileview/QSTileItemView;->forceHideLabel:L`
    `if-eqz R, :L`

### `smali_classes2/miui/systemui/flashlight/NotificationManager.smali` :: `private final getExtraMiuiFocusParam(Landroid/content/Context;)Ljava/lang/String;` (+2)

    `const-string R, "\",\n                        \"colorTitle\": \"#\",\n                        \"content\": \""`
    `const-string R, "\",\n                        \"colorContent\": \"#\",\n                        \"subContent\": \"\",\n                        \"colorSubContent\": \"#\",\n                        \"type\": 2\n                    },\n                    \"bgInfo\": { \"colorBg\": \"#\" },\n                    \"iconTextInfo\" : {\n                       \"title\": \""`

### `smali_classes2/miui/systemui/quicksettings/LocalMiuiQSTilePlugin.smali` :: `public onCreated()V` (+2)

    `iget-object R, R, Lmiui/systemui/quicksettings/LocalMiuiQSTilePlugin;->mSysUIContext:L/content/Context;`
    `invoke-static {R}, Lmiui/systemui/quicksettings/Nr5gTile;->ensureTileInLayout(Landroid/content/Context;)V`

### `smali_classes2/miui/systemui/quicksettings/soundeffect/DolbyAtomsSoundEffectTile.smali` :: `public constructor <init>(Landroid/content/Context;Landroid/content/Context;)V` (+2)

    `const-string R, "dolbyatomssound"`
    `iput-object R, R, Lcom/android/systemui/plugins/qs/QSTile$State;->spec:L/lang/String;`

### `smali/com/android/systemui/MiPlayExtentionsKt.smali` :: `public static final getFullName(Lo0/g;Landroid/content/Context;)Ljava/lang/String;` (+1)

    `const/4 R, 0x0`

### `smali/com/android/systemui/QSControlMiPlayDetailContentSupportLand.smali` :: `public getRVMaxHeight()I` (+1)

    `const R, 0x7f070c3b`

### `smali/com/android/systemui/QSControlMiPlayDetailHeader$addObservers$2.smali` :: `public final invoke(Lcom/miui/miplay/audio/data/MediaMetaData;)V` (+1)

    `const/4 R, 0x4`

### `smali/com/android/systemui/QSControlMiPlayDetailHeader.smali` :: `public final prepareShowPanel()V` (+1)

    `const/4 R, 0x4`

### `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `public static bridge synthetic d(Lcom/android/systemui/miui/globalactions/MiuiGlobalActionsDialog;I)V` (+1)

    `invoke-static {R, R}, Lcom/android/systemui/miui/globalactions/MiuiGlobalActionsDialog;->dj(Ljava/lang/Object;I)V`

### `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `public static bridge synthetic e(Lcom/android/systemui/miui/globalactions/MiuiGlobalActionsDialog;Landroid/content/Context;)Z` (+1)

    `invoke-static {R, R}, Lcom/android/systemui/miui/globalactions/MiuiGlobalActionsDialog;->am(Ljava/lang/Object;Ljava/lang/Object;)Z`

### `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `public static bridge synthetic f(Lcom/android/systemui/miui/globalactions/MiuiGlobalActionsDialog;Landroid/view/MotionEvent;)Z` (+1)

    `invoke-static {R, R}, Lcom/android/systemui/miui/globalactions/MiuiGlobalActionsDialog;->bj(Ljava/lang/Object;Ljava/lang/Object;)Z`

### `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `public static bridge synthetic g(Lcom/android/systemui/miui/globalactions/MiuiGlobalActionsDialog;)V` (+1)

    `invoke-static {R}, Lcom/android/systemui/miui/globalactions/MiuiGlobalActionsDialog;->az(Ljava/lang/Object;)V`

### `smali/com/android/systemui/miui/globalactions/MiuiGlobalActionsDialog.smali` :: `public static synthetic a(Lcom/android/systemui/miui/globalactions/MiuiGlobalActionsDialog;Ljava/lang/Boolean;)V` (+1)

    `invoke-static {R, R}, Lcom/android/systemui/miui/globalactions/MiuiGlobalActionsDialog;->eu(Ljava/lang/Object;Ljava/lang/Object;)V`

### `smali/com/android/systemui/miui/volume/RoundRectFrameLayout.smali` :: `public dispatchDraw(Landroid/graphics/Canvas;)V` (+1)

    `invoke-super {R, R}, Landroid/widget/FrameLayout;->dispatchDraw(Landroid/graphics/Canvas;)V`

### `smali/com/android/systemui/miui/volume/VolumePanelViewController.smali` :: `private onExpandClicked()V` (+1)

    `invoke-static {}, Lmiui/systemui/controlcenter/ModsCenter/VolumeSlim;->exitNow()V`

### `smali/com/android/systemui/miui/volume/VolumePanelViewController.smali` :: `private showVolumePanelH(I)V` (+1)

    `invoke-virtual {R}, Lcom/android/systemui/miui/volume/VolumePanelViewController;->vsEnter()V`

### `smali/com/android/systemui/miui/volume/VolumePanelViewController.smali` :: `public showH(I)V` (+1)

    `invoke-virtual {R, R}, Lcom/android/systemui/miui/volume/VolumePanelViewController;->vsKey(I)V`

### `smali/com/android/systemui/miui/volume/VolumePanelViewController.smali` :: `public static synthetic f(Lcom/android/systemui/miui/volume/VolumePanelViewController;)V` (+1)

    `invoke-virtual {R}, Lcom/android/systemui/miui/volume/VolumePanelViewController;->onMaterialModeChanged()V`

### `smali/miui/systemui/controlcenter/material/ControlCenterMaterialTokens$editButtonToken$2.smali` :: `public final invoke()Lmiui/systemui/controlcenter/material/CCMaterialToken;` (+1)

    `invoke-virtual {R}, Lmiui/systemui/util/MiuiColorBlendToken;->getCC_TILE_DEFAULT_BLEND_COLORS()Lmiuix/theme/token/ColorBlendToken;`

### `smali_classes2/miui/systemui/controlcenter/panel/main/MainPanelTouchController.smali` :: `public handleMotionEvent(Landroid/view/MotionEvent;ZZ)Z` (+1)

    `invoke-static {}, Lmiui/systemui/controlcenter/panel/main/MainPanelTouchController;->isEditPanelShowing()Z`

### `smali_classes2/miui/systemui/controlcenter/panel/main/brightness/BrightnessSliderController.smali` :: `public getRightOrLeft()Z` (+1)

    `const/4 R, 0x1`

### `smali_classes2/miui/systemui/controlcenter/panel/main/devicecontrol/DeviceControlsEntryController.smali` :: `public constructor <init>(Lmiui/systemui/controlcenter/windowview/ControlCenterWindowViewImpl;Landroidx/lifecycle/Lifecycle;Landroid/os/Handler;Ljava/util/concurrent/Executor;LE0/a;Ljava/util/Optional;LE0/a;LE0/a;LE0/a;Lmiui/systemui/util/MiLinkController;Lmiui/systemui/util/HapticFeedback;Lcom/android/systemui/plugins/ActivityStarter;LE0/a;LE0/a;)V` (+1)

    `const/16 R, 0x1`

### `smali_classes2/miui/systemui/controlcenter/panel/main/devicecontrol/DeviceControlsEntryController.smali` :: `public getRightOrLeft()Z` (+1)

    `const/4 R, 0x1`

### `smali_classes2/miui/systemui/controlcenter/panel/main/header/MessageHeaderController$Msg$showConfig$1.smali` :: `public onComplete(Ljava/lang/Object;)V` (+1)

    `const-wide/16 R, 0x0`

### `smali_classes2/miui/systemui/controlcenter/panel/main/media/MediaPlayerController$MediaPlayerViewHolder.smali` :: `private final getDrawableRadius(Landroid/graphics/drawable/Drawable;)F` (+1)

    `sget R, Lmiui/systemui/controlcenter/R$dimen;->device_center_device_item_text_icon_size:L`

### `smali_classes2/miui/systemui/controlcenter/panel/main/media/MediaPlayerController.smali` :: `public constructor <init>(Lmiui/systemui/controlcenter/windowview/ControlCenterWindowViewImpl;Landroidx/lifecycle/Lifecycle;LE0/a;Ljava/util/Optional;LE0/a;LE0/a;Lmiui/systemui/util/HapticFeedback;LE0/a;Lcom/android/systemui/plugins/miui/settings/SuperSaveModeController;Lcom/android/systemui/plugins/miui/settings/IUserTracker;)V` (+1)

    `const/16 R, 0x2`

### `smali_classes2/miui/systemui/controlcenter/panel/main/qs/CompactQSListController.smali` :: `public constructor <init>(Lmiui/systemui/controlcenter/windowview/ControlCenterWindowViewImpl;Landroid/content/Context;LE0/a;Lmiui/systemui/controlcenter/panel/main/qs/QSRecord$Factory;Lmiui/systemui/controlcenter/panel/main/qs/QSItemViewHolder$Factory;Landroid/os/Handler;LE0/a;LE0/a;LE0/a;Lcom/android/systemui/plugins/miui/settings/SuperSaveModeController;)V` (+1)

    `const/16 R, 0x18`

### `smali_classes2/miui/systemui/controlcenter/panel/main/qs/CompactQSListController.smali` :: `public getRightOrLeft()Z` (+1)

    `const/4 R, 0x1`

### `smali_classes2/miui/systemui/controlcenter/panel/main/qs/EditButtonController.smali` :: `public constructor <init>(Lmiui/systemui/controlcenter/windowview/ControlCenterWindowViewImpl;LE0/a;LE0/a;Lcom/android/systemui/plugins/miui/settings/SuperSaveModeController;LE0/a;LE0/a;)V` (+1)

    `const/16 R, 0x28`

### `smali_classes2/miui/systemui/controlcenter/panel/main/qs/EditButtonController.smali` :: `public getRightOrLeft()Z` (+1)

    `const/4 R, 0x1`

### `smali_classes2/miui/systemui/controlcenter/panel/main/qs/QSCardsController.smali` :: `public constructor <init>(Lmiui/systemui/controlcenter/windowview/ControlCenterWindowViewImpl;Landroid/content/Context;LE0/a;Lcom/android/systemui/plugins/miui/qs/MiuiQSHost;LE0/a;Lmiui/systemui/controlcenter/panel/main/qs/QSRecord$Factory;LE0/a;LE0/a;LE0/a;LE0/a;)V` (+1)

    `const/16 R, 0x2`

### `smali_classes2/miui/systemui/controlcenter/panel/main/qs/QSCardsController.smali` :: `public getRightOrLeft()Z` (+1)

    `const/4 R, 0x1`

### `smali_classes2/miui/systemui/controlcenter/panel/main/qs/QSListController.smali` :: `public final addTile(Lmiui/systemui/controlcenter/panel/main/qs/QSRecord;)V` (+1)

    `const/16 R, 0x0`

### `smali_classes2/miui/systemui/controlcenter/panel/main/qs/QSListController.smali` :: `public final removeTile(Lmiui/systemui/controlcenter/panel/main/qs/QSRecord;)V` (+1)

    `const/16 R, 0x0`

### `smali_classes2/miui/systemui/controlcenter/panel/main/qs/QSListController.smali` :: `public onCreate()V` (+1)

    `const/16 R, 0x0`

### `smali_classes2/miui/systemui/controlcenter/panel/main/security/SecurityFooterController.smali` :: `public constructor <init>(Lmiui/systemui/controlcenter/windowview/ControlCenterWindowViewImpl;Landroidx/lifecycle/Lifecycle;Lmiui/systemui/controlcenter/policy/SecurityController;Landroid/os/Handler;Landroid/os/Looper;LE0/a;Lmiui/systemui/util/SystemUIResourcesHelper;LE0/a;LE0/a;Lcom/android/systemui/plugins/miui/statusbar/MiuiSecurityController;)V` (+1)

    `const/16 R, 0x51`

### `smali_classes2/miui/systemui/controlcenter/panel/main/volume/VolumeSliderController.smali` :: `private final updateAnimateIconParams()V` (+1)

    `const/16 R, 0xbc9`

### `smali_classes2/miui/systemui/controlcenter/panel/main/volume/VolumeSliderController.smali` :: `public getRightOrLeft()Z` (+1)

    `const/4 R, 0x1`

### `smali_classes2/miui/systemui/controlcenter/panel/secondary/brightness/BrightnessPanelSliderDelegate.smali` :: `private final updateMaterialTransitionAlpha(F)V` (+1)

    `const/4 R, 0x0`

### `smali_classes2/miui/systemui/controlcenter/panel/secondary/brightness/BrightnessPanelSliderDelegate.smali` :: `private final updateTransitionLayer(Z)V` (+1)

    `invoke-virtual {R, R}, Lmiui/systemui/util/CommonUtils;->setInvisible(Landroid/view/View;)V`

### `smali_classes2/miui/systemui/controlcenter/panel/secondary/brightness/BrightnessPanelTilesDelegate.smali` :: `private final getQSTileItemView(Ljava/lang/String;)Lmiui/systemui/controlcenter/qs/tileview/QSTileItemView;` (+1)

    `invoke-virtual {R}, Lmiui/systemui/controlcenter/qs/tileview/QSTileItemView;->updateSize()V`

### `smali_classes2/miui/systemui/controlcenter/panel/secondary/brightness/BrightnessPanelTilesDelegate.smali` :: `public prepareShow(Lmiui/systemui/controlcenter/panel/secondary/BrightnessPanelParams;)V` (+1)

    `invoke-virtual {R, R}, Lmiui/systemui/controlcenter/panel/secondary/brightness/BrightnessPanelTilesDelegate;->setListening(Z)V`

### `smali_classes2/miui/systemui/controlcenter/panel/secondary/detail/DetailPanelDelegate.smali` :: `private final setupDetailHeader(Lcom/android/systemui/plugins/qs/DetailAdapter;)V` (+1)

    `invoke-static {R, R}, Lbg/mods/plugin/5GSwitch/DetailPanelDelegateHook;->setupDetailHeaderHook(Lmiui/systemui/controlcenter/panel/secondary/detail/DetailPanelDelegate;Lcom/android/systemui/plugins/qs/DetailAdapter;)V`

### `smali_classes2/miui/systemui/controlcenter/panel/secondary/detail/DetailPanelDelegate.smali` :: `private final updateResources(Z)V` (+1)

    `invoke-static {R}, Lbg/mods/plugin/5GSwitch/DetailPanelDelegateHook;->updateResourcesHook(Lmiui/systemui/controlcenter/panel/secondary/detail/DetailPanelDelegate;)V`

### `smali_classes2/miui/systemui/controlcenter/panel/secondary/detail/DetailPanelDelegate.smali` :: `public onCreate()V` (+1)

    `invoke-static {R}, Lbg/mods/plugin/5GSwitch/DetailPanelDelegateHook;->onCreateHook(Lmiui/systemui/controlcenter/panel/secondary/detail/DetailPanelDelegate;)V`

### `smali_classes2/miui/systemui/controlcenter/panel/secondary/detail/DetailPanelDelegate.smali` :: `public onDestroy()V` (+1)

    `invoke-static {}, Lbg/mods/plugin/5GSwitch/DetailPanelDelegateHook;->onDestroyHook()V`

### `smali_classes2/miui/systemui/controlcenter/panel/secondary/media/MediaPanelDelegate.smali` :: `public onConfigurationChanged(I)V` (+1)

    `invoke-direct {R}, Lmiui/systemui/controlcenter/panel/secondary/media/MediaPanelDelegate;->initView()V`

### `smali_classes2/miui/systemui/controlcenter/panel/secondary/volume/VolumePanelDelegate.smali` :: `public final onMaterialModeChanged()V` (+1)

    `invoke-virtual {R}, Lcom/android/systemui/miui/volume/VolumePanelViewController;->onMaterialModeChanged()V`

### `smali_classes2/miui/systemui/controlcenter/panel/secondary/volume/VolumePanelDelegate.smali` :: `public prepareShow(Lmiui/systemui/controlcenter/panel/secondary/VolumePanelParams;)V` (+1)

    `invoke-virtual {R}, Lcom/android/systemui/miui/volume/VolumePanelViewController;->onMaterialModeChanged()V`

### `smali_classes2/miui/systemui/controlcenter/qs/QSController.smali` :: `public final createTile(Ljava/lang/String;)Lcom/android/systemui/plugins/qs/QSTile;` (+1)

    `sput-object R, Lmiui/systemui/controlcenter/qs/QSController;->sInstance:L/systemui/controlcenter/qs/QSController;`

### `smali_classes2/miui/systemui/controlcenter/qs/tileview/QSCardItemView.smali` :: `private final getBackgroundBlendEnabled()Z` (+1)

    `const/4 R, 0x0`

### `smali_classes2/miui/systemui/controlcenter/qs/tileview/QSTileItemIconView.smali` :: `private final updateCornerRadius()V` (+1)

    `sget R, Lmiui/systemui/controlcenter/R$dimen;->control_center_universal_1_row_size:L`

### `smali_classes2/miui/systemui/devicecenter/DeviceCenterController.smali` :: `private final handleDeviceListUpdate(Z)V` (+1)

    `const/4 R, 0x3`

### `smali_classes2/miui/systemui/util/ThemeUtils.smali` :: `public final getDefaultPluginTheme()Z` (+1)

    `const/4 R, 0x1`

### `smali_classes2/miui/systemui/util/ThemeUtils.smali` :: `public final getDefaultSysUiTheme()Z` (+1)

    `const/4 R, 0x1`

### `smali/com/android/systemui/MiPlayExtentionsKt.smali` :: `public static final setItemViewBlurAndBackground(Landroid/view/View;Z)V` (+0)


### `smali/com/android/systemui/QSControlMiPlayDetailContent.smali` :: `public final updateHeight(Ljava/util/ArrayList;ZZ)V` (+0)


### `smali/com/android/systemui/miplay/material/MiPlayMaterialTokensKt$devicesItemSelectedToken$2.smali` :: `public final invoke()Lmiui/systemui/ui/material/MaterialToken;` (+0)


### `smali/com/android/systemui/miui/volume/MiuiVolumeDialogMotion.smali` :: `private updateExpandBgState()V` (+0)


### `smali_classes2/miui/systemui/controlcenter/panel/main/MainPanelContentDistributor.smali` :: `public constructor <init>(Lmiui/systemui/controlcenter/windowview/ControlCenterWindowViewImpl;LE0/a;Lmiui/systemui/controlcenter/panel/main/qs/QSListController;Lmiui/systemui/controlcenter/panel/main/qs/QSCardsController;Lmiui/systemui/controlcenter/panel/main/qs/CompactQSCardController;Lmiui/systemui/controlcenter/panel/main/qs/CompactQSListController;Lmiui/systemui/controlcenter/panel/main/media/MediaPlayerController;Lmiui/systemui/controlcenter/panel/main/brightness/BrightnessSliderController;Lmiui/systemui/controlcenter/panel/main/volume/VolumeSliderController;Lmiui/systemui/controlcenter/panel/main/qs/EditButtonController;Lmiui/systemui/controlcenter/panel/main/qs/WordlessModeController;LE0/a;LE0/a;Lmiui/systemui/controlcenter/panel/main/security/SecurityFooterController;Lmiui/systemui/controlcenter/panel/main/header/HeaderSpaceController$Factory;Lmiui/systemui/controlcenter/panel/main/footer/FooterSpaceController$Factory;Lmiui/systemui/controlcenter/panel/main/recyclerview/MainPanelAdapter$Factory;Landroid/os/Looper;)V` (+0)


### `smali_classes2/miui/systemui/controlcenter/panel/main/devicecontrol/DeviceControlsEntryController.smali` :: `private static final onBindViewHolder$lambda$8(Lmiui/systemui/controlcenter/panel/main/devicecontrol/DeviceControlsEntryController;Landroid/view/View;)Z` (+0)


### `smali_classes2/miui/systemui/controlcenter/panel/main/devicecontrol/DeviceControlsEntryController.smali` :: `public onBindViewHolder()V` (+0)


### `smali_classes2/miui/systemui/controlcenter/panel/main/media/MediaPlayerController.smali` :: `public getRightOrLeft()Z` (+0)


### `smali_classes2/miui/systemui/controlcenter/panel/main/media/MediaPlayerController.smali` :: `public getSpanSize()I` (+0)


### `smali_classes2/miui/systemui/controlcenter/panel/main/qs/CompactQSListController.smali` :: `private final getPrepareShowList()V` (+0)


### `smali_classes2/miui/systemui/controlcenter/panel/main/qs/EditButtonController.smali` :: `public available(Z)Z` (+0)


### `smali_classes2/miui/systemui/controlcenter/panel/main/qs/QSRecord.smali` :: `private final getCardSpanSize()I` (+0)


### `smali_classes2/miui/systemui/controlcenter/panel/main/qs/WordlessModeController.smali` :: `public available(Z)Z` (+0)


### `smali_classes2/miui/systemui/controlcenter/panel/main/recyclerview/ToggleSliderViewHolder.smali` :: `public final updateSize()V` (+0)


### `smali_classes2/miui/systemui/controlcenter/panel/main/security/SecurityFooterController.smali` :: `public available(Z)Z` (+0)


### `smali_classes2/miui/systemui/controlcenter/panel/secondary/brightness/BrightnessPanelSliderDelegate.smali` :: `private final updateBlendBlur(Z)V` (+0)


### `smali_classes2/miui/systemui/controlcenter/panel/secondary/media/MediaPanelAnimator.smali` :: `public frameCallback()V` (+0)


### `smali_classes2/miui/systemui/controlcenter/widget/VerticalSeekBar.smali` :: `public dispatchTouchEvent(Landroid/view/MotionEvent;)Z` (+0)


### `smali_classes2/miui/systemui/controlcenter/windowview/ControlCenterWindowViewImpl.smali` :: `public final setAllowInterceptSwitchEvent(Z)V` (+0)


### `smali_classes2/miui/systemui/dynamicisland/window/DynamicIslandWindowView.smali` :: `public final updateWindowBlur(Z)V` (+0)


### `smali_classes2/miui/systemui/util/ThemeUtils.smali` :: `private final updateDefaultTheme()V` (+0)



## 新增类清单

- `smali/android/widget/NAImageViewOnClickApp$OnClickListener.smali`
- `smali/android/widget/NAImageViewOnClickApp.smali`
- `smali/android/widget/PlayingStatus$1.smali`
- `smali/android/widget/PlayingStatus.smali`
- `smali/android/widget/PowerMenu$1.smali`
- `smali/android/widget/PowerMenu.smali`
- `smali/bg/mods/plugin/5GSwitch/DetailPanelDelegateHook.smali`
- `smali/bg/mods/plugin/5GSwitch/listeners/TitleOnClickListener.smali`
- `smali/bg/mods/plugin/5GSwitch/listeners/TitleOnLongClickListener.smali`
- `smali/bg/mods/plugin/5GSwitch/listeners/ToggleOnCheckedChangeListener.smali`
- `smali/bg/mods/plugin/5GSwitch/listeners/UpdateToggleRunnable.smali`
- `smali/com/android/systemui/MiPlayKeyMargin.smali`
- `smali/com/android/systemui/miui/volume/VolumePanelViewController$KashiRelayout.smali`
- `smali/miui/systemui/controlcenter/panel/main/qs/QsFoldNoOp.smali`
- `smali/miui/systemui/controlcenter/panel/main/qs/QsFoldRefresh.smali`
- `smali/miui/systemui/dynamicisland/anim/DynamicIslandAnimationDelegate$updateOrientationSmallIslandToTempHiddenAnimation$1.smali`
- `smali_classes2/AllinOneButton/AirplaneButton$1.smali`
- `smali_classes2/AllinOneButton/AirplaneButton.smali`
- `smali_classes2/AllinOneButton/BaseButton$1.smali`
- `smali_classes2/AllinOneButton/BaseButton$2.smali`
- `smali_classes2/AllinOneButton/BaseButton$3.smali`
- `smali_classes2/AllinOneButton/BaseButton$6.smali`
- `smali_classes2/AllinOneButton/BaseButton$7.smali`
- `smali_classes2/AllinOneButton/BaseButton.smali`
- `smali_classes2/AllinOneButton/BtButton$1.smali`
- `smali_classes2/AllinOneButton/BtButton$2.smali`
- `smali_classes2/AllinOneButton/BtButton.smali`
- `smali_classes2/AllinOneButton/CellButton$1.smali`
- `smali_classes2/AllinOneButton/CellButton$2.smali`
- `smali_classes2/AllinOneButton/CellButton$3.smali`
- `smali_classes2/AllinOneButton/CellButton$4.smali`
- `smali_classes2/AllinOneButton/CellButton.smali`
- `smali_classes2/AllinOneButton/FlashlightButton$1.smali`
- `smali_classes2/AllinOneButton/FlashlightButton$LP.smali`
- `smali_classes2/AllinOneButton/FlashlightButton$OLC.smali`
- `smali_classes2/AllinOneButton/FlashlightButton.smali`
- `smali_classes2/AllinOneButton/GpsButton$1.smali`
- `smali_classes2/AllinOneButton/GpsButton$2.smali`
- `smali_classes2/AllinOneButton/GpsButton.smali`
- `smali_classes2/AllinOneButton/HotspotButton$1.smali`
- `smali_classes2/AllinOneButton/HotspotButton$2.smali`
- `smali_classes2/AllinOneButton/HotspotButton$3.smali`
- `smali_classes2/AllinOneButton/HotspotButton.smali`
- `smali_classes2/AllinOneButton/MiShareButton$1.smali`
- `smali_classes2/AllinOneButton/MiShareButton$2.smali`
- `smali_classes2/AllinOneButton/MiShareButton.smali`
- `smali_classes2/AllinOneButton/MuteButton$1.smali`
- `smali_classes2/AllinOneButton/MuteButton.smali`
- `smali_classes2/AllinOneButton/NfcButton$1.smali`
- `smali_classes2/AllinOneButton/NfcButton$2.smali`
- `smali_classes2/AllinOneButton/NfcButton.smali`
- `smali_classes2/AllinOneButton/QuietButton$1.smali`
- `smali_classes2/AllinOneButton/QuietButton.smali`
- `smali_classes2/AllinOneButton/RotationButton$1.smali`
- `smali_classes2/AllinOneButton/RotationButton.smali`
- `smali_classes2/AllinOneButton/WifiButton$1.smali`
- `smali_classes2/AllinOneButton/WifiButton.smali`
- `smali_classes2/miui/systemui/controlcenter/panel/main/qs/CardTileConfigHelper.smali`
- `smali_classes2/miui/systemui/controlcenter/panel/main/qs/EditButtonController$cardLongClickListener$1$cardToggleListener$1.smali`
- `smali_classes2/miui/systemui/controlcenter/panel/main/qs/EditButtonController$cardLongClickListener$1$keyboardFocusListener$1.smali`
- `smali_classes2/miui/systemui/controlcenter/panel/main/qs/EditButtonController$cardLongClickListener$1$restartClickListener$1.smali`
- `smali_classes2/miui/systemui/controlcenter/panel/main/qs/EditButtonController$cardLongClickListener$1.smali`
- `smali_classes2/miui/systemui/controlcenter/panel/main/qs/EditButtonController$cardOverlayClickListener$1.smali`
- `smali_classes2/miui/systemui/controlcenter/panel/main/qs/EditButtonHeaderEntry.smali`
- `smali_classes2/miui/systemui/controlcenter/panel/main/qs/PowerHeaderEntry.smali`
- `smali_classes2/miui/systemui/quicksettings/AppIcon.smali`
- `smali_classes2/miui/systemui/quicksettings/AppIconDrawable.smali`
- `smali_classes2/miui/systemui/quicksettings/AppPickerAdapter.smali`
- `smali_classes2/miui/systemui/quicksettings/AppTile$Open.smali`
- `smali_classes2/miui/systemui/quicksettings/AppTile$Picker.smali`
- `smali_classes2/miui/systemui/quicksettings/AppTile.smali`
- `smali_classes2/miui/systemui/quicksettings/AppTilePicker$Add.smali`
- `smali_classes2/miui/systemui/quicksettings/AppTilePicker$Search.smali`
- `smali_classes2/miui/systemui/quicksettings/AppTilePicker$Toggle.smali`
- `smali_classes2/miui/systemui/quicksettings/AppTilePicker.smali`
- `smali_classes2/miui/systemui/quicksettings/AppTiles.smali`
- `smali_classes2/miui/systemui/quicksettings/DimTile.smali`
- `smali_classes2/miui/systemui/quicksettings/FoldTile.smali`
- `smali_classes2/miui/systemui/quicksettings/KeepScreen.smali`
- `smali_classes2/miui/systemui/quicksettings/KeepScreenCustom.smali`
- `smali_classes2/miui/systemui/quicksettings/KeepScreenPick.smali`
- `smali_classes2/miui/systemui/quicksettings/KeepScreenRestore.smali`
- `smali_classes2/miui/systemui/quicksettings/KeepScreenTile.smali`
- `smali_classes2/miui/systemui/quicksettings/LsposedTile.smali`
- `smali_classes2/miui/systemui/quicksettings/Nr5gTile.smali`
- `smali_classes2/miui/systemui/quicksettings/PowerTile$Manager.smali`
- `smali_classes2/miui/systemui/quicksettings/PowerTile.smali`
- `smali_classes2/miui/systemui/quicksettings/RestartLauncherTile.smali`
- `smali_classes2/miui/systemui/quicksettings/RestartSysUITile.smali`
- `smali_classes2/miui/systemui/quicksettings/SunTile.smali`
- `smali_classes3/com/android/systemui/miui/globalactions/KashiIosPowerH$0.smali`
- `smali_classes3/com/android/systemui/miui/globalactions/KashiIosPowerH.smali`
- `smali_classes3/com/android/systemui/miui/globalactions/KashiIosPowerLink.smali`
- `smali_classes3/com/android/systemui/miui/globalactions/d.smali`
- `smali_classes3/com/android/systemui/miui/globalactions/e.smali`
- `smali_classes3/com/android/systemui/miui/globalactions/f.smali`
- `smali_classes3/com/android/systemui/miui/globalactions/g.smali`
- `smali_classes3/com/android/systemui/miui/globalactions/h.smali`
- `smali_classes3/com/kashi/ios/BlurButton$0.smali`
- `smali_classes3/com/kashi/ios/BlurButton$1.smali`
- `smali_classes3/com/kashi/ios/BlurButton.smali`
- `smali_classes3/com/kashi/ios/Ios$1.smali`
- `smali_classes3/com/kashi/ios/Ios.smali`
- `smali_classes3/com/kashi/ios/IosAppTile$0.smali`
- `smali_classes3/com/kashi/ios/IosAppTile$1.smali`
- `smali_classes3/com/kashi/ios/IosAppTile$Mono$1.smali`
- `smali_classes3/com/kashi/ios/IosAppTile$Mono.smali`
- `smali_classes3/com/kashi/ios/IosAppTile.smali`
- `smali_classes3/com/kashi/ios/IosBand.smali`
- `smali_classes3/com/kashi/ios/IosBudsView$0.smali`
- `smali_classes3/com/kashi/ios/IosBudsView$1.smali`
- `smali_classes3/com/kashi/ios/IosBudsView$2.smali`
- `smali_classes3/com/kashi/ios/IosBudsView$3.smali`
- `smali_classes3/com/kashi/ios/IosBudsView$4.smali`
- `smali_classes3/com/kashi/ios/IosBudsView$5.smali`
- `smali_classes3/com/kashi/ios/IosBudsView.smali`
- `smali_classes3/com/kashi/ios/IosChrome$Chip$1.smali`
- `smali_classes3/com/kashi/ios/IosChrome$Chip.smali`
- `smali_classes3/com/kashi/ios/IosChrome.smali`
- `smali_classes3/com/kashi/ios/IosCircleGlass$0.smali`
- `smali_classes3/com/kashi/ios/IosCircleGlass$GlassView$1.smali`
- `smali_classes3/com/kashi/ios/IosCircleGlass$GlassView.smali`
- `smali_classes3/com/kashi/ios/IosCircleGlass.smali`
- `smali_classes3/com/kashi/ios/IosConnEditor$0.smali`
- `smali_classes3/com/kashi/ios/IosConnEditor$1.smali`
- `smali_classes3/com/kashi/ios/IosConnEditor$Panel.smali`
- `smali_classes3/com/kashi/ios/IosConnEditor.smali`
- `smali_classes3/com/kashi/ios/IosConnView$0.smali`
- `smali_classes3/com/kashi/ios/IosConnView$1.smali`
- `smali_classes3/com/kashi/ios/IosConnView$2.smali`
- `smali_classes3/com/kashi/ios/IosConnView$3.smali`
- `smali_classes3/com/kashi/ios/IosConnView$4.smali`
- `smali_classes3/com/kashi/ios/IosConnView$5.smali`
- `smali_classes3/com/kashi/ios/IosConnView$6.smali`
- `smali_classes3/com/kashi/ios/IosConnView$7.smali`
- `smali_classes3/com/kashi/ios/IosConnView$Ref$1$0.smali`
- `smali_classes3/com/kashi/ios/IosConnView$Ref$1.smali`
- `smali_classes3/com/kashi/ios/IosConnView$Ref.smali`
- `smali_classes3/com/kashi/ios/IosConnView.smali`
- `smali_classes3/com/kashi/ios/IosDecor$1.smali`
- `smali_classes3/com/kashi/ios/IosDecor$Dots$1.smali`
- `smali_classes3/com/kashi/ios/IosDecor$Dots.smali`
- `smali_classes3/com/kashi/ios/IosDecor.smali`
- `smali_classes3/com/kashi/ios/IosDetail$0.smali`
- `smali_classes3/com/kashi/ios/IosDetail$1.smali`
- `smali_classes3/com/kashi/ios/IosDetail$10.smali`
- `smali_classes3/com/kashi/ios/IosDetail$11.smali`
- `smali_classes3/com/kashi/ios/IosDetail$12.smali`
- `smali_classes3/com/kashi/ios/IosDetail$13.smali`
- `smali_classes3/com/kashi/ios/IosDetail$2$0.smali`
- `smali_classes3/com/kashi/ios/IosDetail$2.smali`
- `smali_classes3/com/kashi/ios/IosDetail$3.smali`
- `smali_classes3/com/kashi/ios/IosDetail$4.smali`
- `smali_classes3/com/kashi/ios/IosDetail$5.smali`
- `smali_classes3/com/kashi/ios/IosDetail$6.smali`
- `smali_classes3/com/kashi/ios/IosDetail$7.smali`
- `smali_classes3/com/kashi/ios/IosDetail$8.smali`
- `smali_classes3/com/kashi/ios/IosDetail$9.smali`
- `smali_classes3/com/kashi/ios/IosDetail.smali`
- `smali_classes3/com/kashi/ios/IosDetailHolder$1$0.smali`
- `smali_classes3/com/kashi/ios/IosDetailHolder$1.smali`
- `smali_classes3/com/kashi/ios/IosDetailHolder.smali`
- `smali_classes3/com/kashi/ios/IosDotsScrub$0.smali`
- `smali_classes3/com/kashi/ios/IosDotsScrub$Touch$0.smali`
- `smali_classes3/com/kashi/ios/IosDotsScrub$Touch.smali`
- `smali_classes3/com/kashi/ios/IosDotsScrub.smali`
- `smali_classes3/com/kashi/ios/IosEdit$0.smali`
- `smali_classes3/com/kashi/ios/IosEdit$1.smali`
- `smali_classes3/com/kashi/ios/IosEdit$2.smali`
- `smali_classes3/com/kashi/ios/IosEdit$3.smali`
- `smali_classes3/com/kashi/ios/IosEdit$4.smali`
- `smali_classes3/com/kashi/ios/IosEdit$5.smali`
- `smali_classes3/com/kashi/ios/IosEdit$6.smali`
- `smali_classes3/com/kashi/ios/IosEdit.smali`
- `smali_classes3/com/kashi/ios/IosExpand$0.smali`
- `smali_classes3/com/kashi/ios/IosExpand$1.smali`
- `smali_classes3/com/kashi/ios/IosExpand$10.smali`
- `smali_classes3/com/kashi/ios/IosExpand$2.smali`
- `smali_classes3/com/kashi/ios/IosExpand$3.smali`
- `smali_classes3/com/kashi/ios/IosExpand$4.smali`
- `smali_classes3/com/kashi/ios/IosExpand$5.smali`
- `smali_classes3/com/kashi/ios/IosExpand$6.smali`
- `smali_classes3/com/kashi/ios/IosExpand$7.smali`
- `smali_classes3/com/kashi/ios/IosExpand$8.smali`
- `smali_classes3/com/kashi/ios/IosExpand$9.smali`
- `smali_classes3/com/kashi/ios/IosExpand$Host$0.smali`
- `smali_classes3/com/kashi/ios/IosExpand$Host$1.smali`
- `smali_classes3/com/kashi/ios/IosExpand$Host$2.smali`
- `smali_classes3/com/kashi/ios/IosExpand$Host$3.smali`
- `smali_classes3/com/kashi/ios/IosExpand$Host$4.smali`
- `smali_classes3/com/kashi/ios/IosExpand$Host$5.smali`
- `smali_classes3/com/kashi/ios/IosExpand$Host$6.smali`
- `smali_classes3/com/kashi/ios/IosExpand$Host$7.smali`
- `smali_classes3/com/kashi/ios/IosExpand$Host$StripDim.smali`
- `smali_classes3/com/kashi/ios/IosExpand$Host.smali`
- `smali_classes3/com/kashi/ios/IosExpand.smali`
- `smali_classes3/com/kashi/ios/IosFeel$1.smali`
- `smali_classes3/com/kashi/ios/IosFeel.smali`
- `smali_classes3/com/kashi/ios/IosFocusView$0.smali`
- `smali_classes3/com/kashi/ios/IosFocusView$1.smali`
- `smali_classes3/com/kashi/ios/IosFocusView$2.smali`
- `smali_classes3/com/kashi/ios/IosFocusView$3.smali`
- `smali_classes3/com/kashi/ios/IosFocusView$4.smali`
- `smali_classes3/com/kashi/ios/IosFocusView$5.smali`
- `smali_classes3/com/kashi/ios/IosFocusView$6.smali`
- `smali_classes3/com/kashi/ios/IosFocusView$Mode.smali`
- `smali_classes3/com/kashi/ios/IosFocusView.smali`
- `smali_classes3/com/kashi/ios/IosFx.smali`
- `smali_classes3/com/kashi/ios/IosGallery$0.smali`
- `smali_classes3/com/kashi/ios/IosGallery$1.smali`
- `smali_classes3/com/kashi/ios/IosGallery$10.smali`
- `smali_classes3/com/kashi/ios/IosGallery$11.smali`
- `smali_classes3/com/kashi/ios/IosGallery$12.smali`
- `smali_classes3/com/kashi/ios/IosGallery$13.smali`
- `smali_classes3/com/kashi/ios/IosGallery$14.smali`
- `smali_classes3/com/kashi/ios/IosGallery$15.smali`
- `smali_classes3/com/kashi/ios/IosGallery$16.smali`
- `smali_classes3/com/kashi/ios/IosGallery$17.smali`
- `smali_classes3/com/kashi/ios/IosGallery$18.smali`
- `smali_classes3/com/kashi/ios/IosGallery$19.smali`
- `smali_classes3/com/kashi/ios/IosGallery$2.smali`
- `smali_classes3/com/kashi/ios/IosGallery$20.smali`
- `smali_classes3/com/kashi/ios/IosGallery$21.smali`
- `smali_classes3/com/kashi/ios/IosGallery$22.smali`
- `smali_classes3/com/kashi/ios/IosGallery$23.smali`
- `smali_classes3/com/kashi/ios/IosGallery$24.smali`
- `smali_classes3/com/kashi/ios/IosGallery$25.smali`
- `smali_classes3/com/kashi/ios/IosGallery$26.smali`
- `smali_classes3/com/kashi/ios/IosGallery$27.smali`
- `smali_classes3/com/kashi/ios/IosGallery$28.smali`
- `smali_classes3/com/kashi/ios/IosGallery$29.smali`
- `smali_classes3/com/kashi/ios/IosGallery$3.smali`
- `smali_classes3/com/kashi/ios/IosGallery$30.smali`
- `smali_classes3/com/kashi/ios/IosGallery$31.smali`
- `smali_classes3/com/kashi/ios/IosGallery$32.smali`
- `smali_classes3/com/kashi/ios/IosGallery$33.smali`
- `smali_classes3/com/kashi/ios/IosGallery$34.smali`
- `smali_classes3/com/kashi/ios/IosGallery$35.smali`
- `smali_classes3/com/kashi/ios/IosGallery$36.smali`
- `smali_classes3/com/kashi/ios/IosGallery$37.smali`
- `smali_classes3/com/kashi/ios/IosGallery$38.smali`
- `smali_classes3/com/kashi/ios/IosGallery$39.smali`
- `smali_classes3/com/kashi/ios/IosGallery$4.smali`
- `smali_classes3/com/kashi/ios/IosGallery$40.smali`
- `smali_classes3/com/kashi/ios/IosGallery$41.smali`
- `smali_classes3/com/kashi/ios/IosGallery$42.smali`
- `smali_classes3/com/kashi/ios/IosGallery$43.smali`
- `smali_classes3/com/kashi/ios/IosGallery$44.smali`
- `smali_classes3/com/kashi/ios/IosGallery$45.smali`
- `smali_classes3/com/kashi/ios/IosGallery$46.smali`
- `smali_classes3/com/kashi/ios/IosGallery$47.smali`
- `smali_classes3/com/kashi/ios/IosGallery$48.smali`
- `smali_classes3/com/kashi/ios/IosGallery$49.smali`
- `smali_classes3/com/kashi/ios/IosGallery$5.smali`
- `smali_classes3/com/kashi/ios/IosGallery$50.smali`
- `smali_classes3/com/kashi/ios/IosGallery$51.smali`
- `smali_classes3/com/kashi/ios/IosGallery$6.smali`
- `smali_classes3/com/kashi/ios/IosGallery$7.smali`
- `smali_classes3/com/kashi/ios/IosGallery$8.smali`
- `smali_classes3/com/kashi/ios/IosGallery$9.smali`
- `smali_classes3/com/kashi/ios/IosGallery$Entry.smali`
- `smali_classes3/com/kashi/ios/IosGallery$Getter.smali`
- `smali_classes3/com/kashi/ios/IosGallery$GlyphView.smali`
- `smali_classes3/com/kashi/ios/IosGallery$IosSliderView$Listener.smali`
- `smali_classes3/com/kashi/ios/IosGallery$IosSliderView.smali`
- `smali_classes3/com/kashi/ios/IosGallery$IosSwitch$0.smali`
- `smali_classes3/com/kashi/ios/IosGallery$IosSwitch$1.smali`
- `smali_classes3/com/kashi/ios/IosGallery$IosSwitch$Listener.smali`
- `smali_classes3/com/kashi/ios/IosGallery$IosSwitch.smali`
- `smali_classes3/com/kashi/ios/IosGallery$Picker.smali`
- `smali_classes3/com/kashi/ios/IosGallery$Setter.smali`
- `smali_classes3/com/kashi/ios/IosGallery.smali`
- `smali_classes3/com/kashi/ios/IosGhostFrom.smali`
- `smali_classes3/com/kashi/ios/IosGlass.smali`
- `smali_classes3/com/kashi/ios/IosIcons$Color.smali`
- `smali_classes3/com/kashi/ios/IosIcons$Glyph$1.smali`
- `smali_classes3/com/kashi/ios/IosIcons$Glyph.smali`
- `smali_classes3/com/kashi/ios/IosIcons.smali`
- `smali_classes3/com/kashi/ios/IosIsland$0.smali`
- `smali_classes3/com/kashi/ios/IosIsland$Editor$0.smali`
- `smali_classes3/com/kashi/ios/IosIsland$Editor$1.smali`
- `smali_classes3/com/kashi/ios/IosIsland$Editor$2.smali`
- `smali_classes3/com/kashi/ios/IosIsland$Editor$3.smali`
- `smali_classes3/com/kashi/ios/IosIsland$Editor$4.smali`
- `smali_classes3/com/kashi/ios/IosIsland$Editor$5.smali`
- `smali_classes3/com/kashi/ios/IosIsland$Editor$6.smali`
- `smali_classes3/com/kashi/ios/IosIsland$Editor.smali`
- `smali_classes3/com/kashi/ios/IosIsland.smali`
- `smali_classes3/com/kashi/ios/IosIslandPause.smali`
- `smali_classes3/com/kashi/ios/IosLand.smali`
- `smali_classes3/com/kashi/ios/IosLayout$0.smali`
- `smali_classes3/com/kashi/ios/IosLayout$Pager$1.smali`
- `smali_classes3/com/kashi/ios/IosLayout$Pager.smali`
- `smali_classes3/com/kashi/ios/IosLayout.smali`
- `smali_classes3/com/kashi/ios/IosLayoutIO$0.smali`
- `smali_classes3/com/kashi/ios/IosLayoutIO$Note.smali`
- `smali_classes3/com/kashi/ios/IosLayoutIO.smali`
- `smali_classes3/com/kashi/ios/IosLiquid$0.smali`
- `smali_classes3/com/kashi/ios/IosLiquid$1.smali`
- `smali_classes3/com/kashi/ios/IosLiquid$Bump.smali`
- `smali_classes3/com/kashi/ios/IosLiquid.smali`
- `smali_classes3/com/kashi/ios/IosLook$0.smali`
- `smali_classes3/com/kashi/ios/IosLook$1.smali`
- `smali_classes3/com/kashi/ios/IosLook$2.smali`
- `smali_classes3/com/kashi/ios/IosLook$3.smali`
- `smali_classes3/com/kashi/ios/IosLook$4.smali`
- `smali_classes3/com/kashi/ios/IosLook$5.smali`
- `smali_classes3/com/kashi/ios/IosLook$6.smali`
- `smali_classes3/com/kashi/ios/IosLook$NoPaint.smali`
- `smali_classes3/com/kashi/ios/IosLook.smali`
- `smali_classes3/com/kashi/ios/IosMedia$0.smali`
- `smali_classes3/com/kashi/ios/IosMedia$1$0.smali`
- `smali_classes3/com/kashi/ios/IosMedia$1.smali`
- `smali_classes3/com/kashi/ios/IosMedia$2.smali`
- `smali_classes3/com/kashi/ios/IosMedia$3.smali`
- `smali_classes3/com/kashi/ios/IosMedia$4.smali`
- `smali_classes3/com/kashi/ios/IosMedia$5.smali`
- `smali_classes3/com/kashi/ios/IosMedia$Listener.smali`
- `smali_classes3/com/kashi/ios/IosMedia.smali`
- `smali_classes3/com/kashi/ios/IosMediaView$0.smali`
- `smali_classes3/com/kashi/ios/IosMediaView$1.smali`
- `smali_classes3/com/kashi/ios/IosMediaView$2.smali`
- `smali_classes3/com/kashi/ios/IosMediaView$3.smali`
- `smali_classes3/com/kashi/ios/IosMediaView$4.smali`
- `smali_classes3/com/kashi/ios/IosMediaView$5.smali`
- `smali_classes3/com/kashi/ios/IosMediaView$6.smali`
- `smali_classes3/com/kashi/ios/IosMediaView$7.smali`
- `smali_classes3/com/kashi/ios/IosMediaView$8.smali`
- `smali_classes3/com/kashi/ios/IosMediaView$9.smali`
- `smali_classes3/com/kashi/ios/IosMediaView$Spectrum$1.smali`
- `smali_classes3/com/kashi/ios/IosMediaView$Spectrum.smali`
- `smali_classes3/com/kashi/ios/IosMediaView.smali`
- `smali_classes3/com/kashi/ios/IosMenu$0.smali`
- `smali_classes3/com/kashi/ios/IosMenu$1.smali`
- `smali_classes3/com/kashi/ios/IosMenu$2.smali`
- `smali_classes3/com/kashi/ios/IosMenu$3.smali`
- `smali_classes3/com/kashi/ios/IosMenu$4.smali`
- `smali_classes3/com/kashi/ios/IosMenu$5.smali`
- `smali_classes3/com/kashi/ios/IosMenu$6.smali`
- `smali_classes3/com/kashi/ios/IosMenu$Host$0.smali`
- `smali_classes3/com/kashi/ios/IosMenu$Host$1.smali`
- `smali_classes3/com/kashi/ios/IosMenu$Host$2.smali`
- `smali_classes3/com/kashi/ios/IosMenu$Host$3.smali`
- `smali_classes3/com/kashi/ios/IosMenu$Host$4.smali`
- `smali_classes3/com/kashi/ios/IosMenu$Host$5.smali`
- `smali_classes3/com/kashi/ios/IosMenu$Host.smali`
- `smali_classes3/com/kashi/ios/IosMenu$Row.smali`
- `smali_classes3/com/kashi/ios/IosMenu.smali`
- `smali_classes3/com/kashi/ios/IosModel$0.smali`
- `smali_classes3/com/kashi/ios/IosModel$1.smali`
- `smali_classes3/com/kashi/ios/IosModel$2.smali`
- `smali_classes3/com/kashi/ios/IosModel$3.smali`
- `smali_classes3/com/kashi/ios/IosModel$E.smali`
- `smali_classes3/com/kashi/ios/IosModel.smali`
- `smali_classes3/com/kashi/ios/IosModules$0.smali`
- `smali_classes3/com/kashi/ios/IosModules$BandHolder.smali`
- `smali_classes3/com/kashi/ios/IosModules$BandItem.smali`
- `smali_classes3/com/kashi/ios/IosModules$Content.smali`
- `smali_classes3/com/kashi/ios/IosModules$Holder.smali`
- `smali_classes3/com/kashi/ios/IosModules$Item.smali`
- `smali_classes3/com/kashi/ios/IosModules$MediaHolder$0.smali`
- `smali_classes3/com/kashi/ios/IosModules$MediaHolder$1.smali`
- `smali_classes3/com/kashi/ios/IosModules$MediaHolder.smali`
- `smali_classes3/com/kashi/ios/IosModules$ModuleView.smali`
- `smali_classes3/com/kashi/ios/IosModules.smali`
- `smali_classes3/com/kashi/ios/IosPower$0.smali`
- `smali_classes3/com/kashi/ios/IosPower$1.smali`
- `smali_classes3/com/kashi/ios/IosPower$2.smali`
- `smali_classes3/com/kashi/ios/IosPower$3.smali`
- `smali_classes3/com/kashi/ios/IosPower$4.smali`
- `smali_classes3/com/kashi/ios/IosPower$5.smali`
- `smali_classes3/com/kashi/ios/IosPower$6.smali`
- `smali_classes3/com/kashi/ios/IosPower$7.smali`
- `smali_classes3/com/kashi/ios/IosPower$8.smali`
- `smali_classes3/com/kashi/ios/IosPower$9.smali`
- `smali_classes3/com/kashi/ios/IosPower$Host.smali`
- `smali_classes3/com/kashi/ios/IosPower$Item.smali`
- `smali_classes3/com/kashi/ios/IosPower$Track$1.smali`
- `smali_classes3/com/kashi/ios/IosPower$Track.smali`
- `smali_classes3/com/kashi/ios/IosPower.smali`
- `smali_classes3/com/kashi/ios/IosPreview.smali`
- `smali_classes3/com/kashi/ios/IosReorder$0.smali`
- `smali_classes3/com/kashi/ios/IosReorder$1.smali`
- `smali_classes3/com/kashi/ios/IosReorder$2.smali`
- `smali_classes3/com/kashi/ios/IosReorder$3.smali`
- `smali_classes3/com/kashi/ios/IosReorder.smali`
- `smali_classes3/com/kashi/ios/IosSig$1$0.smali`
- `smali_classes3/com/kashi/ios/IosSig$1.smali`
- `smali_classes3/com/kashi/ios/IosSig$Pill.smali`
- `smali_classes3/com/kashi/ios/IosSig.smali`
- `smali_classes3/com/kashi/ios/IosSoundView$0.smali`
- `smali_classes3/com/kashi/ios/IosSoundView$1.smali`
- `smali_classes3/com/kashi/ios/IosSoundView$2.smali`
- `smali_classes3/com/kashi/ios/IosSoundView$3.smali`
- `smali_classes3/com/kashi/ios/IosSoundView$4.smali`
- `smali_classes3/com/kashi/ios/IosSoundView$5.smali`
- `smali_classes3/com/kashi/ios/IosSoundView$6.smali`
- `smali_classes3/com/kashi/ios/IosSoundView.smali`
- `smali_classes3/com/kashi/ios/IosTallTile$BigIcon.smali`
- `smali_classes3/com/kashi/ios/IosTallTile$Labels.smali`
- `smali_classes3/com/kashi/ios/IosTallTile$QuietPaint.smali`
- `smali_classes3/com/kashi/ios/IosTallTile.smali`
- `smali_classes3/com/kashi/ios/IosText.smali`
- `smali_classes3/com/kashi/ios/a.smali`
- `smali_classes3/com/kashi/ios/b.smali`
- `smali_classes3/com/kashi/ios/c.smali`
- `smali_classes3/com/kashi/ios/d.smali`
- `smali_classes3/com/kashi/ios/e.smali`
- `smali_classes3/com/kashi/ios/f.smali`
- `smali_classes3/com/kashi/mpager/KashiLocalSession$0.smali`
- `smali_classes3/com/kashi/mpager/KashiLocalSession$1$0.smali`
- `smali_classes3/com/kashi/mpager/KashiLocalSession$1$1.smali`
- `smali_classes3/com/kashi/mpager/KashiLocalSession$1$2.smali`
- `smali_classes3/com/kashi/mpager/KashiLocalSession$1$3.smali`
- `smali_classes3/com/kashi/mpager/KashiLocalSession$1.smali`
- `smali_classes3/com/kashi/mpager/KashiLocalSession$2$0.smali`
- `smali_classes3/com/kashi/mpager/KashiLocalSession$2.smali`
- `smali_classes3/com/kashi/mpager/KashiLocalSession$3.smali`
- `smali_classes3/com/kashi/mpager/KashiLocalSession$Writer.smali`
- `smali_classes3/com/kashi/mpager/KashiLocalSession.smali`
- `smali_classes3/com/kashi/mpager/KashiMediaPager$0.smali`
- `smali_classes3/com/kashi/mpager/KashiMediaPager$1$1.smali`
- `smali_classes3/com/kashi/mpager/KashiMediaPager$1.smali`
- `smali_classes3/com/kashi/mpager/KashiMediaPager$2.smali`
- `smali_classes3/com/kashi/mpager/KashiMediaPager$3.smali`
- `smali_classes3/com/kashi/mpager/KashiMediaPager$4.smali`
- `smali_classes3/com/kashi/mpager/KashiMediaPager$Dots.smali`
- `smali_classes3/com/kashi/mpager/KashiMediaPager.smali`
- `smali_classes3/com/kashi/mpager/a.smali`
- `smali_classes3/com/kashi/mpager/b.smali`
- `smali_classes3/miui/systemui/controlcenter/ModsCenter/CCBadgeDrawable.smali`
- `smali_classes3/miui/systemui/controlcenter/ModsCenter/CCGroupAddView$1.smali`
- `smali_classes3/miui/systemui/controlcenter/ModsCenter/CCGroupAddView.smali`
- `smali_classes3/miui/systemui/controlcenter/ModsCenter/CCGroupContainer$1.smali`
- `smali_classes3/miui/systemui/controlcenter/ModsCenter/CCGroupContainer$2.smali`
- `smali_classes3/miui/systemui/controlcenter/ModsCenter/CCGroupContainer$3.smali`
- `smali_classes3/miui/systemui/controlcenter/ModsCenter/CCGroupContainer$Content.smali`
- `smali_classes3/miui/systemui/controlcenter/ModsCenter/CCGroupContainer$Holder.smali`
- `smali_classes3/miui/systemui/controlcenter/ModsCenter/CCGroupContainer$Item.smali`
- `smali_classes3/miui/systemui/controlcenter/ModsCenter/CCGroupContainer.smali`
- `smali_classes3/miui/systemui/controlcenter/ModsCenter/CCGroupContainerDetailAdapter$Grid.smali`
- `smali_classes3/miui/systemui/controlcenter/ModsCenter/CCGroupContainerDetailAdapter.smali`
- `smali_classes3/miui/systemui/controlcenter/ModsCenter/CCGroupContainerView$1.smali`
- `smali_classes3/miui/systemui/controlcenter/ModsCenter/CCGroupContainerView$GroupCell$1.smali`
- `smali_classes3/miui/systemui/controlcenter/ModsCenter/CCGroupContainerView$GroupCell.smali`
- `smali_classes3/miui/systemui/controlcenter/ModsCenter/CCGroupContainerView.smali`
- `smali_classes3/miui/systemui/controlcenter/ModsCenter/CCGroupPanel$1.smali`
- `smali_classes3/miui/systemui/controlcenter/ModsCenter/CCGroupPanel$2.smali`
- `smali_classes3/miui/systemui/controlcenter/ModsCenter/CCGroupPanel$Card$1.smali`
- `smali_classes3/miui/systemui/controlcenter/ModsCenter/CCGroupPanel$Card.smali`
- `smali_classes3/miui/systemui/controlcenter/ModsCenter/CCGroupPanel.smali`
- `smali_classes3/miui/systemui/controlcenter/ModsCenter/CCHandleDrawable.smali`
- `smali_classes3/miui/systemui/controlcenter/ModsCenter/CCMainPanelUpdater.smali`
- `smali_classes3/miui/systemui/controlcenter/ModsCenter/CCNewTileCardView$1.smali`
- `smali_classes3/miui/systemui/controlcenter/ModsCenter/CCNewTileCardView$2.smali`
- `smali_classes3/miui/systemui/controlcenter/ModsCenter/CCNewTileCardView$Holder.smali`
- `smali_classes3/miui/systemui/controlcenter/ModsCenter/CCNewTileCardView.smali`
- `smali_classes3/miui/systemui/controlcenter/ModsCenter/CCTileButton$1.smali`
- `smali_classes3/miui/systemui/controlcenter/ModsCenter/CCTileButton$2$1.smali`
- `smali_classes3/miui/systemui/controlcenter/ModsCenter/CCTileButton$2.smali`
- `smali_classes3/miui/systemui/controlcenter/ModsCenter/CCTileButton$GlassOutline.smali`
- `smali_classes3/miui/systemui/controlcenter/ModsCenter/CCTileButton$OnRemoveListener.smali`
- `smali_classes3/miui/systemui/controlcenter/ModsCenter/CCTileButton.smali`
- `smali_classes3/miui/systemui/controlcenter/ModsCenter/CCTouchHandler.smali`
- `smali_classes3/miui/systemui/controlcenter/ModsCenter/CustomDetailHolder.smali`
- `smali_classes3/miui/systemui/controlcenter/ModsCenter/CustomTileStyle.smali`
- `smali_classes3/miui/systemui/controlcenter/ModsCenter/FreeLayout$1.smali`
- `smali_classes3/miui/systemui/controlcenter/ModsCenter/FreeLayout$2.smali`
- `smali_classes3/miui/systemui/controlcenter/ModsCenter/FreeLayout$3.smali`
- `smali_classes3/miui/systemui/controlcenter/ModsCenter/FreeLayout$4.smali`
- `smali_classes3/miui/systemui/controlcenter/ModsCenter/FreeLayout.smali`
- `smali_classes3/miui/systemui/controlcenter/ModsCenter/KashiIosBridge.smali`
- `smali_classes3/miui/systemui/controlcenter/ModsCenter/KashiVolume$0.smali`
- `smali_classes3/miui/systemui/controlcenter/ModsCenter/KashiVolume$1.smali`
- `smali_classes3/miui/systemui/controlcenter/ModsCenter/KashiVolume$2.smali`
- `smali_classes3/miui/systemui/controlcenter/ModsCenter/KashiVolume$3.smali`
- `smali_classes3/miui/systemui/controlcenter/ModsCenter/KashiVolume$4.smali`
- `smali_classes3/miui/systemui/controlcenter/ModsCenter/KashiVolume.smali`
- `smali_classes3/miui/systemui/controlcenter/ModsCenter/LandscapeLayout$1.smali`
- `smali_classes3/miui/systemui/controlcenter/ModsCenter/LandscapeLayout$2.smali`
- `smali_classes3/miui/systemui/controlcenter/ModsCenter/LandscapeLayout$3.smali`
- `smali_classes3/miui/systemui/controlcenter/ModsCenter/LandscapeLayout$4.smali`
- `smali_classes3/miui/systemui/controlcenter/ModsCenter/LandscapeLayout$5.smali`
- `smali_classes3/miui/systemui/controlcenter/ModsCenter/LandscapeLayout$ResetContent.smali`
- `smali_classes3/miui/systemui/controlcenter/ModsCenter/LandscapeLayout$ResetHolder.smali`
- `smali_classes3/miui/systemui/controlcenter/ModsCenter/LandscapeLayout$ResetItem.smali`
- `smali_classes3/miui/systemui/controlcenter/ModsCenter/LandscapeLayout$ResetView$1.smali`
- `smali_classes3/miui/systemui/controlcenter/ModsCenter/LandscapeLayout$ResetView.smali`
- `smali_classes3/miui/systemui/controlcenter/ModsCenter/LandscapeLayout.smali`
- `smali_classes3/miui/systemui/controlcenter/ModsCenter/MediaProgressView$1.smali`
- `smali_classes3/miui/systemui/controlcenter/ModsCenter/MediaProgressView$2.smali`
- `smali_classes3/miui/systemui/controlcenter/ModsCenter/MediaProgressView.smali`
- `smali_classes3/miui/systemui/controlcenter/ModsCenter/NewGridLayoutManager$1.smali`
- `smali_classes3/miui/systemui/controlcenter/ModsCenter/NewGridLayoutManager$Placement.smali`
- `smali_classes3/miui/systemui/controlcenter/ModsCenter/NewGridLayoutManager.smali`
- `smali_classes3/miui/systemui/controlcenter/ModsCenter/ShapePreviewDrawable$1.smali`
- `smali_classes3/miui/systemui/controlcenter/ModsCenter/ShapePreviewDrawable$2.smali`
- `smali_classes3/miui/systemui/controlcenter/ModsCenter/ShapePreviewDrawable$3.smali`
- `smali_classes3/miui/systemui/controlcenter/ModsCenter/ShapePreviewDrawable.smali`
- `smali_classes3/miui/systemui/controlcenter/ModsCenter/VolumeSlim$Anim.smali`
- `smali_classes3/miui/systemui/controlcenter/ModsCenter/VolumeSlim$KashiLayout.smali`
- `smali_classes3/miui/systemui/controlcenter/ModsCenter/VolumeSlim$KashiPost.smali`
- `smali_classes3/miui/systemui/controlcenter/ModsCenter/VolumeSlim$Outline.smali`
- `smali_classes3/miui/systemui/controlcenter/ModsCenter/VolumeSlim$Shake.smali`
- `smali_classes3/miui/systemui/controlcenter/ModsCenter/VolumeSlim.smali`
- `smali_classes3/miui/systemui/controlcenter/panel/main/g.smali`
- `smali_classes3/miui/systemui/controlcenter/panel/main/recyclerview/a.smali`
- `smali_classes3/miui/systemui/controlcenter/panel/main/recyclerview/b.smali`
- `smali_classes3/miui/systemui/controlcenter/panel/main/recyclerview/c.smali`
- `smali_classes3/miui/systemui/controlcenter/xd/KashiTexture.smali`
- `smali_classes3/miui/systemui/controlcenter/xd/XdAdvanceTextureTile$1.smali`
- `smali_classes3/miui/systemui/controlcenter/xd/XdAdvanceTextureTile.smali`
- `smali_classes3/miui/systemui/controlcenter/xd/XdCaffeineTile$1.smali`
- `smali_classes3/miui/systemui/controlcenter/xd/XdCaffeineTile$2.smali`
- `smali_classes3/miui/systemui/controlcenter/xd/XdCaffeineTile$3.smali`
- `smali_classes3/miui/systemui/controlcenter/xd/XdCaffeineTile$4.smali`
- `smali_classes3/miui/systemui/controlcenter/xd/XdCaffeineTile.smali`
- `smali_classes3/miui/systemui/controlcenter/xd/a.smali`
- `smali_classes3/miui/systemui/controlcenter/xd/b.smali`
- `smali_classes3/miui/systemui/controlcenter/xd/c.smali`
- `smali_classes3/miui/systemui/controlcenter/xd/d.smali`
- `smali_classes3/miui/systemui/quicksettings/KashiIds.smali`
- `smali_classes3/miui/systemui/quicksettings/RestartSystemUITile.smali`
- `smali_classes3/miui/systemui/quicksettings/d.smali`
- `smali_classes3/miui/systemui/quicksettings/e.smali`
- `smali_classes3/miui/systemui/quicksettings/f.smali`
- `smali_classes3/miui/systemui/quicksettings/g.smali`
