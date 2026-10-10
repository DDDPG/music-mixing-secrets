# v3 explanatory visualization assets

16 independent SVG + PNG pairs for the eight-page story. These are reusable source figures, not final social-card layouts.

Palette: white #ffffff, ink #1d1d1f, blue #0066cc, subtle comparison #7c8997. Editable SVG text uses Noto Sans CJK SC; rendered PNGs are 1800 px wide.

## Usage rules

- Keep every required caption and assumption with its figure. Never relabel calculated or conceptual data as audio measurement.
- Official image is DUAL/BPM at 120 BPM, with L 1/8D and R 1/2. It is not our Ping Pong/HOST recipe.
- Official screenshot pixels are unchanged. Numbered markers in 01 sit outside its image rectangle. UI crops are exact.
- Original diagram rights do not grant Waves image rights. Public republication permission for Waves material has not been verified. Preserve attribution and review before external publication.
- Never translate Delay as 回声. Use Delay / 延迟信号 / 延迟声部 as appropriate.
- The 0/3/5/8 choices are categorical audition trials. Model g is an amplitude feedback fraction and is not the H-Delay display scale.
- No fabricated waveforms, response curves, dB slopes, audio measures, UI settings, or preset screenshots.

## Page coverage

- Page 1: 01_official_control_map
- Page 2: 02_insert_signal_path, 03_send_signal_path
- Page 3: 04_tempo_duration, 05_ordinary_vs_dotted, 13_ui_time_reference
- Page 4: 06_pingpong_timeline, 14_ui_pingpong_reference
- Page 5: 07_feedback_decay, 15_ui_feedback_drywet
- Page 6: 08_filter_direction, 16_ui_filter_reference
- Page 7: 09_audition_recipe, 10_audition_sequence
- Page 8: 11_diagnostic_map, 12_mono_fold_check

## Asset notes

### 01_official_control_map
- Title: Waves H-Delay：真实界面与控件键
- Evidence: official; sources: S0, S1
- Required caption: Waves 官方界面，仅用于定位控件；图中参数不是本教程设置。
- Notes: Use complete genuine image; do not call screenshot Ping Pong active or HOST synced. External numbered markers do not alter the image.

### 02_insert_signal_path
- Title: 低 Wet 插入路由
- Evidence: conceptual; sources: S1, S3, S4
- Required caption: 功能路由示意，不是插件内部精确 DSP 电路。
- Notes: The dry bypass is inside H-Delay only. Feedback loop must stay on the Delay branch.

### 03_send_signal_path
- Title: 发送与返回的路由
- Evidence: conceptual; sources: S1, S3, S4
- Required caption: 功能路由示意，不是插件内部精确 DSP 电路。
- Notes: Optional secondary figure. Do not combine the send dry route with the insert diagram.

### 04_tempo_duration
- Title: 普通音符的时长比较
- Evidence: calculated; sources: S1, S5
- Required caption: 按固定速度计算，四分音符为一拍。
- Notes: Never align the source screenshot 120 BPM / 1/8D with these ordinary-note values as if it showed our settings.

### 05_ordinary_vs_dotted
- Title: 普通 1/8 与 1/8D 的时长
- Evidence: calculated; sources: S1, S5
- Required caption: 固定 160 BPM；附点为普通时值的 1.5 倍。
- Notes: Secondary warning; keep ordinary and dotted durations visibly distinct.

### 06_pingpong_timeline
- Title: Ping Pong 的左右交替时序
- Evidence: calculated; sources: S1, S3
- Required caption: 单次输入、等间隔时序示意，非音频实测。左右起点可互换。
- Notes: Equal event markers intentionally do not encode amplitude. Dry shown as a separate event, not necessarily a center-panned signal.

### 07_feedback_decay
- Title: Feedback 理想模型中的振幅衰减
- Evidence: calculated; sources: S1, S3
- Required caption: 理想线性模型：相对振幅，不是 H-Delay 旋钮读数、实测或响度倍数。
- Notes: Keep model coefficient g explicitly separate from H-Delay FEEDBACK display values.

### 08_filter_direction
- Title: 延迟声部的滤波方向
- Evidence: audition_proposal; sources: S1, S2, S6
- Required caption: 试听起点；仅示意滤波方向，不是实测频响。
- Notes: Use exact logarithmic positions. Arrows show the affected side or proposed trial direction, never a response slope.

### 09_audition_recipe
- Title: H-Delay 试听起点清单
- Evidence: audition_proposal; sources: S1, S6
- Required caption: 整组为试听起点，不是官方预设。数字按 H-Delay 显示值记录。
- Notes: Do not paste these values onto the genuine product screenshot or simulate a preset UI.

### 10_audition_sequence
- Title: 分步试听 Dry/Wet、音符与 Feedback
- Evidence: audition_proposal; sources: S1
- Required caption: 这是试听对照，数字为 H-Delay 显示值，不是干湿电平比例。
- Notes: Candidate circles are categorical choices, not knob simulation or a numerical spacing claim.

### 11_diagnostic_map
- Title: 问题与控制项的诊断对应
- Evidence: audition_proposal; sources: S2, S8
- Required caption: 诊断顺序为试听建议，结果需结合完整伴奏判断。
- Notes: No fabricated width, LUFS, correlation, waveform, or before/after measurements.

### 12_mono_fold_check
- Title: 单声道检查需要合并左右声道
- Evidence: conceptual; sources: S8
- Required caption: L 与 R 合并为单声道；不是只听左声道。
- Notes: Do not assign an arbitrary fold-down gain or claim guaranteed mono compatibility.

### 13_ui_time_reference
- Title: 真实时间显示与同步按钮
- Evidence: official; sources: S0, S1
- Required caption: 图中为 120 BPM / 1/8D / 1/2，仅用于辨认字符，不是本教程设置。
- Notes: Exact crop A02; preserve all depicted values.

### 14_ui_pingpong_reference
- Title: 真实 PING PONG 按钮参考
- Evidence: official; sources: S0, S1
- Required caption: 真实 PING PONG 按钮定位图，不宣称该图按钮已开启。
- Notes: The > 1 threshold is H-Delay display value, not model coefficient g. Publication rights remain unverified.

### 15_ui_feedback_drywet
- Title: 真实 FEEDBACK 与 DRY/WET 控件
- Evidence: official; sources: S0, S1
- Required caption: 图中旋钮位置不是本教程起点；模型 g 也不是 FEEDBACK 旋钮读数。
- Notes: Maintain disclaimer adjacent if combined with the model chart. Publication rights remain unverified.

### 16_ui_filter_reference
- Title: 真实滤波控件参考
- Evidence: official; sources: S0, S1
- Required caption: 界面局部：Waves 官方产品图 A06；图中旋钮位置不是本教程设置。
- Notes: Attribution must stay adjacent. Exact crop A06; public republication license unverified.

## Validation

{
  "checks": {
    "tempo_formula": true,
    "tempo_25_percent_shorter": true,
    "pingpong_equal_intervals": true,
    "feedback_formula": true,
    "fourth_repeat_amplitude_ratio_8": true,
    "dotted_1_5": true,
    "original_image_hash_unchanged": true,
    "all_crop_pixels_exact": true,
    "no_prohibited_delay_translation": true,
    "eight_pages_covered": true,
    "all_svg_png_pairs_exist": true,
    "all_text_inside_canvas": true,
    "no_text_collisions": true
  },
  "text_overflows": [],
  "text_overlaps": [],
  "status": "passed",
  "not_audio_measured": true,
  "not_final_page_layout": true
}