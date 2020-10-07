from db.run_sql import run_sql

from models.animal import Animal
from models.owner import Owner
from models.vet import Vet

import repositories.owner_repository as owner_repository
import repositories.vet_repository as vet_repository

def save(animal):
    sql = 'INSERT INTO animals (name, dob, type, owner_id, vet_id) VALUES (%s, %s, %s, %s, %s) RETURNING id'
    values = [animal.name, animal.dob, animal.type, animal.owner.id, animal.vet.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    animal.id = id

def select_all():
    animals = []
    sql = 'SELECT * FROM animals'
    results = run_sql(sql)
    for result in results:
        owner = owner_repository.select(result['owner_id'])
        vet = vet_repository.select(result['vet_id'])
        animal = Animal(result['name'], result['dob'], result['type'], owner, vet, result['id'], result['treatment_notes'])
        animals.append(animal)
    return animals

def select(id):
    sql = 'SELECT * FROM animals WHERE id = %s'
    values = [id]
    result = run_sql(sql, values)[0]
    animal = Animal(result['name'], result['dob'], result['type'], result['owner_id'], result['vet_id'], result['id'], result['treatment_notes'])
    return animal

def delete_all():
    sql = 'DELETE FROM animals'
    run_sql(sql)

def delete(id):
    sql = 'DELETE FROM animals WHERE id = %s'
    values = [id]
    run_sql(sql, values)

def update(animal): 
    sql = 'UPDATE animals SET (name, dob, type, owner_id, vet_id, treatment_notes) = (%s, %s, %s, %s, %s, %s) WHERE id =%s'
    values = [animal.name, animal.dob, animal.type, animal.owner.id, animal.vet.id, animal.treatment_notes, animal.id]
    run_sql(sql, values)                        

    
    
    