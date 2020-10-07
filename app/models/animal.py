class Animal: 
    def __init__(self, name, dob, type, owner, vet, id = None, treatment_notes = []):
        self.name = name 
        self.dob = dob
        self.type = type 
        self.owner = owner
        self.vet = vet
        self.id = id
        self.treatment_notes = treatment_notes

