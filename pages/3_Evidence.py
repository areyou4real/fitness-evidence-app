import streamlit as st
from services.evidence_service import generate_evidence

USER_ID = 1

st.title("Evidence-Based Progress")

evidence = generate_evidence(USER_ID)

confidence = evidence["confidence"]

if confidence == "high":
    st.success("High confidence your current approach is working ✅")
elif confidence == "medium":
    st.warning("Mixed signals — progress is possible but not guaranteed ⚠️")
else:
    st.error("Low confidence — changes are likely needed ❌")

st.divider()

st.subheader("What the data suggests")

st.write(
    f"""
    **Strength change:** {evidence['strength_pct']:.1f}%  
    **Bodyweight trend:** {evidence['weight_slope']:.3f} per day
    """
)

st.divider()

st.caption(
    "This assessment is based on trends, not single days. More data increases confidence."
)
