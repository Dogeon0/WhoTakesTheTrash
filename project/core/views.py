from datetime import datetime, timedelta
from django.shortcuts import render, redirect
from . import models, forms
from .update_person import assign_dates  # Import the function from your script

def home(request):
    if request.method == "POST":
        form = forms.AgregarMensaje(request.POST)
        if form.is_valid():
            form.save()
            return redirect("core:home")
        else:
            print(form.errors)
    else:
        form = forms.AgregarMensaje()

    # Assign dates if not already assigned or if the cycle is complete
    today = datetime.now().date()
    if not models.Gente.objects.filter(assignedDate__gte=today).exists():
        assign_dates()

    # Fetch people with their assigned dates
    gente_objects = models.Gente.objects.all().order_by('assignedDate')
    mensajes = models.Mensaje.objects.all().order_by('-id')[:3][::1]
    
    context = {
        "gentes": gente_objects,
        "form": form,
        "mensajes": mensajes
    }

    return render(request, "index.html", context)
