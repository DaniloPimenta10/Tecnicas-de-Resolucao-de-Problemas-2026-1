import sys

def main():

    n = int(sys.stdin.readline().strip())
    l = []
    verificacao = False
    for i in range(n):
        l.append(int(sys.stdin.readline().strip()))

    for mascara in range(1 << n):
        graus = 0
        
        for j in range(n):
            if mascara & (1 << i):
                graus += l[i]

            else:
                graus -= l[i]

        if graus % 360 == 0:
            verificacao = True

    if verificacao:       
        sys.stdout.write(f"YES\n")
    else: 
        sys.stdout.write(f"NO\n")
    
if __name__ == "__main__":
    main()

