class Owner:
    def __init__(self, first_name, last_name, phone_num_1, phone_num_2, address, id = None):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_num_1 = phone_num_1
        self.phone_num_2 = phone_num_2
        self.address = address
        self.id = id
        self.animal = []

    def add_animal_to_owner(self, animal):
        animal.append(self.animal.name)    
    
    