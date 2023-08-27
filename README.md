# audio-uploader-dashboard

  - Audio Dashboard is a web application that provides users with a user-friendly interface to upload, manage, and play audio files.
  - It leverages a Django backend to handle user interactions, store audio file metadata, and calculate the total duration of uploaded audio files.
  - The application is designed to be easy to set up and use.

# Features
  - Upload single or multiple audio files with varying extensions.
  - Display uploaded files in a tabular form, including metadata such as upload date, size, and extension.
  - Play uploaded audio files directly from the dashboard.
  - Generate a warning if the total duration of uploaded files exceeds 10 minutes.

# Prerequisites
  - Before you begin, ensure you have met the following requirements:
    - Python (3.7+)
    - Django (4.0+)
    - MySQL Server
    - PyDub (required for audio file manipulation)
    - Install FFmpeg (Required for Audio Manipulation)

# Installation

  1. Clone the repository:
    - git clone https://github.com/your-username/audio-dashboard.git

  2. Install the required packages:

    - pip install -r requirements.txt
    
  3. Configure the database in settings.py:
    Update the DATABASES section with your database settings.

  4. Run database migrations:
    - python manage.py migrate

# Install MySQL
  - Download and install MySQL from the official website: MySQL Community Downloads.
  - During installation, remember the root password you set for the MySQL server.

# Configure Database

  1. Update the database settings in settings.py:
    Open AudioDashboard/settings.py and locate the DATABASES section.
    Replace 'your_database_name', 'your_mysql_username', and 'your_mysql_password' with your MySQL database information:

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'your_database_name',
            'USER': 'your_mysql_username',
            'PASSWORD': 'your_mysql_password',
            'HOST': 'localhost',  # Or your MySQL server host
            'PORT': '3306',       # Or your MySQL port
        }
    }

  2. Run database migrations:
     Run the following command to apply the database migrations:
      python manage.py migrate

# Run the Application

  1. Start the development server:
     Run the following command to start the development server:

      python manage.py runserver

  2. Access the dashboard:
     Open your web browser and navigate to http://localhost:8000/dashboard/.

  3. Use the application:
    - Use the "Choose Files" button to upload audio files.
    - Uploaded files will be listed with metadata and an option to play them.
    - A warning will appear if the total duration of uploaded files exceeds 10 minutes.
     









