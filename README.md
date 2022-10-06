# SPMG3T7

## What you need to do to run the sql scripts in workbench
1. Run wamp server and start MySql Workbench
2. Under MySql Connections, click on the connection to use > 'Edit Connection' > 'Advanced' > 'Others' and add in 'OPT_LOCAL_INFILE=1'
3. Open the SQL Script which is found in 'database' > 'Script' > 'ddl.sql'
4. If the parent folder of 'SPMG3T7' is not the same as mine (spmProj), then use replace all to your parent folder naming

## Troubleshooting
1. Error Code: 3948. Loading local data is disabled; this must be enabled on both the client and server sides
   Execute this line of statement: SET GLOBAL local-infile = TRUE;
