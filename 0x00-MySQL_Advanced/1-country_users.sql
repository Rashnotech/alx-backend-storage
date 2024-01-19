-- a SQL Script that creates a table
-- users table with the following requirements
CREATE TABLE IF NOT EXIST(
  id  INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  email VARCHAR(255) NOT NULL UNIQUE,
  name VARCHAR(255),
  country ENUM (DEFAULT="US", "CO", "IN")
);
