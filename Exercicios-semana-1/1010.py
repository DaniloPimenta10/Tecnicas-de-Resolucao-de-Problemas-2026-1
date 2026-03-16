import sys

def main():
    a1, b1, c1 = map(float, sys.stdin.readline().split())
    a2, b2, c2 = map(float, sys.stdin.readline().split())

    valor = (b1 * c1) + (b2 * c2)
    sys.stdout.write(f"VALOR A PAGAR: R$ {valor:.2f}\n")

if __name__ == "__main__":
    main()
    