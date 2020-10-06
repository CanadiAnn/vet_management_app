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

# NEW
@animals_blueprint.route('/animals/new', methods=['GET'])
def new_animal():
    owners = owner_repository.select_all()
    vets = vet_repository.select_all()
    return render_template('animals/new.html', all_owners = owners, all_vets = vets)

# CREATE
@animals_blueprint.route('/animals', methods=['POST'])
def create_animal():
    name = request.form['name']
    dob = request.form['dob']
    type = request.form ['type']
    owners = owner_repository.select_all()
    vets = vet_repository.select_all()
    new_animal = Animal(name, dob, type)   # not sure here..
    animal_repository.save(new_animal)
    return redirect('/animals')

# EDIT
@animals_blueprint.route('/animals/<id>/edit')
def edit_animal(id):
    animal = animal_repository.select_all()
    # owner = owner_repository.select(id)
    # vet = vet_repository.select(id)
    return render_template('animals/edit.html')

# UPDATE -- ADD TREATMENT NOTES 
# @animals_blueprint.route('/animals/<id>/update')
# def update_animal(id):
    # name = request.form['name']
    # dob = request.form['dob']
    # type = request.form ['type']
    # animal = Animal(name, dob, type, id)  # not sure here
    # animal_repository.update(animal)
    # return redirect('/animals')

# DELETE
@animals_blueprint.route('/animals/<id>/delete', methods=['POST'])
def delete_human(id):
    animal_repository.delete(id)
    return redirect('/animals')    
