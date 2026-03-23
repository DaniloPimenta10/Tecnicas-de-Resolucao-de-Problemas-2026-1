import sys

def main():
    
    n = sys.stdin.readline().strip()
    l = []
    n = int(n)
    for i in range(n):
        num = 0
        leds = sys.stdin.readline().strip()
        
        for j in leds:
            if j == '1':
                num += 2
            elif j == '7':
                num += 3
            elif j == '4':
                num += 4 
            elif j == '2' or j == '3' or j == '5':
                num += 5
            elif j == '6' or j == '9' or j == '0':
                num += 6
            else:
                num += 7
        
        l.append(f"{num} leds")

    sys.stdout.write("\n".join(l) + "\n")


if __name__ == "__main__":
    main()