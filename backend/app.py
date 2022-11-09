from itertools import groupby
from re import S
from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import delete, insert, update
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

######################################################################################################
#LINK TO DATABASE
######################################################################################################

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

    def __init__(self,journey_id,journey_name,staff_id,role_id):
        self.journey_id=journey_id
        self.journey_name=journey_name
        self.staff_id=staff_id
        self.role_id=role_id

    def to_dict(self):
        columns = self.__mapper__.column_attrs.keys()
        result = {}
        for column in columns:
            result[column] = getattr(self, column)
        return result

class Journey_Skill_Course(db.Model):
    __tablename__ = 'journey_skill_course'

    journey_id = db.Column(db.Integer, db.ForeignKey('journey.journey_id'), nullable=False)
    course_id = db.Column(db.String(10),db.ForeignKey('course.course_id'), nullable=False)
    skill_id = db.Column(db.Integer,db.ForeignKey('skill.skill_id'),nullable=False)

    __table_args__=(
        db.PrimaryKeyConstraint(
            journey_id,skill_id, course_id
        ),
    )

    def __init__(self,journey_id,course_id,skill_id,):
        self.journey_id=journey_id
        self.course_id=course_id
        self.skill_id=skill_id

    def to_dict(self):
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
    user_type = db.Column(db.String(20), nullable=False)

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


with app.app_context():
    db.create_all()
######################################################################################################
#ROUTES TO RETRIEVE INFO
######################################################################################################

#get courses by skill id
@app.route("/courses_by_skill/<int:skill_id>")
def get_courses_by_skill_id(skill_id):
    list = db.session.query(Course_Skill, Course, Skill).select_from(Course_Skill).join(Course).join(Skill).filter(Course_Skill.skill_id==skill_id)
        
    if list.count():
        return jsonify(
            {
                "code": 200,
                "data": {
                    #"skill": [skill.to_dict() for course_skill, course, skill in list][0],
                    "courses": [course.to_dict() for course_skill, course, skill in list]
                }
            }
        ), 200
    return jsonify(
        {
            "code": 404,
            "message": "There are no courses for skill with id = " + str(skill_id) + "." 
        }
    ), 404

#get skills by course id
@app.route("/skills_by_course/<string:course_id>")
def get_skills_by_course_id(course_id):
    list = db.session.query(Course_Skill, Course, Skill).select_from(Course_Skill).join(Course).join(Skill).filter(Course_Skill.course_id==course_id)
        
    if list.count():
        return jsonify(
            {
                "code": 200,
                "data": {
                    "course": [course.to_dict() for course_skill, course, skill in list][0],
                    "skills": [skill.to_dict() for course_skill, course, skill in list]
                }
            }
        ), 200
    return jsonify(
        {
            "code": 404,
            "message": "There are no skills for course with id = " + str(course_id) + "." 
        }
    ), 404

#get courses and skills by course status: 
@app.route("/courses_skills_by_course_status/<string:course_status>")
def get_courses_skills_by_course_status(course_status):
    ans=[]
    clist = Course.query.filter_by(course_status=course_status)
    if clist.count():
        for course in clist:
            tempdic = {
                "course_id": course.course_id,
                "course_name": course.course_name,
                "course_desc": course.course_desc,
                "course_status": course.course_status,
                "course_type": course.course_type,
                "course_category": course.course_category,
            }
            raw_response = make_response(get_skills_by_course_id(course.course_id))
            if raw_response.status_code==404:
                tempdic["course_skills"] = []
                ans.append(tempdic)
            else:
                response=raw_response.get_json()
                skills =  response["data"]["skills"]
                tempdic["course_skills"] = skills
                ans.append(tempdic)
            
        return jsonify(
            {
                "code": 200,
                "data": {
                    "courses": ans,
                }
            }
        ), 200
    return jsonify(
        {
            "code": 404,
            "message": "There are no courses with status = " + course_status + "." 
        }
    ), 404

#get active skills whether in course by course id
@app.route("/active_skills_whether_in_course/<string:course_id>")
def get_active_skills_whether_in_course_by_course_id(course_id):
    course = Course.query.filter_by(course_id=course_id).first()
    cslist = Course_Skill.query.filter_by(course_id = course_id)
    slist = Skill.query.filter_by(skill_status="Active")
    in_course_skills = []
    ans = []

    if cslist.count() != 0:
        for cs in cslist:
            in_course_skills.append(cs.skill_id)
    for s in slist:
        if s.skill_id in in_course_skills:
            tempdic = {
                "skill_id": s.skill_id,
                "skill_name": s.skill_name,
                "skill_status": s.skill_status,
                "skill_in_course": True
            }
        else:
            tempdic = {
                "skill_id": s.skill_id,
                "skill_name": s.skill_name,
                "skill_status": s.skill_status,
                "skill_in_course": False
            }
        ans.append(tempdic)
    return jsonify(
        {
            "code": 200,
            "data": {
                "course": course.to_dict(),
                "skills": ans
            }
        }
    ), 200

