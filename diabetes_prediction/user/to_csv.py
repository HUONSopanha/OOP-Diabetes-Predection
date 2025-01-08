import sqlite3
import csv
def get_from_database():
  # Step 1: Connect to the SQLite database
  conn = sqlite3.connect('db.sqlite3')  # Change this to your database file path
  cursor = conn.cursor()

  # Step 2: Fetch the data (replace 'your_table_name' with your actual table name)
  cursor.execute("SELECT num_pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, DiabetesPedigreeFunction, age, diabetes_prediction FROM user_diabetesprediction")
  rows = cursor.fetchall()  # Fetch all rows
  if rows == []:
      pass
  else:
        # Step 3: Define CSV file path
        csv_file_path = 'user/output.csv'
            # This is where the CSV file will be saved

        # Step 4: Write data to CSV
        with open(csv_file_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            
            # Optionally, write the header row
            column_names = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age', 'Outcome'] # Get column names
            writer.writerow(column_names)
            
            # Write the data rows
            writer.writerows(rows)

        # Close the database connection
        conn.close()
