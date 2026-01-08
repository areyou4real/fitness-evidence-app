import streamlit as st
import matplotlib.pyplot as plt

from services.trend_service import (
    get_strength_data,
    get_bodyweight_data,
    get_nutrition_data,
)
from utils.rolling import rolling_average

USER_ID = 1

st.title("Progress")

# -----------------------
# Strength Trends
# -----------------------
st.subheader("Strength Trends")

strength_df = get_strength_data(USER_ID)

if strength_df.empty:
    st.info("Log workouts to see strength trends.")
else:
    exercises = strength_df["exercise"].unique()
    selected_exercise = st.selectbox(
        "Select exercise",
        options=exercises,
    )

    df = strength_df[strength_df["exercise"] == selected_exercise].copy()
    df["rolling"] = rolling_average(df["volume_load"], window=5)

    fig, ax = plt.subplots()
    ax.plot(df["workout_date"], df["volume_load"], label="Session")
    ax.plot(df["workout_date"], df["rolling"], label="Rolling Avg")
    ax.set_ylabel("Volume Load")
    ax.set_xlabel("Date")
    ax.legend()

    st.pyplot(fig)

    pct_change = (
        (df["rolling"].iloc[-1] - df["rolling"].iloc[0])
        / df["rolling"].iloc[0]
        * 100
        if len(df) > 1
        else 0
    )

    st.write(f"Change over time: **{pct_change:.1f}%**")

st.divider()

# -----------------------
# Bodyweight Trends
# -----------------------
st.subheader("Bodyweight")

bw_df = get_bodyweight_data(USER_ID)

if bw_df.empty:
    st.info("Log bodyweight to see trends.")
else:
    bw_df["rolling"] = rolling_average(bw_df["weight"], window=7)

    fig, ax = plt.subplots()
    ax.plot(bw_df["log_date"], bw_df["weight"], label="Daily")
    ax.plot(bw_df["log_date"], bw_df["rolling"], label="7-day avg")
    ax.set_ylabel("Bodyweight")
    ax.set_xlabel("Date")
    ax.legend()

    st.pyplot(fig)

st.divider()

# -----------------------
# Nutrition Trends
# -----------------------
st.subheader("Calories")

nut_df = get_nutrition_data(USER_ID)

if nut_df.empty:
    st.info("Log calories to see trends.")
else:
    nut_df["rolling"] = rolling_average(nut_df["calories"], window=7)

    fig, ax = plt.subplots()
    ax.plot(nut_df["log_date"], nut_df["calories"], label="Daily")
    ax.plot(nut_df["log_date"], nut_df["rolling"], label="7-day avg")
    ax.set_ylabel("Calories")
    ax.set_xlabel("Date")
    ax.legend()

    st.pyplot(fig)
