with open ('./input.txt','r') as f:
  data = [line.strip() for line in f.readlines()]

depth =0
aim = 0 
distance = 0

for command in data:
  direction = command.split()[0]
  value = int(command.split()[1])

  if direction == 'forward': 
    distance = distance + value
    depth += value * aim
  if direction == 'down':
    aim += value
  if direction == 'up':
    aim -= value

print(f'multiplied depth ({depth}) and distance ({distance}):  {depth * distance}')
