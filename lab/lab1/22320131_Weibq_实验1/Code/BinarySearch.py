def BinarySearch(target, nums, n):
    left = 0
    right = n - 1
    
    while (left <= right):
        mid = (left + right) // 2
        if target < nums[mid]:
            right = mid - 1
        elif target > nums[mid]:
            left = mid + 1
        else:
            return mid
    
    return -1
        
def test1():
    input_nums = input("请输入升序列表")
    nums = list(map(int, input_nums.split()))
    jud = True
    while jud:
        target = int(input("请输入要查找的值："))
        print(f"结果为：{BinarySearch(target, nums, len(nums))}")

test1()