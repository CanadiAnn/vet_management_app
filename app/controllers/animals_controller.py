from flask import Blueprint, Flask, redirect, render_template, request

from models.animal import Animal

import repositories.animal_repository as animal_repository
import repositories.owner_repository as owner_repository
import repositories.vet_repository as vet_repository

animals_blueprint = Blueprint('animals', __name__)

# INDEX
@animals_blueprint.route('/animals', methods=['GET'])
def animals():
    animals = animal_repository.select_all()
    return render_template('animals/index.html', animals = animals)

# NEW / CREATE NEW ANIMAL
@animals_blueprint.route('/animals/new', methods=['GET'])
def new_animal():
    owners = owner_repository.select_all()
    vets = vet_repository.select_all()
    return render_template('animals/new.html', all_owners = owners, all_vets = vets)
    
    
# CREATE - POST NEW ANIMAL
@animals_blueprint.route('/animals', methods=['POST'])
def create_animal():
    name = request.form['name']
    dob = request.form['dob']
    type = request.form['type']
    owner_id = request.form['owner_id']
    vet_id = request.form['vet_id']
    owner = owner_repository.select(owner_id)
    vet = vet_repository.select(vet_id)
    animal = Animal(name, dob, type, owner, vet)
    animal_repository.save(animal)
    return redirect('/animals')


# EDIT - pull the form to make changes
@animals_blueprint.route('/animals/<id>/edit', methods=['GET'])
def edit_animal(id):
    animal = animal_repository.select(id)
    owners = owner_repository.select_all()
    vets = vet_repository.select_all()
    return render_template('animals/edit.html', animal=animal, all_owners = owners, all_vets = vets)

# UPDATE - post the changes to the db /animals/<id>
# @animals_blueprint.route('/animals/<id>', methods=['POST'])
# def update_animal(id):
#   get the data from the form
#   create an instance of the animal class - using the form data
#   ALSO using the id from the url
#   run and update on the database using the update method in the repository passing in the instance of the animal class
#   redirect to all animals

@animals_blueprint.route('/animals/<id>', methods=['POST'])
def update_animal(id):
    name = request.form['name']
    dob = request.form['dob']
    type = request.form['type']
    owner_id = request.form['owner_id']
    vet_id = request.form['vet_id']
    treatment_notes = request.form['treatment_notes']
    owner = owner_repository.select(owner_id)
    vet = vet_repository.select(vet_id)
    animal = Animal(name, dob, type, owner, vet, id, treatment_notes)
    animal_repository.update(animal)
    return redirect('/animals')

# DELETE
@animals_blueprint.route('/animals/<id>/delete', methods=['POST'])
def delete_animal(id):
    animal_repository.delete(id)
    return redirect('/animals')    
