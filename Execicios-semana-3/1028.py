from math import gcd
import sys

def main():

    n = int(sys.stdin.readline().strip())
    
    for i in range(n):
        f1 ,f2 = map(int, sys.stdin.readline().split())

        mdc = gcd(f1, f2)
        sys.stdout.write(f"{mdc}\n")

if __name__ == "__main__":
    main()