import streamlit as st
from src.predict import triage

st.title("Support Ticket Triage")
ticket = st.text_area("Paste a support ticket:")
if st.button("Triage") and ticket.strip():
    r = triage(ticket)
    st.write(f"**Category:** {r['category']}")
    st.write(f"**Urgency:** {r['priority']}")
    st.write(f"**Confidence:** {r['confidence']}")
    st.success(f"Routed to: {r['queue']}")