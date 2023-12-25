def main():
    summ= 0
    for _ in range(5):
        score = int(input())
        if (score < 40):
            score = 40
        summ += score
    print(summ // 5)
    
if __name__ == "__main__":
    main()
