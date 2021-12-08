with open ('./input.txt','r') as f:
  data = [line.strip() for line in f.readlines()]

movement = {}

for command in data:
  direction = command.split()[0]
  value = command.split()[1]

  if direction not in movement:
    movement[direction] = 0
  
  movement[direction] = movement[direction] + int(value)

print(movement)
print(f'multiplied depth and distance: {movement["forward"] * (movement["down"]-movement["up"])}')

# Success!