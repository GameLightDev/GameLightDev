print("Chop Sticks")
print("------------")
print("2 Player\n1 Player\nRules\nExit")
MenuInput = "Base"

def TwoPlayer():

  #Variables
  P1R = 1
  P1L = 1
  P2R = 1
  P2L = 1
  P1Turn = True
  P1Won = False
  P2Won = False
  P1RBefore = 0
  P1LBefore = 0
  P2RBefore = 0
  P2LBefore = 0
  
  print("\n+Two Player Chop Sticks\n----------------------")

  while ((P1Won != True) and (P2Won != True)):

    P1RBefore = P1R
    P1LBefore = P1L
    P2RBefore = P2R
    P2LBefore = P2L
    
    print("\nP1: " + str(P1L) + "  " + str(P1R))
    print("P2: " + str(P2L) + "  " + str(P2R))
    if (P1Turn == True):
      print("\n+P1 Turn: ")
      print("Attack  Split")
      P1Menu = input()

      while (P1Menu.strip().lower() != "split") and (P1Menu.strip().lower() != "attack"):
        P1Menu = input()
      
      while ((P1Menu.strip().lower() != "attack") and ((P1Menu.strip().lower() == "split") or (P1L == 0 or P1R == 0)  and (P1L ==1 or P1R == 0))):
        
        if (((P1L == 0 and P1R == 1) or (P1L == 1 and P1R == 0) and P1Menu.strip().lower() == "split")) or ((P1Menu.strip().lower() == "split") and (P1R == 4 and P1L == 4)):
          print("You Can't Use Split")
          P1Menu = input()
        elif (P1Menu.strip().lower() == "split") and ((P1L > 1 and P1R >= 0) or (P1L >= 0 and P1R > 1)):
          break
        elif ((P1Menu.strip().lower() == "split") and (P1R == 1 and P1L == 1)):
          break
        else:
          print(P1Menu.strip().lower())
          P1Menu = input()
      

      #ATTACK
      if (P1Menu.strip().lower() == "attack"):
  
        #Player 1 left hand = 0
        if (P1L == 0):
          if (P2L == 0):
            P2R = P2R + P1R
          elif (P2R == 0):
            P2L = P2L + P1R
          elif (P2L > 0 and P2R > 0):
            print("+Pick A Hand To Attack")
            print("Left  Right")
            P1Menu = input()
      
            while ((P1Menu.strip().lower() != "left") and (P1Menu.strip().lower() != "right")):
              P1Menu = input()
              
            if (P1Menu.strip().lower() == "left"):
              P2L = P2L+P1R
            if (P1Menu.strip().lower() == "right"):
              P2R = P2R + P1R
          

        #player 1 right hand = 0
        elif (P1R == 0):
          if (P2L == 0):
            P2R = P2R + P1L
          elif (P2R == 0):
            P2L = P2L + P1L
          elif (P2L > 0 and P2R > 0):
            print("+Pick A Hand To Attack")
            print("Left  Right")
            P1Menu = input()
    
            while ((P1Menu.strip().lower() != "left") and (P1Menu.strip().lower() != "right")):
              P1Menu = input()
              
            if (P1Menu.strip().lower() == "left"):
              P2L = P2L + P1L
            if (P1Menu.strip().lower() == "right"):
              P2R = P2R + P1L

        #Player 1 has both hands
        elif (P1R > 0 and P1L > 0):
          
          print("+Pick A Hand To Use")
          print("Left  Right")
          P1Menu = input()
    
          while ((P1Menu.strip().lower() != "left") and (P1Menu.strip().lower() != "right")):
            P1Menu = input()
    
          if (P1Menu.strip().lower() == "left"):
  
            if (P2L == 0):
                P2R = P2R + P1L
            elif (P2R == 0):
                P2L = P2L + P1L
            elif (P2L > 0 and P2R > 0):
              
              print("+Pick A Hand To Attack")
              print("Left  Right")
              P1Menu = input()
      
              while ((P1Menu.strip().lower() != "left") and (P1Menu.strip().lower() != "right")):
                P1Menu = input()
                
              if (P1Menu.strip().lower() == "left"):
                P2L = P2L + P1L
              if (P1Menu.strip().lower() == "right"):
                P2R = P2R + P1L
            
          elif (P1Menu.strip().lower() == "right"):
  
            if (P2L == 0):
              if (P1Menu.strip().lower() == "right"):
                P2R = P2R + P1R
            elif (P2R == 0):
               if (P1Menu.strip().lower() == "left"):
                 P2L = P2L+P1R
            
            print("+Pick A Hand To Attack")
            print("Left  Right")
            P1Menu = input()
    
            while ((P1Menu.strip().lower() != "left") and (P1Menu.strip().lower() != "right")):
              P1Menu = input()
              
            if (P1Menu.strip().lower() == "left"):
              P2L = P2L+P1R
            if (P1Menu.strip().lower() == "right"):
              P2R = P2R + P1R

      #SPLIT
      elif (P1Menu.strip().lower() == "split"):

        #right hand = 0
        if (P1R == 0):
          print("+Amount To Send To Other Hand: ")
          P1Menu = input()
  
          P1RBefore = P1RBefore + int(P1Menu)
          P1LBefore = P1LBefore - int(P1Menu)
            
          while (int(P1Menu) >= P1L + int(P1Menu)):
            print("Enter A Number Between 1 and " + str(P1L))
            P1Menu = input()
          while (int(P1Menu) < 1):
            print("Enter A Number Between 1 and " + str(P1L))
            P1Menu = input()
          while (P1R + int(P1Menu) >= 5):
            print("you can not make your hand equal or over 5: ")
            P1Menu = input()
          while (P1L - int(P1Menu) < 0):
            print("Your hand can not fall below 0")
            P1Menu = input()
            
          while (P1L - int(P1Menu) == P1R and P1R + int(P1Menu) == P1L):
            print("A Split has to make an impact on the game: ")
            P1Menu = input()
  
          P1R = P1R + int(P1Menu)
          P1L = P1L - int(P1Menu)
        #left hand = 0
        elif (P1L == 0):
          print("+Amount To Send To Other Hand: ")
          P1Menu = input()
  
          P1RBefore = P1RBefore + int(P1Menu)
          P1LBefore = P1LBefore - int(P1Menu)
            
          while (int(P1Menu) >= P1R + int(P1Menu)):
            print("Enter A Number Between 1 and " + str(P1R))
            P1Menu = input()
          while (int(P1Menu) < 1):
            print("Enter A Number Between 1 and " + str(P1R))
            P1Menu = input()
          while (P1L + int(P1Menu) >= 5):
            print("you can not make your hand equal or over 5: ")
            P1Menu = input()
          while (P1R - int(P1Menu) < 0):
            print("Your hand can not fall below 0")
            P1Menu = input()
            
          while (P1L + int(P1Menu) == P1R and P1R - int(P1Menu) == P1L):
            print("A Split has to make an impact on the game: ")
            P1Menu = input()
  
          P1L = P1L + int(P1Menu)
          P1R = P1R - int(P1Menu)
        elif (P1R > 0 and P1L > 0):
        
          print("+Pick A Hand To Use")
          print("Left  Right")
          P1Menu = input()
    
          while ((P1Menu.strip().lower() != "left") and (P1Menu.strip().lower() != "right")):
            P1Menu = input()
  
          if (P1Menu.strip().lower() == "left"):
            print("+Amount To Send To Other Hand: ")
            P1Menu = input()
  
            P1RBefore = P1RBefore + int(P1Menu)
            P1LBefore = P1LBefore - int(P1Menu)
            
            while (int(P1Menu) >= P1L + int(P1Menu)):
              print("Enter A Number Between 0 and " + str(P1L))
              P1Menu = input()
            while (int(P1Menu) < 1):
              print("Enter A Number Between 0 and " + str(P1L))
              P1Menu = input()
            while (P1R + int(P1Menu) >= 5):
              print("you can not make your hand equal or over 5: ")
              P1Menu = input()
            while (P1L - int(P1Menu) < 0):
              print("Your hand can not fall below 0")
              P1Menu = input()
            
            while (P1L - int(P1Menu) == P1R and P1R + int(P1Menu) == P1L):
              print("A Split has to make an impact on the game: ")
              P1Menu = input()
  
            P1R = P1R + int(P1Menu)
            P1L = P1L - int(P1Menu)
              
          elif (P1Menu.strip().lower() == "right"):
            print("+Amount To Send To Other Hand: ")
            P1Menu = input()
  
            P1RBefore = P1RBefore + int(P1Menu)
            P1LBefore = P1LBefore - int(P1Menu)
            
            while (int(P1Menu) >= P1R + int(P1Menu)):
              print("Enter A Number Between 0 and " + str(P1R))
              P1Menu = input()
            while (int(P1Menu) < 1):
              print("Enter A Number Between 0 and " + str(P1R))
              P1Menu = input()
            while (P1L + int(P1Menu) >= 5):
              print("you can not make your hand equal or over 5: ")
              P1Menu = input()
            while (P1R - int(P1Menu) < 0):
              print("Your hand can not fall below 0")
              P1Menu = input()
            
            while (P1L + int(P1Menu) == P1R and P1R - int(P1Menu) == P1L):
              print("A Split has to make an impact on the game: ")
              P1Menu = input()
  
            P1L = P1L + int(P1Menu)
            P1R = P1R - int(P1Menu)
              
    #player 2 turn
    elif (P1Turn == False):
      print("\n+P2 Turn: ")
      print("Attack  Split")
      P1Menu = input()

      while (P1Menu.strip().lower() != "split") and (P1Menu.strip().lower() != "attack"):
        P1Menu = input()
      
      while ((P1Menu.strip().lower() != "attack") and ((P1Menu.strip().lower() == "split") or (P2L == 0 and P2R == 0)  and (P2L ==1 and P2R == 0))):
        if (((P2L == 0 and P2R == 1) or (P2L == 1 and P2R == 0) and P1Menu.strip().lower() == "split")) or ((P1Menu.strip().lower() == "split") and (P2R == 4 and P2L == 4)):
          print("You Can't Use Split")
          P1Menu = input()
        elif (P1Menu.strip().lower() == "split") and ((P2L > 1 and P2R >= 0) or (P2L >= 0 and P2R > 1)):
          break
        elif ((P1Menu.strip().lower() == "split") and (P2R == 1 and P2L == 1)):
          print("B")
          break
        else:
          print(P1Menu.strip().lower())
          P1Menu = input()

      

      #ATTACK
      if (P1Menu.strip().lower() == "attack"):
  
        #Player 2 left hand = 0
        if (P2L == 0):
          if (P1L == 0):
            P1R = P1R + P2R
          elif (P1R == 0):
            P1L = P1L + P2R
          elif (P1L > 0 and P1R > 0):
            print("+Pick A Hand To Attack")
            print("Left  Right")
            P1Menu = input()
      
            while ((P1Menu.strip().lower() != "left") and (P1Menu.strip().lower() != "right")):
              P1Menu = input()
              
            if (P1Menu.strip().lower() == "left"):
              P1L = P1L+P2R
            if (P1Menu.strip().lower() == "right"):
              P1R = P1R + P2R
          

        #player 2 right hand = 0
        elif (P2R == 0):
          if (P1L == 0):
            P1R = P1R + P2L
          elif (P1R == 0):
            P1L = P1L + P2L
          elif (P1L > 0 and P1R > 0):
            print("+Pick A Hand To Attack")
            print("Left  Right")
            P1Menu = input()
    
            while ((P1Menu.strip().lower() != "left") and (P1Menu.strip().lower() != "right")):
              P1Menu = input()
              
            if (P1Menu.strip().lower() == "left"):
              P1L = P1L + P2L
            if (P1Menu.strip().lower() == "right"):
              P1R = P1R + P2L

        #Player 2 has both hands
        elif (P2R > 0 and P2L > 0):
          
          print("+Pick A Hand To Use")
          print("Left  Right")
          P1Menu = input()
    
          while ((P1Menu.strip().lower() != "left") and (P1Menu.strip().lower() != "right")):
            P1Menu = input()
    
          if (P1Menu.strip().lower() == "left"):
  
            if (P1L == 0):
                P1R = P1R + P2L
            elif (P1R == 0):
                P1L = P1L + P2L
            elif (P1L > 0 and P1R > 0):
              
              print("+Pick A Hand To Attack")
              print("Left  Right")
              P1Menu = input()
      
              while ((P1Menu.strip().lower() != "left") and (P1Menu.strip().lower() != "right")):
                P1Menu = input()
                
              if (P1Menu.strip().lower() == "left"):
                P1L = P1L + P2L
              if (P1Menu.strip().lower() == "right"):
                P1R = P1R + P2L
            
          elif (P1Menu.strip().lower() == "right"):
  
            if (P1L == 0):
              if (P1Menu.strip().lower() == "right"):
                P1R = P1R + P2R
            elif (P1R == 0):
               if (P1Menu.strip().lower() == "left"):
                 P1L = P1L+P2R
            
            print("+Pick A Hand To Attack")
            print("Left  Right")
            P1Menu = input()
    
            while ((P1Menu.strip().lower() != "left") and (P1Menu.strip().lower() != "right")):
              P1Menu = input()
              
            if (P1Menu.strip().lower() == "left"):
              P1L = P1L+P2R
            if (P1Menu.strip().lower() == "right"):
              P1R = P1R + P2R

      #SPLIT
      elif (P1Menu.strip().lower() == "split"):

        #right hand = 0
        if (P2R == 0):
          print("+Amount To Send To Other Hand: ")
          P1Menu = input()
  
          P2RBefore = P2RBefore + int(P1Menu)
          P2LBefore = P2LBefore - int(P1Menu)
            
          while (int(P1Menu) >= P2L + int(P1Menu)):
            print("Enter A Number Between 1 and " + str(P2L))
            P1Menu = input()
          while (int(P1Menu) < 1):
            print("Enter A Number Between 1 and " + str(P2L))
            P1Menu = input()
          while (P2R + int(P1Menu) >= 5):
            print("you can not make your hand equal or over 5: ")
            P1Menu = input()
          while (P2L - int(P1Menu) < 0):
            print("Your hand can not fall below 0")
            P1Menu = input()
            
          while (P2L - int(P1Menu) == P2R and P2R + int(P1Menu) == P2L):
            print("A Split has to make an impact on the game: ")
            P1Menu = input()
  
          P2R = P2R + int(P1Menu)
          P2L = P2L - int(P1Menu)
        #left hand = 0
        elif (P2L == 0):
          print("+Amount To Send To Other Hand: ")
          P1Menu = input()
  
          P2RBefore = P2RBefore + int(P1Menu)
          P2LBefore = P2LBefore - int(P1Menu)
            
          while (int(P1Menu) >= P2R + int(P1Menu)):
            print("Enter A Number Between 1 and " + str(P2R))
            P1Menu = input()
          while (int(P1Menu) < 1):
            print("Enter A Number Between 1 and " + str(P2R))
            P1Menu = input()
          while (P2L + int(P1Menu) >= 5):
            print("you can not make your hand equal or over 5: ")
            P1Menu = input()
          while (P2R - int(P1Menu) < 0):
            print("Your hand can not fall below 0")
            P1Menu = input()
            
          while (P2L + int(P1Menu) == P2R and P2R - int(P1Menu) == P2L):
            print("A Split has to make an impact on the game: ")
            P1Menu = input()
  
          P2L = P2L + int(P1Menu)
          P2R = P2R - int(P1Menu)
        elif (P2R > 0 and P2L > 0):
        
          print("+Pick A Hand To Use")
          print("Left  Right")
          P1Menu = input()
    
          while ((P1Menu.strip().lower() != "left") and (P1Menu.strip().lower() != "right")):
            P1Menu = input()
  
          if (P1Menu.strip().lower() == "left"):
            print("+Amount To Send To Other Hand: ")
            P1Menu = input()
  
            P2RBefore = P2RBefore + int(P1Menu)
            P2LBefore = P2LBefore - int(P1Menu)
            
            while (int(P1Menu) >= P2L + int(P1Menu)):
              print("Enter A Number Between 0 and " + str(P2L))
              P1Menu = input()
            while (int(P1Menu) < 1):
              print("Enter A Number Between 0 and " + str(P2L))
              P1Menu = input()
            while (P2R + int(P1Menu) >= 5):
              print("you can not make your hand equal or over 5: ")
              P1Menu = input()
            while (P2L - int(P1Menu) < 0):
              print("Your hand can not fall below 0")
              P1Menu = input()
            
            while (P2L - int(P1Menu) == P2R and P2R + int(P1Menu) == P2L):
              print("A Split has to make an impact on the game: ")
              P1Menu = input()
  
            P2R = P2R + int(P1Menu)
            P2L = P2L - int(P1Menu)
              
          elif (P1Menu.strip().lower() == "right"):
            print("+Amount To Send To Other Hand: ")
            P1Menu = input()
  
            P2RBefore = P2RBefore + int(P1Menu)
            P2LBefore = P2LBefore - int(P1Menu)
            
            while (int(P1Menu) >= P2R + int(P1Menu)):
              print("Enter A Number Between 0 and " + str(P2R))
              P1Menu = input()
            while (int(P1Menu) < 1):
              print("Enter A Number Between 0 and " + str(P2R))
              P1Menu = input()
            while (P2L + int(P1Menu) >= 5):
              print("you can not make your hand equal or over 5: ")
              P1Menu = input()
            while (P2R - int(P1Menu) < 0):
              print("Your hand can not fall below 0")
              P1Menu = input()
            
            while (P2L + int(P1Menu) == P2R and P2R - int(P1Menu) == P2L):
              print("A Split has to make an impact on the game: ")
              P1Menu = input()
  
            P2L = P2L + int(P1Menu)
            P2R = P2R - int(P1Menu)
            #end of P2

    if (P1R >= 5):
      P1R = 0
    elif (P1L >= 5):
      P1L = 0
    elif (P2R >= 5):
      P2R = 0
    elif (P2L >= 5):
      P2L = 0
    

    if ((P1R == 0) and (P1L == 0)):
      print("Player 2 Has Won!")
      return 0
    elif ((P2R == 0) and (P2L == 0)):
      print("Player 1 Has Won!")
      return 0
    else:
      if (P1Turn == True):
        P1Turn = False
      elif (P1Turn == False):
        P1Turn = True

def OnePlayer():
  print("Coming Soon")
  return 0

def Rules():
  print("Start with 1 on each hand")
  print("Attack: ")
  print("When you attack you add what ever you hand has onto their hand")
  print("Split: ")
  print("When you split you send some chopsticks from one hand to the other")
  return 0

while ((MenuInput.strip().lower() != "2 player") or (MenuInput.strip().lower() != "1 player") or (MenuInput.strip().lower() != "rules") or (MenuInput.strip().lower() != "exit")):
  MenuInput = input()
  if (MenuInput.strip().lower() == "2 player"):
    TwoPlayer()
  elif (MenuInput.strip().lower() == "1 player"):
    OnePlayer()
  elif (MenuInput.strip().lower() == "rules"):
    Rules()
  elif (MenuInput.strip().lower() == "exit"):
    exit()
