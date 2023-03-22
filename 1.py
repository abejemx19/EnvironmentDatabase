from faker import Faker
fake = Faker()

num_rows = 5 # specify the number of rows you want to generate

for i in range(num_rows):
    user_id = i + 1
    name = fake.name()
    email = fake.email()
    location = fake.city()
    occupation = fake.job()
    date_of_birth = str(fake.date_of_birth())
    phone_number = fake.phone_number()
    gender = fake.simple_profile()['sex']
    password = 'password123'

    sql_statement = f"INSERT INTO Users (user_id, name, email, location, occupation, date_of_birth, phone_number, gender, password) VALUES ({user_id}, '{name}', '{email}', '{location}', '{occupation}', '{date_of_birth}', '{phone_number}', '{gender}', '{password}');"

    print(sql_statement)