import unittest
import flask_testing
import json
from backend.app import app, db, Course, Course_Registration, Course_Skill, Journey, Journey_Skill_Course, Role, Role_Skill, Skill, Staff

class TestApp(flask_testing.TestCase):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/g3t07ddl'
    app.config['SQLALCHEMY_ENGINE_OPTONS'] = {'pool_size': 100,
                                           'pool_recycle': 280}
    app.config['TESTING'] = True

    def create_app(self):
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

class TestCreateSkill(TestApp):
    def test_create_skill(self):
        # skill1 = Skill(skill_name='Data Analysis', skill_status='Active')
        # db.session.add(skill1)
        # db.session.commit()

        request_body = {
            'skill_name': 'Data Analysis',
            'skill_status': 'Active'
        }

        response = self.client.post("/skill/create",
                                    data=json.dumps(request_body),
                                    content_type='application/json')
        self.assertEqual(response.json, {
            'skill_id': 1,
            'skill_name': 'Data Analysis',
            'skill_status': 'Active'
        })

if __name__ == '__main__':
    unittest.main()