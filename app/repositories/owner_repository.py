from db.run_sql import run_sql
from models.owner import Owner

def save(owner):
    sql = 'INSERT INTO owners (name) VALUES (%s) RETURNING id'
    values = [owner.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    owner.id = id

def select_all():
    owners = []
    sql = 'SELECT * FROM owners'
    results = run_sql(sql)
    for result in results:
        owner = Owner(result['first_name'], result['last_name'], result['phone_num_1'], result['phone_num_2'], result['address'], result['id'])
        owners.append(owner)
    return owners

def select(id):
    sql = 'SELECT * FROM owners WHERE id = %s'
    values = [id]
    result = run_sql(sql, values)[0]
    owner = Owner(result['first_name'], result['last_name'], result['phone_num_1'], result['phone_num_2'], result['address'], result['id'])
    return owner

def delete_all():
    sql = 'DELETE FROM owners'
    run_sql(sql)

def delete(id):
    sql = 'DELETE FROM owners WHERE id = %s'
    values = [id]
    run_sql(sql, values)

def update(owner):
    sql = 'UPDATE owners SET name = %s WHERE id = %s'
    values = [owner.name, owner.id]
    run_sql(sql, values)                        