import time
import sys


def update_progress(count, total):
    bar_len = 60
    filled_len = int(round(bar_len * count / float(total)))

    percents = round(100.0 * count / float(total), 1)
    bar = '=' * filled_len + '-' * (bar_len - filled_len)

    sys.stdout.write(f'\r[{bar}] {percents}%')
    sys.stdout.flush()


def fake_progress(speed: int):
    if speed > 10:
        raise Exception('speed must be between 0 and 1')

    time.sleep(1)

    for i in range(101):
        time.sleep(0.1 - speed / 100)
        update_progress(i, 100)

    time.sleep(1)


if __name__ == '__main__':
    fake_progress(9)
