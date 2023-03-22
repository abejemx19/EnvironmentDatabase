# EnvironmentDatabase/ Sustainability Database

This repository contains the structure and data for a sustainability database that I created. The database consists of several tables that store information about users, businesses, energy consumption, transportation habits, waste production, carbon footprint calculations, recommendations, sustainability goals progress tracking and social connections.

## Database Structure

The database consists of the following tables:

- `Users`: This table stores information about individual users. Each user has a unique `user_id`, as well as a `name`, `email`, and `location`.

- `Businesses`: This table stores information about businesses. Each business has a unique `business_id`, as well as a `name`, `industry_type`, and `location`.

- `Energy_Consumption`: This table stores information about energy consumption by users and businesses. Each record has a unique `consumption_id`, as well as a `user_business_id` (which references either a user or business), an `energy_type` (e.g., electricity or water), a usage_amount (in kilowatt-hours or gallons), and date.

-  `Transportation_Habits`: This table stores information about transportation habits by users and businesses. Each record has a unique transportation_id as well as user_business_id (which references either a user or business) transportation_mode (e.g., car or bike) distance traveled (in miles or kilometers) and date.

- `Waste_Production`: This table stores information about waste production by users and businesses. Each record has a unique waste_id as well as user_business_id (which references either a user or business) waste_type (e.g., plastic or food) amount produced (in pounds or kilograms) and date.

- `Carbon_Footprint_Calculations`: This table stores information about carbon footprint calculations for users and businesses. Each record has a unique calculation_id as well as user_business_id (which references either a user or business) carbon_footprint (in metric tons of CO2 equivalent) and date.

- `Recommendations`: This table stores information about recommendations for users and businesses. Each record has a unique recommendation_id as well as user_business_id (which references either a user or business) recommendation_type (e.g., reduce energy consumption or switch to renewable energy) and date.

- `Sustainability_Goals`: This table stores information about sustainability goals set by businesses. Each record has a unique goal_id as well as business_id (which references a business) goal_type (e.g., reduce carbon emissions or increase renewable energy usage) target_value (the desired value to be achieved) and target_date (the date by which the goal should be achieved).

- `Progress_Tracking`: This table stores information about progress towards sustainability goals by businesses. Each record has a unique progress_id as well as business_id (which references a business) goal_id (which references a specific sustainability goal) current_value (the current value towards achieving the goal) and date.

- `Social_Connections`: This table stores information about social connections between users. Each record has a unique connection_id as well as user_id_1 and user_id_2 (which reference two connected users) and connection_date (the date on which the connection was established).

## Data Generation

To populate the database with realistic data, I used the Python library [INSERT LIBRARY NAME HERE] to generate random but plausible values for each field in each table. This allowed me to quickly create large amounts of data for testing and analysis.

## How to Use this Database

This database can be used to track and analyze sustainability-related data for individuals and businesses. By storing information about energy consumption transportation habits waste production carbon footprint calculations recommendations sustainability goals progress tracking in one place you can gain insights into patterns and trends that can help inform decision-making around sustainability initiatives.

For example you could use this database to:

- Calculate the average carbon footprint per person or per business in your community
- Identify which types of businesses have the highest energy consumption
- Track progress towards community-wide sustainability goals
- Generate personalized recommendations for individuals or businesses based on their energy consumption transportation habits waste production etc
