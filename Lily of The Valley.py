import time

print("\033[35m", end='')  # Set text color to purple

lyrics_lines = [
    "Lily of The Valley",
    "Song by DANIEL ‧ 2020",
    ["My love is ", "A flower in your hands"],
    ["우리의 ", "시간이야"],
    ["I'll give you something ", "unforgettable"],
    ["영원한 ", "마음이야"]
]

delays = [
    0.5,  # Lily of The Valley
    1.5,  # Song by DANIEL ‧ 2020
    [2.5, 2.5],  # My love is, A flower in your hands
    [1.5, 3.5],  # 우리의, 시간이야
    [2, 3.4],  # I'll give you something, unforgettable
    [1.9, 2]  # 영원한, 마음이야
]

stops = [
    [],  # Lily of The Valley
    [],  # Song by DANIEL ‧ 2020
    [0.5],  # pause after My love is
    [1],  # pause after 우리의
    [1],  # pause after I'll give you something
    [0.1]  # pause after 영원한
]

inter_stops = [
    0,    # pause after A flower in your hands
    3.5,  # pause after 시간이야
    1.6   # pause after unforgettable
]

for i, line in enumerate(lyrics_lines):
    if i < 2:  # title, song
        print(line)
        time.sleep(delays[i])
    else:  # chorus
        if isinstance(line, list):
            for k, subline in enumerate(line):
                typing_delay = delays[i][k] / len(subline)
                for char in subline:
                    print(char, end='', flush=True)
                    time.sleep(typing_delay)
                print()  # newline after each subline
                if k < len(line) - 1:
                    time.sleep(stops[i][k])
        else:
            typing_delay = delays[i] / len(line)
            for char in line:
                print(char, end='', flush=True)
                time.sleep(typing_delay)
            print()
        if i >= 2 and i < len(lyrics_lines) - 1:
            time.sleep(inter_stops[i - 2])

print("\033[0m", end='')  # Reset color