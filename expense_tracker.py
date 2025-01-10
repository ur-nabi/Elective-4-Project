import csv
from datetime import datetime

# Function to log an expense
def log_expense(amount, category, description):
    try:
        with open('expenses.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([datetime.now(), amount, category, description])
        print(f"Logged expense: ${amount} for {category} - {description}")
    except Exception as e:
        print(f"Error logging expense: {e}")

# Function to generate a summary report
def generate_report():
    try:
        with open('expenses.csv', 'r') as file:
            reader = csv.reader(file)
            total = 0
            print("\n--- Expense Summary ---")
            for row in reader:
                if row:  # Skip empty rows
                    print(f"{row[0]} - ${row[1]} - {row[2]} - {row[3]}")
                    total += float(row[1])
            print(f"Total Expenses: ${total:.2f}")
    except FileNotFoundError:
        print("No expenses logged yet. Please add some expenses first.")
    except Exception as e:
        print(f"Error generating report: {e}")

# Example usage
if __name__ == "__main__":
    # Log some sample expenses
    log_expense(50, 'Groceries', 'Bought fruits and vegetables')
    log_expense(20, 'Transport', 'Taxi fare')
    log_expense(100, 'Entertainment', 'Movie tickets')
    
    # Generate a summary report
    generate_report()
