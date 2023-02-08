# 🧠 Learning Journey Planning System 

A learning journey tracker which recommends employees which courses to take based on a desired goal. It allows them to track which courses they have completed, and see how many more they still have left. 

The application also allows HR personnel to update the application with new courses. They are able to map skills and roles to new courses.

Done with Flask, Vue.js, and Bootstrap. Test-driven development using Unittest.

## Installation guide
1. Set up and run a WAMP or MAMP server
2. Set default-storage-engine in MySQL config file to InnoDB
3. Copy and paste the entire database folder into this directory 'C:\wamp64\tmp'
4. Execute the contents of 'ddl.sql' (spm_database/Script) in phpMyAdmin, i.e. at:
      http://localhost/phpmyadmin  OR
	   http://localhost/phpMyAdmin
5. Find your web server's root directory (e.g. C:\wamp\www) and create a folder called 'SPMG3T7'. Copy the folder 'frontend' into 'SPMG3T7'.
6. If you don't already have Flask installed, do:
	   python -m pip install flask
	   python -m pip install flask_cors
	   python -m pip install Flask-SQLAlchemy
	   python -m pip install mysql-connector-python
7. In the 'flask' directory, run "python app.py" in a terminal.
8. Go to http://localhost/SPMG3T7 where the application should be working!

## Running tests
1. To run unit and integration tests, go into the 'flask' folder on your command line and do:
      python unit_tests.py
      python integration_tests.py
2. If you get an error message, it may be due to missing packages. Resolve this by doing: 
      python -m pip install flask_testing 
      for each missing package (in this case, 'flask_testing').

## Troubleshooting
1. If loading databse get error code 3948, this means loading local data is disabled, which must be enabled on both the client and server sides.
      Execute this line of statement SQL tab to solve it: 
      SET GLOBAL local-infile = TRUE;
2. If running the Flask application gives you an error message along the lines of "ProgrammingError: (mysql.connector.errors.ProgrammingError) Character set '255' unsupported", then the following temporary 'fix' will resolve it:
      python -m pip install mysql-connector-python==0.29

## Frontend accounts
- HR: id=hr; password=hr, staff_id=150265
- Staff: id=staff; password=staff, staff_id=150008


## API endpoints
### Course skills
- Get courses by skill id: http://localhost:5000/courses_by_skill/<int:skill_id>
- Get skills by course id: http://localhost:5000/skills_by_course/<string:course_id>
- Get courses and skills by course status: http://localhost:5000/courses_skills_by_course_status/<string:course_status>
- Get active skills whether in course by course id: http://localhost:5000/active_skills_whether_in_course/<string:course_id>
- Update course skill: http://localhost:5000/course_skill/update

### Journey, journey skill courses
- Get all journey info by journey id: http://localhost:5000/all_journey_info/<int:journey_id>
- Get all journeys info by staff id: http://localhost:5000/all_journeys_info/<int:staff_id>
- Remove journey by id: http://localhost:5000/journey_remove/<int:id>
- Remove journey skill course: http://localhost:5000/remove_journey_skill_course/<int:journey_id>/<int:skill_id>/<string:course_id>
- Create journey: http://localhost:5000/journey/create
- Create journey skill course: http://localhost:5000/journey_skill_course/create
- Update journey info: http://localhost:5000/update_journey_info

### Roles
- Get roles by status: http://localhost:5000/roles/<string:status>
- Create role: http://localhost:5000/role/create

### Role skills
- Get roles with skills by role status: http://localhost:5000/roles_with_skills/<string:role_status>
- Get active skills by role id: http://localhost:5000/active_skills_by_role/<int:role_id>
- Get active skills whether in role by role id: http://localhost:5000/active_skills_whether_in_role/<string:role_id>
- Update role info: http://localhost:5000/role_info/update

### Skills
- Get skill by id: http://localhost:5000/skill/<int:id>
- Get skills by status: http://localhost:5000/skills/<string:status>
- Create skill: http://localhost:5000/skill/create
- Update skill info by id: http://localhost:5000/update_skill_info/<int:skill_id>
