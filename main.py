from typing import List

def notZero(x: int):
    return x != -9999999999

def thirdMax(nums: List[int]) -> int:
    nums.sort()
    for i in range(len(nums) - 1):
        if nums[i] == nums[i + 1]:
            nums[i] = -9999999999
    nums.sort()
    reverse_nums: List[int] = list(filter(notZero, nums[::-1]))
    return reverse_nums[0] if len(reverse_nums) < 3 else reverse_nums[2]
    
def main() -> None:
    print(thirdMax([3,2,1]))
    print(thirdMax([1,2]))
    print(thirdMax([2,2,3,1]))
    print(thirdMax([1,1,2]))
    print(thirdMax([1,2,-2147483648]))
    
if __name__ == "__main__":
    main()