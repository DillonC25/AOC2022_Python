def part1():
  file = open("sample.txt","r")
  Lines = file.readlines()
  total = [0] * 260
  
  count = 0
  max = 0
  currTop = 0

  for line in Lines:
      if(line.strip() != ""):
        total[count] += int(line)
      if(line.strip() == ""):
        count += 1
        
      
      for i in range(0,len(total)):
        if(total[i] > currTop):
          currTop=total[i]
        
  
  print(currTop)

def part2():
  file = open("calories.txt","r")
  Lines = file.readlines()
  total = [0] * 260
  
  count = 0
  max = 0

  for line in Lines:
      if(line.strip() != ""):
        total[count] += int(line)
      if(line.strip() == ""):
        count += 1
        
  top3 = 0
  currTop = 0
  for i in range(0,len(total)):
    if(total[i] > currTop):
      currTop=total[i]
  top3+=currTop
  total.remove(currTop)
  currTop = 0
  
  for i in range(0,len(total)):
    if(total[i] > currTop):
      currTop=total[i]
  top3+=currTop
  total.remove(currTop)
  currTop = 0
  
  for i in range(0,len(total)):
    if(total[i] > currTop):
      currTop=total[i]
  top3+=currTop
  
  print(top3)
