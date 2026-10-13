# Travel Management System

A desktop application for managing travel offers, developed in Python using Tkinter, MySQL, and the Model-View-Controller (MVC) architecture.

## Overview

This project was developed as part of a Human-Computer Interaction (HCI/IHM) exercise. It provides a graphical interface for managing travel information stored in a MySQL database.

## Features

- Add new travel offers.
- Display available travel offers in a table.
- Search for trips by destination.
- View detailed information about a selected trip.
- Validate user input for dates, prices, and available seats.
- Display a slideshow of travel images.
- Store travel information in a MySQL database.
- Organize the application using the MVC architecture.

## Technologies

- Python
- Tkinter and ttk
- MySQL
- `mysql-connector-python`
- Pillow (PIL)

## Project Structure

```text
travel-management-system/
├── main.py
├── model.py
├── view.py
├── controller.py
├── images/
├── requirements.txt
├── .gitignore
└── README.md
```

## Prerequisites

- Python 3
- MySQL Server
- A MySQL database named `voyage`

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/YOUR-USERNAME/travel-management-system.git
   ```

2. Navigate to the project directory:

   ```bash
   cd travel-management-system
   ```

3. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Create the MySQL database:

   ```sql
   CREATE DATABASE voyage;
   ```

5. Configure the database connection in `model.py` according to your local MySQL settings.

6. Run the application:

   ```bash
   python main.py
   ```

## Database

The application creates a `consultations` table to store travel offers, including:

- Destination
- Departure date
- Return date
- Price
- Available seats
- Description

## Architecture

The application follows the Model-View-Controller (MVC) pattern:

- **Model:** manages the MySQL connection and database operations.
- **View:** implements the graphical interface with Tkinter.
- **Controller:** connects user actions to the model and updates the view.

## Project Status

Academic project developed as part of an IHM exercise.

## Author

Dalia Graiche
