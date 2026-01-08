from db.connection import get_connection


USERS_TABLE = """
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
"""


EXERCISES_TABLE = """
CREATE TABLE IF NOT EXISTS exercises (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    primary_muscle TEXT NOT NULL,
    secondary_muscles TEXT,
    category TEXT
);
"""


WORKOUTS_TABLE = """
CREATE TABLE IF NOT EXISTS workouts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    workout_date DATE NOT NULL,
    name TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id)
);
"""


SETS_TABLE = """
CREATE TABLE IF NOT EXISTS sets (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    workout_id INTEGER NOT NULL,
    exercise_id INTEGER NOT NULL,
    set_number INTEGER,
    reps INTEGER NOT NULL,
    weight REAL NOT NULL,
    rpe REAL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (workout_id) REFERENCES workouts(id),
    FOREIGN KEY (exercise_id) REFERENCES exercises(id)
);
"""


NUTRITION_LOGS_TABLE = """
CREATE TABLE IF NOT EXISTS nutrition_logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    log_date DATE NOT NULL,
    calories INTEGER NOT NULL,
    protein REAL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE (user_id, log_date),
    FOREIGN KEY (user_id) REFERENCES users(id)
);
"""


BODYWEIGHT_LOGS_TABLE = """
CREATE TABLE IF NOT EXISTS bodyweight_logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    log_date DATE NOT NULL,
    weight REAL NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE (user_id, log_date),
    FOREIGN KEY (user_id) REFERENCES users(id)
);
"""


USER_SETTINGS_TABLE = """
CREATE TABLE IF NOT EXISTS user_settings (
    user_id INTEGER PRIMARY KEY,
    experience_level TEXT DEFAULT 'beginner',
    goal TEXT,
    units TEXT DEFAULT 'metric',
    show_rpe BOOLEAN DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id)
);
"""


SCHEMA = [
    USERS_TABLE,
    EXERCISES_TABLE,
    WORKOUTS_TABLE,
    SETS_TABLE,
    NUTRITION_LOGS_TABLE,
    BODYWEIGHT_LOGS_TABLE,
    USER_SETTINGS_TABLE,
]


def create_schema():
    """
    Create all database tables if they don't exist.
    Safe to run multiple times.
    """
    conn = get_connection()
    cursor = conn.cursor()

    for table_sql in SCHEMA:
        cursor.execute(table_sql)

    conn.commit()
    conn.close()
