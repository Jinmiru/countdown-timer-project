import time

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

# Example usage
minutes, seconds = get_time_input()
print(f"Time entered: {minutes} minutes, {seconds} seconds")
