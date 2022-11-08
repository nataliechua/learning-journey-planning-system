# SPMG3T7

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
### course skills
- (kj) Get courses by skill id: http://localhost:5000/courses_by_skill/<int:skill_id>
- (used) Get skills by course id: http://localhost:5000/skills_by_course/<string:course_id>
- (kj) Get courses and skills by course status: http://localhost:5000/courses_skills_by_course_status/<string:course_status>
- (kj) Get active skills whether in course by course id: http://localhost:5000/active_skills_whether_in_course/<string:course_id>
- (kj) Update course skill: http://localhost:5000/course_skill/update

### journeys, journey skill courses
- (ps) Get all journey info by journey id: http://localhost:5000/all_journey_info/<int:journey_id>
- (ll, ps) Get all journeys info by staff id: http://localhost:5000/all_journeys_info/<int:staff_id>
- (kj?) Remove journey by id: http://localhost:5000/journey_remove/<int:id>
- (kj?, ll) Remove journey skill course: http://localhost:5000/remove_journey_skill_course/<int:journey_id>/<int:skill_id>/<string:course_id>
- (kj) Create journey: http://localhost:5000/journey/create
- (ll) Create journey skill course: http://localhost:5000/journey_skill_course/create
- (ll) update journey info: http://localhost:5000/update_journey_info

### roles
- (kj) Get roles by status: http://localhost:5000/roles/<string:status>
- (nat) Create role: http://localhost:5000/role/create

### role skills
- (nat) Get roles with skills by role status: http://localhost:5000/roles_with_skills/<string:role_status>
- (kj) Get active skills by role id: http://localhost:5000/active_skills_by_role/<int:role_id>
- (kj, val) Get active skills whether in role by role id: http://localhost:5000/active_skills_whether_in_role/<string:role_id>
- (val) Update role info: http://localhost:5000/role_info/update

### skills
- (ps) Get skill by id: http://localhost:5000/skill/<int:id>
- (val) Get skills by status: http://localhost:5000/skills/<string:status>
- (ll) Create skill: http://localhost:5000/skill/create
- (ps) Update skill info by id: http://localhost:5000/update_skill_info/<int:skill_id>


### not used
#### courses
- Get all courses: http://localhost:5000/courses
- Get course by id: http://localhost:5000/course/<string:id>
- Get courses by status: http://localhost:5000/courses/<string:status>
#### course registrations
- Get all course registrations: http://localhost:5000/course_registrations
- Get course registration(s) by staff id and course id: http://localhost:5000/course_registration/<int:staff_id>/<string:course_id>
#### course skills
- Get all course skills: http://localhost:5000/course_skills
- Remove course skill: http://localhost:5000/remove_course_skill/<string:course_id>/<int:skill_id>
- Create course skill: http://localhost:5000/course_skill/create
#### journeys
- Get all journeys: http://localhost:5000/journeys
- Get journey by id: http://localhost:5000/journey/<int:id>
- Get journeys by staff id: http://localhost:5000/journeys_by_staff/<int:staff_id>
#### journey skill courses
- Get all journey skill course: http://localhost:5000/journey_skill_course
- Get skills not inside journey by journey id: http://localhost:5000/skills_not_in_journey/<int:journey_id>
#### roles
- Get all roles: http://localhost:5000/roles
- Get role by id: http://localhost:5000/role/<int:id>
- Update role status by role id: http://localhost:5000/update_role_status/<int:role_id>
#### role skills
- Get all role skills: http://localhost:5000/role_skills
- Get all roles with skills: http://localhost:5000/roles_with_skills
- Remove role skill: http://localhost:5000/remove_role_skill/<int:role_id>/<int:skill_id>
- Create role skill: http://localhost:5000/role_skill/create
- Update role skill: http://localhost:5000/role_skill/update
#### skills
- Get all skills: http://localhost:5000/skills
#### staffs
- Get all staffs: http://localhost:5000/staffs

