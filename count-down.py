import time
import threading

class Timer:
    def __init__(self, total_seconds):
        self.total_seconds = total_seconds
        self.paused = False
        self.running = True

    def countdown(self):
        print("Press 'p' to pause/resume or 'q' to quit.")
        while self.running and self.total_seconds > 0:
            if not self.paused:
                mins, secs = divmod(self.total_seconds, 60)
                print(f"{mins:02d}:{secs:02d}", end="\r")
                time.sleep(1)
                self.total_seconds -= 1
        if self.running and self.total_seconds == 0:
            print("\nTimer completed!")

def handle_input(timer):
    while timer.running:
        cmd = input().strip().lower()
        if cmd == 'p':
            timer.paused = not timer.paused
            state = "paused" if timer.paused else "resumed"
            print(f"\nTimer {state}.")
        elif cmd == 'q':
            timer.running = False
            print("\nTimer stopped!")

def get_time_input():
    while True:
        time_input = input("Enter the time in 'mm:ss' or 'seconds': ").strip()
        try:
            if ":" in time_input:
                minutes, seconds = map(int, time_input.split(":"))
                if minutes < 0 or seconds < 0:
                    print("Time cannot be negative. Please try again.")
                    continue
                return minutes * 60 + seconds
            else:
                seconds = int(time_input)
                if seconds < 0:
                    print("Time cannot be negative. Please try again.")
                    continue
                return seconds
        except ValueError:
            print("Invalid input. Please enter time in 'mm:ss' or numeric seconds format.")

if __name__ == "__main__":
    total_seconds = get_time_input()
    timer = Timer(total_seconds)

    threading.Thread(target=handle_input, args=(timer,), daemon=True).start()

    timer.countdown()
