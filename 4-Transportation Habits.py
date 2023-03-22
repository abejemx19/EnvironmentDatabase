from faker import Faker
fake = Faker()

num_rows = 5 # specify the number of rows you want to generate

for i in range(num_rows):
    transportation_id = i + 1
    user_business_id = fake.random_int(min=1, max=10)
    transportation_mode = fake.random_element(elements=('Car', 'Bus', 'Train', 'Bike', 'Walk'))
    distance = round(fake.random.uniform(0.0, 100.0), 2)
    date = str(fake.date_between(start_date='-1y', end_date='today'))

    sql_statement = f"INSERT INTO Transportation_Habits (transportation_id, user_business_id, transportation_mode, distance, date) VALUES ({transportation_id}, {user_business_id}, '{transportation_mode}', {distance}, '{date}');"

    print(sql_statement)