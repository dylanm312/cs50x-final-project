# Vehicle Maintenance Tracker

This repository contains my final project for the Harvard CS50x course. The project is a Vehicle Maintenance Tracker designed to help individuals or corporations manage the maintenance schedules of their vehicles. The application is written in Python using Django and Bootstrap.

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Screenshots](#screenshots)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

The Vehicle Maintenance Tracker is a tool designed to keep track of maintenance tasks for personal or corporate vehicles. It allows users to log maintenance activities, set reminders for upcoming services, and view the history of services performed on each vehicle.

## Features

- **Add Vehicles**: Users can add multiple vehicles to the tracker.
- **Log Maintenance**: Record details of maintenance activities performed.
- **Set Reminders**: Schedule reminders for future maintenance tasks.
- **View History**: Access a log of all maintenance activities for each vehicle.
- **User Authentication**: Secure user login to protect data.

## Installation

### Prerequisites

- Python 3.x
- Django 5.x or later

### Clone the Repository

```bash
git clone https://github.com/yourusername/vehicle-maintenance-tracker.git
cd vehicle-maintenance-tracker
```

### Setup Python Environment

1. Create a virtual environment:

    ```bash
    python3 -m venv .venv
    ```

2. Activate the virtual environment:

    ```bash
    source .venv/bin/activate
    ```

3. Install required Python packages:

    ```bash
    pip3 install -r requirements.txt
    ```

### Apply Migrations

Apply database migrations:

```bash
python manage.py migrate
```

### Create a Superuser

Create a superuser to access the Django admin interface:

```bash
python manage.py createsuperuser
```

## Usage

1. Start the Django development server:

    ```bash
    python manage.py runserver
    ```

2. Open your web browser and navigate to `http://localhost:8000/`.

3. Log in using the superuser credentials to access the admin interface and start adding vehicles and logging maintenance activities.

[comment]: ## Screenshots

[comment]: ![Dashboard](screenshots/dashboard.png)
[comment]: *Dashboard showing an overview of vehicles and upcoming maintenance tasks.*

[comment]: ![Log Maintenance](screenshots/log_maintenance.png)
[comment]: *Interface for logging maintenance activities.*

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch:

    ```bash
    git checkout -b feature-branch
    ```

3. Make your changes.
4. Commit your changes:

    ```bash
    git commit -m "Description of changes"
    ```

5. Push to the branch:

    ```bash
    git push origin feature-branch
    ```

6. Open a Pull Request.

## License

This project is licensed under the GNU GPLv3 License. See the [LICENSE](LICENSE) file for details.

---

Thank you for checking out the Vehicle Maintenance Tracker! If you have any questions or need further assistance, feel free to open an issue in the repository.