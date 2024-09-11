from gpiozero import TonalBuzzer
from gpiozero.tones import Tone
from gpiozero.tools import sin_values
import time
buzzer_pin = 17
CL = [0, 131, 147, 165, 175, 196, 211, 248]	# Frequency of Low C notes
CM = [0, 262, 294, 330, 350, 393, 441, 495]		# Frequency of Middle C notes
CH = [0, 525, 589, 661, 700, 786, 882, 990]		# Frequency of High C notes

song_1 = [	CM[3], CM[5], CM[6], CM[3], CM[2], CM[3], CM[5], CM[6], # Notes of song1
			CH[1], CM[6], CM[5], CM[1], CM[3], CM[2], CM[2], CM[3],
			CM[5], CM[2], CM[3], CM[3], CL[6], CL[6], CL[6], CM[1],
			CM[2], CM[3], CM[2], CL[7], CL[6], CM[1], CL[5]	]

beat_1 = [	1, 1, 3, 1, 1, 3, 1, 1, 			# Beats of song 1, 1 means 1/8 beats
			1, 1, 1, 1, 1, 1, 3, 1,
			1, 3, 1, 1, 1, 1, 1, 1,
			1, 2, 1, 1, 1, 1, 1, 1,
			1, 1, 3	]

song_2 = [	CM[1], CM[1], CM[1], CL[5], CM[3], CM[3], CM[3], CM[1], # Notes of song2
			CM[1], CM[3], CM[5], CM[5], CM[4], CM[3], CM[2], CM[2],
			CM[3], CM[4], CM[4], CM[3], CM[2], CM[3], CM[1], CM[1],
			CM[3], CM[2], CL[5], CL[7], CM[2], CM[1]	]

beat_2 = [	1, 1, 2, 2, 1, 1, 2, 2, 			# Beats of song 2, 1 means 1/8 beats
			1, 1, 2, 2, 1, 1, 3, 1,
			1, 2, 2, 1, 1, 2, 2, 1,
			1, 2, 2, 1, 1, 3 ]

def loop():
    while True:
        print('\n    Playing song 1...')
        for i in range(len(song_1)):
            tb.play(song_1[i])
            time.sleep(beat_1[i] * 0.5)
        print('\n    Playing song 2...')
        for i in range(len(song_2)):
            tb.play(song_2[i])
            time.sleep(beat_2[i] * 0.5)


# 创建TonalBuzzer对象，引脚号为20（根据实际情况调整）
if __name__ == '__main__':
    tb = TonalBuzzer(buzzer_pin)
    try:
        loop()
    except KeyboardInterrupt:
        tb.close()