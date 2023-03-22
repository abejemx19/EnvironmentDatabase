from faker import Faker
fake = Faker()

num_rows = 5 # specify the number of rows you want to generate

for i in range(num_rows):
    waste_id = i + 1
    user_business_id = fake.random_int(min=1, max=10)
    waste_type = fake.random_element(elements=('Organic', 'Plastic', 'Paper', 'Metal', 'Glass'))
    amount = round(fake.random.uniform(0.0, 1000.0), 2)
    date = str(fake.date_between(start_date='-1y', end_date='today'))

    sql_statement = f"INSERT INTO Waste_Production (waste_id, user_business_id, waste_type, amount, date) VALUES ({waste_id}, {user_business_id}, '{waste_type}', {amount}, '{date}');"

    print(sql_statement)