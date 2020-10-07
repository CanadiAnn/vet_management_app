from flask import Blueprint, Flask, redirect, render_template, request

from models.vet import Vet
import repositories.vet_repository as vet_repository

vets_blueprint = Blueprint('vets', __name__)

# INDEX
@vets_blueprint.route('/vets', methods=['GET'])
def vets():
    vets = vet_repository.select_all()
    return render_template('vets/index.html', vets = vets)


# NEW / CREATE NEW VET
@vets_blueprint.route('/vets/new', methods=['GET'])
def new_vet():
    return render_template('vets/new.html')


# CREATE / POST NEW VET
@vets_blueprint.route('/vets', methods=['POST'])
def create_vet():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    license = request.form['license']
    vet = Vet(first_name, last_name, license)
    vet_repository.save(vet)
    return redirect('/vets')


# EDIT - pull the form to make a change
@vets_blueprint.route('/vets/<id>/edit', methods=['GET']) #works with a POST WTF?
def edit_vet(id):
    vet = vet_repository.select(id)
    return render_template('vets/edit.html', vet=vet)

# UPDATE - post changes to the db    
@vets_blueprint.route('/vets/<id>', methods=['POST'])
def update_vet(id):
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    license = request.form ['license']
    vet = Vet(first_name, last_name, license, id)
    vet_repository.update(vet)
    return redirect('/vets')

# DELETE
@vets_blueprint.route('/vets/<id>/delete', methods=['POST'])
def delete_vet(id):
    vet_repository.delete(id)
    return redirect('/vets')    
