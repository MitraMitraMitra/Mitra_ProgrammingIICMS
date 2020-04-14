import uuid
class Patient:
    def __init__(self, name, dob):
        self.ID = str(uuid.uuid1())
        self.name = name
        self.dob = dob
        self.mf='none'
    
    def serialize(self):
        return {
            'id': self.ID,
            'name': self.name, 
            'dob': self.dob,
            'type': self.type,
            'medical facility': self.mf,
        }
