
import json
import csv


def save_niraj_json_to_csv(
        input_json, output_csv, 
        headers = ["URL", "Country", "Domain", "Category", "Score"], 
        ):
    with open(input_json, 'r') as json_file:
        data = json.load(json_file)

    with open(output_csv, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        
        writer.writerow(headers)

        for entry in data:
            writer.writerow(entry)
    return output_csv