#update course skill
@app.route("/course_skill/update", methods=['POST'])
def update_course_skill():
    data = request.get_json()
    course_id=data["course_id"]
    skill_ids=data["skill_ids"]
    try:
        Course_Skill.query.filter_by(course_id = course_id).delete()
        db.session.commit()
    except Exception as e:
        return jsonify(
            {
                "code":500,
                "message": "An error occurred while deleting course skill pair(s) with course_id = "+course_id+". " ,
                "error":str(e)
            }
        )
    try:
        for skill_id in skill_ids:
            cs = {
                "course_id":course_id,
                "skill_id":skill_id
            }
            course_skill = Course_Skill(**cs)
            db.session.add(course_skill)
            db.session.commit()
    except Exception as e:
        return jsonify(
            {
                "code": 500,
                "message": "An error occurred while creating the course skill pairs. " ,
                "error":str(e)
            }
        ), 500

    return jsonify(
        {
            "code": 201,
            "message": "Course skill pair(s) updated successfully.",
            "data": data
        }
    ), 201

#get all journey info by journey id
@app.route("/all_journey_info/<int:journey_id>")
def get_all_journey_info_by_journey_id(journey_id):
    journey = Journey.query.filter_by(journey_id=journey_id).first()
    if journey:
        jsclist = Journey_Skill_Course.query.filter_by(journey_id=journey_id)
        track = []
        ans = []
        role = Role.query.filter_by(role_id=journey.role_id).first()
        for jsc in jsclist:
            if jsc.skill_id not in track:
                skill = Skill.query.filter_by(skill_id=jsc.skill_id).first()
                temp={
                    "skill_id":skill.skill_id,
                    "skill_name":skill.skill_name,
                    "skill_status":skill.skill_status,
                    "skill_courses":[]
                }
                ans.append(temp)
                track.append(jsc.skill_id)
            for skill in ans:
                if skill["skill_id"]==jsc.skill_id:
                    course_info = Course.query.filter_by(course_id=jsc.course_id).first()
                    course_ans = course_info.to_dict()
                    course_registration_info = Course_Registration.query.filter_by(staff_id=journey.staff_id,course_id=jsc.course_id).first()
                    if course_registration_info:
                        course_ans["course_completion_status"] =course_registration_info.completion_status
                    else:
                        course_ans["course_completion_status"] = "Not Registered"
                    
                    skill["skill_courses"].append(course_ans)

        return jsonify(
            {
                "code": 200,
                "data": {
                    "journey_id": journey_id,
                    "journey_name":journey.journey_name,
                    #"role_id":journey.role_id,
                    "role": role.to_dict(),
                    "staff_id":journey.staff_id,
                    "journey_completion_status": journey_completion_status(ans),
                    "skills": ans
                }
            }
        ), 200

    return jsonify(
        {
            "code": 404,
            "message": "There is no journey with journey id = "+journey_id+ "."
        }
    ), 404

def journey_completion_status(skills_list):
    skills_count = 0
    skills_completed_count = 0
    for skill in skills_list:
        skills_count +=1
        for course in skill["skill_courses"]:
            if course["course_completion_status"] =="Completed":
                skills_completed_count +=1
                break
        
    return round(skills_completed_count/skills_count * 100)

#get all journeys info by staff id
@app.route("/all_journeys_info/<int:staff_id>")
def get_all_journeys_info_by_staff_id(staff_id):
    journeys = Journey.query.filter_by(staff_id=staff_id)
    ans=[]
    if journeys.count()==0:
        return jsonify(
            {
                "code": 404,
                "message": "There is no journey with staff id = "+staff_id+ "."
            }
        ), 404

    for journey in journeys:
        raw_response = make_response(get_all_journey_info_by_journey_id(journey.journey_id))
        response=raw_response.get_json()
        data =  response["data"]
        ans.append(data)
    
    return jsonify(
        {
            "code": 200,
            "data": {
                "staff_id":staff_id,
                "journeys":ans
            }
        }
    ), 200


#remove journey by id
@app.route("/journey_remove/<int:id>")
def remove_journey_by_id(id):
    try:
        j = Journey.query.filter_by(journey_id = id).delete()
        if not j:
            return jsonify(
                {
                    "code": 404,
                    "message": "Journey with id = " + str(id) + " not found."
                }
            ), 404
        db.session.commit()
    except Exception as e:
        return jsonify(
            {
                "code":500,
                "message": "An error occurred while deleting the journey. " ,
                "error":str(e)
            }
        )
    
    try:
        jsc = Journey_Skill_Course.query.filter_by(journey_id = id).delete()
        db.session.commit()
    except Exception as e:
        return jsonify(
            {
                "code":500,
                "message": "An error occurred while deleting the journey skill course pair. " ,
                "error":str(e)
            }
        )
    
    return jsonify(
        {
            "code": 202,
            "message": "Journey deleted successfully."
        }
    ), 202

