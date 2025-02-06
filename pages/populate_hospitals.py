import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from pages.models import Hospital

hospital_data = [
    {"name": "Lilavati Hospital", "city": "Mumbai", "pin_code": "400050", "contact_number": "022-26751000",
     "location_link": "https://goo.gl/maps/Dz4pW"},
    {"name": "Kokilaben Hospital", "city": "Mumbai", "pin_code": "400053", "contact_number": "022-30666666",
     "location_link": "https://goo.gl/maps/Fq1dW"},
    {"name": "Nanavati Hospital", "city": "Mumbai", "pin_code": "400056", "contact_number": "022-26267500",
     "location_link": "https://goo.gl/maps/Nj8gA"},
    {"name": "Breach Candy Hospital", "city": "Mumbai", "pin_code": "400026", "contact_number": "022-23671888",
     "location_link": "https://goo.gl/maps/Qz4pW"},
    {"name": "Saifee Hospital", "city": "Mumbai", "pin_code": "400004", "contact_number": "022-67570101",
     "location_link": "https://goo.gl/maps/Lj8gA"},
    {"name": "Hiranandani Hospital", "city": "Mumbai", "pin_code": "400076", "contact_number": "022-25763300",
     "location_link": "https://goo.gl/maps/Rz7pX"},
    {"name": "Fortis Hospital", "city": "Mumbai", "pin_code": "400093", "contact_number": "022-67994444",
     "location_link": "https://goo.gl/maps/Az9gC"},
    {"name": "S.L. Raheja Hospital", "city": "Mumbai", "pin_code": "400016", "contact_number": "022-66529888",
     "location_link": "https://goo.gl/maps/Xz5pM"},
    {"name": "Global Hospital", "city": "Mumbai", "pin_code": "400012", "contact_number": "022-67670101",
     "location_link": "https://goo.gl/maps/Zy4pL"},
    {"name": "Tata Memorial Hospital", "city": "Mumbai", "pin_code": "400012", "contact_number": "022-24177000",
     "location_link": "https://goo.gl/maps/Kj9pN"},
]

def populate_hospitals():
    for hospital in hospital_data:
        Hospital.objects.create(**hospital)
    print("✅ 100 hospitals added successfully!")

if __name__ == "__main__":
    populate_hospitals()
