import csv

output_lines = []

# Read the CSV file
with open('decklist.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader)  # Skip the header row, remove this line if there's no header

    for row in csvreader:
        name = row[2]  # Assuming C is the third column, index starts from 0
        set_code = row[6]  # Assuming G is the seventh column
        number = row[7]  # Assuming H is the eighth column
        formatted_line = f"{name} ({set_code}) {number}"
        output_lines.append(formatted_line)

# Write to the text file
with open('cards.txt', 'w') as txtfile:
    for line in output_lines:
        txtfile.write(line + '\n')

print(f'Processed {len(output_lines)} lines.')
