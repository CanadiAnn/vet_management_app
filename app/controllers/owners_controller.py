from flask import Blueprint, Flask, redirect, render_template, request

from models.owner import Owner
import repositories.owner_repository as owner_repository

owners_blueprint = Blueprint('owners', __name__)

# INDEX
@owners_blueprint.route('/owners')
def owners():
    owners = owner_repository.select_all()
    return render_template('owners/index.html', owners = owners)

# NEW
@owners_blueprint.route('/owners/new')
def new_owner():
    return render_template('owners/new.html')

# CREATE
@owners_blueprint.route('/owners', methods=['POST'])
def create_owner():
    first_name = request.form['first name']
    last_name = request.form['last name']
    new_owner = owner(first_name, last_name, phone_num_1, phone_num_2, address, id)   # not sure here..
    owner_repository.save(new_owner)
    return redirect('/owners')

# EDIT
@owners_blueprint.route('/owners/<id>/edit')
def edit_owner(id):
    owner = owner_repository.select(id)
    return render_template('owners/edit.html')

# UPDATE    
@owners_blueprint.route('/owners/<id>', methods=['POST'])
def update_owner(id):
    first_name = request.form['first name']
    last_name = request.form['last name']
    owner = owner(first_name, last_name, id)  # not sure here
    owner_repository.update(owner)
    return redirect('/owners')

# DELETE
@owners_blueprint.route('/owners/<id>/delete', methods=['POST'])
def delete_human(id):
    owner_repository.delete(id)
    return redirect('/owners')    
