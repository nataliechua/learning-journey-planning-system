from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from os import environ
from flask_cors import CORS
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/g3t07ddl'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_size': 100,
                                           'pool_recycle': 280}

db = SQLAlchemy(app)

CORS(app)


class Course(db.Model):
    __tablename__ = 'course'

    course_id = db.Column(db.String(10), primary_key=True, nullable=False)
    course_name = db.Column(db.String(50), nullable=False)
    course_desc = db.Column(db.String(255))
    course_status = db.Column(db.String(15))
    course_type = db.Column(db.String(10))
    course_category = db.Column(db.String(50))

    def __init__(self,course_id,course_name,course_desc,course_status,course_type,course_category):
        self.course_id=course_id
        self.course_name=course_name
        self.course_desc=course_desc
        self.course_status=course_status
        self.course_type=course_type
        self.course_category=course_category

    def to_dict(self):
        """
        'to_dict' converts the object into a dictionary,
        in which the keys correspond to database columns
        """
        columns = self.__mapper__.column_attrs.keys()
        result = {}
        for column in columns:
            result[column] = getattr(self, column)
        return result

class Course_Registration(db.Model):
    __tablename__ = 'course_registration'

    reg_id = db.Column(db.Integer, primary_key=True, nullable=False)
    course_id = db.Column(db.String(10), db.ForeignKey('course.course_id'), nullable=False)
    staff_id = db.Column(db.Integer, db.ForeignKey('staff.staff_id'), nullable=False)
    reg_status = db.Column(db.String(15), nullable=False)
    completion_status = db.Column(db.String(15))

    def __init__(self,reg_id,course_id,staff_id,reg_status,completion_status):
        self.reg_id=reg_id
        self.course_id=course_id
        self.staff_id=staff_id
        self.reg_status=reg_status
        self.completion_status=completion_status

    def to_dict(self):
        """
        'to_dict' converts the object into a dictionary,
        in which the keys correspond to database columns
        """
        columns = self.__mapper__.column_attrs.keys()
        result = {}
        for column in columns:
            result[column] = getattr(self, column)
        return result

class Course_Skill(db.Model):
    __tablename__ = 'course_skill'

    course_id = db.Column(db.String(10), db.ForeignKey('course.course_id'), nullable=False)
    skill_id = db.Column(db.Integer, db.ForeignKey('skill.skill_id'), nullable=False)

    __table_args__=(
        db.PrimaryKeyConstraint(
            course_id,skill_id
        ),
    )

    def __init__(self,course_id,skill_id):
        self.course_id=course_id
        self.skill_id=skill_id

    def to_dict(self):
        """
        'to_dict' converts the object into a dictionary,
        in which the keys correspond to database columns
        """
        columns = self.__mapper__.column_attrs.keys()
        result = {}
        for column in columns:
            result[column] = getattr(self, column)
        return result

class Journey(db.Model):
    __tablename__ = 'journey'

    journey_id = db.Column(db.Integer, primary_key=True, nullable=False)
    journey_name = db.Column(db.String(30), nullable=False)
    staff_id = db.Column(db.Integer, db.ForeignKey('staff.staff_id'), nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey('role.role_id'),nullable=False)
    skill_id = db.Column(db.Integer, db.ForeignKey('skill.skill_id'), nullable=False)
    course_id = db.Column(db.String(10), db.ForeignKey('course.course_id'), nullable=False)
    completion_status = db.Column(db.String(15))

    def __init__(self,journey_id,journey_name,staff_id,role_id,skill_id,course_id,completion_status):
        self.journey_id=journey_id
        self.journey_name=journey_name
        self.staff_id=staff_id
        self.role_id=role_id
        self.skill_id=skill_id
        self.course_id=course_id
        self.completion_status=completion_status

    def to_dict(self):
        """
        'to_dict' converts the object into a dictionary,
        in which the keys correspond to database columns
        """
        columns = self.__mapper__.column_attrs.keys()
        result = {}
        for column in columns:
            result[column] = getattr(self, column)
        return result

