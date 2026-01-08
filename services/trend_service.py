import pandas as pd
from db.connection import get_connection


def get_strength_data(user_id):
    """
    Returns per-exercise strength data using top set per workout.
    """
    conn = get_connection()
    query = """
    SELECT
        w.workout_date,
        e.name AS exercise,
        MAX(s.weight * s.reps) AS volume_load
    FROM sets s
    JOIN workouts w ON s.workout_id = w.id
    JOIN exercises e ON s.exercise_id = e.id
    WHERE w.user_id = ?
    GROUP BY w.workout_date, e.name
    ORDER BY w.workout_date;
    """
    df = pd.read_sql(query, conn, params=(user_id,))
    conn.close()
    return df


def get_bodyweight_data(user_id):
    conn = get_connection()
    df = pd.read_sql(
        """
        SELECT log_date, weight
        FROM bodyweight_logs
        WHERE user_id = ?
        ORDER BY log_date;
        """,
        conn,
        params=(user_id,),
    )
    conn.close()
    return df


def get_nutrition_data(user_id):
    conn = get_connection()
    df = pd.read_sql(
        """
        SELECT log_date, calories, protein
        FROM nutrition_logs
        WHERE user_id = ?
        ORDER BY log_date;
        """,
        conn,
        params=(user_id,),
    )
    conn.close()
    return df
