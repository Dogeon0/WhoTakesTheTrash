import os
import django
from datetime import datetime, timedelta

# Dynamically determine the project's settings module
settings_module = os.environ.get("DJANGO_SETTINGS_MODULE")
if not settings_module:
    raise RuntimeError("DJANGO_SETTINGS_MODULE environment variable is not set.")
django.setup()

from core.models import Gente

def assign_dates():
    # Get the current date
    today = datetime.now().date()

    # Fetch all people from the Gente table
    people = Gente.objects.all()

    # Loop through each person and assign dates sequentially
    for index, person in enumerate(people):
        assigned_date = today + timedelta(days=index)
        person.assignedDate = assigned_date
        person.save()

    return people
