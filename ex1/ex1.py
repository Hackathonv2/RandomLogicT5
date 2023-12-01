import sys

if __name__ == "__main__":
    line = sys.stdin.readline()
    try:
        power = int(line)
    except ValueError:
        sys.exit(1)
    for i in range(4):
        if power % 3 == 0:
            power /= 3
        elif power % 2 == 0:
            power /= 2
        else:
            power -= 1
    sys.stdin.close()
    print(int(power))
