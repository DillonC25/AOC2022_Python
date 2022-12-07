def part1():
  file = open("input.txt","r")
  Lines = file.readlines()

  for line in Lines:
    
   for i in range(0,len(line)-3):
    currFour = line[i:i+4]
    
    next = 0
    for x in range(0,4):
      count = 0
      for y in range(0,4):
        if(currFour[x] == currFour[y]):
          count += 1
      if(count >= 2):
        next += 1
        break
    if(next == 0):
      print(i+4)
      break

def part2():
  file = open("input.txt","r")
  Lines = file.readlines()

  for line in Lines:
    
   for i in range(0,len(line)-13):
    currFour = line[i:i+14]
    
    next = 0
    for x in range(0,14):
      count = 0
      for y in range(0,14):
        if(currFour[x] == currFour[y]):
          count += 1
      if(count >= 2):
        next += 1
        break
    if(next == 0):
      print(i+14)
      break
