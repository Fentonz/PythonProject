DROP DATABASE "PC_PARTS";
DROP USER "pcadmin";
CREATE DATABASE "PC_PARTS";

CREATE USER "pcadmin" WITH PASSWORD 'adminpass';

ALTER DATABASE "PC_PARTS" OWNER TO pcadmin;

\c "PC_PARTS" "pcadmin";
adminpass

CREATE TABLE products(
	id SERIAL PRIMARY KEY,
	product_id VARCHAR NOT NULL,
	name VARCHAR NOT NULL,
	category VARCHAR NOT NULL,
	price NUMERIC(12,2) NOT NULL,
	shop VARCHAR NOT NULL,
	date DATE NOT NULL
);
