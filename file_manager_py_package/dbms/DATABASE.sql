-- This SQL script creates a table named 'person' if it does not already exist.
CREATE TABLE IF NOT EXISTS person(
    person_id INTEGER PRIMARY KEY AUTOINCREMENT,
    person_name VARCHAR(100) NOT NULL
);

-- This SQL script creates a table named 'recordingSession' if it does not already exist.
CREATE TABLE IF NOT EXISTS recordingSession(
    recordingSession_id INTEGER PRIMARY KEY AUTOINCREMENT,
    recordingSession_name VARCHAR(100) NOT NULL,
    recordingSession_date DATETIME NOT NULL,
    recordingSession_relative_time DECIMAL(7, 2) NOT NULL,
    fk_person_id INTEGER,
    fk_sensor_1_id INTEGER,
    fk_sensor_2_id INTEGER,
    fk_electrode_1_id INTEGER,
    fk_electrode_2_id INTEGER,
    fk_frequency_id INTEGER,
    fk_amplitude_id INTEGER,
    -- Foreign Keys
    FOREIGN KEY (fk_person_id) REFERENCES person(person_id),
    FOREIGN KEY (fk_sensor_1_id) REFERENCES sensor(sensor_id),
    FOREIGN KEY (fk_sensor_2_id) REFERENCES sensor(sensor_id),
    FOREIGN KEY (fk_electrode_1_id) REFERENCES electrode(electrode_id),
    FOREIGN KEY (fk_electrode_2_id) REFERENCES electrode(electrode_id),
    FOREIGN KEY (fk_frequency_id) REFERENCES frequency(frequency_id),
    FOREIGN KEY (fk_amplitude_id) REFERENCES amplitude(amplitude_id)
);

-- This SQL script creates a table named 'sensor' (Flexsensor) if it does not already exist.
CREATE TABLE IF NOT EXISTS sensor(
    sensor_id INTEGER PRIMARY KEY AUTOINCREMENT,
    sensor_name VARCHAR(100) NOT NULL
);

-- This SQL script creates a table named 'electrode' if it does not already exist.
CREATE TABLE IF NOT EXISTS electrode(
    electrode_id INTEGER PRIMARY KEY AUTOINCREMENT,
    electrode_name VARCHAR(2) NOT NULL
);

-- This SQL script creates a table named 'frequency' if it does not already exist.
CREATE TABLE IF NOT EXISTS frequency(
    frequency_id INTEGER PRIMARY KEY AUTOINCREMENT,
    frequency_value DECIMAL(7, 2) UNIQUE,
    frequency_unit VARCHAR(20)
);

CREATE TABLE IF NOT EXISTS amplitude(
    amplitude_id INTEGER PRIMARY KEY AUTOINCREMENT,
    amplitude_value DECIMAL(7, 2) UNIQUE,
    amplitude_unit VARCHAR(20)
);
