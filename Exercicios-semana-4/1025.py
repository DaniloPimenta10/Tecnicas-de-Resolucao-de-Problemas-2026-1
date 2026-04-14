def main():
    n , q = [int(x) for x in input().split()]
    cont = 1
    while n != 0 and q != 0:
        l = []
        
        for i in range(n):
            aux = int(input())
            l.append(aux)

        l.sort()
        
        print(f"CASE# {cont}:")
        for j in range(q):
            
            consulta = int(input())

            e = 0
            d = len(l) - 1
            r = -1

            while e <= d:
                meio = e + (d - e) // 2
                    
                if consulta == l[meio]:
                    r = meio
                    d = meio -1

                elif consulta > l[meio]:
                    e = meio + 1
                    
                else:
                    d = meio - 1

            if r != -1:
                print(f"{consulta} found at {r + 1}")

            else:
                print(f"{consulta} not found")

        cont += 1
        n , q = [int(x) for x in input().split()]


if __name__ == "__main__":
    main()