# SPMG3T7

## What you need to do to run the sql scripts in workbench/
1. Run wamp server and start MySql Workbench
2. Copy and paste the entire database folder into this directory 'C:\wamp64\tmp'
3. Open the SQL Script which is found in 'database' > 'Script' > 'ddl.sql'

## Troubleshooting
1. Error Code: 3948. Loading local data is disabled; this must be enabled on both the client and server sides
   Execute this line of statement: SET GLOBAL local-infile = TRUE;
   
## Required API endpoints
- Get all courses from LMS
- Update course with skills
- Get all skills
- Update skill status
- Get all roles
- Update role status
- Update skills required for a role
- Get skills based on role
- Get course based on skills
