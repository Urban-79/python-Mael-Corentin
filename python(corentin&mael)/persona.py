import json
import os 
dir_path = os.path.dirname(os.path.realpath(__file__))

class Persona:
    
    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.address_street = ""
        self.address_number = 0
        self.city = ""
        self.postcode = ''
        

    def __str__(self):
         return f"Hi ! I'm {self.first_name} {self.last_name}" 
        
    def set_address(self,address_street, address_number, city, postcode):
        self.address_street = address_street
        self.address_number = address_number
        self.city = city
        self.postcode = postcode
    
    def show_address(self):
        return f"My full address is : {self.address_number} {self.address_street}, {self.city} ({self.postcode})"
        

    
Json = open(dir_path + '/' + 'data.json')
data = json.load(Json)

for i in data:
    persona = Persona(i['first_name'],i['last_name'])
    print(persona)
    persona.set_address(i['address_street'],i['address_number'],i['city'],i['postcode'])
    print(persona.show_address())
    print('--')



