import sys
input = sys.stdin.readline

def solution(document, search):
    docuN = len(document)
    searN = len(search)
    
    count = 0
    i = 0
    while i < docuN:
        if i + searN - 1 >= docuN:
            break
        if document[i:i+searN] == search:
            count += 1
            i += searN
        else:
            i += 1
    return count
    
def main():
    document = input().strip()
    search = input().strip()
    ans = solution(document, search)
    print(ans)
    
if __name__ == "__main__":
    main()
