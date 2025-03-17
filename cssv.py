import os
import csv

# Define the folder path (Change this to your target directory)
folder_path = "/storage/emulated/0/Download"  # Example: Downloads folder

# Get list of files
files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

# Define the output CSV file path
csv_filename = "/storage/emulated/0/Download/file_list.csv"

# Write to CSV with progress updates
total_files = len(files)

with open(csv_filename, mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Filename"])  # Header

    for index, f in enumerate(files, start=1):
        writer.writerow([f])
        print(f"Processed {index}/{total_files}: {f}")  # Real-time progress update

print(f"\n✅ CSV file saved at: {csv_filename}")
