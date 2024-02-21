
# Hash map
def singleNumber(nums):
    count = {}
    for number in nums:
        if number not in count:
            count[number] = 1
        else:
            del count[number]

    return list(count.keys())[0]


print(singleNumber([4, 1, 2, 1, 2]))
