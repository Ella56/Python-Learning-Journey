#Moduls and Global Varibales
from abc import ABC,abstractclassmethod

import string
import random



class PasswordGeneratorAbbstract(ABC):
    
    @abstractclassmethod
    def password_generate(self,length=8):
        pass


#Numeric password generator

class NumericPasswordGenerator(PasswordGeneratorAbbstract):
    
    letters = string.digits
    
    def password_generate(self,length=8):
        
        
        return "".join(str(random.choice(self.letters)) for _ in range(length))
        """
        result = ""
        for _ in range(length):
            result += str(random.choice(self.letters))
        return result
        """
        



#letter password generator

class LetterPasswordGenerator(PasswordGeneratorAbbstract):
    
    letters = string.ascii_letters
    
    def password_generate(self,length=8):
        return "".join(str(random.choice(self.letters)) for _ in range(length))
        




#mix password generator    

class MixPasswordGenerator(PasswordGeneratorAbbstract):
    
    letters = string.ascii_letters + string.digits
    
    def password_generate(self,length=8):
    
        return "".join(str(random.choice(self.letters)) for _ in range(length))



#Main
generator = MixPasswordGenerator()
print(generator.password_generate())
    