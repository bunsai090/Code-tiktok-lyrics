import os
import sys
import time


PEACHY = '\033[38;2;255;105;180m'
RESET = '\033[0m'

LYRICS_FILE = os.path.join(os.path.dirname(__file__), 'so_easy_lyrics.txt')


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
                # default fields
                speed = None
                delay = None
                start = None
                end = None

                def parse_time(t):
                    # accepts mm:ss or m:ss or ss; returns seconds (float)
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
                    # detect if parts[1] is a time (contains ':') else numeric speed
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
    title = 'So Easy - by Olivia Dean'
    
    start_color = (255, 105, 180)  
    end_color = (150, 50, 200)      
    print()
    gradient_print(title, start_color, end_color)
    
    underline = '-' * len(title)
    gradient_print(underline, end_color, start_color)
    print()

    lyrics = parse_lyrics_file(LYRICS_FILE)
    if lyrics is None:
        # fallback (simple list of dicts)
        lyrics = [
            {'text': "Cause I make it so easy...", 'speed': None, 'delay': 0.0, 'start': 0, 'end': 4},
            {'text': "to fall in love", 'speed': None, 'delay': 0.0, 'start': 4, 'end': 6.70},
            {'text': "So, come give me a Calll...", 'speed': None, 'delay': 0.0, 'start': 7, 'end': 10.70},
            {'text': "and we'll fall into us", 'speed': None, 'delay': 0.0, 'start': 11, 'end': 13.70},
            {'text': "I'm the perfect mix of", 'speed': None, 'delay': 0.0, 'start': 14, 'end': 15.80},
            {'text': "Saturday night and the rest of your life", 'speed': None, 'delay': 0.0, 'start': 16, 'end': 19},
            {'text': "Anyone with a heart would agree", 'speed': None, 'delay': 0.0, 'start': 19.80, 'end': 21.60},
            {'text': "It's so easy", 'speed': None, 'delay': 0.0, 'start': 23, 'end': 25},
            {'text': "To fall in love with me", 'speed': None, 'delay': 0.0, 'start': 26, 'end': 28.70},
        ]

    # Detect scheduled mode if any line has start/end times
    scheduled = any(item.get('start') is not None and item.get('end') is not None for item in lyrics)

    if scheduled:
        # Normalize start times so earliest start becomes 0.0
        starts = [item['start'] for item in lyrics if item.get('start') is not None]
        min_start = min(starts) if starts else 0.0
        for item in lyrics:
            if item.get('start') is not None:
                item['start'] = item['start'] - min_start
            if item.get('end') is not None:
                item['end'] = item['end'] - min_start

        # Sort by start time
        scheduled_lines = sorted(lyrics, key=lambda x: x.get('start') if x.get('start') is not None else 0)
        t0 = time.time()
        for item in scheduled_lines:
            start = item.get('start')
            end = item.get('end')
            text = item['text']
            if start is None or end is None:
                # fallback to immediate print
                speed = item.get('speed') if item.get('speed') is not None else 0.08
                type_text(text, speed)
                if item.get('delay'):
                    time.sleep(item.get('delay'))
                continue
            # wait until scheduled start
            now = time.time()
            wait = t0 + start - now
            if wait > 0:
                time.sleep(wait)
            # compute typing speed so typing lasts (end-start)
            duration = max(0.05, end - start)
            speed = item.get('speed') if item.get('speed') is not None else duration / max(1, len(text))
            type_text(text, speed)
            # no extra delay; next line scheduled by its own start
        return

    # Non-scheduled mode: simple sequential printing using speed/delay
    for item in lyrics:
        text = item['text']
        speed = item.get('speed') if item.get('speed') is not None else 0.08
        delay = item.get('delay') if item.get('delay') is not None else 0.5
        type_text(text, speed)
        time.sleep(delay)


if __name__ == '__main__':
    main()
