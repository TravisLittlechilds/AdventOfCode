with open ('./input.txt','r') as f:
  data = [line.strip() for line in f.readlines()]

life_support = 1

def reduce(search: str, position: int, nums:list) -> list:
  binary_0 = [x for x in nums if int(x[position]) == 0]
  binary_1 = [x for x in nums if int(x[position]) == 1]
  if (search == 'o2'):
    if len(binary_0) > len(binary_1):
      return binary_1
    return binary_0
  if (search == 'co2'):
    if len(binary_0) > len(binary_1):
      return binary_0
    return binary_1

for i in ['o2','co2']:
  nums = data
  for j in range(0, len(nums[0])):
    if len(nums) == 1:
      continue
    nums = reduce(i, j, nums)
  life_support = life_support * int("".join(x for x in nums),2) 

print(f'current life support rating is: {life_support}.')      
