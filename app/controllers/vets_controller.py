from flask import Blueprint, Flask, redirect, render_template, request

from models.vet import Vet
import repositories.vet_repository as vet_repository

vets_blueprint = Blueprint('vets', __name__)

# INDEX
@vets_blueprint.route('/vets')
def vets():
    vets = vet_repository.select_all()
    return render_template('vets/index.html', vets = vets)

# NEW
@vets_blueprint.route('/vets/new')
def new_vet():
    return render_template('vets/new.html')

# CREATE
@vets_blueprint.route('/vets', methods=['POST'])
def create_vet():
    first_name = request.form['first name']
    last_name = request.form['last name']
    license = request.form ['license']
    new_vet = vet(first_name, last_name, license, id)   # not sure here..
    vet_repository.save(new_vet)
    return redirect('/vets')

# EDIT
@vets_blueprint.route('/vets/<id>/edit')
def edit_vet(id):
    vet = vet_repository.select(id)
    return render_template('vets/edit.html')

# UPDATE    
@vets_blueprint.route('/vets/<id>', methods=['POST'])
def update_vet(id):
    first_name = request.form['first name']
    last_name = request.form['last name']
    license = request.form ['license']
    vet = vet(first_name, last_name, license, id)  # not sure here
    vet_repository.update(vet)
    return redirect('/vets')

# DELETE
@vets_blueprint.route('/vets/<id>/delete', methods=['POST'])
def delete_human(id):
    vet_repository.delete(id)
    return redirect('/vets')    
