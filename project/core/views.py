from django.shortcuts import render
from . import models
from .update_person import choose_and_update_person  # Import the function from your script

def home(request):

    random_person_nombre = choose_and_update_person()
    
    # Retrieve all people from the Gente table
    gente_objects = models.Gente.objects.all()
    
    # Pass the list of people and the randomly chosen person's name (if any) to the template context
    context = {"gentes": gente_objects, "random_person_nombre": random_person_nombre}
    
    # Render the index.html template with the context
    return render(request, "index.html", context)