class Journey_Course(db.Model):
    __tablename__ = 'journey_course'

    journey_id = db.Column(db.Integer, db.ForeignKey('journey.journey_id'), nullable=False)
    course_id = db.Column(db.String(10),db.ForeignKey('course.course_id'), nullable=False)
    completion_status = db.Column(db.String(15))

    __table_args__=(
        db.PrimaryKeyConstraint(
            journey_id,course_id
        ),
    )

    def __init__(self,journey_id,course_id,completion_status):
        self.journey_id=journey_id
        self.course_id=course_id
        self.completion_status=completion_status

    def to_dict(self):
        """
        'to_dict' converts the object into a dictionary,
        in which the keys correspond to database columns
        """
        columns = self.__mapper__.column_attrs.keys()
        result = {}
        for column in columns:
            result[column] = getattr(self, column)
        return result

class Journey_Skill(db.Model):
    __tablename__ = 'journey_skill'

    journey_id = db.Column(db.Integer, db.ForeignKey('journey.journey_id'), nullable=False)
    skill_id = db.Column(db.Integer,db.ForeignKey('skill.skill_id'),nullable=False)
    completion_status = db.Column(db.String(15))

    __table_args__=(
        db.PrimaryKeyConstraint(
            journey_id,skill_id
        ),
    )

    def __init__(self,journey_id,course_id,completion_status):
        self.journey_id=journey_id
        self.course_id=course_id
        self.completion_status=completion_status

    def to_dict(self):
        """
        'to_dict' converts the object into a dictionary,
        in which the keys correspond to database columns
        """
        columns = self.__mapper__.column_attrs.keys()
        result = {}
        for column in columns:
            result[column] = getattr(self, column)
        return result

class Role(db.Model):
    __tablename__ = 'role'

    role_id = db.Column(db.Integer,primary_key=True, nullable=False)
    role_name = db.Column(db.String(50))
    role_status = db.Column(db.String(15))

    def __init__(self,role_id,role_name,role_status):
        self.role_id=role_id
        self.role_name=role_name
        self.role_status=role_status

    def to_dict(self):
        """
        'to_dict' converts the object into a dictionary,
        in which the keys correspond to database columns
        """
        columns = self.__mapper__.column_attrs.keys()
        result = {}
        for column in columns:
            result[column] = getattr(self, column)
        return result

class Role_Skill(db.Model):
    __tablename__ = 'role_skill'

    role_id = db.Column(db.Integer, db.ForeignKey('role.role_id'), nullable=False)
    skill_id = db.Column(db.Integer, db.ForeignKey('skill.skill_id'),nullable=False)

    __table_args__=(
        db.PrimaryKeyConstraint(
            role_id,skill_id
        ),
    )

    def __init__(self,role_id,skill_id):
        self.role_id=role_id
        self.skill_id=skill_id

    def to_dict(self):
        """
        'to_dict' converts the object into a dictionary,
        in which the keys correspond to database columns
        """
        columns = self.__mapper__.column_attrs.keys()
        result = {}
        for column in columns:
            result[column] = getattr(self, column)
        return result

class Skill(db.Model):
    __tablename__ = 'skill'

    skill_id = db.Column(db.Integer,primary_key=True, nullable=False)
    skill_name = db.Column(db.String(50), nullable=False)
    skill_status = db.Column(db.String(15), nullable=False)

    def __init__(self,skill_id,skill_name,skill_status):
        self.skill_id=skill_id
        self.skill_name=skill_name
        self.skill_status=skill_status

    def to_dict(self):
        """
        'to_dict' converts the object into a dictionary,
        in which the keys correspond to database columns
        """
        columns = self.__mapper__.column_attrs.keys()
        result = {}
        for column in columns:
            result[column] = getattr(self, column)
        return result

class Staff(db.Model):
    __tablename__ = 'staff'

    staff_id = db.Column(db.Integer,primary_key=True, nullable=False)
    staff_fname = db.Column(db.String(30), nullable=False)
    staff_lname = db.Column(db.String(30), nullable=False)
    dept = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    user_type = db.Column(db.Integer,db.ForeignKey('user_type.usetype_id'), nullable=False)

    def __init__(self,staff_id,staff_fname,staff_lname,dept,email,user_type):
        self.staff_id=staff_id
        self.staff_fname=staff_fname
        self.staff_lname=staff_lname
        self.dept=dept
        self.email=email
        self.user_type=user_type
    
    # __mapper_args__ = {
    #     'polymorphic_identity': 'staff'
    # }

    def to_dict(self):
        """
        'to_dict' converts the object into a dictionary,
        in which the keys correspond to database columns
        """
        columns = self.__mapper__.column_attrs.keys()
        result = {}
        for column in columns:
            result[column] = getattr(self, column)
        return result

