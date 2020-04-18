from CovidManagementSystem import *
import uuid
class Patient:
    def __init__(self, name, dob):
        self.ID = str(uuid.uuid1())
        self.name = name
        self.dob = dob
        self.mf='none'
        self.mf_name=''
    
    def serialize(self):
        if self.mf_name=='':
            return {
                'id': self.ID,
                'name': self.name, 
                'dob': self.dob,
                'medical facility': self.mf,
            }
        else:
            return {
               'id': self.ID,
                'name': self.name, 
                'dob': self.dob,
                'medical facility': self.mf+" ("+self.mf_name+")",
            }