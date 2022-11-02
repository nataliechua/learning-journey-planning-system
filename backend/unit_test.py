import unittest
from app import Course, Course_Registration,Course_Skill,Journey,Journey_Skill_Course,Role,Role_Skill,Skill,Staff

class TestCourse(unittest.TestCase):
    def test_to_dict(self):
        course = Course(course_id = "CAT101",
            course_name = "Cat behavior",
            course_desc = "Study about why cats never fail to facinate human beings",
            course_status = "Active",
            course_type = "External",
            course_category = "Core")
        self.assertEqual(course.to_dict(), {
            "course_id": "CAT101",
            "course_name": "Cat behavior",
            "course_desc": "Study about why cats never fail to facinate human beings",
            "course_status": "Active",
            "course_type": "External",
            "course_category": "Core"}
        )

class TestCourseRegistration(unittest.TestCase):
    def test_to_dict(self):
        cr = Course_Registration(reg_id = 100,
            course_id = "CAT101",
            staff_id = 150999,
            reg_status = "Registered",
            completion_status = "OnGoing")
        self.assertEqual(cr.to_dict(), {
            "reg_id": 100,
            "course_id": "CAT101",
            "staff_id": 150999,
            "reg_status": "Registered",
            "completion_status": "OnGoing"}
        )

class TestCourseSkill(unittest.TestCase):
    def test_to_dict(self):
        cs = Course_Skill(course_id = "CAT101",
            skill_id = 6)
        self.assertEqual(cs.to_dict(), {
            "course_id": "CAT101",
            "skill_id": 6}
        )

class TestJourney(unittest.TestCase):
    def test_to_dict(self):
        j = Journey(journey_id = None,
                    journey_name = "Want to be an astronaut",
                    staff_id = 150999,
                    role_id = 8)
        self.assertEqual(j.to_dict(), {
            "journey_id": None,
            "journey_name": "Want to be an astronaut",
            "staff_id": 150999,
            "role_id": 8}
        )

class TestJourneySkillCourse(unittest.TestCase):
    def test_to_dict(self):
        jsc = Journey_Skill_Course(journey_id = 7,
            course_id = "CAT101",
            skill_id = 2)
        self.assertEqual(jsc.to_dict(), {
            "journey_id": 7,
            "course_id": "CAT101",
            "skill_id": 2}
        )

class TestRole(unittest.TestCase):
    def test_to_dict(self):
        role = Role(role_id = None,
            role_name = "Astronaut",
            role_status = "Active")
        self.assertEqual(role.to_dict(), {
            "role_id": None,
            "role_name": "Astronaut",
            "role_status": "Active"}
        )

class TestRoleSkill(unittest.TestCase):
    def test_to_dict(self):
        rs = Role_Skill(role_id = 9,
            skill_id = 19)
        self.assertEqual(rs.to_dict(), {
            "role_id": 9,
            "skill_id": 19}
        )

class TestSkill(unittest.TestCase):
    def test_to_dict(self):
        skill = Skill(skill_id = None,
            skill_name = "land on Mars",
            skill_status="Active")
        self.assertEqual(skill.to_dict(), {
            "skill_id": None,
            "skill_name": "land on Mars",
            "skill_status": "Active"}
        )

class TestStaff(unittest.TestCase):
    def test_to_dict(self):
        staff = Staff(staff_id = None,
            staff_fname="Foo",
            staff_lname="Andy",
            dept="Investigation",
            email="andy.foo@allinone.com.sg",
            user_type="Admin")
        self.assertEqual(staff.to_dict(), {
            "staff_id": None,
            "staff_fname": "Foo",
            "staff_lname": "Andy",
            "dept": "Investigation",
            "email": "andy.foo@allinone.com.sg",
            "user_type": "Admin"}
        )


if __name__ == "__main__":
    unittest.main()