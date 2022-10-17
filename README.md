# SPMG3T7

## What you need to do to run the sql scripts in workbench/
1. Run wamp server and start MySql Workbench
2. Copy and paste the entire database folder into this directory 'C:\wamp64\tmp'
3. Open the SQL Script which is found in 'database' > 'Script' > 'ddl.sql'

## Troubleshooting
1. Error Code: 3948. Loading local data is disabled; this must be enabled on both the client and server sides
   Execute this line of statement: SET GLOBAL local-infile = TRUE;
   
## API endpoints
- Get all courses: http://localhost:5000/courses
- Get all course registrations: http://localhost:5000/course_registrations
- Get all course skills: http://localhost:5000/course_skills
- Get all roles: http://localhost:5000/roles
- Get all role skills: http://localhost:5000/role_skills
- Get all skills: http://localhost:5000/skills
- Get all staffs: http://localhost:5000/staffs
- Get all user types: http://localhost:5000/user_types

- Update course with skills
- Update skill status
- Update role status
- Update skills required for a role
- Get skills based on role
- Get course based on skills

- Get all learning journey based on staff id
- Add learning journey 
- Get a learning journey based on learning journey id
- Get existing skills that is not inside a learning journey based on learning journey id
- Update skills and courses based on learning journey id
- Remove learning journey

- Get all active skills
- Get all course + skills details based on course status
- Add skill to course
- Remove course from skills

## Frontend accounts
- HR: id=hr; password=hr
- Staff: id=staff; password=staff
