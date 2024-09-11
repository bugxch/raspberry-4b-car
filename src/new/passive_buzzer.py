from gpiozero import TonalBuzzer
from gpiozero.tones import Tone
from gpiozero.tools import sin_values
import time
buzzer_pin = 17
# 创建TonalBuzzer对象，引脚号为20（根据实际情况调整）
tb = TonalBuzzer(buzzer_pin)

# 定义音符和持续时间列表
notes_and_durations = [
    (Tone('C4'), 0.5),
    (Tone('E4'), 0.5),
    (Tone('G4'), 0.5),
    (Tone('C5'), 0.5)
]

# 播放音符序列
for note, duration in notes_and_durations:
    tb.tone = note
    time.sleep(duration)
    tb.tone = None
    time.sleep(0.1)  # 空气间隔

# 关闭TonalBuzzer
tb.close()
