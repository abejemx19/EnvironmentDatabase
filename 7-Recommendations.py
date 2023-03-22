from faker import Faker
fake = Faker()

num_rows = 5 # specify the number of rows you want to generate

for i in range(num_rows):
    recommendation_id = i + 1
    user_business_id = fake.random_int(min=1, max=10)
    recommendation_type = fake.random_element(elements=('Reduce Energy Consumption', 'Switch to Renewable Energy', 'Reduce Waste Production', 'Increase Recycling Efforts', 'Use Public Transportation'))
    date = str(fake.date_between(start_date='-1y', end_date='today'))

    sql_statement = f"INSERT INTO Recommendations (recommendation_id, user_business_id, recommendation_type, date) VALUES ({recommendation_id}, {user_business_id}, '{recommendation_type}', '{date}');"

    print(sql_statement)