#remove journey skill course
@app.route("/remove_journey_skill_course/<int:journey_id>/<int:skill_id>/<string:course_id>")
def remove_journey_skill_course(journey_id,skill_id,course_id):
    try:
        jsc = Journey_Skill_Course.query.filter_by(journey_id = journey_id,course_id = course_id, skill_id=skill_id).delete()
        if not jsc:
            return jsonify(
                {
                    "code": 404,
                    "message": "Journey skill course pair with journey_id = " + str(journey_id) + ", course_id = " + str(course_id) + " and skill_id = " + str(skill_id) + " not found."
                }
            ), 404        
        db.session.commit()
    except Exception as e:
        return jsonify(
            {
                "code":500,
                "message": "An error occurred while deleting the journey skill course pair. " ,
                "error":str(e)
            }
        )
    return jsonify(
        {
            "code": 202,
            "message": "Journey skill course pair deleted successfully."
        }
    ), 202

#create journey
@app.route("/journey/create", methods=['POST'])
def create_journey():
    journey_data = request.get_json()

    if not all(key in journey_data.keys() for 
               key in ("journey_name","staff_id","role_id","skills")):
        return jsonify({
            "message": "Invalid JSON input. Journey name, staff id, role id and journey skills should be provided in the JSON object."
        }), 500
    
    if journey_data["journey_name"].isspace() or journey_data["journey_name"] == None or len(journey_data["journey_name"])==0:
        return jsonify(
            {   
                "code": 500,
                "message": "Journey name should not be empty or just contain white spaces."
            }
        ), 500 

    if journey_data["role_id"] == "":
        return jsonify(
            {   
                "code": 500,
                "message": "A Journey should at least have one role."
            }
        ), 500

    if journey_data["skills"] == [
                {
                    "skill_id": "",
                    "course_ids": [""]
                }
            ]:
        return jsonify(
            {   
                "code": 500,
                "message": "A Journey should at least have one skill."
            }
        ), 500 
    
    if len(journey_data["skills"])==1 and journey_data["skills"][0]["course_ids"]==[""]:
        return jsonify(
            {   
                "code": 500,
                "message": "A Journey should at least have one course."
            }
        ), 500 

    for skill in journey_data["skills"]:
        if not all(key in skill.keys() for 
               key in ("skill_id","course_ids")):
            return jsonify({
                "message": "Invalid JSON input. Skill id and corresponding courses ids should be provided in the JSON object."
            }), 500
        
        if skill["skill_id"] == None:
            return jsonify(
            {   
                "code": 500,
                "message": "A Skill must be chosen for each skill courses pair."
            }
        ), 500

        if skill["course_ids"] == None or skill["course_ids"] == [] or skill["course_ids"] == [""]:
            return jsonify(
            {   
                "code": 500,
                "message": "At least a course must be chosen for each skill courses pair."
            }
        ), 500 

    journey_input = {
        "journey_name":journey_data["journey_name"],
        "staff_id":journey_data["staff_id"],
        "role_id":journey_data["role_id"]
    }
    skills = journey_data["skills"]

    try:
        journey = Journey(**journey_input,journey_id = None)
        db.session.add(journey)
        db.session.commit()
        journey_id = journey.journey_id
    except Exception as e:
        return jsonify(
            {
                "code": 500,
                "message": "An error occurred while creating the journey. " ,
                "error":str(e)
            }
        ), 500

    try:
        for skill in skills:
            for course_id in skill["course_ids"]:
                journey_skill_course_input ={
                    "journey_id":journey_id,
                    "course_id":course_id,
                    "skill_id":skill["skill_id"]
                }
                journey_skill_course = Journey_Skill_Course(**journey_skill_course_input)
                db.session.add(journey_skill_course)
                db.session.commit()
        
    except Exception as e:
        return jsonify(
            {
                "code": 500,
                "message": "An error occurred while creating the journey skill course pair(s). " ,
                "error":str(e)
            }
        ), 500

    return jsonify(
        {
            "code": 201,
            "message": "Jounrey and journey skill course pair(s) created successfully.",
            "data": {
                "journey_id":journey_id,
                "journey": journey_data
            }
        }
    ), 201

