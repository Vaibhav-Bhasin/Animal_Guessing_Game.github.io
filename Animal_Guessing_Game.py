####'''''Topic'''''####
# Animal Guessing Game 
 
 
 
print("Animal Guessing Game")
Features=  [["Small","Brown","Non Mammal"],
            ["Small","Golden","Mammal"],
            ["Small","Black","Mammal"],
            ["Small","Green","Non Mammal"]]
            
outcomes=   ["Hen" ,
            "Dog" ,
            "Cat", 
           "Turtle"]
a=input("Is it Small or Big ? \n")
b=input("What Colour It is ? \n")
c=input("Is it Mammal or Non Mammal ? \n")
if a == "small":
 print("Ok")
 if b == "Brown":
  print("Ok") 
  if c == "Non Mammal":
    print("Its a hen")
  else:
    print("")
 else:
    print("")
else:
  print("")  
 
  
if a == "Small":
 print("Ok")
 if b == "Golden":
  print("Ok") 
  if c == "Mammal":
    print("Is it a Dog")
  else:
    print("")
 else:
    print("")
else:
  print("") 
 
  
 
