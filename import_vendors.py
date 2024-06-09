import os
import sys
import django
import csv

sys.path.append(r'C:\Users\user\Desktop\Office\dummy vend')
os.environ['DJANGO_SETTINGS_MODULE'] = 'ven.settings'
django.setup()


from django.contrib.auth import get_user_model
from vendors.models import Category, Vendor

User = get_user_model()


# CSV file path
csv_file = r'C:\Users\user\Office\clean_business_data.csv'

# Open the CSV file and read data
with open(csv_file, 'r', newline='', encoding='utf-8') as file:
    csv_reader = csv.DictReader(file)

    for row in csv_reader:
        sub_category = row['Subcategory']
        company_name = row['Name']
        mobile_number = row['Mobile Numbers']
        website = row['Website']
        location = row['Location']
        map = row['Map Coordinates'].split(',')
        latitude = map[0]
        longitude = map[-1]
        print(latitude, longitude)

        try:
            sub_category_obj = Category.objects.get(category_name = sub_category)
        except:
            print('subcategory not found. Skipping!', sub_category)
            continue
        
        user, created = User.objects.get_or_create(phone_number=mobile_number)
        
        if created:
            print(f"User with phone number {mobile_number} created.")
        else:
            print(f"User with phone number {mobile_number} already exists.")

        vendor, created = Vendor.objects.get_or_create(company_name=company_name, category=sub_category_obj, contact_number=mobile_number, user=user, website=website, location=location, latitude=latitude, longitude=longitude)
        
        if created:
            print(f"vendor with phone number {mobile_number} created.")
        else:
            print(f"vendor with phone number {mobile_number} already exists.")

        # break  # Remove this break to process all rows