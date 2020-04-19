from flask import Flask, request, jsonify
from CovidManagementSystem import *
from Patient import *
from Hospital import *
from Quarantine import *

app = Flask(__name__)

# Root object for the management system
ms = CovidManagementSystem ()

#Add a new hospital (parameters: name, capacity). 
@app.route("/hospital", methods=["POST"])
def addHospital():
    ms.addHospital(request.args.get('name'), request.args.get('capacity'))   
    return jsonify(f"Added a new hospital called {request.args.get('name')} with capacity {request.args.get('capacity')}")


#Return the details of a hospital of the given hospital_id. 
@app.route("/hospital/<hospital_id>", methods=["GET"])
def hospitalInfo(hospital_id):     
    h = ms.getHospitalById(hospital_id)
    if(h!=None):
        print(jsonify(h.serialize()))
        return jsonify(h.serialize())
    return jsonify(
            success = False, 
            message = "Hospital with ID "+hospital_id+" not found")

# Admission of a patient to a given hospital 
@app.route("/hospital/<hospital_id>/patient", methods=["POST"])
def admitpatienth(hospital_id):       
    h = ms.getHospitalById(hospital_id)
    if(h!=None):
        h.admission(request.args.get('name'), request.args.get('dob'))
        try:
            x=ms.getPatientById(h.patients[-1].ID)
            if(x==None):
                ms.addPatient(h.patients[-1])
        except:
            pass
        
        return jsonify(
                success = 1, 
                message = "Patient "+request.args.get('name')+" has been admitted to hospital "+h.name) 
    else:
        return jsonify(
                success = null, 
                message = "There was an error. Please check the URL and try again.")
    
@app.route("/hospital/<hospital_id>", methods=["DELETE"])
def deleteHospital(hospital_id):
    
    result = ms.deleteHospital(hospital_id)   
    if(result): 
        message = f"Hospital with id{hospital_id} was deleted" 
    else: 
        message = "Hospital not found" 
    return jsonify(
            success = result, 
            message = message)

@app.route("/hospitals", methods=["GET"])
def allHospitals():   
    return jsonify(hospitals=[h.serialize() for h in ms.getHospitals()])








#Add a new quarantine area (parameters: name, capacity). 
@app.route("/quarantine", methods=["POST"])
def addquarantine():
    ms.addQuarantine(request.args.get('name'), request.args.get('capacity'))   
    return jsonify(f"Added a new quarantine area called {request.args.get('name')} with capacity {request.args.get('capacity')}")

#Return the details of a quarantine of the given qu_id. 
@app.route("/quarantine/<qu_id>", methods=["GET"])
def quarantineInfo(qu_id):       
    h = ms.getQuarantineById(qu_id)
    if(h!=None): 
        return jsonify(h.serialize())
    return jsonify(
            success = False, 
            message = "Quarantine area not found")

# Admission of a patient to a given quarantine area 
@app.route("/quarantine/<qu_id>/patient", methods=["POST"])
def admitpatientq(qu_id):       
    h = ms.getQuarantineById(qu_id)
    if(h!=None):
        h.admission(request.args.get('name'), request.args.get('dob'))
        try:
            x=ms.getPatientById(h.patients[-1].ID)
            if(x==None):
                ms.addPatient(h.patients[-1])
        except:
            pass
        
        return jsonify(
                success = 1, 
                message = "Patient "+request.args.get('name')+" has been admitted to quarantine "+h.name) 
    else:
        return jsonify(
                success = null, 
                message = "There was an error. Please check the URL and try again.")
    
@app.route("/quarantine/<qu_id>", methods=["DELETE"])
def deleteQuarantine(qu_id):
    
    result = ms.deleteQuarantine(qu_id)   
    if(result): 
        message = f"Quarantine area with id{qu_id} was deleted" 
    else: 
        message = "Quarantine area not found" 
    return jsonify(
            success = result, 
            message = message)

@app.route("/quarantines", methods=["GET"])
def allQuarantines():   
    return jsonify(quarantines=[h.serialize() for h in ms.getQuarantines()])



#Add a new staff member to the system (parameters: name, dob, type). 
@app.route("/staff", methods=["POST"])
def addStaff():
    ms.addStaff(request.args.get('name'), request.args.get('dob'), request.args.get('type'))
    if request.args.get('type')=='doctor' or request.args.get('type')=='nurse':
        return jsonify(f"Added a new {request.args.get('type')} named {request.args.get('name')} with the date of birth {request.args.get('dob')}")
    else:
        return jsonify("'type' of new staff member should be either doctor or nurse.")


@app.route("/staff", methods=["GET"])
def allStaff():   
    return jsonify(staff=[h.serialize() for h in ms.getStaff()])


@app.route("/staff/<staff_id>", methods=["PUT"])
def assignWorkplace(staff_id):
    return jsonify(ms.assignTo(staff_id,request.args.get('workplace')))


@app.route("/staff/<staff_id>", methods=["DELETE"])
def delStaff(staff_id):
    result = ms.deleteStaff(staff_id)   
    if(result): 
        message = f"Staff member with ID {staff_id} was deleted."
    else: 
        message = f"There is no staff member with ID {staff_id}."
    return jsonify(message)
    
    
    

#Add a new patient to the system (parameters: name, dob). 
@app.route("/patient", methods=["POST"])
def addPatient():
    ms.addpatient(request.args.get('name'), request.args.get('dob'))   
    return jsonify(f"Added a new patient named {request.args.get('name')} with the date of birth {request.args.get('dob')}")



@app.route("/patient/<pat_id>/admit/<facility_id>", methods=["PUT"])
def admitPatient(pat_id,facility_id):
    return jsonify(ms.admitP(pat_id,facility_id))


@app.route("/patient/<pat_id>/discharge/<facility_id>", methods=["PUT"])
def dischargePatient(pat_id,facility_id):
    return jsonify(ms.dischargeP(pat_id,facility_id))


@app.route("/patients", methods=["GET"])
def allPatients():
    return jsonify(patients=[p.serialize() for p in ms.getPatients()])


@app.route("/patient/<pat_id>/diagnosis", methods=["POST"])
def diagnosePatient(pat_id):
    return jsonify(ms.diagnose(pat_id))


@app.route("/patient/<pat_id>/cure", methods=["POST"])
def curePatient(pat_id):
    return jsonify(ms.cure(pat_id))


@app.route("/stats", methods=["GET"])
def Statistics():
    return jsonify(ms.stats())


@app.route("/")
def index():
    return jsonify(
            success = True, 
            message = "Your server is running! Welcome to the Covid API.")

@app.after_request
def add_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] =  "Content-Type, Access-Control-Allow-Headers, Authorization, X-Requested-With"
    response.headers['Access-Control-Allow-Methods']=  "POST, GET, PUT, DELETE"
    return response

if __name__ == "__main__":
    app.run(debug=False, port=8888)