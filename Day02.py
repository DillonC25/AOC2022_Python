def part1():
  file = open("input.txt","r")
  Lines = file.readlines()

  #A for Rock, B for Paper, C for Scissors
  #X for Rock, Y for Paper, Z for Scissors
  #1 for Rock, 2 for Paper, 3 for Scissors
  #0 for lost, 3 for draw, 6 for win

  count = 0

  for line in Lines:
    opp = line[0]
    mine = line[2]

    #Draw
    if((opp == "A" and mine == "X") | (opp == "B" and mine == "Y") | (opp == "C" and mine == "Z")):
      count+=3
      if(mine == "X"):
        count+=1
      elif(mine == "Y"):
        count+=2
      else:
        count+=3

    elif((mine == "X" and opp == "C") | (mine == "Z" and opp == "B") | (mine == "Y" and opp =="A")):
      count+=6
      if(mine == "X"):
        count+=1
      elif(mine == "Y"):
        count+=2
      else:
        count+=3
    else:
        if(mine == "X"):
          count+=1
        elif(mine == "Y"):
          count+=2
        else:
          count+=3
  print(count)

def part2():
  file = open("input.txt","r")
  Lines = file.readlines()

  count = 0
  for line in Lines:
      opp = line[0]
      outCome = line[2]
      
  
      if(outCome == "Y"):
        count+=3
        if(opp == "A"):
          other = "X"
        elif(opp == "B"):
          other = "Y"
        else:
          other = "Z"

        if(other == "X"):
            count+=1
        elif(other == "Y"):
            count+=2
        else:
            count+=3
      elif(outCome == "Z"):
        
        count+=6
        if(opp == "A"):
          other = "Y"
        elif(opp == "B"):
          other = "Z"
        else:
          other = "X"

        if(other == "X"):
            count+=1
        elif(other == "Y"):
            count+=2
        else:
            count+=3
  
      else:
        
        if(opp == "A"):
          other = "Z"
        elif(opp == "B"):
          other = "X"
        else:
          other = "Y"

        if(other == "X"):
            count+=1
        elif(other == "Y"):
            count+=2
        else:
            count+=3
  print(count)
