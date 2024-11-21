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

# Example usage
timer = Timer(30)  # 30초 타이머 생성
timer.countdown()

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