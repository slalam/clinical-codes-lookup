/* 
DROP TABLE IF EXISTS SNOMEDCT_CODES;
CREATE TABLE SNOMEDCT_CODES(
  id INT NOT NULL AUTO_INCREMENT,
  CONCEPT_ID INT NOT NULL,
  CONCEPT_DESCRIPTION VARCHAR(255) NOT NULL,
  PRIMARY KEY (id)
);
LOAD DATA LOCAL INFILE '/Users/satya_lalam/Desktop/clinical-codes-lookup/files/sct2_Description_Full-en_INT_20210131.txt' 
INTO TABLE SNOMEDCT_CODES 
FIELDS TERMINATED BY '\t'
LINES TERMINATED BY '\r\n' 
IGNORE 1 ROWS (
  @dummy, 
  @dummy,
  @dummy,
  @dummy,
  CONCEPT_ID,
  @dummy,
  @dummy,
  CONCEPT_DESCRIPTION,
  @dummy
);

DROP TABLE IF EXISTS LOINC_CODES;
CREATE TABLE LOINC_CODES (
  id INT NOT NULL AUTO_INCREMENT,
  LOINC_NUM VARCHAR(25) NOT NULL,
  LONG_COMMON_NAME VARCHAR(255) NOT NULL,
  PRIMARY KEY (id)
);
LOAD DATA LOCAL INFILE '/Users/satya_lalam/Desktop/clinical-codes-lookup/files/LoincTableCore.csv' 
INTO TABLE LOINC_CODES 
FIELDS TERMINATED BY ',' ENCLOSED BY '"' 
LINES TERMINATED BY '\r\n' 
IGNORE 1 ROWS (
  LOINC_NUM,
  @dummy,
  @dummy,
  @dummy,
  @dummy,
  @dummy,
  @dummy,
  @dummy,
  @dummy,
  LONG_COMMON_NAME,
  @dummy,
  @dummy,
  @dummy,
  @dummy,
  @dummy
); 
*/

DROP TABLE IF EXISTS DIAGNOSIS_CODES;
CREATE TABLE DIAGNOSIS_CODES (
  id INT NOT NULL AUTO_INCREMENT,
  CURRENT_ICD10_LIST VARCHAR(254) NULL,
  DIAGNOSIS_ID INT NOT NULL,
  DIAGNOSIS_NAME VARCHAR(200) NULL,
  DIAGNOSIS_GROUP VARCHAR(200) NULL,
  PRIMARY KEY (id)
);
LOAD DATA LOCAL INFILE '/Users/satya_lalam/Desktop/clinical-codes-lookup/files/DIAGNOSIS.csv' 
INTO TABLE DIAGNOSIS_CODES 
FIELDS TERMINATED BY ',' ENCLOSED BY '"' 
LINES TERMINATED BY '\r\n' 
IGNORE 1 
ROWS (
  CURRENT_ICD10_LIST,
  DIAGNOSIS_ID,
  DIAGNOSIS_NAME,
  DIAGNOSIS_GROUP
);

DROP TABLE IF EXISTS LAB_CODES;
CREATE TABLE LAB_CODES (
  id INT NOT NULL AUTO_INCREMENT,
  COMPONENT_ID INT NOT NULL,
  COMPONENT_NAME VARCHAR(75) NULL,
  COMPONENT_ALIAS_NAME VARCHAR(75) NULL,
  PRIMARY KEY (id)
);
LOAD DATA LOCAL INFILE '/Users/satya_lalam/Desktop/clinical-codes-lookup/files/LABS.csv' 
INTO TABLE LAB_CODES 
FIELDS TERMINATED BY ',' ENCLOSED BY '"' 
LINES TERMINATED BY '\r\n' 
IGNORE 1 
ROWS (
  COMPONENT_ID,
  COMPONENT_NAME,
  COMPONENT_ALIAS_NAME
);

DROP TABLE IF EXISTS PROCEDURE_CODES;
CREATE TABLE PROCEDURE_CODES (
  id INT NOT NULL AUTO_INCREMENT,
  PROCEDURE_ID INT NOT NULL,
  PROC_NAME VARCHAR(189) NULL,
  PROCEDURE_CPT_CODE VARCHAR(40) NULL,
  PATIENT_FRIENDLY_NAME VARCHAR(254) NULL,
  ORDER_DISPLAY_NAME VARCHAR(254) NULL,
  PROCEDURE_CATEGORY_ID VARCHAR(254) NOT NULL,
  PROCEDURE_CATEGORY_NAME VARCHAR(200) NULL,
  PRIMARY KEY (id)
);
LOAD DATA LOCAL INFILE '/Users/satya_lalam/Desktop/clinical-codes-lookup/files/PROCEDURES.csv' 
INTO TABLE PROCEDURE_CODES 
FIELDS TERMINATED BY ',' ENCLOSED BY '"' 
LINES TERMINATED BY '\r\n' 
IGNORE 1 
ROWS (
  PROCEDURE_ID,
  PROC_NAME,
  PROCEDURE_CPT_CODE,
  PATIENT_FRIENDLY_NAME,
  ORDER_DISPLAY_NAME,
  PROCEDURE_CATEGORY_ID,
  PROCEDURE_CATEGORY_NAME
);

