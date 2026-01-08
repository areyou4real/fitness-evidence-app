from db.connection import get_connection


def get_exercises():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, name FROM exercises ORDER BY name;")
    rows = cursor.fetchall()
    conn.close()
    return rows


def create_workout(user_id, workout_date, name=None):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        """
        INSERT INTO workouts (user_id, workout_date, name)
        VALUES (?, ?, ?)
        """,
        (user_id, workout_date, name),
    )
    workout_id = cursor.lastrowid
    conn.commit()
    conn.close()
    return workout_id


def insert_set(workout_id, exercise_id, set_number, reps, weight, rpe=None):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        """
        INSERT INTO sets (workout_id, exercise_id, set_number, reps, weight, rpe)
        VALUES (?, ?, ?, ?, ?, ?)
        """,
        (workout_id, exercise_id, set_number, reps, weight, rpe),
    )
    conn.commit()
    conn.close()


def upsert_nutrition(user_id, log_date, calories, protein):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        """
        INSERT INTO nutrition_logs (user_id, log_date, calories, protein)
        VALUES (?, ?, ?, ?)
        ON CONFLICT(user_id, log_date)
        DO UPDATE SET calories=excluded.calories, protein=excluded.protein;
        """,
        (user_id, log_date, calories, protein),
    )
    conn.commit()
    conn.close()


def upsert_bodyweight(user_id, log_date, weight):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        """
        INSERT INTO bodyweight_logs (user_id, log_date, weight)
        VALUES (?, ?, ?)
        ON CONFLICT(user_id, log_date)
        DO UPDATE SET weight=excluded.weight;
        """,
        (user_id, log_date, weight),
    )
    conn.commit()
    conn.close()
