import os
import sys
import time


PEACHY = '\033[38;2;255;105;180m'
RESET = '\033[0m'

LYRICS_FILE = os.path.join(os.path.dirname(__file__), 'the_less_i_know_the_better_lyrics.txt')


def parse_lyrics_file(path):
    lines = []
    try:
        with open(path, 'r', encoding='utf-8') as f:
            for raw in f:
                line = raw.rstrip('\n')
                if not line.strip():
                    continue
                parts = [p.strip() for p in line.split('|')]
                text = parts[0]
                speed = None
                delay = None
                start = None
                end = None

                def parse_time(t):
                    if ':' in t:
                        a, b = t.split(':')
                        try:
                            return int(a) * 60 + float(b)
                        except Exception:
                            return None
                    try:
                        return float(t)
                    except Exception:
                        return None

                if len(parts) >= 2 and parts[1]:
                    if ':' in parts[1]:
                        start = parse_time(parts[1])
                    else:
                        try:
                            speed = float(parts[1])
                        except Exception:
                            speed = None

                if len(parts) >= 3 and parts[2]:
                    if ':' in parts[2]:
                        end = parse_time(parts[2])
                    else:
                        try:
                            delay = float(parts[2])
                        except Exception:
                            delay = None

                lines.append({'text': text, 'speed': speed, 'delay': delay, 'start': start, 'end': end})
    except FileNotFoundError:
        return None
    return lines


def type_text(text, speed):
    sys.stdout.write(PEACHY)
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(speed)
    sys.stdout.write(RESET)
    print()


def _clamp(v, a=0, b=255):
    return max(a, min(b, int(v)))


def gradient_print(text, start_rgb, end_rgb):
    length = max(1, len(text))
    for i, ch in enumerate(text):
        t = i / (length - 1) if length > 1 else 0
        r = _clamp(start_rgb[0] + (end_rgb[0] - start_rgb[0]) * t)
        g = _clamp(start_rgb[1] + (end_rgb[1] - start_rgb[1]) * t)
        b = _clamp(start_rgb[2] + (end_rgb[2] - start_rgb[2]) * t)
        sys.stdout.write(f'\033[38;2;{r};{g};{b}m{ch}')
    sys.stdout.write(RESET + "\n")


def main():
    title = 'The Less I Know the Better - By Tame Impala'

    start_color = (255, 105, 180)
    end_color = (150, 50, 200)
    print()
    gradient_print(title, start_color, end_color)

    underline = '-' * len(title)
    gradient_print(underline, end_color, start_color)
    print()

    lyrics = parse_lyrics_file(LYRICS_FILE)
    if lyrics is None:
        # fallback
        lyrics = [
            {'text': "Is this what you want?", 'speed': None, 'delay': 0.0, 'start': 0.0, 'end': 2.0},
            {'text': "Is this who you are?", 'speed': None, 'delay': 0.0, 'start': 2.50, 'end': 5.0},
            {'text': "I was doin' fine without you", 'speed': None, 'delay': 0.0, 'start': 6.0, 'end': 9.0},
            {'text': "'Til I saw your eyes turn away from mine", 'speed': None, 'delay': 0.0, 'start': 10.0, 'end': 12.50},
            {'text': "Oh, sweet darling,", 'speed': None, 'delay': 0.0, 'start': 13.0, 'end': 15.0},
            {'text': "where he wants you", 'speed': None, 'delay': 0.0, 'start': 15.70, 'end': 17.0},
            {'text': 'Said, "Come on Superman,"', 'speed': None, 'delay': 0.0, 'start': 17.50, 'end': 19.0},
            {'text': '"say your stupid line"', 'speed': None, 'delay': 0.0, 'start': 19.70, 'end': 21.70},
        ]

    scheduled = any(item.get('start') is not None and item.get('end') is not None for item in lyrics)

    if scheduled:
        starts = [item['start'] for item in lyrics if item.get('start') is not None]
        min_start = min(starts) if starts else 0.0
        for item in lyrics:
            if item.get('start') is not None:
                item['start'] = item['start'] - min_start
            if item.get('end') is not None:
                item['end'] = item['end'] - min_start

        scheduled_lines = sorted(lyrics, key=lambda x: x.get('start') if x.get('start') is not None else 0)
        t0 = time.time()
        for item in scheduled_lines:
            start = item.get('start')
            end = item.get('end')
            text = item['text']
            if start is None or end is None:
                speed = item.get('speed') if item.get('speed') is not None else 0.08
                type_text(text, speed)
                if item.get('delay'):
                    time.sleep(item.get('delay'))
                continue
            now = time.time()
            wait = t0 + start - now
            if wait > 0:
                time.sleep(wait)
            duration = max(0.05, end - start)
            speed = item.get('speed') if item.get('speed') is not None else duration / max(1, len(text))
            type_text(text, speed)
        dot_animation()
        return

    for item in lyrics:
        text = item['text']
        speed = item.get('speed') if item.get('speed') is not None else 0.08
        delay = item.get('delay') if item.get('delay') is not None else 0.5
        type_text(text, speed)
        time.sleep(delay)

    dot_animation()


def dot_animation():
    """Blinking '....' animation that appears and disappears repeatedly (loops forever)."""
    dots = '....'
    while True:
        # type dots one by one
        sys.stdout.write(PEACHY)
        for ch in dots:
            sys.stdout.write(ch)
            sys.stdout.flush()
            time.sleep(0.18)
        sys.stdout.write(RESET)
        sys.stdout.flush()
        time.sleep(0.4)
        # erase dots
        sys.stdout.write('\r' + ' ' * len(dots) + '\r')
        sys.stdout.flush()
        time.sleep(0.3)


if __name__ == '__main__':
    main()
