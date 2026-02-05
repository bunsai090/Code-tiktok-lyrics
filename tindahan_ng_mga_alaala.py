import time
import sys

# ANSI color codes
PEACHY = '\033[38;2;255;180;124m'  # Peachy/salmon color
RESET = '\033[0m'  # Reset to default color

# Timing based on song: "Tindahan ng mga Alaala"
# Each line is a tuple: (lyrics_text, typing_speed, line_delay)

lyrics = [
    # Line 1: 0:00-0:03 (3 seconds) - 31 chars
    ("Pabili po ng alaalang masaya", 0.10, 0.0),
    
    # Line 2: 0:03-0:08 (5 seconds) - 47 chars
    ("Panghimagas ko sa buhay at siyang aking pahinga", 0.06, 1.0),
    
    # Line 3: 0:11-0:15 (4 seconds) - 40 chars
    ("Pabili po ng relos kahit wala nang baterya", 0.10, 0.0),
    
    # Line 4: 0:15-0:19 (4 seconds) - 45 chars
    ("Nang dumungaw lang muli ang nalimutang pahina", 0.09, 0.0),
    
    # Line 5: 0:20-0:23 (3 seconds) - 44 chars
    ("Pwede bang pautang muna ng tahol ng aso naming", 0.07, 0.0),
    
    # Line 6: 0:23-0:28 (5 seconds) - 40 chars
    ("Matagal-tagal ko nang hindi nakakapiling?", 0.12, 0.0),
    
    # Line 7: 0:28-0:34 (6 seconds) - 38 chars
    ("Pabili po sa tindahan ng mga alaala", 0.17, 0.0),
]

def type_text(text, speed):
    """Print text with typing animation effect"""
    sys.stdout.write(PEACHY)  # Apply color
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    sys.stdout.write(RESET)  # Reset color
    print()  # New line after typing is complete

for line_text, typing_speed, line_delay in lyrics:
    type_text(line_text, typing_speed)
    time.sleep(line_delay)
