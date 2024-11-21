import time

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

def parse_time_input(time_input):
    if ":" in time_input:
        minutes, seconds = map(int, time_input.split(":"))
        return minutes * 60 + seconds
    else:
        return int(time_input)

# Example usage
time_in_seconds = parse_time_input("2:30")  # "2분 30초"를 초 단위로 변환
print(f"Time in seconds: {time_in_seconds}")


def parse_time_input(time_input):
    if ":" in time_input:
        minutes, seconds = map(int, time_input.split(":"))
        return minutes * 60 + seconds
    else:
        return int(time_input)

# Example usage
time_in_seconds = parse_time_input("2:30")  # "2분 30초"를 초 단위로 변환
print(f"Time in seconds: {time_in_seconds}")
