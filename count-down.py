import time
import platform

def play_sound():
    if platform.system() == "Windows":
        import winsound
        winsound.Beep(1000, 1000)  # 1kHz 소리를 1초 동안 재생
    else:
        print("\a")  # 기본 알림음

# Example usage
print("Timer completed!")
play_sound()

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