# Hospital Finder

Hospital Finder is a Django-based web application that helps users locate nearby hospitals based on their location and search criteria.

![image](static\images\homepage.png)
![image](static\images\aboutpage.png)

## Prerequisites

Ensure you have the following installed before proceeding:

- Python (>= 3.8)
- pip (Python package manager)
- virtualenv (recommended)
- PostgreSQL (if using a production database)

## Installation

1. **Clone the Repository**
   ```sh
   git clone https://github.com/therealyash/Emergency-Hospital-Finder/
   cd hospital-finder
   ```

2. **Create a Virtual Environment**
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```sh
   pip install -r requirements.txt
   ```

4. **Set Up Environment Variables**
   - Create a `.env` file in the root directory.

5. **Apply Migrations**
   ```sh
   python manage.py migrate
   ```

6. **Create a Superuser (Optional, for Admin Access)**
   ```sh
   python manage.py createsuperuser
   ```

7. **Run the Development Server**
   ```sh
   python manage.py runserver
   ```

The application will be accessible at `http://127.0.0.1:8000/`.

## Features

- Search for hospitals by name, location, or specialty.
- View detailed hospital profiles including services offered.
- User authentication and admin panel access.
- Google Maps API integration for location-based search.


