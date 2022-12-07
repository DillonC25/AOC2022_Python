import re

def part1():
  file = open("sample.txt","r")
  Lines = file.readlines()
  #letList = [[], ["Z","N"], ["M","C","D"], ["P"]]
  letList = [[], ["W","B","D","N","C","F","J"], ["P","Z","V","Q","L","S","T"], ["P","Z","B","G","J","T"], ["D","T","L","J","Z","B","H", "C"],["G","V","B","J","S"],["B","V","D","F","L","M","P", "N"],["P","S","M","F","B","D","L", "R"], ["V", "D", "T", "R"]]

  for line in Lines:
    temp = re.findall(r'\d+', line)
    test = list(map(int,temp))
    amountMove = test[0]
    before = test[1]
    after = test[2]
    
    for i in range(len(letList[before])-1,len(letList[before])-1-amountMove,-1):
      #print(str(before) + " " + str(i))
      curr = letList[before][i]
      letList[after].append(curr)
      letList[before].pop(i)
      
      
  print(letList)

def part2():
  file = open("input.txt","r")
  Lines = file.readlines()
  #letList = [[], ["Z","N"], ["M","C","D"], ["P"]]
  letList = [[], ["W","B","D","N","C","F","J"], ["P","Z","V","Q","L","S","T"], ["P","Z","B","G","J","T"], ["D","T","L","J","Z","B","H", "C"],["G","V","B","J","S"], ["P", "S", "Q"],["B","V","D","F","L","M","P", "N"],["P","S","M","F","B","D","L", "R"], ["V", "D", "T", "R"]]

  for line in Lines:
    temp = re.findall(r'\d+', line)
    test = list(map(int,temp))
    test2 = []
    amountMove = test[0]
    beforeList = test[1]
    afterList = test[2]
    for i in range(len(letList[beforeList])-amountMove,len(letList[beforeList])):      
      currText = letList[beforeList][i]
      test2.append(currText)
    for i in range(len(test2)):      
      letList[beforeList].pop()
    letList[afterList]+=test2
  print(letList)
