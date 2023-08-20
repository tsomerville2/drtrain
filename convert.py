import csv

# write out the training data as you like
with open('rawtrain.csv', 'r') as infile, open('train.csv', 'w') as outfile:
    reader = csv.DictReader(infile)
    outfile.write("Human,Assistant\n")  # headers
    
    for row in reader:
        if not row['Category'].lower().startswith('category'): 
            diary = row['Diary_Entry']
            emotion = row['Emotion_Reflection']
            goal = row['Lorenzo_Goal'] 
            tag = row['Lorenzo_Tag']

            #text_out = f"\n### Instruction: Respond like DrLorenzo to the diary\n### Human: {diary}\n\n### Assistant: {emotion} {goal}\n[>>{tag}\n"
            text_out = f"\"{diary}\",\"{emotion}  {goal} :->{tag}\"\n"

            outfile.write(text_out)

# read it back in and throw out any rows that fucked up somehow (more than expected # of rows)
expected_num_rows = 2
rows = []
good_count = 0

with open('train.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    header = next(reader)

    for i, row in enumerate(reader):
        try:
            if len(row) == expected_num_rows:
                rows.append(row)
                good_count = good_count + 1
        except Exception as e:
            print(f"Error in row {i+1}: {e}")

# Writing the rows to a new CSV file
output_filename = 'train-clean.csv'
with open(output_filename, 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(header)  # Writing the header row
    writer.writerows(rows)   # Writing the data rows

print(f"{good_count} Rows written to {output_filename}")
