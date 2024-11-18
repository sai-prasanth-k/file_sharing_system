# Secure File Sharing System

This project implements a secure file-sharing system using Django. The system includes user authentication and allows operation users to upload files with specific formats.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Models](#models)
- [Contributing](#contributing)
- [License](#license)

## Installation

Follow these steps to set up the project:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/sai-prasanth-k/file_sharing_system.git
    cd file_sharing_system
    ```

2. **Install pipenv** (if not already installed):
    ```bash
    pip install pipenv
    ```

3. **Install dependencies**:
    ```bash
    pipenv install
    ```

4. **Start a new Django project**:
    ```bash
    pipenv run django-admin startproject secure_file_sharing .
    ```

5. **Create a new Django app**:
    ```bash
    pipenv run python manage.py startapp filesharing
    ```

6. **Configure the database** in `file_sharing_system/settings.py`:
    ```python
    DATABASES = {
        'default': {
            'ENGINE': 'djongo',
            'NAME': 'file_sharing_db',
        }
    }
    ```

7. **Apply migrations**:
    ```bash
    pipenv run python manage.py makemigrations
    pipenv run python manage.py migrate
    ```

## Usage

To run the development server:

```bash
pipenv run python manage.py runserver
