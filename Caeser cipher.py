logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""
print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
plain_text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caeser(plain_text,shift_amount,decide):
  if decide=="encode" or decide=="decode":  
    cipher_text=""
    for i in plain_text:
        if decide=="encode":
            if i in alphabet:
                position=alphabet.index(i)
                new_position=position+shift_amount
                new_position%=26 
                new_letter=alphabet[new_position]
                cipher_text+=new_letter
            else:
                cipher_text+=i        
        elif decide=="decode":
            if i in alphabet:    
                position=alphabet.index(i)
                new_position=position-shift_amount
                if new_position<0:
                    new_position+=26  
                    new_letter=alphabet[new_position]
                    cipher_text+=new_letter
                else:
                    new_letter=alphabet[new_position]
                    cipher_text+=new_letter
            else:
                cipher_text+=i             
    print(f"The encoded text is: {cipher_text}")           
  else:
      print("You entered something invalid,other than ENCODING or DECODING choice.\nTry Again")  

caeser(plain_text=text,shift_amount=shift,decide=direction)
ask=input("Do you like to continue?\n").lower()
while ask=="yes":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caeser(plain_text=text,shift_amount=shift,decide=direction)
    ask=input("Do you like to continue?\n").lower()
print("Goodbye")    