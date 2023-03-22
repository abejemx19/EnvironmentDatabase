from faker import Faker
fake = Faker()

num_rows = 5 # specify the number of rows you want to generate

for i in range(num_rows):
    connection_id = i + 1
    user_id_1 = fake.random_int(min=1, max=10)
    user_id_2 = fake.random_int(min=1, max=10)
    connection_date = str(fake.date_between(start_date='-1y', end_date='today'))

    sql_statement = f"INSERT INTO Social_Connections (connection_id, user_id_1, user_id_2, connection_date) VALUES ({connection_id}, {user_id_1}, {user_id_2}, '{connection_date}');"

    print(sql_statement)