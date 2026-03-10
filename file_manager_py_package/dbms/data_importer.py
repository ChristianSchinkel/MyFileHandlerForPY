"""Data Importer"""

import os
import glob
import sqlite3
import io
import re
import pandas as pd

# 1. Define your Input and Output Directories
CSV_DIRECTORY = './input_csv_files'  # Replace with your actual CSV folder path
DATABASE_FILE = './output_db/health_telemetry.db'
# Replace with your target DB path

# Create the target directory for the database if it doesn't exist
os.makedirs(os.path.dirname(DATABASE_FILE), exist_ok=True)

# 2. Connect to the Database
conn = sqlite3.connect(DATABASE_FILE)
cursor = conn.cursor()


# Helper function to get or create foreign keys
def get_or_create(table, column, value):
    """Get the ID of a record from the specified table and column,
    or create it if it doesn't exist."""
    # Handle missing numerical data
    if pd.isna(value) or value == 'N/A':
        value = 0

    cursor.execute(
        f"SELECT {table}_id FROM {table} WHERE {column} = ?",
        (str(value),)
    )
    result = cursor.fetchone()
    if result:
        return result[0]

    cursor.execute(f"INSERT INTO {table} ({column}) VALUES (?)", (str(value),))
    return cursor.lastrowid


# 3. Locate and Process CSV Files
csv_files = glob.glob(os.path.join(CSV_DIRECTORY, '*.csv'))
print(f"Found {len(csv_files)} file(s) to process.")

for file_path in csv_files:
    filename = os.path.basename(file_path)
    print(f"Processing: {filename}...")

    # Extract session date from the filename (e.g., 2026-02-27T18-31-47)
    match = re.search(r'(\d{4}-\d{2}-\d{2}T\d{2}-\d{2}-\d{2})', filename)
    if match:
        # Convert to standard DATETIME format: YYYY-MM-DD HH:MM:SS
        session_date = match.group(1).replace('T', ' ').replace('-', ':', 2)
    else:
        session_date = "1970-01-01 00:00:00"

    # Split the file to remove the # Markers section at the bottom
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    try:
        marker_index = next(i for i, line in enumerate(lines)
                            if line.startswith('# Markers:'))
        sensor_lines = lines[:marker_index]
    except StopIteration:
        sensor_lines = lines  # Fallback if no markers exist in the file

    # Load into Pandas DataFrame
    df = pd.read_csv(io.StringIO(''.join(sensor_lines)))

    # Get or create the Person
    person_name = df['patientName'].iloc[0]
    person_id = get_or_create('person', 'person_name', person_name)

    # 4. Prepare Batch Insert Data
    session_records = []

    for index, row in df.iterrows():
        # Retrieve or generate primary keys for dimensions
        electrode_1_id = get_or_create(
            'electrode', 'electrode_name', row['electrode1']
        )
        electrode_2_id = get_or_create(
            'electrode', 'electrode_name', row['electrode2']
        )
        sensor_1_id = get_or_create(
            'sensor', 'sensor_name', row['sensor1']
        )
        sensor_2_id = get_or_create(
            'sensor', 'sensor_name', row['sensor2']
        )
        frequency_id = get_or_create(
            'frequency', 'frequency_value', row['frequency']
        )
        amplitude_id = get_or_create(
            'amplitude', 'amplitude_value', row['amplitude']
        )

        # Bundle the row data
        session_records.append((
            row['sensorName'],
            session_date,
            row['relative_time_s'],
            person_id,
            sensor_1_id,
            sensor_2_id,
            electrode_1_id,
            electrode_2_id,
            frequency_id,
            amplitude_id
        ))

    # 5. Execute Bulk Insert
    cursor.executemany("""
        INSERT INTO recordingSession (
            recordingSession_name, recordingSession_date,
            recordingSession_relative_time,
            fk_person_id, fk_sensor_1_id, fk_sensor_2_id,
            fk_electrode_1_id, fk_electrode_2_id,
            fk_frequency_id, fk_amplitude_id
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, session_records)

    conn.commit()
    print(f"Successfully inserted {len(session_records)}"
          f"records for {person_name}.\n")

conn.close()
print("All files processed and imported successfully!")
