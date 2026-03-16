import sys
import math
def main():
    a, b, c = map(float, sys.stdin.readline().split())

    if a == 0:
        sys.stdout.write(f"Impossivel calcular\n")
    else:
        hip = b**2 - 4 * a * c
        if hip < 0:
            sys.stdout.write(f"Impossivel calcular\n")
        else:
            sys.stdout.write(f"R1 = {(-b + math.sqrt(hip)) / (2*a):.5f}\n")
            sys.stdout.write(f"R2 = {(-b - math.sqrt(hip)) / (2*a):.5f}\n")
if __name__ == "__main__":
    main()