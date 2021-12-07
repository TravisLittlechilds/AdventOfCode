with open ('./input.txt','r') as f:
  previous_measure = None
  count_increasing = 0
  inputs = f.readlines()
  for i in inputs:
    if not previous_measure:
      previous_measure = int(i)
      continue
    if (int(i) > previous_measure):
      count_increasing = count_increasing + 1
      print(f'count {count_increasing} -- {int(i)} > {previous_measure}')
    previous_measure = int(i)

  print(f'count increasing: {count_increasing}')

# had some issues that took way too long to figure out on this one 
# with the biggest one being that I wasn't converting each input to 
# a number, which meant that I got 1520, intead of 1521 (from when 
# it changed from 3 digits to 4 digits)