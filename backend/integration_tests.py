import unittest
import flask_testing
import json
from app import app, db, Course, Course_Registration,Course_Skill,Journey,Journey_Skill_Course,Role,Role_Skill,Skill,Staff


class TestApp(flask_testing.TestCase):
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite://"
    app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {}
    app.config['TESTING'] = True

    def create_app(self):
        return app

    def setUp(self):
        db.create_all()
        db.session.begin_nested()

    def tearDown(self):
        db.session.rollback()
        #db.session.remove()
        #db.drop_all()


#########################
#LJT-29 (Create skills)
#########################
class TestCreateSkills(TestApp):
    def test_create_active_skill(self):
        request_body = {
            "skill_name":"R Programming",
            "skill_status":"Active"
        }

        response = self.client.post("/skill/create",
                            data=json.dumps(request_body),
                            content_type='application/json')

        self.assertEqual(response.json, {
            "code": 201,
            "data": {
                "skill_id": response.json["data"]["skill_id"],
                "skill_name": "R Programming",
                "skill_status": "Active"
            },
            "message": "Skill created successfully."
        })

    def test_create_retired_skill(self):
        request_body = {
            "skill_name":"PHP Programming",
            "skill_status":"Retired"
        }

        response = self.client.post("/skill/create",
                            data=json.dumps(request_body),
                            content_type='application/json')

        self.assertEqual(response.json, {
            "code": 201,
            "data": {
                "skill_id": response.json["data"]["skill_id"],
                "skill_name": "PHP Programming",
                "skill_status": "Retired"
            },
            "message": "Skill created successfully."
        })
    
    def test_create_exisiting_skill(self):
        request_body = {
            "skill_name": "Big Data",
            "skill_status": "Active"
        }

        try: 
            self.client.post("/skill/create",
                            data=json.dumps(request_body),
                            content_type='application/json')

        except Exception as e:
            self.assertEqual(str(e),
                             "Skill with name = Big Data alreasy exsit!")

    def test_create_skill_without_skill_name(self):
        request_body = {
            "skill_name":"",
            "skill_status":"Active"
        }

        try:
            self.client.post("/skill/create",
                            data=json.dumps(request_body),
                            content_type='application/json')
        except Exception as e:
            self.assertEqual(str(e),
                             'Skill name should not be empty or just contain white spaces.')

    def test_create_skill_without_skill_status(self):
        request_body = {
            "skill_name":"Visual Design",
            "skill_status":""
        }
        try:
            self.client.post("/skill/create",
                                data=json.dumps(request_body),
                                content_type='application/json')
        except Exception as e:
            self.assertEqual(str(e),
                             "Skill status should be either 'Active' or 'Retired'.")

#########################
#LJT-44 (Update course skill)
#########################
class TestUpdateCourseSkill(TestApp):
    def test_update_course_skill_by_adding_a_new_skill(self):
        request_body = {
            "course_id":"COR001",
            "skill_ids":[10,11,15]
        }

        response = self.client.post("/course_skill/update",
                            data=json.dumps(request_body),
                            content_type='application/json')

        self.assertEqual(response.json, {
            "code": 201,
            "data": {
                "course_id": "COR001",
                "skill_ids": [10,11,15]
            },
            "message": "Course skill pair(s) updated successfully."
        })
    
    def test_update_course_skill_by_adding_multiple_new_skills(self):
        request_body = {
            "course_id":"HRD001",
            "skill_ids":[7,8]
        }

        response = self.client.post("/course_skill/update",
                            data=json.dumps(request_body),
                            content_type='application/json')

        self.assertEqual(response.json, {
            "code": 201,
            "data": {
                "course_id": "HRD001",
                "skill_ids": [7,8]
            },
            "message": "Course skill pair(s) updated successfully."
        })

    def test_update_course_skill_by_removing_an_exisitng_skill(self):
        request_body = {
            "course_id":"COR001",
            "skill_ids":[11]
        }

        response = self.client.post("/course_skill/update",
                            data=json.dumps(request_body),
                            content_type='application/json')

        self.assertEqual(response.json, {
            "code": 201,
            "data": {
                "course_id": "COR001",
                "skill_ids": [11]
            },
            "message": "Course skill pair(s) updated successfully."
        })

