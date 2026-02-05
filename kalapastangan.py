import time
import sys

# ANSI color codes
PEACHY = '\033[38;2;255;180;124m'  # Peachy/salmon color
RESET = '\033[0m'  # Reset to default color

# Timing based on song: 3:03 - 3:38
# Each line is a tuple: (lyrics_text, typing_speed, line_delay)
# Calculated from actual song timestamps

lyrics = [
    
    ("Mamamatay akong nakangiti", 0.08, 2.0),
    
    ("Kapag ikaw ang nasa aking tabi", 0.10, 2.0),
    
    ("Mabubuhay akong nagsisisi", 0.08, 2.0),
    
    ("Kapag isang araw hindi kita mapangiti", 0.08, 2.0),
    
    ("Kalapastangan ang 'di ka ibigin", 0.08, 2.0),
    
    ("Kalokohan ang 'di ka isipin", 0.08, 2.0),
    
    ("Kung ang mundo ay biglang gugunawin", 0.06, 2.0),
    
    ("Ikaw ang una kong hahanapin", 0.10, 2.5),
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

# Print each line with custom typing animation and delay
for line_text, typing_speed, line_delay in lyrics:
    type_text(line_text, typing_speed)
    time.sleep(line_delay)