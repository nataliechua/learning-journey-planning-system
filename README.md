# SPMG3T7

## What you need to do to run the sql scripts in workbench/
1. Run wamp server and start MySQL Workbench
2. Set default-storage-engine in MySQL config file to InnoDB
3. Copy and paste the entire database folder into this directory 'C:\wamp64\tmp'
4. Open the SQL Script which is found in 'database' > 'Script' > 'ddl.sql'

## Troubleshooting
1. Error Code: 3948. Loading local data is disabled; this must be enabled on both the client and server sides
   Execute this line of statement: SET GLOBAL local-infile = TRUE;

## API endpoints
### courses
- Get all courses: http://localhost:5000/courses
- Get course by id: http://localhost:5000/course/<string:id>
- Get courses by status: http://localhost:5000/courses/<string:status>

### course registrations
- Get all course registrations: http://localhost:5000/course_registrations
- Get course registration(s) by staff id and course id: http://localhost:5000/course_registration/<int:staff_id>/<string:course_id>

### course skills
- Get all course skills: http://localhost:5000/course_skills
- (used) Get courses by skill id: http://localhost:5000/courses_by_skill/<int:skill_id>
- Get skills by course id: http://localhost:5000/skills_by_course/<string:course_id>
- (used) Get courses and skills by course status: http://localhost:5000/courses_skills_by_course_status/<string:course_status>
- (used) Get active skills whether in course by course id: http://localhost:5000/active_skills_whether_in_course/<string:course_id>
- Remove course skill: http://localhost:5000/remove_course_skill/<string:course_id>/<int:skill_id>
- Create course skill: http://localhost:5000/course_skill/create
- (used) Update course skill: http://localhost:5000/course_skill/update

### journeys
- Get all journeys: http://localhost:5000/journeys
- Get journey by id: http://localhost:5000/journey/<int:id>
- Get journeys by staff id: http://localhost:5000/journeys_by_staff/<int:staff_id>
- Remove journey by id: http://localhost:5000/journey_remove/<int:id>
- Create journey: http://localhost:5000/journey/create

### journey skill courses
- Get all journey skill course: http://localhost:5000/journey_skill_course
- (used) Get all journey info by journey id: http://localhost:5000/all_journey_info/<int:journey_id>
- (used) Get all journeys info by staff id: http://localhost:5000/all_journeys_info/<int:staff_id>
- Get skills not inside journey by journey id: http://localhost:5000/skills_not_in_journey/<int:journey_id>
- (used) Remove journey skill course: http://localhost:5000/remove_journey_skill_course/<int:journey_id>/<int:skill_id>/<string:course_id>
- Create journey skill course: http://localhost:5000/journey_skill_course/create

### roles
- Get all roles: http://localhost:5000/roles
- Get role by id: http://localhost:5000/role/<int:id>
- (used) Get roles by status: http://localhost:5000/roles/<string:status>
- Update role status by role id: http://localhost:5000/update_role_status/<int:role_id>
- (used) Create role: http://localhost:5000/role/create

### role skills
- Get all role skills: http://localhost:5000/role_skills
- Get all roles with skills: http://localhost:5000/roles_with_skills
- (used) Get active skills by role id: http://localhost:5000/active_skills_by_role/<int:role_id>
- (used) Get active skills whether in role by role id: http://localhost:5000/active_skills_whether_in_role/<string:role_id>
- Remove role skill: http://localhost:5000/remove_role_skill/<int:role_id>/<int:skill_id>
- Create role skill: http://localhost:5000/role_skill/create
- Update role skill: http://localhost:5000/role_skill/update
- (used) Update role info: http://localhost:5000/role_info/update

### skills
- Get all skills: http://localhost:5000/skills
- (used) Get skill by id: http://localhost:5000/skill/<int:id>
- Get skills by status: http://localhost:5000/skills/<string:status>
- (used) Update skill status by skill id: http://localhost:5000/update_skill_status/<int:skill_id>
- Create skill: http://localhost:5000/skill/create

### staffs
- Get all staffs: http://localhost:5000/staffs

## Frontend accounts
- HR: id=hr; password=hr
- Staff: id=staff; password=staff
