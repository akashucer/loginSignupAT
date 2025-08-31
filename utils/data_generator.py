from faker import Faker
from datetime import datetime, date
import random

fake = Faker()

def generate_hex_phone():
    # Generate phone number in format "6B9C04F490"
    hex_chars = '0123456789'  # Using full hexadecimal characters
    phone = '6'  # Start with 6
    phone += ''.join(random.choice(hex_chars) for _ in range(9))  # 9 more characters to make it 10 total
    return phone

def generate_user():
    # Generate a date for a person between 13 and 80 years old.
    today = date.today()
    start_date = today.replace(year=today.year - 80)
    end_date = today.replace(year=today.year - 13)
    dob = fake.date_between_dates(date_start=start_date, date_end=end_date)
    
    # Format date as YYYY-MM-DD for the date input field
    formatted_dob = dob.strftime("%Y-%m-%d")
    
    # Generate a strong password
    password = fake.password(length=12, special_chars=True, digits=True, upper_case=True, lower_case=True)
    
    return {
        "First Name": fake.first_name(),
        "Last Name": fake.last_name(),
        "Email": fake.email(),
                "Phone No": fake.numerify(text='##########'),
        "DOB": formatted_dob,
        "Street Address": fake.street_address(),
        "City": fake.city(),
        "State": fake.state(),
        "Zip Code": fake.zipcode(),
        "Country": "United States",
        "Occupation": fake.job(),
        "Password": password,
        "Confirm Password": password,  # Same as password field
        "Gender": "male"  # Fixed value for male gender
    }# print(generate_user())