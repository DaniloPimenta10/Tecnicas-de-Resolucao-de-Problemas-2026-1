import sys
import collections

def main():

    n = sys.stdin.readline().strip()
    n = int(n)
    while n != 0:
        l = []

        fila = collections.deque(range(1 , n + 1))

        while len(fila) >= 2:
            l.append(fila[0])
            
            fila.popleft()
            
            aux = fila[0]
            fila.popleft()
            fila.append(aux)

        
        sys.stdout.write("Discarded cards: " + ", ".join(map(str, l)) + "\n")
        sys.stdout.write("Remaining card: " + ", ".join(map(str, fila)) + "\n")


        n = sys.stdin.readline().strip()
        n = int(n)


if __name__ == "__main__":
    main()