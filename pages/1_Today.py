import streamlit as st
from datetime import date

from db.crud import (
    get_exercises,
    create_workout,
    insert_set,
    upsert_nutrition,
    upsert_bodyweight,
)

USER_ID = 1  # MVP: single user


st.title("Today")

log_date = st.date_input("Date", value=date.today())

st.divider()

# -----------------------
# Workout Logging
# -----------------------
st.subheader("Workout")

exercises = get_exercises()
exercise_map = {ex["name"]: ex["id"] for ex in exercises}

selected_exercise = st.selectbox(
    "Exercise",
    options=list(exercise_map.keys()),
)

num_sets = st.number_input(
    "Number of sets",
    min_value=1,
    max_value=10,
    value=3,
    step=1,
)

sets_data = []

for i in range(int(num_sets)):
    with st.container():
        st.markdown(f"**Set {i + 1}**")
        cols = st.columns(3)
        reps = cols[0].number_input(
            "Reps",
            min_value=1,
            max_value=30,
            value=8,
            key=f"reps_{i}",
        )
        weight = cols[1].number_input(
            "Weight",
            min_value=0.0,
            step=2.5,
            value=0.0,
            key=f"weight_{i}",
        )
        rpe = cols[2].number_input(
            "RPE (optional)",
            min_value=1.0,
            max_value=10.0,
            step=0.5,
            value=8.0,
            key=f"rpe_{i}",
        )

        sets_data.append((i + 1, reps, weight, rpe))


if st.button("Save Workout"):
    workout_id = create_workout(
        user_id=USER_ID,
        workout_date=log_date,
        name=selected_exercise,
    )

    exercise_id = exercise_map[selected_exercise]

    for set_number, reps, weight, rpe in sets_data:
        insert_set(
            workout_id=workout_id,
            exercise_id=exercise_id,
            set_number=set_number,
            reps=reps,
            weight=weight,
            rpe=rpe,
        )

    st.success("Workout saved!")

st.divider()

# -----------------------
# Nutrition Logging
# -----------------------
st.subheader("Nutrition")

calories = st.number_input(
    "Calories",
    min_value=0,
    step=50,
)

protein = st.number_input(
    "Protein (g)",
    min_value=0.0,
    step=5.0,
)

if st.button("Save Nutrition"):
    upsert_nutrition(
        user_id=USER_ID,
        log_date=log_date,
        calories=calories,
        protein=protein,
    )
    st.success("Nutrition saved!")

st.divider()

# -----------------------
# Bodyweight Logging
# -----------------------
st.subheader("Bodyweight")

bodyweight = st.number_input(
    "Bodyweight",
    min_value=0.0,
    step=0.1,
)

if st.button("Save Bodyweight"):
    upsert_bodyweight(
        user_id=USER_ID,
        log_date=log_date,
        weight=bodyweight,
    )
    st.success("Bodyweight saved!")
