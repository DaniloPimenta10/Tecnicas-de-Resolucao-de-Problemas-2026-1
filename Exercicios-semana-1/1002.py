import sys

def main():

    r = sys.stdin.readline().strip()
    area = 3.14159 * float(r)**2
    sys.stdout.write(f"A={area:.4f}\n")

if __name__  == "__main__":
    main()