# class HR(Staff):
#     __tablename__ = 'HR'

#     id = db.Column(db.Integer, db.ForeignKey('person.id'), primary_key=True)
#     reg_num = db.Column(db.String(15))
#     hourly_rate = db.Column(db.Integer)

#     __mapper_args__ = {
#         'polymorphic_identity': 'doctor',
#     }

#     def calculate_charges(self, num_mins):
#         """
#         Uses the doctor's hourly rate to determine how much
#         a 'num_mins' length appointment should be charged.
#         NB: an appointment shorter than 10 mins is charged
#         as if it were 10 mins long.
#         """
#         if num_mins < 10:
#             result = self.hourly_rate / 6
#         else:
#             result = self.hourly_rate * (num_mins / 60)
#         return result

class User_Type(db.Model):
    __tablename__ = 'user_type'

    usertype_id = db.Column(db.Integer,primary_key=True, nullable=False)
    usertype_name = db.Column(db.String(20), nullable=False)

    def __init__(self,usertype_id,usertype_name):
        self.usertype_id=usertype_id
        self.usertype_name=usertype_name

    def to_dict(self):
        """
        'to_dict' converts the object into a dictionary,
        in which the keys correspond to database columns
        """
        columns = self.__mapper__.column_attrs.keys()
        result = {}
        for column in columns:
            result[column] = getattr(self, column)
        return result

db.create_all()

#############################################################################
@app.route("/courses")
def get_all_courses():
    clist = Course.query.all()
    if clist:
        return jsonify(
            {
                "code": 200,
                "data": {
                    "courses": [course.to_dict() for course in clist]
                }
            }
        ), 200
    return jsonify(
        {
            "code": 404,
            "message": "There are no courses."
        }
    ), 404

@app.route("/course_registrations")
def get_all_course_registrations():
    crlist = Course_Registration.query.all()
    if crlist:
        return jsonify(
            {
                "code": 200,
                "data": {
                    "course_registrations": [course_registration.to_dict() for course_registration in crlist]
                }
            }
        ), 200
    return jsonify(
        {
            "code": 404,
            "message": "There are no course registrations."
        }
    ), 404

@app.route("/course_skills")
def get_all_course_skills():
    cslist = Course_Skill.query.all()
    if cslist:
        return jsonify(
            {
                "code": 200,
                "data": {
                    "course_skills": [course_skill.to_dict() for course_skill in cslist]
                }
            }
        ), 200
    return jsonify(
        {
            "code": 404,
            "message": "There are no course skills."
        }
    ), 404

@app.route("/roles")
def get_all_roles():
    rlist = Role.query.all()
    if rlist:
        return jsonify(
            {
                "code": 200,
                "data": {
                    "roles": [role.to_dict() for role in rlist]
                }
            }
        ), 200
    return jsonify(
        {
            "code": 404,
            "message": "There are no roles."
        }
    ), 404

@app.route("/role_skills")
def get_all_role_skills():
    rslist = Role_Skill.query.all()
    if rslist:
        return jsonify(
            {
                "code": 200,
                "data": {
                    "role_skills": [role_skill.to_dict() for role_skill in rslist]
                }
            }
        ), 200
    return jsonify(
        {
            "code": 404,
            "message": "There are no role skills."
        }
    ), 404

@app.route("/skills")
def get_all_skills():
    slist = Skill.query.all()
    if slist:
        return jsonify(
            {
                "code": 200,
                "data": {
                    "skills": [skill.to_dict() for skill in slist]
                }
            }
        ), 200
    return jsonify(
        {
            "code": 404,
            "message": "There are no skills."
        }
    ), 404

@app.route("/staffs")
def get_all_staffs():
    slist = Staff.query.all()
    if slist:
        return jsonify(
            {
                "code": 200,
                "data": {
                    "staffs": [staff.to_dict() for staff in slist]
                }
            }
        ), 200
    return jsonify(
        {
            "code": 404,
            "message": "There are no staffs."
        }
    ), 404