DROP TABLE IF EXISTS MEDICATION_CODES;
CREATE TABLE MEDICATION_CODES (
  id INT NOT NULL AUTO_INCREMENT,
  MEDICATION_ID INT NOT NULL,
  MEDICATION_NAME VARCHAR(255) NULL,
  SIMPLE_GENERIC_C VARCHAR(66) NULL,
  SIMPLE_GENERIC_NAME VARCHAR(254) NULL,
  THERA_CLASS_C INT NULL,
  THERA_CLASS_NAME VARCHAR(254) NULL,
  PHARM_CLASS_C INT NULL,
  PHARM_CLASS_NAME VARCHAR(254) NULL,
  PHARM_SUBCLASS_C INT NULL,
  PHARM_SUBCLASS_NAME VARCHAR(254) NULL,
  ROUTE VARCHAR(50) NULL,
  FORM VARCHAR(50) NULL,
  PRIMARY KEY (id)
);
LOAD DATA LOCAL INFILE '/Users/satya_lalam/Desktop/clinical-codes-lookup/files/MEDICATIONS.csv' 
INTO TABLE MEDICATION_CODES 
FIELDS TERMINATED BY ',' ENCLOSED BY '"' 
LINES TERMINATED BY '\r\n' 
IGNORE 1 
ROWS (
  MEDICATION_ID,
  MEDICATION_NAME,
  SIMPLE_GENERIC_C,
  SIMPLE_GENERIC_NAME,
  THERA_CLASS_C,
  THERA_CLASS_NAME,
  PHARM_CLASS_C,
  PHARM_CLASS_NAME,
  PHARM_SUBCLASS_C,
  PHARM_SUBCLASS_NAME,
  ROUTE,
  FORM
);

DROP TABLE IF EXISTS SURGERY_CODES;
CREATE TABLE SURGERY_CODES (
  id INT NOT NULL AUTO_INCREMENT,
  OR_PROCEDURE_ID VARCHAR(254) NOT NULL,
  OR_PROCEDURE_NAME VARCHAR(200) NULL,
  PRIMARY KEY (id)
);
LOAD DATA LOCAL INFILE '/Users/satya_lalam/Desktop/clinical-codes-lookup/files/OR_SURGERIES.csv' 
INTO TABLE SURGERY_CODES 
FIELDS TERMINATED BY ',' ENCLOSED BY '"' 
LINES TERMINATED BY '\r\n' 
IGNORE 1 
ROWS (
  OR_PROCEDURE_ID, 
  OR_PROCEDURE_NAME
);

DROP TABLE IF EXISTS SAMPLE_TYPE_COUNTS;
CREATE TABLE SAMPLE_TYPE_COUNTS (
  id INT NOT NULL AUTO_INCREMENT,
  TYPE VARCHAR(254) NOT NULL,
  COUNTS INT NOT NULL,
  PRIMARY KEY (id)
);
LOAD DATA LOCAL INFILE '/Users/satya_lalam/Desktop/clinical-codes-lookup/files/SAMPLE_TYPE_COUNTS.csv' 
INTO TABLE SAMPLE_TYPE_COUNTS 
FIELDS TERMINATED BY ',' ENCLOSED BY '"' 
LINES TERMINATED BY '\r\n' 
IGNORE 1 
ROWS (
  TYPE, 
  COUNTS
);

DROP TABLE IF EXISTS DX_SAMPLE_COUNTS;
CREATE TABLE DX_SAMPLE_COUNTS (
  id INT NOT NULL AUTO_INCREMENT,
  CURRENT_ICD10_LIST VARCHAR(254) NOT NULL,
  DX_ID INT NOT NULL,
  DX_NAME VARCHAR(254) NOT NULL,
  WHOLEBLOOD INT NOT NULL,
  PLASMA INT NOT NULL,
  SERUM INT NOT NULL,
  DNA INT NOT NULL,
  PRIMARY KEY (id)
);
LOAD DATA LOCAL INFILE '/Users/satya_lalam/Desktop/clinical-codes-lookup/files/DX_SAMPLE_COUNTS.csv' 
INTO TABLE DX_SAMPLE_COUNTS 
FIELDS TERMINATED BY ',' ENCLOSED BY '"' 
LINES TERMINATED BY '\r\n' 
IGNORE 1 
ROWS (
  CURRENT_ICD10_LIST,
  DX_ID,
  DX_NAME,
  WHOLEBLOOD,
  PLASMA,
  SERUM,
  DNA
);