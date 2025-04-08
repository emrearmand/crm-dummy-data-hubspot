import csv
from collections import Counter

with open('hubspot-crm-exports-all-customers-2025-04-08.csv', mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    data = list(reader)

# Hitung total kontak
total_contacts = len(data)

# Hitung jumlah per Lead Status
lead_status_counts = Counter(row['Lead Status'] for row in data if row['Lead Status'])

# Hitung jumlah per Favorite Content Topics
content_topic_counts = Counter(row['Favorite Content Topics'] for row in data if row['Favorite Content Topics'])

# Hitung jumlah per Preferred channels
channel_counts = Counter(row['Preferred channels'] for row in data if row['Preferred channels'])

# Cetak hasil
print(f'Total Contacts: {total_contacts}\n')

print('Lead Status:')
for status, count in lead_status_counts.items():
    print(f'- {status}: {count}')

print('\nFavorite Content Topics:')
for topic, count in content_topic_counts.items():
    print(f'- {topic}: {count}')

print('\nPreferred Channels:')
for channel, count in channel_counts.items():
    print(f'- {channel}: {count}')
