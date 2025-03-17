import os
import csv

folder_path = "/storage/emulated/0/Download"  # Change this to your folder

files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

csv_filename = "/storage/emulated/0/Download/file_list.csv"

with open(csv_filename, mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Filename"])
    for f in files:
        writer.writerow([f])

print(f"CSV file saved at: {csv_filename}")
