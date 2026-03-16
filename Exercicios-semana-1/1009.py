import sys

def main():
    nome = sys.stdin.readline().strip()
    fixo = sys.stdin.readline().strip()
    vendas = sys.stdin.readline().strip()
    
    salario = float(fixo) + (float(vendas) * 0.15)
    sys.stdout.write(f"TOTAL = R$ {salario:.2f}\n")

if __name__ == "__main__":
    main()