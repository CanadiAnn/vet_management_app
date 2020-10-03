class Animal: 
    def __init__(self, name, dob, type, owner, id = None):
        self.name = name 
        self.dob = dob
        self.type = type 
        self.owner_id = owner
        self.id = id
        
        # self.vet_id = vet
        # self.treatment_notes = treatment_notes