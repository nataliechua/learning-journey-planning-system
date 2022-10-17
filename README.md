# SPMG3T7

## What you need to do to run the sql scripts in workbench/
1. Run wamp server and start MySql Workbench
2. Copy and paste the entire database folder into this directory 'C:\wamp64\tmp'
3. Open the SQL Script which is found in 'database' > 'Script' > 'ddl.sql'

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

### course skills
- Get all course skills: http://localhost:5000/course_skills
- Get courses by skill id: http://localhost:5000/courses_by_skill/<int:skill_id>
- Get skills by course id: http://localhost:5000/skills_by_course/<string:course_id>
- Get courses and skills by course status: http://localhost:5000/skills_by_course/courses_skills_by_course_status/<string:course_status>
- Remove course skill: http://localhost:5000/remove_course_skill/<string:course_id>/<int:skill_id>
- create course skill: http://localhost:5000/course_skill/create

### journeys
- Get all journeys: http://localhost:5000/journeys
- Get journey by id: http://localhost:5000/journey/<int:id>
- Get journeys by staff id: http://localhost:5000/journeys_by_staff/<int:staff_id>
- Remove journey by id: http://localhost:5000/journey_remove/<int:id>
- Create journey: 

### journey skill courses
- Get all journey skill course: http://localhost:5000/journey_skill_course
- Get skills not inside journey by journey id: http://localhost:5000/skills_not_in_journey/<int:journey_id>
- remove journey skill course: http://localhost:5000/remove_journey_skill_course/<int:journey_id>/<string:course_id>/<int:skill_id>
- Create journey skill course: 

### roles
- Get all roles: http://localhost:5000/roles
- Get role by id: http://localhost:5000/role/<int:id>
- Update role status by role id: http://localhost:5000/update_role_status/<int:role_id>

### role skills
- Get all role skills: http://localhost:5000/role_skills
- Get skills by role id: http://localhost:5000/skills_by_role/<int:role_id>
- Remove role skill: http://localhost:5000/remove_role_skill/<int:role_id>/<int:skill_id>
- Create role skill: http://localhost:5000/role_skill/create

### skills
- Get all skills: http://localhost:5000/skills
- Get skills by status: http://localhost:5000/skills/<string:status>
- Update skill status by skill id: http://localhost:5000/update_skill_status/<int:skill_id>

### staffs
- Get all staffs: http://localhost:5000/staffs

### user types
- Get all user types: http://localhost:5000/user_types

## Frontend accounts
- HR: id=hr; password=hr
- Staff: id=staff; password=staff
