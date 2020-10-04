from flask import Blueprint, Flask, redirect, render_template, request

from models.animal import Animal
import repositories.animal_repository as animal_repository

animals_blueprint = Blueprint('animals', __name__)

# INDEX
@animals_blueprint.route('/animals')
def animals():
    animals = animal_repository.select_all()
    return render_template('animals/index.html', animals = animals)

# NEW
@animals_blueprint.route('/animals/new')
def new_animal():
    return render_template('animals/new.html')

# CREATE
@animals_blueprint.route('/animals', methods=['POST'])
def create_animal():
    name = request.form['name']
    dob = request.form['dob']
    type = request.form ['type']
    new_animal = Animal(name, dob, type)   # not sure here..
    animal_repository.save(new_animal)
    return redirect('/animals')

# EDIT
@animals_blueprint.route('/animals/<id>/edit')
def edit_animal(id):
    animal = animal_repository.select(id)
    return render_template('animals/edit.html')

# UPDATE    
@animals_blueprint.route('/animals/<id>', methods=['POST'])
def update_animal(id):
    name = request.form['name']
    dob = request.form['dob']
    type = request.form ['type']
    animal = Animal(name, dob, type, id)  # not sure here
    animal_repository.update(animal)
    return redirect('/animals')

# DELETE
@animals_blueprint.route('/animals/<id>/delete', methods=['POST'])
def delete_human(id):
    animal_repository.delete(id)
    return redirect('/animals')    
