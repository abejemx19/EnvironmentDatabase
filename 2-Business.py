from faker import Faker
fake = Faker()

num_rows = 5 # specify the number of rows you want to generate

for i in range(num_rows):
    business_id = i + 1
    name = fake.company()
    industry_type = fake.job()
    location = fake.city()

    sql_statement = f"INSERT INTO Businesses (business_id, name, industry_type, location) VALUES ({business_id}, '{name}', '{industry_type}', '{location}');"

    print(sql_statement)