from faker import Faker
fake = Faker()

num_rows = 5 # specify the number of rows you want to generate

for i in range(num_rows):
    calculation_id = i + 1
    user_business_id = fake.random_int(min=1, max=10)
    carbon_footprint = round(fake.random.uniform(0.0, 100.0), 2)
    date = str(fake.date_between(start_date='-1y', end_date='today'))

    sql_statement = f"INSERT INTO Carbon_Footprint_Calculations (calculation_id, user_business_id, carbon_footprint, date) VALUES ({calculation_id}, {user_business_id}, {carbon_footprint}, '{date}');"

    print(sql_statement)