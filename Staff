from CovidManagementSystem import *
import uuid
class Staff:
    def __init__(self, name, dob, t):
        self.ID = str(uuid.uuid1())
        self.name = name
        self.dob = dob
        self.type=t
        self.workplace='none'
        self.workplace_name=''
    
    def serialize(self):
        if self.workplace_name=='':
            return {
                'id': self.ID,
                'name': self.name, 
                'dob': self.dob,
                'type': self.type,
                'workplace': self.workplace,
            }
        else:
            return {
                'id': str(self.ID),
                'name': self.name, 
                'dob': self.dob,
                'type': self.type,
                'workplace': self.workplace+"("+self.workplace_name+")",
            }
