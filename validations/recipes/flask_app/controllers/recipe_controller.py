from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.user_model import User
from flask_app.models.recipe_model import Recipe


@app.route('/dashboard')
def dashboard():
    
    if not 'user_id' in session:
        flash('Please Login')
        return redirect('/')
    
    data = {
        'id' : session['user_id']
    }
    
    logged_in_user = User.get_one_by_id(data)
    recipes = Recipe.get_all()
    
    return render_template('recipes.html', recipes = recipes, user = logged_in_user)

# create new recipe

@app.route('/recipes/new')
def new_recipe():
    
    if not 'user_id' in session:
        flash('Please Login')
        return redirect('/')
    
    return render_template('add.html')

@app.route('/create_recipe', methods=['POST'])
def create_recipe():
    
    if not Recipe.validate_recipe(request.form):
        return redirect(request.referrer)
    
    data = {
        **request.form,
        'user_id' : session['user_id']
    }
    
    Recipe.save(data)
    
    return redirect('/dashboard')

# view one recipe

@app.route('/view/<int:recipe_id>')
def view(recipe_id):
    
    if not 'user_id' in session:
        flash('Please Login')
        return redirect('/')
    
    data = {
        'id' : recipe_id,
    }
    user_data = {
        'id' : session['user_id']
    }
    recipe = Recipe.view_recipe(data)
    user = User.get_one_by_id(user_data)
    
    return render_template('view.html', recipe = recipe, user = user)

# edit recipe

@app.route('/recipes/edit/<int:recipe_id>')
def edit(recipe_id):
    if not 'user_id' in session:
        flash('Please Login')
        return redirect('/')
    
    data = {
        'id' : recipe_id,
    }
    
    recipe = Recipe.get_one(data)
    
    if session['user_id'] != recipe.user_id:
        return redirect('/dashboard')
    
    return render_template('edit.html', recipe = recipe)

# save edits

@app.route('/save_recipe/<int:recipe_id>', methods=['POST'])
def save_recipe(recipe_id):
    
    if not Recipe.validate_recipe(request.form):
        return redirect(request.referrer)
    
    data = {
        **request.form,
        'id' : recipe_id
    }
    
    Recipe.update(data)
    
    return redirect('/dashboard')

# delete recipe

@app.route('/delete/<int:recipe_id>')
def delete(recipe_id):
    data = {
        **request.form,
        'id' : recipe_id
    }
    
    Recipe.delete_recipe(data)
    
    return redirect('/dashboard')