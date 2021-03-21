# create databases
CREATE DATABASE IF NOT EXISTS `pg-teste`;

# create root user and grant rights
CREATE USER 'admin'@'localhost' IDENTIFIED BY 'admin';
GRANT ALL ON *.* TO 'admin'@'%';