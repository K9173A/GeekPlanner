CREATE DATABASE geekplanner;
CREATE USER admin with PASSWORD 'admin';
GRANT ALL PRIVILEGES ON DATABASE geekplanner TO admin;
ALTER ROLE admin SET CLIENT_ENCODING TO 'UTF8';
ALTER ROLE admin SET default_transaction_isolation TO 'READ COMMITTED';
ALTER ROLE admin SET TIME ZONE 'Europe/Moscow';