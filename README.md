# WhoTakesTheTrash

A Django web application to manage and display the rotation schedule for taking out the trash in a student household. The app dynamically adjusts the list of names and dates based on the current residents.

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Models](#models)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Project Overview

"WhoTakesTheTrash" is a simple web app designed to help student households keep track of whose turn it is to take out the trash. The app displays a schedule with names and dates, allowing users to easily manage the rotation. Users can add or remove residents, ensuring the schedule remains up-to-date.

## Features

- **Dynamic Schedule Management**: Easily add or remove residents to keep the schedule accurate.
- **Simple Interface**: A straightforward display of names and dates.
- **Data Persistence**: Information is stored and managed using Django's ORM.

## Technologies Used

- **Backend**: Django
- **Frontend**: HTML/CSS (add any additional frontend technologies you use)
- **Database**: SQLite (or any other database you are using)


## Installation

To set up and run the project locally, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/WhoTakesTheTrash.git
   cd WhoTakesTheTrash
   ```

2. **Create a virtual environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up the database**:
   ```bash
   python manage.py migrate
   ```

5. **Run the server**:
   ```bash
   python manage.py runserver
   ```

6. **Access the app**:
   Open your web browser and go to `http://localhost:8000`.

## Usage

Once the server is running, the web app will display the current trash rotation schedule. Users can:

- **View the schedule**: See whose turn it is to take out the trash.
- **Add a resident**: Add a new person to the "gente" list.
- **Remove a resident**: Remove someone who has moved out.


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For any questions or suggestions, feel free to reach out:

- **Santiago Enciso**: mailencisosantiago@gmail.com
- **GitHub**: [Link](github.com/Dogeon0)
