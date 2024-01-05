def logic(mul, add, nums, n):
    for i in range(1, n):
        if mul * nums[i-1] + add != nums[i]:
            return False
    return True

def main():
    n = int(input())
    nums = [*map(int, input().split())]
    if n == 1:
        print('A')
    elif n == 2:
        if nums[1] == nums[0]:
            print(nums[0])
        else:
            print('A')
    else:
        mul = 0 if nums[1] - nums[0] == 0 else ((nums[2] - nums[1]) // (nums[1] - nums[0]))
        add = nums[1] - mul * nums[0]
        for i in range(1, n):
            if mul * nums[i-1] + add != nums[i]:
                print('B')
                exit(0)
        print(mul*nums[-1] + add)
    
if __name__ == "__main__":
    main()
