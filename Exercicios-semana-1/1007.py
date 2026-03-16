import sys

def main():
    a = sys.stdin.readline().strip()
    b = sys.stdin.readline().strip()
    c = sys.stdin.readline().strip()
    d = sys.stdin.readline().strip()
    
    dif = (int(a) * int(b)) - (int(c) * int(d))
    sys.stdout.write(f"DIFERENCA = {dif}\n")

if __name__ == "__main__":
    main()