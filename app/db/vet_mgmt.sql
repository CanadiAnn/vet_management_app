
DROP TABLE animals;
DROP TABLE owners;
DROP TABLE vets;


CREATE TABLE owners(
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    phone_num_1 INT,
    phone_num_2 INT,
    address VARCHAR(255)
);

CREATE TABLE vets(
    id SERIAL PRIMARY KEY, 
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    license INT
);

CREATE TABLE animals(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    dob VARCHAR(255),
    type VARCHAR(255),
    owner_id INT REFERENCES owners(id),
    vet_id INT REFERENCES vets(id),
    treatment_notes VARCHAR(255)
);

-- OWNER DB console.py from task manager

INSERT INTO owners (first_name, last_name, phone_num_1, phone_num_2, address) VALUES ('Ann', 'Loz', 12345, 123456, '15 Bread St, Midlothian, Edinburgh');
INSERT INTO owners (first_name, last_name, phone_num_1, phone_num_2, address) VALUES ('Lulu', 'Dagenais', 23456, 123456, '25 Castlehill Terrace, Midlothian, Edinburgh');
INSERT INTO owners (first_name, last_name, phone_num_1, phone_num_2, address) VALUES ('Vanessa', 'Constantini', 43215, 123456, '46 Paris St, Midlothian, Edinburgh');

-- SELECT * FROM owners;

-- VET DB

INSERT INTO vets (first_name, last_name, license) VALUES ('Kate', 'Bees', 10004567);
INSERT INTO vets (first_name, last_name, license) VALUES ('Alex', 'Padmore', 10009876);

-- SELECT * FROM vets;       

-- ANIMAL DB

INSERT INTO animals (name, dob, type, owner_id, vet_id, treatment_notes) VALUES ('Boubou', '4/08/2008', 'cat', 1, 1, 'test1' );
INSERT INTO animals (name, dob, type, owner_id, vet_id, treatment_notes) VALUES ('Ti-Gars', '17/11/2012', 'fat cat', 2, 1, 'test2');
INSERT INTO animals (name, dob, type, owner_id, vet_id, treatment_notes) VALUES ('Brasco', '23/03/2015', 'dog', 3, 2, 'test3');

-- SELECT * FROM animals;
   
