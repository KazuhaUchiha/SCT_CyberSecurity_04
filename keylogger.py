from pynput import keyboard
from datetime import datetime

def log_key(key, log_file="keystrokes.log"):
    try:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        key_str = str(key).replace("'", "")

        if key == keyboard.Key.space:
            key_str = " [SPACE] "
        elif key == keyboard.Key.enter:
            key_str = " [ENTER]\n"
        elif key == keyboard.Key.backspace:
            key_str = " [BACKSPACE] "

        with open(log_file, "a") as f:
            f.write(f"{timestamp} : {key_str}\n")

    except Exception as e:
        print(f"Error logging key: {e}")

def main():
    print("Recording... Press ESC to stop.")

    with keyboard.Listener(on_press=log_key) as listener:
        listener.join()

if __name__ == "__main__":
    main()
