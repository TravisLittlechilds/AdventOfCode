with open ('./input.txt','r') as f:
  data = [line.strip() for line in f.readlines()]

gamma = []
epsilon = []

for bit in range(0, len(data[1])):
  total = 0
  for binary in data:
    total += int(binary[bit])
  if total > len(data)/2:
    gamma.append('1')
    epsilon.append('0')
  if total < len(data)/2:
    gamma.append('0')
    epsilon.append('1')

gamma_i = int("".join(x for x in gamma),2)
epsilon_i = int("".join(x for x in epsilon),2)

print(f'current power consumption is: {gamma_i * epsilon_i}')