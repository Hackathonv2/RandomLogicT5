import sys

def main():
    line = sys.stdin.readline()
    arr = [int(c) for c in line.split()]
    if not arr:
        return
    e_max = arr[0]
    e_min = arr[0]
    for e in arr:
        if arr.count(e) > arr.count(e_max):
            e_max = e
        elif arr.count(e) < arr.count(e_min):
            e_min = e
        elif arr.count(e) == arr.count(e_max) and e > e_max:
            e_max = e
        elif arr.count(e) == arr.count(e_min) and e < e_min:
            e_min = e
    print(e_max - e_min)
    sys.stdin.close()

if __name__ == "__main__":
    main()
