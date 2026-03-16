import sys

def main():
    a = sys.stdin.readline().strip()
    b = sys.stdin.readline().strip()
    c = sys.stdin.readline().strip()
    
    MEDIA = ((float(a) * 2) + (float(b) * 3) + (float(c) * 5)) / 10
    sys.stdout.write(f"MEDIA = {MEDIA:.1f}\n")

if __name__ == "__main__":
    main()