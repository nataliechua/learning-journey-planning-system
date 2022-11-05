DROP SCHEMA IF EXISTS G3T07ddl;
CREATE SCHEMA G3T07ddl;
USE G3T07ddl;

CREATE TABLE ROLE
(
Role_ID int auto_increment NOT NULL PRIMARY KEY,
Role_Name varchar(50),
Role_Status varchar(15)
);

CREATE TABLE SKILL
(
Skill_ID int auto_increment NOT NULL PRIMARY KEY,
Skill_Name varchar(50) NOT NULL,
Skill_Status varchar(15) NOT NULL
);

CREATE TABLE ROLE_SKILL
(
Role_ID int NOT NULL,
Skill_ID int NOT NULL,
CONSTRAINT rs_pk PRIMARY KEY (Role_ID, Skill_ID),
CONSTRAINT rs_fk1 FOREIGN KEY (Role_ID) REFERENCES ROLE(Role_ID),
CONSTRAINT rs_fk2 FOREIGN KEY (Skill_ID) REFERENCES SKILL(Skill_ID)
);

CREATE TABLE STAFF
(
Staff_ID int auto_increment NOT NULL PRIMARY KEY,
Staff_FName varchar(30) NOT NULL,
Staff_LName varchar(30) NOT NULL,
Dept varchar(50) NOT NULL,
Email varchar(50) NOT NULL,
User_Type varchar(20) NOT NULL
);

CREATE TABLE COURSE
(
Course_ID varchar(10) NOT NULL PRIMARY KEY,
Course_Name varchar(50) NOT NULL,
Course_Desc varchar(255),
Course_Status varchar(15),
Course_Type varchar(10),
Course_Category varchar(50)
);

CREATE TABLE COURSE_SKILL
(
Course_ID varchar(10) NOT NULL,
Skill_ID int NOT NULL,
CONSTRAINT cs_pk PRIMARY KEY (Course_ID, Skill_ID),
CONSTRAINT cs_fk1 FOREIGN KEY (Course_ID) REFERENCES COURSE(Course_ID),
CONSTRAINT cs_fk2 FOREIGN KEY (Skill_ID) REFERENCES SKILL(Skill_ID)
);

CREATE TABLE JOURNEY
(
Journey_ID int auto_increment NOT NULL PRIMARY KEY,
Journey_Name varchar(30) NOT NULL,
Staff_ID int NOT NULL,
Role_ID int NOT NULL,
CONSTRAINT journey_fk1 FOREIGN KEY (Staff_ID) REFERENCES STAFF(Staff_ID),
CONSTRAINT journey_fk2 FOREIGN KEY (Role_ID) REFERENCES ROLE(Role_ID)
);

CREATE TABLE JOURNEY_SKILL_COURSE
(
Journey_ID int NOT NULL,
Course_ID varchar(10) NOT NULL,
Skill_ID int NOT NULL,
CONSTRAINT jsc_pk PRIMARY KEY (Journey_ID, Skill_ID, Course_ID),
CONSTRAINT jsc_fk1 FOREIGN KEY (Journey_ID) REFERENCES JOURNEY(Journey_ID) ON DELETE CASCADE,
CONSTRAINT jsc_fk2 FOREIGN KEY (Skill_ID) REFERENCES SKILL(Skill_ID),
CONSTRAINT jsc_fk3 FOREIGN KEY (Course_ID) REFERENCES COURSE(Course_ID)
);

CREATE TABLE COURSE_REGISTRATION
(
Reg_ID int NOT NULL PRIMARY KEY,
Course_ID varchar(10) NOT NULL,
Staff_ID int NOT NULL,
Reg_Status varchar(15) NOT NULL,
Completion_Status varchar(15),
CONSTRAINT cr_fk1 FOREIGN KEY (Course_ID) REFERENCES COURSE(Course_ID),
CONSTRAINT cr_fk2 FOREIGN KEY (Staff_ID) REFERENCES STAFF(Staff_ID)
);

/*Import Role CSV File*/ 
LOAD DATA INFILE 'C:/wamp64/tmp/spm_database/RawData/role.csv'
INTO TABLE ROLE   
FIELDS TERMINATED BY ','  
OPTIONALLY ENCLOSED BY '"'  
LINES TERMINATED BY '\r\n'   
IGNORE 1 ROWS;

