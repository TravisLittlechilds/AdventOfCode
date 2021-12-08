with open('./input.txt', 'r') as f:

  count:int = 0
  input_array = [int(line) for line in f.readlines()]
  current:int = 0
  previous:int = input_array[0] + input_array[1] + input_array[2]

  for i in range(0, (len(input_array)-2)):
    current = input_array[i] + input_array[i+1] + input_array[i+2]
    if current > previous:
      count = count + 1
      print(f'count {count} -- {current} > {previous}')
    previous = current

  print(f'count increasing: {count}')

  # don't even know what I did to fix this one, I was getting 1214 for the longest time
  # rewrote, changed the input to convert to int when it reads in. Hardcoded the initial 3
  # values so that it doesn't need to check for previous. 

  # learned from a comment section on reddit that by thinking it through, I could optimise this
  # a + b + c < b + c + d can be canceled down to a < d.