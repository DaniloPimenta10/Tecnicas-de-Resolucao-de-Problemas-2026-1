import sys

def main():
    l = list(map(int, sys.stdin.readline().split()))
    
    l1 = l[:]
    for x in range(len(l1)):
        for i in range(len(l1) -1 -x):
            if l1[i] > l1[i+1]:
                l1[i] , l1[i+1] = l1[i+1] , l1[i]

    sys.stdout.write("\n".join(map(str, l1)) + "\n")
    sys.stdout.write("\n")
    sys.stdout.write("\n".join(map(str, l)) + "\n")


if __name__ == "__main__":
    main()