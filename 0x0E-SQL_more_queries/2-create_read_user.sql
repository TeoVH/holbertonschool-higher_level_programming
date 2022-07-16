-- Script that creates the database hbtn_0d_2 and the user user_0d_2
-- User should have only SELECT privilege in the database hbtn_0d_2
-- User password should be set to user_0d_2_pwd
-- If user or database already exist, your script should not fail

CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON `hbtn_0d_2`.* TO 'user_0d_2'@'localhost';
FLUSH PRIVILEGES;