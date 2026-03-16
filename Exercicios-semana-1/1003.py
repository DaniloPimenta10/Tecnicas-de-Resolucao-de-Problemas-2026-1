import sys

def main():
    a = sys.stdin.readline().strip()
    b = sys.stdin.readline().strip()
    
    SOMA = int(a) + int(b)
    sys.stdout.write(f"SOMA = {SOMA}\n")

if __name__ == "__main__":
    main()