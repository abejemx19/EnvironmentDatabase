from faker import Faker
fake = Faker()

num_rows = 5 # specify the number of rows you want to generate

for i in range(num_rows):
    goal_id = i + 1
    business_id = fake.random_int(min=1, max=10)
    goal_type = fake.random_element(elements=('Reduce Carbon Footprint', 'Increase Renewable Energy Usage', 'Reduce Waste Production', 'Increase Recycling Efforts', 'Reduce Water Consumption'))
    target_value = round(fake.random.uniform(0.0, 100.0), 2)
    target_date = str(fake.date_between(start_date='today', end_date='+5y'))

    sql_statement = f"INSERT INTO Sustainability_Goals (goal_id, business_id, goal_type, target_value, target_date) VALUES ({goal_id}, {business_id}, '{goal_type}', {target_value}, '{target_date}');"

    print(sql_statement)