#create journey skill course
@app.route("/journey_skill_course/create", methods=['POST'])
def create_journey_skill_course():
    data = request.get_json()
    journey_skill_course = Journey_Skill_Course(**data)

    try:
        db.session.add(journey_skill_course)
        db.session.commit()
    except Exception as e:
        return jsonify(
            {
                "code": 500,
                "message": "An error occurred while creating the journey skill course pair. " ,
                "error":str(e)
            }
        ), 500
    
    print(json.dumps(journey_skill_course.to_dict(), default=str)) # convert a JSON object to a string and print
    print()

    return jsonify(
        {
            "code": 201,
            "message": "Journey skill course pair created successfully.",
            "data": journey_skill_course.to_dict()
        }
    ), 201

#update journey info
@app.route("/update_journey_info", methods=['POST'])
def update_journey_info():
    data = request.get_json()

    if not all(key in data.keys() for 
               key in ("journey_id","journey_name","skills")):
        return jsonify({
            "message": "Invalid JSON input. Journey id, name, and corresponded skills should be provided in the JSON object."
        }), 500

    if data["journey_name"].isspace() or data["journey_name"] == None or len(data["journey_name"])==0:
        return jsonify(
            {   
                "code": 500,
                "message": "Journey name should not be empty or just contain white spaces."
            }
        ), 500
    
    if data["skills"] == [
                {
                    "skill_id": "",
                    "course_ids": [""]
                }
            ]:
        return jsonify(
            {   
                "code": 500,
                "message": "A Journey should at least have one skill."
            }
        ), 500 
    
    if len(data["skills"])==1 and data["skills"][0]["course_ids"]==[""]:
        return jsonify(
            {   
                "code": 500,
                "message": "A Journey should at least have one course."
            }
        ), 500 

    for skill in data["skills"]:
        if not all(key in skill.keys() for 
               key in ("skill_id","course_ids")):
            return jsonify({
                "message": "Invalid JSON input. Skill id and corresponding courses ids should be provided in the JSON object."
            }), 500
        
        if skill["skill_id"] == None:
            return jsonify(
            {   
                "code": 500,
                "message": "A Skill must be chosen for each skill courses pair."
            }
        ), 500

        if skill["course_ids"] == None or skill["course_ids"] == [] or skill["course_ids"] == [""]:
            return jsonify(
            {   
                "code": 500,
                "message": "At least a course must be chosen for each skill courses pair."
            }
        ), 500 

    journey_id=data["journey_id"]
    skills=data["skills"]

    try:
        journey = Journey.query.filter_by(journey_id=journey_id).first()
        journey.journey_name = data["journey_name"]
        db.session.commit()
    except Exception as e:
        return jsonify(
            {
                "code":500,
                "message": "An error occurred while updating journey name with journey id = "+str(journey_id)+". " ,
                "error":str(e)
            }
        )
    
    try:
        Journey_Skill_Course.query.filter_by(journey_id = journey_id).delete()    
        db.session.commit()
    except Exception as e:
        return jsonify(
            {
                "code":500,
                "message": "An error occurred while deleting the journey skill course pairs with journey id = "+journey_id+". " ,
                "error":str(e)
            }
        )
    
    try:
        for skill in skills:
            for course_id in skill["course_ids"]:
                journey_skill_course_input ={
                    "journey_id":journey_id,
                    "course_id":course_id,
                    "skill_id":skill["skill_id"]
                }
                journey_skill_course = Journey_Skill_Course(**journey_skill_course_input)
                db.session.add(journey_skill_course)
                db.session.commit()
    except Exception as e:
        return jsonify(
            {
                "code": 500,
                "message": "An error occurred while creating the jounrey skill course pairs. " ,
                "error":str(e)
            }
        ), 500

    return jsonify(
        {
            "code": 201,
            "message": "Journey info updated successfully.",
            "data": data
        }
    ), 201

#get roles by status
@app.route("/roles/<string:status>")
def get_roles_by_status(status):
    rlist = Role.query.filter_by(role_status=status)
    if rlist.count():
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
            "message": "There are no roles with status = "+status+"."
        }
    ), 404

#create role
@app.route("/role/create", methods=['POST'])
def create_role():
    data = request.get_json()

    if not all(key in data.keys() for 
               key in ("role_name","role_status")):
        return jsonify({
            "message": "Invalid JSON input. Role name and status should be provided in the JSON object."
        }), 500
    
    if data["role_name"].isspace() or data["role_name"] == None or len(data["role_name"])==0:
        return jsonify(
            {   
                "code": 500,
                "message": "Role name should not be empty or just contain white spaces."
            }
        ), 500 

    if data["role_status"] not in ["Active","Retired"]:
        return jsonify(
            {   
                "code": 500,
                "message": "Role status should be either 'Active' or 'Retired'."
            }
        ), 500

    exsiting = Role.query.filter_by(role_name=data["role_name"]).first()
    if exsiting:
        return jsonify(
            {   
                "code": 500,
                "message": "Role with name = " + data["role_name"] + " already exists!"
            }
        ), 500

    role = Role(role_id=None,**data)

    try:
        db.session.add(role)
        db.session.commit()
    except Exception as e:
        return jsonify(
            {
                "code": 500,
                "message": "An error occurred while creating the role. " ,
                "error":str(e)
            }
        ), 500
    
    print(json.dumps(role.to_dict(), default=str)) # convert a JSON object to a string and print
    print()

    return jsonify(
        {
            "code": 201,
            "message": "Role created successfully.",
            "data": role.to_dict()
        }
    ), 201

