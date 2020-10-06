from db.run_sql import run_sql

from models.animal import Animal
from models.owner import Owner
from models.vet import Vet

def save(animal):
    sql = 'INSERT INTO animals (name) VALUES (%s) RETURNING id'
    values = [animal.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    animal.id = id

def select_all():
    animals = []
    sql = 'SELECT * FROM animals'
    results = run_sql(sql)
    for result in results:
        animal = Animal(result['name'], result['dob'], result['type'], result['owner_id'], result['vet_id'], result['id'])
        animals.append(animal)
    return animals

def select(id):
    sql = 'SELECT * FROM animals WHERE id = %s'
    values = [id]
    result = run_sql(sql, values)[0]
    animal = Animal(result['name'], result['dob'], result['type'], result['owner_id'], result['vet_id'], result['id'])
    return animal

def delete_all():
    sql = 'DELETE FROM animals'
    run_sql(sql)

def delete(id):
    sql = 'DELETE FROM animals WHERE id = %s'
    values = [id]
    run_sql(sql, values)

def update(animal): #NOT WORKING
    sql = 'UPDATE animal SET (name, dob, type, owner_id, vet_id) = (%s, %s, %s, %s, %s) WHERE id =%s'
    values = [animal.name, animal.dob, animal.type, animal.owner_id, animal.vet_id, animal.id]
    print(values)
    run_sql(sql, values)                        

    