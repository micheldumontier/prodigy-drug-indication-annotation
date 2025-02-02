import pandas as pd
import json
import sys

def clean_text(text):
    return ' '.join(text.strip().split())

def csv_to_jsonl(csv_file, jsonl_file):
    # Read CSV file into a DataFrame
    df = pd.read_csv(csv_file)
    
    # # Convert DataFrame to a list of dictionaries
    # records = df.to_dict(orient='records')

    # Select the "indication" column
    indications = df["indication"].tolist()

    # Clean the text in each indication
    cleaned_indications = [clean_text(indication) for indication in indications]

    # Prepare JSONL data
    jsonl_data = [{"text": indication, "meta": {"source": "Dailymed"}} for indication in cleaned_indications]

    # Write each dictionary as a JSON object in the JSONL file
    with open(jsonl_file, 'w') as f:
        for record in jsonl_data:
            json.dump(record, f)
            f.write('\n')

if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(f"Right usage: {sys.argv[0]} [input.csv] [output.jsonl]") 
        
    csv_to_jsonl(sys.argv[1], sys.argv[2])