#########################
#LJT-32 (Create Roles)
#########################
class TestCreateRoles(TestApp):
    def test_create_active_role(self):
        request_body = {
            "role_name": "Management Consultant",
            "role_status": "Active"
        }

        response = self.client.post("/role/create",
                            data=json.dumps(request_body),
                            content_type='application/json')

        self.assertEqual(response.json, {
            "code": 201,
            "data": {
                "role_id": response.json["data"]["role_id"],
                "role_name": "Management Consultant",
                "role_status": "Active"
            },
            "message": "Role created successfully."
        })

    def test_create_retired_role(self):
        request_body = {
            "role_name":"Strategy Consultant",
            "role_status":"Retired"
        }

        response = self.client.post("/role/create",
                            data=json.dumps(request_body),
                            content_type='application/json')

        self.assertEqual(response.json, {
            "code": 201,
            "data": {
                "role_id": response.json["data"]["role_id"],
                "role_name": "Strategy Consultant",
                "role_status": "Retired"
            },
            "message": "Role created successfully."
        })
    
    def test_create_exisiting_role(self):
        request_body = {
            "role_name":"Data Consultance",
            "role_status":"Active"
        }

        try: 
            self.client.post("/role/create",
                            data=json.dumps(request_body),
                            content_type='application/json')

        except Exception as e:
            self.assertEqual(str(e),
                             "Role with name = Data Consultance alreasy exsit!")

    def test_create_role_without_role_name(self):
        request_body = {
            "role_name": "",
            "role_status": "Active"
        }

        try:
            self.client.post("/role/create",
                            data=json.dumps(request_body),
                            content_type='application/json')
        except Exception as e:
            self.assertEqual(str(e),
                             'Role name should not be empty or just contain white spaces.')

    def test_create_role_without_role_status(self):
        request_body = {
            "role_name": "Software Engineer",
            "role_status": ""
        }
        try:
            self.client.post("/role/create",
                                data=json.dumps(request_body),
                                content_type='application/json')
        except Exception as e:
            self.assertEqual(str(e),
                             "Role status should be either 'Active' or 'Retired'.")

#########################
#LJT-12 (Update Roles)
#########################
class TestUpdateRoles(TestApp):
    def test_update_role_by_removing_skills(self):
        request_body = {
            "role_id": 1,
            "role_name": "Data Analyst",
            "role_status": "Active",
            "skill_ids": []
        }

        response = self.client.post("/role_info/update",
                            data=json.dumps(request_body),
                            content_type='application/json')

        self.assertEqual(response.json, {
            "code": 201,
            "data": {
                "role_id": request_body["role_id"],
                "role_name": "Data Analyst",
                "role_status": "Active",
                "skill_ids": []
            },
            "message": "Role info updated successfully."
        })

    def test_update_role_by_removing_and_adding_skills(self):
        request_body = {
            "role_id": 1,
            "role_name": "Data Analyst",
            "role_status": "Active",
            "skill_ids": [4,10]
        }

        response = self.client.post("/role_info/update",
                            data=json.dumps(request_body),
                            content_type='application/json')

        self.assertEqual(response.json, {
            "code": 201,
            "data": {
                "role_id": request_body["role_id"],
                "role_name": "Data Analyst",
                "role_status": "Active",
                "skill_ids": [4,10]
            },
            "message": "Role info updated successfully."
        })
    
    def test_update_role_by_changing_role_status(self):
        request_body = {
            "role_id": 1,
            "role_name": "Data Analyst",
            "role_status": "Retired",
            "skill_ids": [10,11,12]
        }

        response = self.client.post("/role_info/update",
                            data=json.dumps(request_body),
                            content_type='application/json')

        self.assertEqual(response.json, {
            "code": 201,
            "data": {
                "role_id": request_body["role_id"],
                "role_name": "Data Analyst",
                "role_status": "Retired",
                "skill_ids": [10,11,12]
            },
            "message": "Role info updated successfully."
        })
    
    # change role name
    # update by add skills
    # updating role to exsiting role -> cannot do this

#########################
#LJT-1 (Update Skills)
#########################
class TestUpdateSkills(TestApp):
    def test_update_skill_by_changing_skill_status(self):
        request_body = {
            "skill_name":"Communication",
            "skill_status":"Retired"
        }

        response = self.client.put("/update_skill_info/7",
                            data=json.dumps(request_body),
                            content_type='application/json')

        self.assertEqual(response.json, {
            "code": 200,
            "data": {
                "skill_id": 7,
                "skill_name": "Communication",
                "skill_status": "Retired"
            },
            "message": "Skill info for skill id = 7 updated successfully."
        })

    # change skill name
    # change to existing skills, should not do this

