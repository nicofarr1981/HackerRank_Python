import sys

if __name__ == '__main__':
    t = int(sys.stdin.readline())
    for i in range(t):
        lenA = int(sys.stdin.readline())
        A = set(map(int,sys.stdin.readline().split()))
        lenB = int(sys.stdin.readline())
        B = set(map(int,sys.stdin.readline().split()))
        print(A.issubset(B))