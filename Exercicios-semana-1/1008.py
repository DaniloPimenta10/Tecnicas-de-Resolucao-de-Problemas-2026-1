import sys

def main():
    num = sys.stdin.readline().strip()
    horas = sys.stdin.readline().strip()
    dinheiro = sys.stdin.readline().strip()
    
    salario = int(horas) * float(dinheiro)
    sys.stdout.write(f"NUMBER = {num}\n")
    sys.stdout.write(f"SALARY = U$ {salario:.2f}\n")

if __name__ == "__main__":
    main()