@app.route("/user_types")
def get_all_user_types():
    utlist = User_Type.query.all()
    if utlist:
        return jsonify(
            {
                "code": 200,
                "data": {
                    "user_types": [user_type.to_dict() for user_type in utlist]
                }
            }
        ), 200
    return jsonify(
        {
            "code": 404,
            "message": "There are no user types."
        }
    ), 404


#############################################################################
# @app.route("/persons/<int:person_id>")
# def person_by_id(person_id):
#     person = Person.query.filter_by(id=person_id).first()
#     if person:
#         return jsonify({
#             "data": person.to_dict()
#         }), 200
#     else:
#         return jsonify({
#             "message": "Person not found."
#         }), 404


# @app.route("/doctors")
# def doctors():
#     search_name = request.args.get('name')
#     if search_name:
#         doctor_list = Doctor.query.filter(Doctor.name.contains(search_name))
#     else:
#         doctor_list = Doctor.query.all()
#     return jsonify(
#         {
#             "data": [doctor.to_dict() for doctor in doctor_list]
#         }
#     ), 200

# @app.route("/doctors", methods=['POST'])
# def create_doctor():
#     data = request.get_json()
#     if not all(key in data.keys() for
#                key in ('name', 'title',
#                        'reg_num', 'hourly_rate')):
#         return jsonify({
#             "message": "Incorrect JSON object provided."
#         }), 500
#     doctor = Doctor(**data)
#     try:
#         db.session.add(doctor)
#         db.session.commit()
#         return jsonify(doctor.to_dict()), 201
#     except Exception:
#         return jsonify({
#             "message": "Unable to commit to database."
#         }), 500


# @app.route("/patients")
# def patients():
#     search_name = request.args.get('name')
#     if search_name:
#         patient_list = Patient.query.filter(Doctor.name.contains(search_name))
#     else:
#         patient_list = Patient.query.all()
#     return jsonify(
#         {
#             "data": [patient.to_dict() for patient in patient_list]
#         }
#     ), 200


# @app.route("/patients", methods=['POST'])
# def create_patient():
#     data = request.get_json()
#     if not all(key in data.keys() for
#                key in ('name', 'title',
#                        'contact_num', 'ewallet_balance')):
#         return jsonify({
#             "message": "Incorrect JSON object provided."
#         }), 500
#     patient = Patient(**data)
#     try:
#         db.session.add(patient)
#         db.session.commit()
#         return jsonify(patient.to_dict()), 201
#     except Exception:
#         return jsonify({
#             "message": "Unable to commit to database."
#         }), 500


# @app.route("/consultations")
# def consultations():
#     consultation_list = Consultation.query.all()
#     return jsonify(
#         {
#             "data": [consultation.to_dict()
#                      for consultation in consultation_list]
#         }
#     ), 200


# @app.route("/consultations", methods=['POST'])
# def create_consultation():
#     data = request.get_json()
#     if not all(key in data.keys() for
#                key in ('doctor_id', 'patient_id',
#                        'diagnosis', 'prescription', 'length')):
#         return jsonify({
#             "message": "Incorrect JSON object provided."
#         }), 500

#     # (1): Validate doctor
#     doctor = Doctor.query.filter_by(id=data['doctor_id']).first()
#     if not doctor:
#         return jsonify({
#             "message": "Doctor not valid."
#         }), 500

#     # (2): Compute charges
#     charge = doctor.calculate_charges(data['length'])

#     # (3): Validate patient
#     patient = Patient.query.filter_by(id=data['patient_id']).first()
#     if not patient:
#         return jsonify({
#             "message": "Patient not valid."
#         }), 500

#     # (4): Subtract charges from patient's e-wallet
#     try:
#         patient.ewallet_withdraw(charge)
#     except Exception:
#         return jsonify({
#             "message": "Patient does not have enough e-wallet funds."
#         }), 500

#     # (4): Create consultation record
#     consultation = Consultation(
#         diagnosis=data['diagnosis'], prescription=data['prescription'],
#         doctor_id=data['doctor_id'], patient_id=data['patient_id'],
#         charge=charge
#     )

#     # (5): Commit to DB
#     try:
#         db.session.add(consultation)
#         db.session.commit()
#         return jsonify(consultation.to_dict()), 201
#     except Exception:
#         return jsonify({
#             "message": "Unable to commit to database."
#         }), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)