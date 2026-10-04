import pandas as pd
from datetime import datetime

monthly_budget = 10000

data = {
    "Date": [
        "2026-10-01", "2026-10-02", "2026-10-03",
        "2026-10-04", "2026-10-05", "2026-10-06",
        "2026-10-07", "2026-10-08", "2026-10-09",
        "2026-10-10"
    ],

    "Item": [
        "Lunch", "Bus Ticket", "Shoes", "Groceries", "Mobile Recharge",
        "Movie", "Dinner", "Auto Fare", "Headphones", "Breakfast"
    ],

    "Amount": [
        250, 80, 2500, 1800, 500,
        350, 300, 150, 1800, 120
    ],

    "Payment Method": [
        "GPay", "Cash", "Card", "PhonePe", "GPay",
        "Cash", "PhonePe", "GPay", "Card", "Bank Transfer"
    ]
}

df = pd.DataFrame(data)

df["Date"] = pd.to_datetime(df["Date"])
df = df.sort_values("Date")

total_expense = df["Amount"].sum()
average_expense = df["Amount"].mean()
remaining_budget = monthly_budget - total_expense

monthly_expense = df.groupby(df["Date"].dt.strftime("%B %Y"))["Amount"].sum()

address = input("Enter your address: ")

now = datetime.now()
today_date = now.strftime("%d-%m-%Y")
current_time = now.strftime("%I:%M %p")

df.to_csv("monthly_expense_data.csv", index=False)

print("\n" + "=" * 82)
print("                      MONTHLY EXPENSE BILL")
print("=" * 82)
print(f"Address: {address}")
print(f"Generated Date: {today_date}")
print(f"Generated Time: {current_time}")
print("-" * 82)

print(f"{'DATE':<14} | {'ITEM':<22} | {'AMOUNT':<15} | {'PAYMENT METHOD':<18}")

print("-" * 82)

for _, row in df.iterrows():
    date_value = row["Date"].strftime("%d-%m-%Y")

    print(
        f"{date_value:<14} | "
        f"{row['Item']:<22} | "
        f"₹{row['Amount']:<14.2f} | "
        f"{row['Payment Method']:<18}"
    )

print("-" * 82)

for month, amount in monthly_expense.items():
    print(f"{'MONTHLY EXPENSE - ' + month:<60} | ₹{amount:.2f}")

print(f"{'MONTHLY BUDGET':<60} | ₹{monthly_budget:.2f}")
print(f"{'AVERAGE EXPENSE':<60} | ₹{average_expense:.2f}")
print(f"{'REMAINING BUDGET':<60} | ₹{remaining_budget:.2f}")

print("-" * 82)

if total_expense > monthly_budget:
    print("BUDGET STATUS: OVER BUDGET - Reduce your spending!")
elif total_expense >= monthly_budget * 0.8:
    print("BUDGET STATUS: WARNING - You used 80% or more of your budget.")
else:
    print("BUDGET STATUS: GOOD - You are under budget.")

print("=" * 82)

