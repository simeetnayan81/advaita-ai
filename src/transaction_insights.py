import json

customer_transaction_insights = None
with open("./data/customer_monthly_transaction_insights.json", "r") as file:
  customer_transaction_insights= json.load(file)


def getCustomerTransactionsInsight(customerID):
  for customer in customer_transaction_insights:
    if(customer["CustomerID"]==customerID):
      return customer
   