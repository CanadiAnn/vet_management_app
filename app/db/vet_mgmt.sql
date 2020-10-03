DROP TABLE animals;
DROP TABLE owners;
DROP TABLE vets;

CREATE TABLE animals (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    dob VARCHAR(255),
    type VARCHAR(255),
    owner VARCHAR(255)
);

CREATE TABLE owners(
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    phone_num VARCHAR(11),
    address VARCHAR(255)
):

CREATE TABLE vets(
    id SERIAL PRIMARY KEY, 
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    license VARCHAR (8)
);
