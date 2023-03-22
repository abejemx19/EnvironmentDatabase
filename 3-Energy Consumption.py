from faker import Faker
fake = Faker()

num_rows = 5 # specify the number of rows you want to generate

for i in range(num_rows):
    consumption_id = i + 1
    user_business_id = fake.random_int(min=1, max=10)
    energy_type = fake.random_element(elements=('Electricity', 'Gas', 'Water'))
    usage_amount = round(fake.random.uniform(0.0, 1000.0), 2)
    date = str(fake.date_between(start_date='-1y', end_date='today'))

    sql_statement = f"INSERT INTO Energy_Consumption (consumption_id, user_business_id, energy_type, usage_amount, date) VALUES ({consumption_id}, {user_business_id}, '{energy_type}', {usage_amount}, '{date}');"

    print(sql_statement)