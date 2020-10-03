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



            # self, name, dob, type, owner, id = None):