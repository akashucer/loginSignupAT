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
    # Calculate date ranges for someone at least 13 years old
    today = date.today()
    start_year = today.year - 80  # 80 years ago
    end_year = today.year - 13    # 13 years ago
    
    # Generate random month and day
    month = random.randint(1, 12)
    day = random.randint(1, 28)  # Using 28 to be safe for all months
    year = random.randint(start_year, end_year)
    
    # Create date object and format it
    dob = date(year, month, day)
    formatted_dob = dob.strftime("%m/%d/%Y")  # Ensures MM/DD/YYYY format
    
    # Generate a strong password
    password = fake.password(length=12, special_chars=True, digits=True, upper_case=True, lower_case=True)
    
    return {
        "First Name": fake.first_name(),
        "Last Name": fake.last_name(),
        "Email": fake.email(),
        "Phone No": generate_hex_phone(),
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
    }

# print(generate_user())