#########################
#LJT16 (Select Skills When Creating LJ)
#########################
class TestSelectSkillsWhenCreatingLJ(TestApp):
    def test_add_a_skill_when_creating_LJ(self):
        request_body = {
            "journey_name": "add a skill when creating LJ",
            "staff_id": 140008,
            "role_id": 8,
            "skills": [
                {
                    "skill_id": 1,
                    "course_ids": [
                        "MGT001"
                    ]
                }
            ]
        }

        response = self.client.post("/journey/create",
                            data=json.dumps(request_body),
                            content_type='application/json')
        print(response.json)
        self.assertEqual(response.json, {
            "code": 201,
            "data": {
                "journey": {
                    "journey_name": "add a skill when creating LJ",
                    "role_id": 8,
                    "skills": [
                        {
                            "course_ids": [
                                "MGT001"
                            ],
                            "skill_id": 1
                        }
                    ],
                    "staff_id": 140008
                },
                "journey_id": response.json["data"]["journey_id"]
            },
            "message": "Jounrey and journey skill course pair(s) created successfully."
        })

    def test_create_journey_without_a_skill(self):
        request_body = {
            "journey_name": "add no skill when creating LJ",
            "staff_id": "150008",
            "role_id": 8,
            "skills": [
                {
                    "skill_id": "",
                    "course_ids": [""]
                }
            ]
        }

        try:
            self.client.post("/journey/create",
                            data=json.dumps(request_body),
                            content_type='application/json')
        except Exception as e:
            self.assertEqual(str(e),
                             'A Journey should at least have one skill.')

#########################
#LJT4 (Select Courses When Creating LJ)
#########################
class TestSelectCoursesWhenCreatingLJ(TestApp):
    def test_add_course_for_one_skill_when_creating_LJ(self):
        request_body = {
            "journey_name": "add courses for one skill",
            "staff_id": 140008,
            "role_id": 8,
            "skills": [
                {
                    "skill_id": 1,
                    "course_ids": [
                        "MGT001",
                        "MGT003"
                    ]
                }
            ]
        }

        response = self.client.post("/journey/create",
                            data=json.dumps(request_body),
                            content_type='application/json')
        print(response.json)
        self.assertEqual(response.json, {
            "code": 201,
            "data": {
                "journey": {
                    "journey_name": "add courses for one skill",
                    "role_id": 8,
                    "skills": [
                        {
                            "course_ids": [
                                "MGT001",
                                "MGT003"
                            ],
                            "skill_id": 1
                        }
                    ],
                    "staff_id": 140008
                },
                "journey_id": response.json["data"]["journey_id"]
            },
            "message": "Jounrey and journey skill course pair(s) created successfully."
        })

    def test_add_courses_for_two_skill_when_creating_LJ(self):
        request_body = {
        "journey_name": "add courses for two skills",
        "staff_id": 140008,
        "role_id": 8,
        "skills": [
            {
                "skill_id": 1,
                "course_ids": [
                    "MGT001",
                    "MGT003"
                ]
            },
            {
                "skill_id": 8,
                "course_ids": [
                    "MGT004"
                ]
            }
        ]
    }

        response = self.client.post("/journey/create",
                            data=json.dumps(request_body),
                            content_type='application/json')

        self.assertEqual(response.json, {
            "code": 201,
            "data": {
                "journey": {
                    "journey_name": "add courses for two skills",
                    "role_id": 8,
                    "skills": [
                        {
                            "course_ids": [
                                "MGT001",
                                "MGT003"
                            ],
                            "skill_id": 1
                        },
                        {
                            "course_ids": [
                                "MGT004"
                            ],
                            "skill_id": 8
                        }
                    ],
                    "staff_id": 140008
                },
                "journey_id": response.json["data"]["journey_id"]
            },
            "message": "Jounrey and journey skill course pair(s) created successfully."
        })
        
    def test_create_journey_without_a_course(self):
        request_body = {
            "journey_name": "add no course when creating LJ",
            "staff_id": "150008",
            "role_id": 8,
            "skills": [
                {
                "skill_id": 8,
                "course_ids": [
                    ""
                ]
                }
            ]
        }

        try:
            self.client.post("/journey/create",
                            data=json.dumps(request_body),
                            content_type='application/json')
        except Exception as e:
            self.assertEqual(str(e),
                             'A Journey should at least have one course.')

