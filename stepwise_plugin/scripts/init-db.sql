DROP DATABASE IF EXISTS `swm`;
CREATE DATABASE `swm`;
CREATE USER IF NOT EXISTS 'swm'@'localhost' IDENTIFIED BY 'swm';
GRANT ALL PRIVILEGES ON `swm`.* TO "swm"@"localhost";
FLUSH PRIVILEGES;
