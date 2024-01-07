from collections import deque

def main():
    n, k = map(int, input().split())
    queue = deque([i for i in range(1, n + 1)])
    k -= 1
    print("<", end="")
    while len(queue) > 1:
        queue.rotate(-k)
        print(queue.popleft(), end = ", ")
    queue.rotate(-k)
    print(queue.popleft(), end = ">")
    
if __name__ == "__main__":
    main()
