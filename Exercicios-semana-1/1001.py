import sys

def main():
    a = sys.stdin.readline().strip()
    b = sys.stdin.readline().strip()
    
    x = int(a) + int(b)
    sys.stdout.write(f"X = {x}\n")

if __name__ == "__main__":
    main()