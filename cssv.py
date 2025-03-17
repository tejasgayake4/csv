import os
import csv

# File paths (modify if needed)
csv_file_path = "/sdcard/Download/files_to_delete.csv"
file_directory = "/sdcard/Documents/"

print("📂 Starting file deletion process...\n")

# Read CSV and delete files
try:
    with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            filename = row[0].strip()
            file_path = os.path.join(file_directory, filename)

            print(f"🔍 Checking: {filename}")

            if os.path.exists(file_path):
                print(f"🗑️ Deleting: {filename} ... ", end="")
                try:
                    os.remove(file_path)
                    print("✅ Deleted successfully!")
                except Exception as e:
                    print(f"❌ Error deleting: {e}")
            else:
                print(f"⚠️ File not found: {filename}")

    print("\n✅ Process completed!")
except FileNotFoundError:
    print("❌ CSV file not found!")
except Exception as e:
    print(f"⚠️ Error reading CSV file: {e}")
