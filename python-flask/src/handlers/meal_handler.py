from flask import render_template


class MealHandler():
    @classmethod
    def list(cls):
        return render_template("static/about.html")
    
    @classmethod
    def new(cls):
        return render_template("static/about.html")
    
    @classmethod
    def create(cls, form):
        return render_template("static/about.html")
    
    @classmethod
    def get(cls, meal_id):
        return render_template("static/about.html")
    
    @classmethod
    def edit(cls, meal_id):
        return render_template("static/about.html")
    
    @classmethod
    def update(cls, meal_id, form):
        return render_template("static/about.html")
    
    @classmethod
    def delete(cls, meal_id):
        return render_template("static/about.html")
