import csv

# Input filter
preferred_channel = input("Masukkan Preferred Channel (misal: Instagram): ").strip()
content_topic = input("Masukkan Favorite Content Topic (misal: Operational): ").strip()

filtered_data = []

with open('hubspot-crm-exports-all-customers-2025-04-08.csv', mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        if (row['Preferred channels'] == preferred_channel or
            row['Favorite Content Topics'] == content_topic):
            filtered_data.append(row)

# Simpan hasil filter ke file baru
output_file = 'filtered_crm_results.csv'
with open(output_file, mode='w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=reader.fieldnames)
    writer.writeheader()
    writer.writerows(filtered_data)

print(f'{len(filtered_data)} baris data berhasil disimpan ke {output_file}')
