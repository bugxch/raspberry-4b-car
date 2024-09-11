from gpiozero import TonalBuzzer
from gpiozero.tones import Tone
from gpiozero.tools import sin_values
import time
buzzer_pin = 17
# CM = [0, 131, 147, 165, 175, 196, 220, 248]	# Frequency of Low C notes
CM = [0, 262, 294, 330, 350, 393, 441, 495]		# Frequency of Middle C notes
CH = [0, 525, 589, 661, 700, 786, 880, 880]		# Frequency of High C notes

song_1 = [CM[3], CM[5], CM[6], CM[3], CM[2], CM[3], CM[5], CM[6],  # Notes of song1
          CH[1], CM[6], CM[5], CM[1], CM[3], CM[2], CM[2], CM[3],
          CM[5], CM[2], CM[3], CM[3], CM[6], CM[6], CM[6], CM[1],
          CM[2], CM[3], CM[2], CM[7], CM[6], CM[1], CM[5]]

beat_1 = [1, 1, 3, 1, 1, 3, 1, 1, 			# Beats of song 1, 1 means 1/8 beats
          1, 1, 1, 1, 1, 1, 3, 1,
          1, 3, 1, 1, 1, 1, 1, 1,
          1, 2, 1, 1, 1, 1, 1, 1,
          1, 1, 3]

song_2 = [CM[1], CM[1], CM[1], CM[5], CM[3], CM[3], CM[3], CM[1],  # Notes of song2
          CM[1], CM[3], CM[5], CM[5], CM[4], CM[3], CM[2], CM[2],
          CM[3], CM[4], CM[4], CM[3], CM[2], CM[3], CM[1], CM[1],
          CM[3], CM[2], CM[5], CM[7], CM[2], CM[1]]

beat_2 = [1, 1, 2, 2, 1, 1, 2, 2, 			# Beats of song 2, 1 means 1/8 beats
          1, 1, 2, 2, 1, 1, 3, 1,
          1, 2, 2, 1, 1, 2, 2, 1,
          1, 2, 2, 1, 1, 3]


def loop():
    print('\n    Playing song 1... min freq {} max freq {}'.format(
        tb.min_tone.frequency, tb.max_tone.frequency))
    while True:
        for i in range(1, len(song_1)):
            # print("paly {} {}".format(i, song_1[i]))
            tb.play(song_1[i])
            time.sleep(beat_1[i] * 0.5)
        print('\n    Playing song 2...')
        for i in range(1, len(song_2)):
            tb.play(song_2[i])
            time.sleep(beat_2[i] * 0.5)


# 创建TonalBuzzer对象，引脚号为20（根据实际情况调整）
if __name__ == '__main__':
    tb = TonalBuzzer(buzzer_pin)
    try:
        loop()
    except KeyboardInterrupt:
        tb.close()
