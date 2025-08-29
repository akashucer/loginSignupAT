from faker import Faker

fake = Faker()

def generate_user():
    return {
        "First Name": fake.first_name(),
        "Last Name": fake.last_name(),
        "Email" : fake.email(),
        "Phone No" : fake.phone_number(),
        "DOB" : fake.date_of_birth(),
        "Street Address": fake.street_address(),
        "City" : fake.city(),
        "State" : fake.state(),
        "Zip Code" : fake.zipcode(),
        "Occupation" : fake.job(),
        "Password": fake.password()
    }

# print(generate_user())