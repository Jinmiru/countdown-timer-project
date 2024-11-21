import time
class Timer:
    def __init__(self, total_seconds):
        self.total_seconds = total_seconds
        self.paused = False

    def countdown(self):
        while self.total_seconds > 0:
            if not self.paused:
                mins, secs = divmod(self.total_seconds, 60)
                print(f"{mins:02d}:{secs:02d}", end="\r")
                time.sleep(1)
                self.total_seconds -= 1
            else:
                time.sleep(0.5)
        print("\nTimer completed!")
        self.play_sound()

    def toggle_pause(self):
        self.paused = not self.paused

    def play_sound(self):
        print("\a")  # 알림음 출력

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end='\r')
        time.sleep(1)
        t -= 1
    
    print('타이머 완료!')

t = input('원하는 시간을 입력하세요(초 단위): ')

countdown(int(t))
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
        if self.total_seconds == 0:
            print("\nTimer completed!")

def handle_input(timer):
    while timer.running:
        cmd = input().strip().lower()
        if cmd == 'p':
            timer.paused = not timer.paused
        elif cmd == 'q':
            timer.running = False

if __name__ == "__main__":
    total_seconds = int(input("Enter the time in seconds: "))
    timer = Timer(total_seconds)

    threading.Thread(target=handle_input, args=(timer,), daemon=True).start()
    timer.countdown()

def get_time_input():
    while True:
        time_input = input("원하는 시간을 '분:초' 또는 '초'로 입력해주세요: ").strip()
        try:
            if ":" in time_input:
                minutes, seconds = map(int, time_input.split(":"))
                return minutes, seconds
            else:
                seconds = int(time_input)
                return 0, seconds
        except ValueError:
            print("유효하지 않은 입력입니다. 숫자를 입력해주세요.")

countdown(int(t))

def parse_time_input(time_input):
    if ":" in time_input:
        minutes, seconds = map(int, time_input.split(":"))
        return minutes * 60 + seconds
    else:
        return int(time_input)

def parse_time_input(time_input):
    if ":" in time_input:
        minutes, seconds = map(int, time_input.split(":"))
        return minutes * 60 + seconds
    else:
        return int(time_input)
