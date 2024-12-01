import sqlite3
import matplotlib.pyplot as plt

conn = sqlite3.connect('population.db')

cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS population (
    city TEXT,
    year INTEGER,
    population INTEGER)
''')

cities_population = [
    ('Miami', 2024, 467963),
    ('Orlando', 2024, 309154),
    ('Tampa', 2024, 398139),
    ('Jacksonville', 2024, 949611),
    ('Tallahassee', 2024, 197102),
    ('St. Petersburg', 2024, 263255),
    ('Fort Lauderdale', 2024, 182760),
    ('Gainesville', 2024, 141085),
    ('Sarasota', 2024, 57618),
    ('Naples', 2024, 21027)
]

cursor.executemany('INSERT INTO population (city, year, population) VALUES (?, ?, ?)', cities_population)

def simulate_population_growth(cities_population, growth_rate=0.02, years=20):
    for city, start_year, start_population in cities_population:
        current_population = start_population
        for year in range(1, years + 1):
            new_year = start_year + year
            current_population = int(current_population * (1 + growth_rate))
            cursor.execute('INSERT INTO population (city, year, population) VALUES (?, ?, ?)', (city, new_year, current_population))

simulate_population_growth(cities_population)

def get_population_data(city):
    cursor.execute('SELECT year, population FROM population WHERE city=? ORDER BY year', (city,))
    return cursor.fetchall()

def plot_population_growth(city):
    data = get_population_data(city)
    if data:
        years = [row[0] for row in data]
        populations = [row[1] for row in data]
        
        plt.figure(figsize=(10, 6))
        plt.plot(years, populations, marker='o')
        plt.title(f'Population Growth in {city}')
        plt.xlabel('Year')
        plt.ylabel('Population')
        plt.grid(True)
        plt.show()
    else:
        print(f"No data available for {city}")

def user_interface():
    cities = [city for city, _, _ in cities_population]
    while True:
        print("Choose a city to view its population growth:")
        for i, city in enumerate(cities, 1):
            print(f"{i}. {city}")
        print("0. Exit")
        
        choice = input("Enter the number of your choice: ")
        if choice == '0':
            break
        elif choice.isdigit() and 1 <= int(choice) <= len(cities):
            city = cities[int(choice) - 1]
            plot_population_growth(city)
        else:
            print("Invalid choice. Please try again.")

user_interface()

conn.commit()

conn.close()

print("Database and table created, data inserted, and population growth displayed successfully.")
