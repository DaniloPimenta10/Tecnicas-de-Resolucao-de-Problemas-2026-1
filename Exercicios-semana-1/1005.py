import sys

def main():
    a = sys.stdin.readline().strip()
    b = sys.stdin.readline().strip()
    
    MEDIA = ((float(a) * 3.5) + (float(b) * 7.5)) / 11
    sys.stdout.write(f"MEDIA = {MEDIA:.5f}\n")

if __name__ == "__main__":
    main()