from flask import Blueprint, Flask, redirect, render_template, request

from models.owner import Owner
import repositories.owner_repository as owner_repository

owners_blueprint = Blueprint('owners', __name__)

# INDEX
@owners_blueprint.route('/owners', methods=['GET'])
def owners():
    owners = owner_repository.select_all()
    return render_template('owners/index.html', owners = owners)

# NEW / CREATE NEW OWNER
@owners_blueprint.route('/owners/new', methods=['GET'])
def new_owner():
    return render_template('owners/new.html')
    

# CREATE / POST NEW OWNER
@owners_blueprint.route('/owners', methods=['POST'])
def create_owner():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    phone_num_1 = request.form['phone_num_1']
    phone_num_2 = request.form['phone_num_2']
    address = request.form['address']
    owner = Owner(first_name, last_name, phone_num_1, phone_num_2, address, id)   # not sure here..
    owner_repository.save(owner)
    return redirect('/owners')

# EDIT - pull the form to make changes
@owners_blueprint.route('/owners/<id>/edit')
def edit_owner(id):
    owner = owner_repository.select(id)
    return render_template('owners/edit.html', owner=owner)

# UPDATE    
@owners_blueprint.route('/owners/<id>', methods=['POST'])
def update_owner(id):
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    phone_num_1 = request.form['phone_num_1']
    phone_num_2 = request.form['phone_num_2']
    address = request.form['address']
    owner = Owner(first_name, last_name, phone_num_1, phone_num_2, address, id)
    owner_repository.update(owner)
    return redirect('/owners')

# DELETE
@owners_blueprint.route('/owners/<id>/delete', methods=['POST'])
def delete_owner(id):
    owner_repository.delete(id)
    return redirect('/owners')    
