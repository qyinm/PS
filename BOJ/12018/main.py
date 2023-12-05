def solution(classes, mileage):
    require = []

    for _ in range(classes):
        student, rank = map(int, input().split())
        students = [*map(int, input().split())]
        
        # 학생이 수강 정원 이하일 때
        if student <= rank:
            require.append(1)
        else:
            # 마일리지가 같을 경우 성준이에게 우선순위
            students.sort(reverse=True)
            require.append(students[rank-1])

    require.sort()

    ans = 0
    for req in require:
        if mileage < req:
            break
        mileage -= req
        ans += 1

    return ans

def main():
    classes, mileage = map(int, input().split())
    result = solution(classes, mileage)
    print(result)

if __name__ == "__main__":
    main()
