from faker import Faker
fake = Faker()

num_rows = 5 # specify the number of rows you want to generate

for i in range(num_rows):
    user_id = i + 1
    name = fake.name()
    email = fake.email()
    location = fake.city()

    sql_statement = f"INSERT INTO Users (user_id, name, email, location) VALUES ({user_id}, '{name}', '{email}', '{location}');"

    print(sql_statement)