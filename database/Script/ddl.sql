DROP SCHEMA IF EXISTS G3T07ddl;
CREATE SCHEMA G3T07ddl;
USE G3T07ddl;

CREATE TABLE ROLE
(
Role_ID int NOT NULL PRIMARY KEY,
Role_Name varchar(20) NOT NULL
);

CREATE TABLE ORG_ROLE
(
Org_Role_ID int NOT NULL PRIMARY KEY,
Org_Role_Name varchar(50),
Org_Role_Status varchar(10)
);

CREATE TABLE SKILL
(
Skill_ID int NOT NULL PRIMARY KEY,
Skill_Name varchar(50) NOT NULL,
Skill_Status varchar(10) NOT NULL
);

CREATE TABLE ROLE_SKILLS
(
Org_Role_ID int NOT NULL,
Skill_ID int NOT NULL,
CONSTRAINT rs_pk PRIMARY KEY (Org_Role_ID, Skill_ID),
CONSTRAINT rs_fk1 FOREIGN KEY (Skill_ID) REFERENCES SKILL(Skill_ID),
CONSTRAINT rs_fk2 FOREIGN KEY (Org_Role_ID) REFERENCES ORG_ROLE(Org_Role_ID)
);

CREATE TABLE STAFF
(
Staff_ID int NOT NULL PRIMARY KEY,
Staff_FName varchar(50) NOT NULL,
Staff_LName varchar(50) NOT NULL,
Dept varchar(50) NOT NULL,
Email varchar(50) NOT NULL,
Role int NOT NULL,
CONSTRAINT user_fk1 FOREIGN KEY (Role) REFERENCES ROLE(Role_Name)
);

CREATE TABLE COURSE
(
Course_ID varchar(20) NOT NULL,
Course_Name varchar(50) NOT NULL,
Course_Desc varchar(255),
Course_Status varchar(15),
Course_Type varchar(10),
Course_Category varchar(50),
CONSTRAINT course_pk PRIMARY KEY (Course_ID)
);

CREATE TABLE COURSE_SKILLS
(
Course_ID varchar(20) NOT NULL,
Skill_ID varchar(50) NOT NULL,
CONSTRAINT cs_pk PRIMARY KEY (Course_ID, Skill_ID),
CONSTRAINT cs_fk1 FOREIGN KEY (Skill_ID) REFERENCES SKILL(Skill_ID),
CONSTRAINT cs_fk2 FOREIGN KEY (Course_ID) REFERENCES SKILL(Course_ID)
);

CREATE TABLE JOURNEY
(
Journey_ID int NOT NULL,
Staff_ID int NOT NULL,
Course_ID varchar(20) NOT NULL,
Skill_ID int NOT NULL,
CONSTRAINT journey_pk PRIMARY KEY (Journey_ID, Staff_ID, Course_ID, Skill_ID),
CONSTRAINT journey_fk1 FOREIGN KEY (Staff_ID) REFERENCES USER(User_ID),
CONSTRAINT journey_fk2 FOREIGN KEY (Course_ID) REFERENCES COURSE(Course_ID),
CONSTRAINT journey_fk3 FOREIGN KEY (Skill_ID) REFERENCES SKILL(Skill_ID)
);

/*Import Role CSV File*/ 
LOAD DATA LOCAL INFILE '/spmProj/SPMG3T7/database/RawData/role.csv'
INTO TABLE ROLE   
FIELDS TERMINATED BY ','  
OPTIONALLY ENCLOSED BY '"'  
LINES TERMINATED BY '\n'   
IGNORE 1 ROWS;

/*Import Org Role CSV File*/ 
LOAD DATA LOCAL INFILE '/spmProj/SPMG3T7/database/RawData/orgRole.csv'
INTO TABLE ORG_ROLE   
FIELDS TERMINATED BY ','  
OPTIONALLY ENCLOSED BY '"'  
LINES TERMINATED BY '\n'   
IGNORE 1 ROWS;

/*Import Skills CSV File*/ 
LOAD DATA LOCAL INFILE '/spmProj/SPMG3T7/database/RawData/skills.csv'
INTO TABLE SKILL   
FIELDS TERMINATED BY ','  
OPTIONALLY ENCLOSED BY '"'  
LINES TERMINATED BY '\n'   
IGNORE 1 ROWS;  

/*Import Staff CSV File*/ 
LOAD DATA LOCAL INFILE '/spmProj/SPMG3T7/database/RawData/staff.csv'
INTO TABLE STAFF
FIELDS TERMINATED BY ','  
OPTIONALLY ENCLOSED BY '"'  
LINES TERMINATED BY '\n'   
IGNORE 1 ROWS;  

/*Import Course CSV File*/ 
LOAD DATA LOCAL INFILE '/spmProj/SPMG3T7/database/RawData/courses.csv'
INTO TABLE COURSE   
FIELDS TERMINATED BY ','  
OPTIONALLY ENCLOSED BY '"'  
LINES TERMINATED BY '\n'   
IGNORE 1 ROWS;  

/*Simulate skills that are already assigned to course*/
INSERT INTO COURSE_SKILLS
VALUES 
('COR001', 1),
('COR001', 5),
('COR001', 7),
('COR002', 1);

/*Simulate skills that are already assigned to role*/
INSERT INTO ROLE_SKILLS
VALUES 
(1, 1),
(1, 5),
(1, 7),
(2, 1);

select * from role_skills