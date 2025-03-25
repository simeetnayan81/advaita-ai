import numpy as np
import pickle
import json


def make_dataset(customerId):
    with open("./data/customer_monthly_transaction_insights.json", "r") as file:
        trx_data = json.load(file)
    trxns = []
    for cus in trx_data:
        if cus["CustomerID"] == customerId:
            trxInsights = cus["Transaction_Insights"]
            for trx in trxInsights:
                trxns.append(trx["Total_Transaction_Amount"])
            return trxns
    return trxns
    

def generate_prediction(transaction_data):
    with open("./models/TransactionModel.pkl", "rb") as file:
        lr_model = pickle.load(file)
    
    prediction = lr_model.predict(transaction_data)[0]
    return prediction

def predict_transaction(customerId):
    transaction_data = make_dataset(customerId)
    if(len(transaction_data) < 12):
        return None

    transaction_data = np.array(transaction_data)
    
    mx=transaction_data.max()
    mn=transaction_data.min()

    transaction_data=transaction_data[-11:]
    prediction = generate_prediction(np.array([transaction_data]))

    score = (prediction - mn)/(mx-mn)
    if score > 1:
        score = 1
    elif score < 0:
        score = 0

    return {"predicted": prediction, "score": score}
