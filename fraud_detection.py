import streamlit as st
import joblib
import pandas as pd

# Load model
model = joblib.load("fraud_detection_model.pkl")

st.title("Fraud Detection")

st.markdown(
    "Please enter the following details to predict whether the transaction is fraudulent or not."
)

st.divider()

transaction_type = st.selectbox(
    "Transaction Type",
    ["PAYMENT", "TRANSFER", "CASH_OUT", "DEBIT"]
)

amount = st.number_input(
    "Transaction Amount",
    min_value=0.0,
    value=1000.0
)

oldbalanceOrg = st.number_input(
    "Old Balance of Origin Account",
    min_value=0.0,
    value=1000.0
)

newbalanceOrig = st.number_input(
    "New Balance of Origin Account",
    min_value=0.0,
    value=9000.0
)

oldbalanceDest = st.number_input(
    "Old Balance of Destination Account",
    min_value=0.0,
    value=0.0
)

newbalanceDest = st.number_input(
    "New Balance of Destination Account",
    min_value=0.0,
    value=0.0
)

if st.button("Predict"):

    input_df = pd.DataFrame({
        "type": [transaction_type],
        "amount": [amount],
        "oldbalanceOrg": [oldbalanceOrg],
        "newbalanceOrig": [newbalanceOrig],
        "oldbalanceDest": [oldbalanceDest],
        "newbalanceDest": [newbalanceDest]
    })

    prediction = model.predict(input_df)

    if prediction[0] == 0:
        st.success("The transaction is not fraudulent.")
    else:
        st.error("The transaction is fraudulent.")