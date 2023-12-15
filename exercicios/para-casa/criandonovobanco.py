import sqlite3
import csv

connect = sqlite3.connect('banco_starbucks.db')
cursor = connect.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS starbucks(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    Beverage_category TEXT NOT NULL,
    Beverage TEXT NOT NULL,
    Beverage_prep TEXT NOT NULL,
    Calories FLOAT, 
    Total_Fat_g FLOAT,
    Trans_Fat_g FLOAT,
    Saturated_Fat_g FLOAT, 
    Sodium_mg FLOAT,
    Total_Carbohydrates_g FLOAT,
    Cholesterol_mg FLOAT,
    Dietary_Fibre_g FLOAT,
    Sugars_g FLOAT,
    Protein_g FLOAT,
    Vitamin_A_DV FLOAT,
    Vitamin_C_DV FLOAT,
    Calcium_DV FLOAT,
    Iron_DV FLOAT,
    Caffeine_mg FLOAT
)
               '''
)

file = open("starbucks.csv")

conteudo = csv.reader(file)

inserir_conteudo = "INSERT INTO starbucks (Beverage_category,Beverage,Beverage_prep,Calories, Total_Fat_g,Trans_Fat_g ,Saturated_Fat_g, Sodium_mg, Total_Carbohydrates_g, Cholesterol_mg, Dietary_Fibre_g, Sugars_g, Protein_g ,Vitamin_A_DV ,Vitamin_C_DV, Calcium_DV ,Iron_DV ,Caffeine_mg) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"

cursor.executemany(inserir_conteudo, conteudo)

selecionar_tudo = "SELECT * FROM starbucks"
entradas = cursor.execute(selecionar_tudo).fetchall()

connect.commit()
connect.close()
