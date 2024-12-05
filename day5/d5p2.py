with open("input.txt", "r") as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]

order = {}
ans = 0
for line in lines:
    if "|" in line:
        a, b = line.split('|')
        order[a] = order.get(a, []) + [b]
    elif line:
        flag = False
        nums = line.split(',')
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[j] in order[nums[i]]:
                    flag = True
                    nums[j], nums[i] = nums[i], nums[j]
        if flag:
            ans += int(nums[len(nums)//2])
print(ans)