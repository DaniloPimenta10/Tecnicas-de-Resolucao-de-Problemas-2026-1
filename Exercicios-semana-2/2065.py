import sys
import heapq

def main():

    n, m = map(int, sys.stdin.readline().split())
    
    v = list(map(int, sys.stdin.readline().split()))
    c = list(map(int, sys.stdin.readline().split()))
    
    fila = []

    for i in range(n):
        heapq.heappush(fila , (0 , i))    

    for j in c:
        aux = heapq.heappop(fila)
        
        heapq.heappush(fila , (aux[0] + j*v[aux[1]] , aux[1]))

    sys.stdout.write(str(max(fila)[0]) + '\n')


if __name__ == "__main__":
    main()