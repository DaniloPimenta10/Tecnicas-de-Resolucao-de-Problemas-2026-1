import sys

def main():
    a = sys.stdin.readline().strip()
    b = sys.stdin.readline().strip()
    
    PROD = int(a) * int(b)
    sys.stdout.write(f"PROD = {PROD}\n")

if __name__ == "__main__":
    main()