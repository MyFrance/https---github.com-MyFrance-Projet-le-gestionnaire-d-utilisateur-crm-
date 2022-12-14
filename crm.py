class User:
    def __init__(self, first_name:str, last_name:str, phone_number:str="", address:str=""):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.address = address 
    
    #representation de la classe(recréer un objet à partir des infos qu'on a)
    def __repr__(self) -> str: 
        return f"User({self.first_name} {self.last_name})" 

    def __str__(self) -> str: # fonction d'affichage 
        #return(f"{self.first_name}\n {self.last_name}\n {self.phone_number}\n,{self.address}") On modifie cette ligne en remplaçant le nom et prenom par le full_name
        return(f"{self.full_name}\n {self.phone_number}\n {self.address}")
        
    @property # Création d'une propriété qui permet d'afficher le nom et prenom de façon dynamique
    def full_name(self):
        return f"{self.first_name} {self.last_name}" 

#Affichage dans ce fichier uniquement
if __name__ =="__main__":
    from faker import Faker
    fake = Faker(locale="fr_Fr")
    for _ in range(10): # on test le code pour les attributs de la classe
        user = User(first_name=fake.first_name(),
                    last_name=fake.last_name(),
                    phone_number=fake.phone_number(),
                    address = fake.address())  
        print(f"{user}")
        print("-" * 20)  
        #print(f"le print avec le full_name:\n {user.full_name}")
        #print("-" * 20)  
        #print(f"le print avec le repr:\n {repr(user)}")
        #print("-" * 20)    