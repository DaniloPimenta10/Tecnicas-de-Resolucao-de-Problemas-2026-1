import collections
import sys
import heapq

def main():
    for linha in sys.stdin:
        n = int(linha.strip())
        
        ver_pilha = True
        ver_fila = True
        ver_prioridade = True

        fila = collections.deque()
        pilha = []
        filaprioridade = []

        for _ in range(n):
            a, b = map(int, sys.stdin.readline().split())
            
            if a == 1:
                if ver_pilha:
                    pilha.append(b)
                if ver_fila:
                    fila.append(b)
                if ver_prioridade:
                    heapq.heappush(filaprioridade, -b)
            else:
                if ver_pilha:
                    if not pilha or pilha.pop() != b:
                        ver_pilha = False
                
                if ver_fila:
                    if not fila or fila.popleft() != b:
                        ver_fila = False

                if ver_prioridade:
                    if not filaprioridade or -heapq.heappop(filaprioridade) != b:
                        ver_prioridade = False
        
        res = [ver_pilha, ver_fila, ver_prioridade]
        if sum(res) == 0:
            print("impossible")
        elif sum(res) > 1:
            print("not sure")
        elif ver_pilha:
            print("stack")
        elif ver_fila:
            print("queue")
        elif ver_prioridade:
            print("priority queue")

if __name__ == "__main__":
    main()