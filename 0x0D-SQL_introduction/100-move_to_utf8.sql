-- Script that converts hbtn_0c_0 database to UTF8 in MySQL server
-- Convert DataBase:
ALTER DATABASE hbtn_0c_0 CHARACTER SET = utf8mb4 COLLATE utf8mb4_unicode_ci;
-- Convert Table:
ALTER TABLE hbtn_0c_0.first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;