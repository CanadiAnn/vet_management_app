from db.run_sql import run_sql
from models.animal import Animal

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
        animal = Animal(result['name'], result['id'])
        animals.append(animal)
    return animals

def select(id):
    sql = 'SELECT * FROM animals WHERE id = %s'
    values = [id]
    result = run_sql(sql, values)[0]
    animal = Animal(result['name'], result['id'])
    return animal

def delete_all():
    sql = 'DELETE FROM animals'
    run_sql(sql)

def delete(id):
    sql = 'DELETE FROM animals WHERE id = %s'
    values = [id]
    run_sql(sql, values)

def update(animal):
    sql = 'UPDATE animals SET name = %s WHERE id = %s'
    values = [animal.name, animal.id]
    run_sql(sql, values)                        