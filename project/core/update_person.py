import os
import django
from datetime import datetime, time, timedelta

# Dynamically determine the project's settings module
settings_module = os.environ.get("DJANGO_SETTINGS_MODULE")
if not settings_module:
    raise RuntimeError("DJANGO_SETTINGS_MODULE environment variable is not set.")
django.setup()

import random
from core.models import Gente

def choose_and_update_person():
    # Get the current date
    today = datetime.now().date()

    # Check if the script has been executed today
    if os.path.exists('last_execution_date.txt'):
        # If the file exists, read the last execution date from it
        with open('last_execution_date.txt', 'r') as file:
            last_execution_date_str = file.read().strip()
            last_execution_date = datetime.strptime(last_execution_date_str, '%Y-%m-%d').date()
            # If the last execution date is today, return the last chosen person
            if last_execution_date == today:
                if os.path.exists('last_chosen_person.txt'):
                    with open('last_chosen_person.txt', 'r') as chosen_file:
                        chosen_person = chosen_file.read().strip()
                    return chosen_person
                else:
                    return None
    else:
        # If the file doesn't exist, create it and write today's date
        with open('last_execution_date.txt', 'w') as file:
            file.write(str(today))

    # Define the scheduled time for updating (e.g., 1:00 PM)
    scheduled_time = time(00, 0)  # 1:00 PM

    # Get the current time
    now = datetime.now().time()

    # Check if the current time is past the scheduled time
    if now >= scheduled_time:
        # Get all people from the Gente table
        people = Gente.objects.all()

        # Filter people whose last chosen date is older than 7 days
        threshold_date = today - timedelta(days=7)
        eligible_people = people.filter(lastChosen__lte=threshold_date)

        # Check if there are eligible people to choose from
        if eligible_people.exists():
            # Choose a random person from eligible ones
            random_person = random.choice(eligible_people)

            # Update the last chosen date for the chosen person
            random_person.lastChosen = today
            random_person.save()
            chosen_person_name = random_person.nombre
            
            # Save the last chosen person in a text file
            with open('last_chosen_person.txt', 'w') as chosen_file:
                chosen_file.write(chosen_person_name)

            # Update the last execution date in the file
            with open('last_execution_date.txt', 'w') as file:
                file.write(str(today))

            return chosen_person_name
        else:
            print("No eligible people found in the Gente table.")
    else:
        print("It's not yet time for updating.")

if __name__ == "__main__":
    chosen_person = choose_and_update_person()
    if chosen_person:
        print(f"Randomly chosen person: {chosen_person}. Last chosen date updated to today.")
    else:
        print("Script already executed today.")
