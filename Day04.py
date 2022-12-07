import re
def part1():
  file = open("input.txt","r")
  Lines = file.readlines()
  count = 0
  for line in Lines:
    temp = re.findall(r'\d+', line)
    test = list(map(int, temp))
    firstPairFirst = int(test[0])
    firstPairSecond = int(test[1])
    secondPairFirst = int(test[2])
    secondPairSecond = int(test[3])

    if(((firstPairFirst >= secondPairFirst) & (firstPairSecond <= secondPairSecond)) | ((secondPairFirst >= firstPairFirst) & (secondPairSecond <= firstPairSecond)) ):
      count+=1
    
  print(count)

def part2():
  file = open("input.txt","r")
  Lines = file.readlines()
  
  count = 0
  for line in Lines:
    temp = re.findall(r'\d+', line)
    test = list(map(int, temp))
    firstPairFirst = int(test[0])
    firstPairSecond = int(test[1])
    secondPairFirst = int(test[2])
    secondPairSecond = int(test[3])
    list1 = []
    list2 = []
    x = 0
    
    for i in range(firstPairFirst,firstPairSecond+1):
      list1.append(i)
      if(x < (firstPairSecond-firstPairFirst+1)):
        x+=1
    x = 0
    for i in range(secondPairFirst,secondPairSecond+1):
      list2.append(i)
      if(x < (secondPairSecond-secondPairFirst+1)):
        x+=1
    if((len(list1) >= len(list2))):
      for i in range(len(list1)):
        
        if list1[i] in list2:
          count +=1
          
          break

    if((len(list2) > len(list1))):
      for i in range(len(list2)):
        
        if list2[i] in list1:
          count +=1
          break
  print(count)
