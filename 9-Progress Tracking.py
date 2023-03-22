from faker import Faker
fake = Faker()

num_rows = 5 # specify the number of rows you want to generate

for i in range(num_rows):
    progress_id = i + 1
    business_id = fake.random_int(min=1, max=10)
    goal_id = fake.random_int(min=1, max=10)
    current_value = round(fake.random.uniform(0.0, 100.0), 2)
    date = str(fake.date_between(start_date='-1y', end_date='today'))

    sql_statement = f"INSERT INTO Progress_Tracking (progress_id, business_id, goal_id, current_value, date) VALUES ({progress_id}, {business_id}, {goal_id}, {current_value}, '{date}');"

    print(sql_statement)