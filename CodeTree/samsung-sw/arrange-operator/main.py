minn = float('inf')
maxx = float('-inf')

def find_min(idx, nums, opers, curr_num):
    global minn
    if (minn <= curr_num) and ((curr_num < 0 and opers[1] == 0 and opers[2] == 0) or (curr_num >= 0 and opers[1] == 0)):
        return
    if idx == len(nums):
        minn = min(minn, curr_num)
        return

    for oper, point in enumerate(opers):
        if point <= 0:
            continue
        opers[oper] -= 1
        if oper == 0:
            find_min(idx + 1, nums, opers, curr_num + nums[idx])
        elif oper == 1:
            find_min(idx + 1, nums, opers, curr_num - nums[idx])
        else:
            find_min(idx + 1, nums, opers, curr_num * nums[idx])
        opers[oper] += 1

    return

def find_max(idx, nums, opers, curr_num):
    global maxx
    if curr_num < maxx and ((curr_num < 0 and opers[0] == 0) or (curr_num >= 0 and (opers[0] == 0 and opers[2] == 0))):
        return
    if idx == len(nums):
        maxx = max(maxx, curr_num)
        return

    for oper, point in enumerate(opers):
        if point <= 0:
            continue
        opers[oper] -= 1
        if oper == 0:
            find_max(idx + 1, nums, opers, curr_num + nums[idx])
        elif oper == 1:
            find_max(idx + 1, nums, opers, curr_num - nums[idx])
        else:
            find_max(idx + 1, nums, opers, curr_num * nums[idx])
        opers[oper] += 1
    return

def main():
    n = int(input())
    nums = list(map(int, input().split()))
    # plus, minus, multi
    opers = list(map(int, input().split()))

    xopers = opers[:]
    nopers = opers[:]
    find_max(1, nums, xopers, nums[0])
    find_min(1, nums, nopers, nums[0])
    print(minn, maxx)

if __name__ == "__main__":
    main()