/*Import Skills CSV File*/ 
LOAD DATA INFILE 'C:/wamp64/tmp/spm_database/RawData/skills.csv'
INTO TABLE SKILL   
FIELDS TERMINATED BY ','  
OPTIONALLY ENCLOSED BY '"'  
LINES TERMINATED BY '\r\n'   
IGNORE 1 ROWS;  

/*Import Staff CSV File*/ 
LOAD DATA INFILE 'C:/wamp64/tmp/spm_database/RawData/staff.csv'
INTO TABLE STAFF
FIELDS TERMINATED BY ','  
OPTIONALLY ENCLOSED BY '"'  
LINES TERMINATED BY '\n'   
IGNORE 1 ROWS;  

/*Import Course CSV File*/ 
LOAD DATA INFILE 'C:/wamp64/tmp/spm_database/RawData/courses.csv'
INTO TABLE COURSE   
FIELDS TERMINATED BY ','  
OPTIONALLY ENCLOSED BY '"'  
LINES TERMINATED BY '\r\n'   
IGNORE 1 ROWS;  

/*Import Course Registration CSV File*/ 
LOAD DATA INFILE 'C:/wamp64/tmp/spm_database/RawData/registration.csv'
INTO TABLE COURSE_REGISTRATION   
FIELDS TERMINATED BY ','  
OPTIONALLY ENCLOSED BY '"'  
LINES TERMINATED BY '\r\n'   
IGNORE 1 ROWS;  

/*Simulate skills that are already assigned to role*/
INSERT INTO ROLE_SKILL
VALUES 
(1, 10),
(1, 11),
(1, 12),
(2, 11),
(2, 12),
(3, 13),
(4, 9),
(4, 16),
(4, 17),
(5, 18),
(6, 14),
(7, 15),
(8, 1),
(8, 2),
(8, 3),
(8, 4),
(8, 5),
(8, 8);

/*Simulate skills that are already assigned to course*/
INSERT INTO COURSE_SKILL
VALUES 
('COR001', 11),
('COR001', 15),
('COR002', 12),
('MGT001', 1),
('MGT001', 8),
('MGT002', 6),
('MGT003', 1),
('MGT004', 3),
('MGT004', 8),
('FIN001', 12),
('tch008', 11),
('tch013', 14),
('tch013', 15),
('tch001', 18),
('tch013', 18),
('tch015', 18);

/*Simulate journey that is created by user*/
INSERT INTO JOURNEY
VALUES 
(1, 'Aiming Data Analyst', 130001, 1),
(2, 'I want to be a DC', 150008, 2),
(3, 'Data Consultance', 130001, 2),
(4, 'Data Consultance Path', 150265, 2),
(5, 'Want to be Security Analyst', 150265, 5),
(6, 'Aiming Project Manager', 150008, 8);

/*Simulate journey_skill that is created by user*/
INSERT INTO JOURNEY_SKILL_COURSE
VALUES 
(1, 'COR001', 11),
(3, 'COR002', 12),
(2, 'COR002', 12),
(2, 'MGT001', 8),
(2, 'tch008', 11),
(4, 'COR002', 12),
(5, 'tch001', 18),
(5, 'tch013', 18),
(5, 'tch015', 18),
(6, 'MGT001', 1);

/*GET learning journey by role and user and learning journey role*/
SELECT j.Journey_ID, j.Journey_Name, j.Staff_ID, r.Role_Name, c.Course_Name, cr.Completion_Status, s.Skill_Name
FROM JOURNEY j
INNER JOIN JOURNEY_SKILL_COURSE jsc ON j.Journey_ID = jsc.Journey_ID
INNER JOIN COURSE c ON jsc.Course_ID = c.Course_ID
INNER JOIN SKILL s ON s.Skill_ID = jsc.Skill_ID
INNER JOIN ROLE r ON r.Role_ID = j.Role_ID
RIGHT JOIN COURSE_REGISTRATION cr ON cr.Course_ID = jsc.Course_ID
WHERE j.Staff_ID = 130001 AND j.Role_ID = 1 AND cr.Staff_ID = j.Staff_ID AND j.journey_ID = jsc.journey_ID;