#get roles with skills by role status
@app.route("/roles_with_skills/<string:role_status>")
def get_roles_with_skills_by_role_status(role_status):
    ans=[]
    rlist = Role.query.filter_by(role_status=role_status)
    if rlist.count():
        for role in rlist:
            tempdic = {
                "role_id": role.role_id,
                "role_name": role.role_name,
                "role_status": role.role_status,
                "role_skills":[]
            }

            list = db.session.query(Role_Skill, Skill).select_from(Role_Skill).join(Skill).filter(Role_Skill.role_id==role.role_id)
            for role_skill,skill in list:
                tempdic["role_skills"].append(skill.to_dict())  
            ans.append(tempdic)
        
        return jsonify(
            {
                "code": 200,
                "data": {
                    "roles": ans,
                }
            }
        ), 200
    return jsonify(
        {
            "code": 404,
            "message": "There are no roles with status = "+role_status+"." 
        }
    ), 404

#get active skills by role id
@app.route("/active_skills_by_role/<int:role_id>")
def get_active_skills_by_role_id(role_id):
    list = db.session.query(Role_Skill, Skill).select_from(Role_Skill).join(Skill).filter(Role_Skill.role_id==role_id,Skill.skill_status=="Active")
    if list.count():
        return jsonify(
            {
                "code": 200,
                "data": {
                    "active_skills": [skill.to_dict() for role_skill,skill in list]
                }
            }
        ), 200
    return jsonify(
        {
            "code": 404,
            "message": "There are no active skills for role id = "+str(role_id)+"."
        }
    ), 404

#Get active skills whether in role by role id
@app.route("/active_skills_whether_in_role/<int:role_id>")
def get_active_skills_whether_in_role_by_role_id(role_id):
    role = Role.query.filter_by(role_id=role_id).first()
    rslist = Role_Skill.query.filter_by(role_id = role_id)
    slist = Skill.query.filter_by(skill_status="Active")
    in_role_skills = []
    ans = []

    if rslist.count() != 0:
        for rs in rslist:
            in_role_skills.append(rs.skill_id)
    for s in slist:
        if s.skill_id in in_role_skills:
            tempdic = {
                "skill_id": s.skill_id,
                "skill_name": s.skill_name,
                "skill_status": s.skill_status,
                "skill_in_role": True
            }
        else:
            tempdic = {
                "skill_id": s.skill_id,
                "skill_name": s.skill_name,
                "skill_status": s.skill_status,
                "skill_in_role": False
            }
        ans.append(tempdic)
    
    return jsonify(
        {
            "code": 200,
            "data": {
                "role": role.to_dict(),
                "skills": ans
            }
        }
    ), 200

#update role info
@app.route("/role_info/update", methods=['POST'])
def update_role_info():
    data = request.get_json()

    if not all(key in data.keys() for 
               key in ("role_id","role_name","role_status","skill_ids")):
        return jsonify({
            "message": "Invalid JSON input. Role id, name, status and corresponded skill ids should be provided in the JSON object."
        }), 500

    if data["role_name"].isspace() or data["role_name"] == None or len(data["role_name"])==0:
        return jsonify(
            {   
                "code": 500,
                "message": "Role name should not be empty or just contain white spaces."
            }
        ), 500 
    
    if data["role_status"] not in ["Active","Retired"]:
        return jsonify(
            {   
                "code": 500,
                "message": "Role status should be either 'Active' or 'Retired'."
            }
        ), 500 
    
    role_id=data["role_id"]
    role_name=data["role_name"]
    role_status=data["role_status"]
    skill_ids=data["skill_ids"]

    existings = Role.query.filter_by(role_name=role_name)
    if existings:
        for existing in existings:
            if existing.to_dict()["role_id"]!=role_id:
                return jsonify(
                    {   
                        "code": 500,
                        "message": "Cannot have duplicated Roles."
                    }
                ), 500

    try:
        role = Role.query.filter_by(role_id=role_id).first()
        role.role_name = role_name
        role.role_status = role_status
        db.session.commit()
    except Exception as e:
        return jsonify(
            {
                "code":500,
                "message": "An error occurred while updating role info with role_id = "+str(role_id)+". " ,
                "error":str(e)
            }
        )

    try:
        Role_Skill.query.filter_by(role_id = role_id).delete()
        db.session.commit()
    except Exception as e:
        return jsonify(
            {
                "code":500,
                "message": "An error occurred while deleting role skill pair(s) with role_id = "+str(role_id)+". " ,
                "error":str(e)
            }
        )
    
    try:
        for skill_id in skill_ids:
            cs = {
                "role_id":role_id,
                "skill_id":skill_id
            }
            role_skill = Role_Skill(**cs)
            db.session.add(role_skill)
            db.session.commit()
    except Exception as e:
        return jsonify(
            {
                "code": 500,
                "message": "An error occurred while creating the role skill pairs. " ,
                "error":str(e)
            }
        ), 500

    return jsonify(
        {
            "code": 201,
            "message": "Role info updated successfully.",
            "data": data
        }
    ), 201