#########################
#LJT15 (Select A Role When Creating LJ)
#########################
class TestSelectARoleWhenCreatingLJ(TestApp):
    def test_create_journey_without_a_role(self):
        request_body = {
            "journey": {
                "journey_name": "LearnThis",
                "staff_id": "150008",
                "role_id": "",
                "skills": []
            }
        }

        try:
            self.client.post("/journey/create",
                            data=json.dumps(request_body),
                            content_type='application/json')
        except Exception as e:
            self.assertEqual(str(e),
                             'A Journey should at least have one role.')

# class TestCreateConsultation(TestApp):
#     def test_create_consultation(self):
#         d1 = Doctor(name='Imran', title='Dr',
#                     reg_num='UKM123', hourly_rate=30)
#         p1 = Patient(name='Phris Coskitt', title='HRH',
#                      contact_num='+65 8888 8888', ewallet_balance=15)
#         db.session.add(d1)
#         db.session.add(p1)
#         db.session.commit()

#         request_body = {
#             'doctor_id': d1.id,
#             'patient_id': p1.id,
#             'diagnosis': 'Itchy armpits',
#             'prescription': 'Better deodrant',
#             'length': 15
#         }

#         response = self.client.post("/consultations",
#                                     data=json.dumps(request_body),
#                                     content_type='application/json')
#         self.assertEqual(response.json, {
#             'id': 1,
#             'doctor_id': 1,
#             'patient_id': 2,
#             'diagnosis': 'Itchy armpits',
#             'prescription': 'Better deodrant',
#             'charge': 7.5
#         })

#     def test_create_consultation_invalid_doctor(self):
#         p1 = Patient(name='Hyacinth Bucket', title='Mrs',
#                      contact_num='+65 8888 8888', ewallet_balance=15)
#         db.session.add(p1)
#         db.session.commit()

#         request_body = {
#             'doctor_id': p1.id,
#             'patient_id': p1.id,
#             'diagnosis': 'Itchy armpits',
#             'prescription': 'Better deodrant',
#             'length': 15
#         }

#         response = self.client.post("/consultations",
#                                     data=json.dumps(request_body),
#                                     content_type='application/json')
#         self.assertEqual(response.status_code, 500)
#         self.assertEqual(response.json, {
#             'message': 'Doctor not valid.'
#         })

#     def test_create_consultation_invalid_patient(self):
#         d1 = Doctor(name='Imran', title='Dr',
#                     reg_num='UKM123', hourly_rate=30)
#         db.session.add(d1)
#         db.session.commit()

#         request_body = {
#             'doctor_id': d1.id,
#             'patient_id': d1.id,
#             'diagnosis': 'Itchy armpits',
#             'prescription': 'Better deodrant',
#             'length': 15
#         }

#         response = self.client.post("/consultations",
#                                     data=json.dumps(request_body),
#                                     content_type='application/json')
#         self.assertEqual(response.status_code, 500)
#         self.assertEqual(response.json, {
#             'message': 'Patient not valid.'
#         })

#     def test_create_consultation_insufficient_balance(self):
#         d1 = Doctor(name='Imran', title='Dr',
#                     reg_num='UKM123', hourly_rate=30)
#         p1 = Patient(name='Hyacinth Bucket', title='Mrs',
#                      contact_num='+65 8888 8888', ewallet_balance=15)
#         db.session.add(d1)
#         db.session.add(p1)
#         db.session.commit()

#         request_body = {
#             'doctor_id': d1.id,
#             'patient_id': p1.id,
#             'diagnosis': 'Itchy armpits',
#             'prescription': 'Better deodrant',
#             'length': 60
#         }

#         response = self.client.post("/consultations",
#                                     data=json.dumps(request_body),
#                                     content_type='application/json')
#         self.assertEqual(response.status_code, 500)
#         self.assertEqual(response.json, {
#             'message': 'Patient does not have enough e-wallet funds.'
#         })


if __name__ == '__main__':
    unittest.main()