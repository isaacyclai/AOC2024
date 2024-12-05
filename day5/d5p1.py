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
        flag = True
        nums = line.split(',')
        for i in range(len(nums)-1):
            if nums[i] in order[nums[i+1]]:
                flag = False
                break            
        if flag:
            # print(nums[len(nums)//2])
            ans += int(nums[len(nums)//2])
print(ans)