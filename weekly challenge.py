
from typing import Text


Username= "1Beefste@3Bowl"

def count_chars(Username):
    result = 0
    for char in Username:
        result += 1
    return result
print('Number of characters: ',count_chars(Username))


Username= "1Beefste@3Bowl"
def count_lower(Username):
    l = 0
    for i in Username:
      if (i>='a'and i<='z'):
        l=l+1  
    return l
print('Lowercase characters: ',count_lower(Username))

Username= "1Beefste@3Bowl"
def count_upper(Username):
    u = 0
    for i in Username:                       
       if (i>='A'and i<='Z'):
        u=u+1 
    return u
print('Uppercase characters: ',count_upper(Username))


Username= "1Beefste@3Bowl"
digits = 0
for i in Username:
    if i.isdigit():
        digits += 1

print('Number of numbers: ', digits)


Username= "1Beefste@3Bowl"

def count_special_character(Username): 
    special_char= 0
    for i in Username:  

        if i.isalpha(): 
            continue
        
        elif i.isdigit():
            continue
            
        else: 
            special_char += 1
            
            
    if special_char >= 1:    
        print("String contains {} Special Character/s ".format(special_char))  
    else:
        print("There are no Special Characters in this String.")
  
count_special_character(Username)  

#For validation
Username= "1Beefste@3Bowl"

def count_chars(Username):
    UsernameLength= len(Username)
    if UsernameLength <=14 and UsernameLength >=4 :
        print('Number of chars is between 4 and 14')
    else :
        print('Number of chars in not between 4 and 14')    

count_chars(Username)


Username= "1Beefste@3Bowl"
def check_lower(Username):
    l = 0
    for i in Username:
      if (i>='a'and i<='z'):
        l=l+1  
    

    if l >= 1:
      print('There are lowercases in username')
    else:
        print('There are no lowercases in username')
check_lower(Username)


Username= "1Beefste@3Bowl"
def check_upper(Username):
    u = 0
    for i in Username:                       
       if (i>='A'and i<='Z'):
        u=u+1 

    if u >= 1:
        print('There are uppercases in chars')
    else:
        print('There are no uppercases chars')
check_upper(Username)    


Username= "1Beefste@3Bowl"
def check_digit(Username):
    digits = 0
    for i in Username:
        if i.isdigit():
            digits += 1

        if digits >= 1 :
            print('There are numbers')
        else:
            print('There are no numbers')    
check_digit(Username)               