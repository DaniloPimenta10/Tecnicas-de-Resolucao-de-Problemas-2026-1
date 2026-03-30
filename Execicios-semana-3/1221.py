import sys
from math import isqrt
def main():

    n = int(sys.stdin.readline().strip())
    
    for i in range(n):
        
        primo = True
        x = int(sys.stdin.readline().strip())

        if x == 2:
            primo = True
        
        elif x % 2 == 0 or x < 2:
            primo = False

        else:    
            for j in range(3 , isqrt(x) + 1):
                if x != j and x % j == 0:
                    primo = False

        
        if primo:
            sys.stdout.write(f"Prime\n")

        else:
            sys.stdout.write(f"Not Prime\n")


if __name__ == "__main__":
    main()