#get skill by id
@app.route("/skill/<int:id>")
def get_skill_by_id(id):
    skill = Skill.query.filter_by(skill_id=id).first()
    if skill:
        return jsonify(
            {
                "code": 200,
                "data": skill.to_dict()
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "Skill which id = " + str(id) + " not found."
        }
    ), 404

#create skill
@app.route("/skill/create", methods=['POST'])
def create_skill():
    data = request.get_json()

    if not all(key in data.keys() for 
               key in ("skill_name","skill_status")):
        return jsonify({
            "message": "Invalid JSON input. Skill name and status should be provided in the JSON object."
        }), 500
    
    if data["skill_name"].isspace() or data["skill_name"] == None or len(data["skill_name"])==0:
        return jsonify(
            {   
                "code": 500,
                "message": "Skill name should not be empty or just contain white spaces."
            }
        ), 500 
    
    if data["skill_status"] not in ["Active","Retired"]:
        return jsonify(
            {   
                "code": 500,
                "message": "Skill status should be either 'Active' or 'Retired'."
            }
        ), 500 
    
    exsiting = Skill.query.filter_by(skill_name=data["skill_name"]).first()
    if exsiting:
        return jsonify(
            {   
                "code": 500,
                "message": "Skill with name = " + data["skill_name"] + " already exist!"
            }
        ), 500 

    skill = Skill(skill_id = None,**data)

    try:
        db.session.add(skill)
        db.session.commit()
    except Exception as e:
        return jsonify(
            {
                "code": 500,
                "message": "An error occurred while creating the skill. " ,
                "error":str(e)
            }
        ), 500
    
    print(json.dumps(skill.to_dict(), default=str)) # convert a JSON object to a string and print
    print()

    return jsonify(
        {
            "code": 201,
            "message": "Skill created successfully.",
            "data": skill.to_dict()
        }
    ), 201

#Update skill info by id
@app.route("/update_skill_info/<int:skill_id>", methods=['PUT'])
def update_skill_info(skill_id):

    skill = Skill.query.filter_by(skill_id=skill_id).first()
    if not skill:
        return jsonify(
            {
                "code": 404,
                "message": "Skill with id = " + str(skill_id) + " not found."
            }
        ), 404

    try:
        data = request.get_json()
        skill.skill_status = data['skill_status']
        skill.skill_name = data['skill_name']

        existings = Skill.query.filter_by(skill_name=data['skill_name'],skill_status=data['skill_status'])
        if existings:
            for existing in existings:
                if existing.to_dict()["skill_id"]!=skill_id:
                    return jsonify(
                        {   
                            "code": 500,
                            "message": "Cannot have duplicated skills."
                        }
                    ), 500

        db.session.commit()
        return jsonify(
            {
                "code": 200,
                "data": skill.to_dict(),
                "message": "Skill info for skill id = " + str(skill_id) + " updated successfully."
            }
        ), 200
    except Exception as e:
        return jsonify(
            {
                "code": 500,
                "message": "An error occurred while updating skill info which id = " + str(skill_id) + ". " ,
                "error":str(e)
            }
        ), 500

######################################################################################################
#NOT USED ROUTES
######################################################################################################

#get all courses
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

#get course by id
@app.route("/course/<string:id>")
def get_course_by_id(id):
    course = Course.query.filter_by(course_id=id).first()
    if course:
        return jsonify(
            {
                "code": 200,
                "data": course.to_dict()
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "Course which id = " + str(id) + " not found."
        }
    ), 404

