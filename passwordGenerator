import string
import random

def generator():
    
    password = ''
  
    for i in range(2):
        password += random.choice(string.ascii_uppercase) + random.choice(string.ascii_lowercase) + random.choice(string.digits) + random.choice(string.punctuation)
    

        passList = list(password)
        random.shuffle(passList)
        password = "".join(passList)

    print(f"Your password is: {password}")    
 

if __name__ =='__main__':
    generator()
