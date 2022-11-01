DROP SCHEMA IF EXISTS G3T07ddlTest;
CREATE SCHEMA G3T07ddlTest;
USE G3T07ddlTest;

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