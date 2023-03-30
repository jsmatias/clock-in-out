
timeEntriesSchema = """
    CREATE TABLE time_entries (
        entry_id INT PRIMARY KEY,
        date DATE,
        start VARCHAR(8) NOT NULL,
        end VARCHAR(8) NOT NULL,
        worked_time INT
    );
"""
