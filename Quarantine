from Patient import *
import uuid
class Quarantine:
    def __init__(self, name, capacity):
        self.ID= str(uuid.uuid1())
        self.name = name
        self.capacity = int (capacity) 
        self.patients = [] # List of patients admitted to the quarantine 
        self.staff = [] # List of doctors and nurses working in the quarantine
    
    # return the percentage of occupancy of this quarantine
    def occupancy (self):         
        return int(1000* len(self.patients) / self.capacity)/10
    
    # admit a patient to the quarantine of given name and date of birth 
    def admission (self, name, dob):         
        p = Patient (name, dob)
        self.patients.append(p)
    
    def serialize(self):
        return {
            'id': self.ID, 
            'name': self.name, 
            'capacity': self.capacity,
            'occupancy': str(self.occupancy())+"%",
        }
    

    
