"""Flask app for adopt app."""

from flask import Flask, render_template, redirect, request, flash

from flask_debugtoolbar import DebugToolbarExtension

from models import db, connect_db, Pet

from forms import AddPetForm

app = Flask(__name__)

app.config['SECRET_KEY'] = "secret"

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql:///adopt"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


toolbar = DebugToolbarExtension(app)
connect_db(app)
db.create_all()

# Having the Debug Toolbar show redirects explicitly is often useful;
# however, if you want to turn it off, you can uncomment this line:
#
# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False


@app.get('/')
def home_page():
    """go to the home page"""
    pets = Pet.query.all()

    return render_template('index.html', pets=pets)

# @app.get('/add')
# def show_add_pet():
#     """go to the show add pet form"""

#     return render_template('add_pet_form.html')

@app.route("/add", methods=["GET", "POST"])
def add_pet():
    """Pet add form; handle adding."""

    form = AddPetForm()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data

        # do stuff with data/insert to db

        pet = Pet(
            name=name,
            species=species,
            photo_url=photo_url,
            age=age,
            notes=notes
            )

        db.session.add(pet)
        db.session.commit()

        flash(f"Added {name}")
        return redirect("/")

    else:
        return render_template(
            "add_pet_form.html", form=form)


@app.route("/<int:id>", methods=["GET", "POST"])
def edit_pet(id):
    """Pet edit form; handle editing."""

    pet = Pet.query.get_or_404(id)
    form = AddPetForm(obj=pet) #populates form

    if form.validate_on_submit():
        # gets data from form, and validates
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data

        db.session.commit()

        flash(f"Edited {pet.name}")
        return redirect("/")

    else:
        return render_template(
            "edit_pet_form.html", pet=pet, form=form)
