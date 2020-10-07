from db.run_sql import run_sql
from models.owner import Owner

def save(owner):
    sql = 'INSERT INTO owners (first_name, last_name, phone_num_1, phone_num_2, address) VALUES (%s, %s, %s, %s, %s) RETURNING id'
    values = [owner.first_name, owner.last_name, owner.phone_num_1, owner.phone_num_2, owner.address]
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
    sql = 'UPDATE owners SET (first_name, last_name, phone_num_1, phone_num_2, address) = (%s, %s, %s, %s, %s) WHERE id = %s'
    values = [owner.first_name, owner.last_name, owner.phone_num_1, owner.phone_num_2, owner.address, owner.id]
    run_sql(sql, values)                        