from flask import Blueprint, Flask, redirect, render_template, request

from models.animal import Animal

import repositories.animal_repository as animal_repository
import repositories.owner_repository as owner_repository
import repositories.vet_repository as vet_repository

animals_blueprint = Blueprint('animals', __name__)

# INDEX
@animals_blueprint.route('/animals')
def animals():
    animals = animal_repository.select_all()
    return render_template('animals/index.html', animals = animals)

# NEW / CREATE NEW ANIMAL
@animals_blueprint.route('/animals/new', methods=['GET'])
def new_animal():
    owners = owner_repository.select_all()
    vets = vet_repository.select_all()
    return render_template('animals/new.html', all_owners = owners, all_vets = vets)
    
    
# CREATE - POST
@animals_blueprint.route('/animals', methods=['POST'])
def create_animal():
    name = request.form['name']
    dob = request.form['dob']
    type = request.form['type']
    owner_id = request.form['owner_id']
    vet_id = reqiest.form['vet_id']
    animal = Animal(name, dob, type, owner_id, vet_id)
    animal_repository.save(animal)
    return redirect('/animals')


# EDIT
@animals_blueprint.route('/animals/<id>/edit', methods=['GET'])
def edit_animal(id):
    animal = animal_repository.select(id)
    owners = owner_repository.select_all()
    vets = vet_repository.select_all()
    return render_template('animals/edit.html', animal=animal, all_owners = owners, all_vets = vets)

# UPDATE -- ADD TREATMENT NOTES 
@animals_blueprint.route('/animals/<id>/update', methods=['GET'])
def update_animal(id):
    animal = animal_repository.select(id)
    owner = owner_repository.select(id)
    vet = vet_repository.select(id)
    animal_repository.update(animal)
    return render_template('/animals/update.html', animal=animal, owner=owner, vet=vet)

# DELETE
@animals_blueprint.route('/animals/<id>/delete', methods=['POST'])
def delete_human(id):
    animal_repository.delete(id)
    return redirect('/animals')    