#get courses by status
@app.route("/courses/<string:status>")
def get_courses_by_status(status):
    clist = Course.query.filter_by(course_status=status)
    if clist.count():
        return jsonify(
            {
                "code": 200,
                "data": {
                    "courses": [course.to_dict() for course in clist]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "Courses which status = " + status + " not found."
        }
    ), 404

#get all course registrations
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

#get course registration(S) by staff id and course id
@app.route("/course_registration/<int:staff_id>/<string:course_id>")
def get_course_registration_by_staff_id_and_course_id(staff_id,course_id):
    crlist = Course_Registration.query.filter_by(staff_id=staff_id,course_id=course_id)
    if crlist.count():
        return jsonify(
            {
                "code": 200,
                "data": {
                    "course_registration(S)": [course_registration.to_dict() for course_registration in crlist]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "Course registration with staff_id = " + str(staff_id) + " and course_id = " + str(course_id) + " not found."
        }
    ), 404

#get all course skills
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

#remove course skill
@app.route("/remove_course_skill/<string:course_id>/<int:skill_id>")
def remove_course_skill(course_id,skill_id):
    try:
        cs = Course_Skill.query.filter_by(course_id = course_id, skill_id=skill_id).delete()
        if not cs:
            return jsonify(
                {
                    "code": 404,
                    "message": "Course skill pair with course_id = "+str(course_id)+" and skill_id = " + str(skill_id) + " not found."
                }
            ), 404

        db.session.commit()
    except Exception as e:
        return jsonify(
            {
                "code":500,
                "message": "An error occurred while deleting the course skill pair. " ,
                "error":str(e)
            }
        )
    return jsonify(
        {
            "code": 202,
            "message": "Course skill pair deleted successfully."
        }
    ), 202

#create course skill
@app.route("/course_skill/create", methods=['POST'])
def create_course_skill():
    data = request.get_json()
    course_skill = Course_Skill(**data)

    try:
        db.session.add(course_skill)
        db.session.commit()
    except Exception as e:
        return jsonify(
            {
                "code": 500,
                "message": "An error occurred while creating the course skill pair. " ,
                "error":str(e)
            }
        ), 500
    
    print(json.dumps(course_skill.to_dict(), default=str)) # convert a JSON object to a string and print
    print()

    return jsonify(
        {
            "code": 201,
            "message": "Course skill pair created successfully.",
            "data": course_skill.to_dict()
        }
    ), 201

#get all journeys
@app.route("/journeys")
def get_all_journeys():
    jlist = Journey.query.all()
    if jlist:
        return jsonify(
            {
                "code": 200,
                "data": {
                    "journeys": [journey.to_dict() for journey in jlist]
                }
            }
        ), 200
    return jsonify(
        {
            "code": 404,
            "message": "There are no journeys."
        }
    ), 404

#get journey by id
@app.route("/journey/<int:id>")
def get_journey_by_id(id):
    journey = Journey.query.filter_by(journey_id=id).first()
    if journey:
        return jsonify(
            {
                "code": 200,
                "data": journey.to_dict()
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "Journey which id = " + str(id) + " not found."
        }
    ), 404

#get journeys by staff id
@app.route("/journeys_by_staff/<int:staff_id>")
def get_journeys_by_staff_id(staff_id):
    jlist = Journey.query.filter_by(staff_id=staff_id)
    if jlist.count():
        return jsonify(
            {
                "code": 200,
                "data": {
                    "journeys": [journey.to_dict() for journey in jlist]
                }
            }
        ), 200
    return jsonify(
        {
            "code": 404,
            "message": "There are no journeys for staff id = "+str(staff_id)+"."
        }
    ), 404

#get all journey skill course
@app.route("/journey_skill_course")
def get_all_journey_skill_course():
    jsclist = Journey_Skill_Course.query.all()
    if jsclist:
        return jsonify(
            {
                "code": 200,
                "data": {
                    "journey_skill_course": [journey_skill_course.to_dict() for journey_skill_course in jsclist]
                }
            }
        ), 200
    return jsonify(
        {
            "code": 404,
            "message": "There is no journey skill course."
        }
    ), 404

#get skills not inside journey by journey id
@app.route("/skills_not_in_journey/<int:journey_id>")
def get_skills_not_in_journey(journey_id):
    jsclist = Journey_Skill_Course.query.filter_by(journey_id=journey_id)    
    if jsclist.count():
        skills =[]
        for jsc in jsclist:
            skills.append(jsc.skill_id)
        #print(skills)
        slist = Skill.query.filter(Skill.skill_id.not_in(skills))
        return jsonify(
            {
                "code": 200,
                "data": {
                    "skills not in journey": [skill.to_dict() for skill in slist]
                }
            }
        ), 200
    return jsonify(
        {
            "code": 404,
            "message": "There are no journey skill course with journey id = "+str(journey_id)+"."
        }
    ), 404

#get all roles
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

#get role by id
@app.route("/role/<int:id>")
def get_role_by_id(id):
    role = Role.query.filter_by(role_id=id).first()
    if role:
        return jsonify(
            {
                "code": 200,
                "data": role.to_dict()
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "Role which id = " + str(id) + " not found."
        }
    ), 404


#update role status by role id
@app.route("/update_role_status/<int:role_id>", methods=['PUT'])
def update_role_status(role_id):
    try:
        role = Role.query.filter_by(role_id=role_id).first()
        if not role:
            return jsonify(
                {
                    "code": 404,
                    "message": "Role with id = " + str(role_id) + " not found."
                }
            ), 404

        # update role status
        data = request.get_json()
        if data['role_status']:
            role.role_status = data['role_status']
            db.session.commit()
            return jsonify(
                {
                    "code": 200,
                    "data": role.to_dict(),
                    "message": "Status for role id = " + str(role_id) + " updated successfully."
                }
            ), 200
    except Exception as e:
        return jsonify(
            {
                "code": 500,
                "message": "An error occurred while updating role status which id = " + str(role_id) + ". " ,
                "error":str(e)
            }
        ), 500

#get all role skills
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

#get all roles with skills
@app.route("/roles_with_skills")
def get_all_roles_with_skills():
    ans=[]
    rlist = Role.query.all()
    if rlist:
        for role in rlist:
            tempdic = {
                "role_id": role.role_id,
                "role_name": role.role_name,
                "role_status": role.role_status,
                "role_skills":[]
            }

            list = db.session.query(Role_Skill, Skill).select_from(Role_Skill).join(Skill).filter(Role_Skill.role_id==role.role_id)
            for role_skill,skill in list:
                tempdic["role_skills"].append(skill.to_dict())  
            ans.append(tempdic)
        
        return jsonify(
            {
                "code": 200,
                "data": {
                    "roles": ans,
                }
            }
        ), 200
    return jsonify(
        {
            "code": 404,
            "message": "There are no roles." 
        }
    ), 404

#remove role skill
@app.route("/remove_role_skill/<int:role_id>/<int:skill_id>")
def remove_role_skill(role_id,skill_id):
    try:
        rs = Role_Skill.query.filter_by(role_id = role_id, skill_id=skill_id).delete()
        if not rs:
            return jsonify(
                {
                    "code": 404,
                    "message": "Role skill pair with role_id = " + str(role_id) + " and skll_id = " + str(skill_id) + " not found."
                }
            ), 404        
        db.session.commit()
    except Exception as e:
        return jsonify(
            {
                "code":500,
                "message": "An error occurred while deleting the role skill pair. " ,
                "error":str(e)
            }
        )
    return jsonify(
        {
            "code": 202,
            "message": "Role skill pair deleted successfully."
        }
    ), 202

#create role skill
@app.route("/role_skill/create", methods=['POST'])
def create_role_skill():
    data = request.get_json()
    role_skill = Role_Skill(**data)

    try:
        db.session.add(role_skill)
        db.session.commit()
    except Exception as e:
        return jsonify(
            {
                "code": 500,
                "message": "An error occurred while creating the role skill pair. " ,
                "error":str(e)
            }
        ), 500
    
    print(json.dumps(role_skill.to_dict(), default=str)) # convert a JSON object to a string and print
    print()

    return jsonify(
        {
            "code": 201,
            "message": "Role skill pair created successfully.",
            "data": role_skill.to_dict()
        }
    ), 201

#update role skill
@app.route("/role_skill/update", methods=['POST'])
def update_role_skill():
    data = request.get_json()
    role_id=data["role_id"]
    skill_ids=data["skill_ids"]
    try:
        Role_Skill.query.filter_by(role_id = role_id).delete()
        db.session.commit()
    except Exception as e:
        return jsonify(
            {
                "code":500,
                "message": "An error occurred while deleting role skill pair(s) with role_id = "+role_id+". " ,
                "error":str(e)
            }
        )
    try:
        for skill_id in skill_ids:
            cs = {
                "role_id":role_id,
                "skill_id":skill_id
            }
            role_skill = Role_Skill(**cs)
            db.session.add(role_skill)
            db.session.commit()
    except Exception as e:
        return jsonify(
            {
                "code": 500,
                "message": "An error occurred while creating the role skill pairs. " ,
                "error":str(e)
            }
        ), 500

    return jsonify(
        {
            "code": 201,
            "message": "Role skill pair(s) updated successfully.",
            "data": data
        }
    ), 201

#get all skills
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

#get skills by status
@app.route("/skills/<string:status>")
def get_skills_by_status(status):
    slist = Skill.query.filter_by(skill_status=status)
    if slist.count():
        return jsonify(
            {
                "code": 200,
                "data": {
                    "skills": [skill.to_dict() for skill in slist]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "Skills with status = " + status + " not found."
        }
    ), 404

#get all staffs
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

#############################################################################
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