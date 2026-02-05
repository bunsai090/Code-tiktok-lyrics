import time

print("\033[35m", end='')  # Set text color to purple

# Title layout
print("=" * 50)
print("Team by Lorde".center(50))
print("=" * 50)
print()

time.sleep(2.0)  # Delay after title

lyrics_lines = [
    "Even the comatose",
    "They don't dance and tell",
    "We live in cities",
    "you'll never see on-screen",
    "Not very pretty,",
    "but we sure know how to run things",
    "Livin' in ruins",
    "of a palace within my dreams",
    "And you know",
    "we're on each other's team"
]

delays = [
    2.30,  # Even the comatose
    2.0,   # They don't dance and tell
    2.0,   # We live in cities
    1.80,  # you'll never see on-screen
    1.50,  # Not very pretty,
    2.40,  # but we sure know how to run things
    2.0,   # Livin' in ruins
    3.0,   # of a palace within my dreams
    1.80,  # And you know
    2.20   # we're on each other's team
]

stops = [
    [],  # Even the comatose
    [],  # They don't dance and tell
    [],  # We live in cities
    [],  # you'll never see on-screen
    [],  # Not very pretty,
    [],  # but we sure know how to run things
    [],  # Livin' in ruins
    [],  # of a palace within my dreams
    [],  # And you know
    []   # we're on each other's team
]

inter_stops = [
    0.20,  # pause after Even the comatose
    0.20,  # pause after They don't dance and tell
    1.20,  # pause after We live in cities
    0.10,  # pause after you'll never see on-screen
    0.1,   # pause after Not very pretty,
    0.30,  # pause after but we sure know how to run things
    0.1,   # pause after Livin' in ruins
    1.0,   # pause after of a palace within my dreams
    0.0    # pause after And you know
]

for i, line in enumerate(lyrics_lines):
    typing_delay = delays[i] / len(line)
    for char in line:
        print(char, end='', flush=True)
        time.sleep(typing_delay)
    print()  # newline after each line
    if i < len(lyrics_lines) - 1:
        time.sleep(inter_stops[i])

print("\033[0m", end='')  # Reset color