import csv
import os

# Path to collect data from the Resources folder
budget_data_csv = os.path.join(os.path.dirname(__file__), '..', 'Resources', 'budget_data.csv')

# Lists to store data
months = []
profit_losses = []

# Read in the CSV file
try:
    with open(budget_data_csv, newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        
        # Read the header row first
        csv_header = next(csvreader)
        
        # Read each row of data after the header
        for row in csvreader:
            months.append(row[0])
            profit_losses.append(int(row[1]))

except FileNotFoundError:
    print(f"Error: The file at {budget_data_csv} was not found.")
    exit()
except ValueError as e:
    print(f"Error: There was a problem with the data format: {e}")
    exit()
except Exception as e:
    print(f"An unexpected error occurred: {e}")
    exit()

# Ensure we have data to work with
if months and profit_losses:
    # Calculate total number of months
    total_months = len(months)

    # Calculate net total amount of "Profit/Losses"
    net_total = sum(profit_losses)

    # Calculate changes in "Profit/Losses" and find average change
    changes = [profit_losses[i+1] - profit_losses[i] for i in range(len(profit_losses)-1)]
    average_change = sum(changes) / len(changes) if changes else 0

    # Find greatest increase in profits
    greatest_increase = max(changes, default=0)
    greatest_increase_month = months[changes.index(greatest_increase) + 1] if changes else "N/A"

    # Find greatest decrease in losses
    greatest_decrease = min(changes, default=0)
    greatest_decrease_month = months[changes.index(greatest_decrease) + 1] if changes else "N/A"

    # Prepare the analysis summary
    analysis = (
        "Financial Analysis\n"
        "----------------------------\n"
        f"Total Months: {total_months}\n"
        f"Total: ${net_total}\n"
        f"Average Change: ${average_change:.2f}\n"
        f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})\n"
        f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})\n"
    )

    # Print the analysis to the terminal
    print(analysis)

    # Save the results to a text file
    output_path = os.path.join(os.path.dirname(__file__), '..', 'analysis', 'financial_analysis.txt')

    try:
        with open(output_path, "w") as txtfile:
            txtfile.write(analysis)
    except Exception as e:
        print(f"Error writing to file: {e}")
else:
    print("No data available to analyze.")
