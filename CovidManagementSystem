from Staff import *
from Patient import *
from Hospital import *
from Quarantine import *

class CovidManagementSystem:    
    def __init__(self):
        self.hospitals = [] # list of hospitals known to the system
        self.quarantines = [] # list of quarantine areas known to the system
        self.staff = [] # list of staff known to the system
        self.patients = [] # list of patients in the system
        
    def getHospitals (self): 
        return self.hospitals

    def addHospital (self, name, capacity): 
        h = Hospital (name, capacity)
        self.hospitals.append(h)
    
    def getHospitalById(self, id_):
        for h in self.hospitals: 
            if(h.ID==id_):
                return h
            else: 
                return None 
    
    def deleteHospital (self, id_):
        h = self.getHospitalById(id_)
        if(h!=None): 
            self.hospitals.remove (h)
        return h!=None

    def getQuarantines (self): 
        return self.quarantines

    def addQuarantine (self, name, capacity): 
        h = Quarantine (name, capacity)
        self.quarantines.append(h)
    
    def getQuarantineById(self, id_): 
        for h in self.quarantines: 
            if(h.ID==id_):
                return h
        return None 
    
    def deleteQuarantine (self, id_):
        h = self.getQuarantineById(id_)
        if(h!=None):
            i=0
            while(len(h.patients)!=0):
                if i<len(self.quarantines):
                    self.quarantines[i].patients.append(h.patients[-1])
                    h.patients=h.patients[0:-1]
                    i=i+1
                else:
                    i=0
            self.quarantines.remove (h)
        return h!=None  

    def addStaff (self,name,dob,t): 
        s=Staff(name,dob,t)
        self.staff.append(s)
    
    def getStaff (self): 
        return self.staff   

    def assignTo (self, s_ID, w):
        q=0
        for i in self.staff:
            if i.ID==s_ID:
                q=1
                for j in self.hospitals:
                    if j.ID==w:
                        q=2
                        j.staff.append(i)
                        i.workplace=w
                        i.workplace_name=j.name
                if q==1:
                    for j in self.quarantines:
                        if j.ID==w:
                            j.staff.append(i)
                            i.workplace=w
                            i.workplace_name=j.name
        if q==0:
            return("There is no staff member with that ID")
        elif q==1:
            return("There is no medical facility with that ID")
        else:
            return("The staff member with the ID "+str(s_ID)+" has been assigned to the medical facility with the ID "+str(w)+".")
            
            
    def deleteStaff (self,s_ID):
        q=0
        for i in self.staff:
            if i.ID==s_ID:
                q=1
                for j in self.hospitals:
                    j.staff.remove(i)
                for j in self.quarantines:
                    j.staff.remove(i)
                self.staff.remove(i)
        return q
            



    def getPatientById(self, id_):
            for h in self.patients: 
                if(h.ID==id_):
                    return 1
                else: 
                    return None  
    
    def addpatient(self, a,b):
        p=Patient(a,b)
        self.patients.append(p)
        
        
        
    def admitP (self, p_ID, f_ID):
        q=0
        for i in self.patients:
            if i.ID==p_ID:
                q=1
                for j in self.hospitals:
                    if j.ID==f_ID:
                        q=2
                        j.patients.append(i)
                        i.mf=f_ID
                        i.mf_name=j.name
                if q==1:
                    for j in self.quarantines:
                        if j.ID==f_ID:
                            j.patients.append(i)
                            i.mf=f_ID
                            i.mf_name=j.name
        if q==0:
            return("There is no patient with that ID.")
        elif q==1:
            return("There is no medical facility with that ID.")
        else:
            return("The patient with the ID "+str(p_ID)+" has been assigned to the medical facility with the ID "+str(f_ID)+".")
