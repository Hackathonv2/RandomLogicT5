import sys

def main():
    line1 = sys.stdin.readline()
    line2 = sys.stdin.readline()
    arr1 = [c for c in line1 if c in line2]
    arr2 = [c for c in line2 if c in line1]
    if arr1 == arr2:
        print("TEMPETE")
        print("".join(arr1))
    else:
        print("NORMAL")
    sys.stdin.close()

if __name__ == "__main__":
    main()
