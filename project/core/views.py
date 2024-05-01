from django.shortcuts import render, redirect
from . import models, forms
from .update_person import choose_and_update_person  # Import the function from your script

def home(request):
    if request.method == "POST":
        form = forms.AgregarMensaje(request.POST)
        if form.is_valid():
            form.save()
            return redirect("core:home")
        else:
            print(form.errors)
    else:
        form = forms.MostrarMensajes()

    
    random_person_nombre = choose_and_update_person()
    gente_objects = models.Gente.objects.all()
    mensajes = models.Mensaje.objects.all().order_by('-id')[:3][::1]
    context = {
        "gentes": gente_objects, 
        "random_person_nombre": random_person_nombre,
        "form": form,
        "mensajes":mensajes}
    return render(request, "index.html", context)

