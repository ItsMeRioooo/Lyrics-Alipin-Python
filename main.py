import time
import sys

lyrics = [
    ("Ako'y alipin mo kahit hindi batid", 1.60, 0.13),
    ("Aaminin ko minsan ako'y manhid", 2.0, 0.15),
    ("Sana at iyong naririnig...", 2.1, 0.18),
    ("Sa'yong yakap ako'y nasasabik", 0.7, 0.15)
]

def type_out(text, char_delay=0.1):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(char_delay)
    sys.stdout.write('\n')
    sys.stdout.flush()

def play_lyrics(lyrics):
    for line, line_delay, char_delay in lyrics:
        type_out(line, char_delay)
        time.sleep(line_delay)

if __name__ == "__main__":
    print("Now playing: Alipin\n")
    play_lyrics(lyrics)