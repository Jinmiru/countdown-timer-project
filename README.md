# Countdown Timer Python Project
카운트다운 타이머를 파이썬으로 만드는 프로젝트입니다.

<br>

## 세부 내용
- 참고 링크
  - 프로젝트 리스트 : https://www.freecodecamp.org/news/python-projects-for-beginners/
  - 카운트다운 타이머 구현 참고 영상 : https://youtu.be/SqvVm3QiQVk?si=z1rp_VLoPGtMGl0r&t=1992

<br>

## 영상 제공 코드
```python
import time

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end='\r')
        time.sleep(1)
        t -= 1
    
    print('Timer completed!')

t = input('Enter the time in seconds: ')

countdown(int(t))
```
