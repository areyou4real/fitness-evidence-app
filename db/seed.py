from db.connection import get_connection
from exercises.exercise_list import EXERCISES


def seed_exercises():
    """
    Insert canonical exercises if table is empty.
    Safe to run multiple times.
    """
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM exercises;")
    count = cursor.fetchone()[0]

    if count > 0:
        conn.close()
        return

    for ex in EXERCISES:
        cursor.execute(
            """
            INSERT INTO exercises (name, primary_muscle, secondary_muscles, category)
            VALUES (?, ?, ?, ?);
            """,
            (
                ex["name"],
                ex["primary_muscle"],
                ex["secondary_muscles"],
                ex["category"],
            ),
        )

    conn.commit()
    conn.close()
