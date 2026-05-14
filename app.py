import streamlit as st

st.title("Steven Pay Calculator")

hours_worked = st.number_input("Hours worked", min_value=0.0)
pay_per_hour = st.number_input("Pay per hour", min_value=0.0)

if hours_worked > 40:
    overtime_hours = hours_worked - 40
    gross_pay = (40 * pay_per_hour) + (overtime_hours * pay_per_hour * 1.5)
else:
    gross_pay = hours_worked * pay_per_hour

deductions = gross_pay * 0.25
net_pay = gross_pay - deductions

st.write(f"Gross Pay: ${gross_pay:.2f}")
st.write(f"Total Deductions: ${deductions:.2f}")
st.write(f"Net Pay: ${net_pay:.2f}")
st.write(f"Annual Gross Pay: ${gross_pay * 52:.2f}")
st.write(f"Annual Net Pay: ${net_pay * 52:.2f}")
