with open("input.txt",'r') as f:
    data = f.read()
stripes, towels = data.split('\n\n')

stripes = set(stripes.split(', '))
towels = towels.split('\n')

p1 = 0
p2 = 0

DP = {}
def ways(words, target):
    if target in DP:
        return DP[target]
    ans = 0
    if not target:
        ans = 1
    for word in words:
        if target.startswith(word):
            ans += ways(words, target[len(word):])
    DP[target] = ans
    return ans

for towel in towels:
    relevant_stripes = set()
    for stripe in stripes:
        if stripe in towel:
            relevant_stripes.add(stripe)
    target_ways = ways(relevant_stripes, towel)
    if target_ways > 0:
        p1 += 1
    p2 += target_ways

print(p1)
print(p2)
