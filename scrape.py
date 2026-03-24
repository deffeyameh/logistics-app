import requests
import json
import re

cookies = {
    'laravel_session': 'eyJpdiI6Im5scXpONUlodHc5VXlJUE9BK2RaSkE9PSIsInZhbHVlIjoiQ0JLQ2dJTDhyeVNEVmVvNmkxa0p6YmVrU2M5NVJOSUhBaUpNN2N0Q2FUKy9PU1pHZWxVbVhCWjBpQVZ3N2daTFRBei9EMy9Ed0JyajgrL2hvL1c2TnNBdklzRC9IZFZOM25KYXpMa1ZhenZWbmNQQXBDWVdaWmRlZVhnMDdDTS8iLCJtYWMiOiIwN2Q1NzJiMzMwOGJmYTc4ZWNhYmEzNjliNDUyM2FiNWE5N2NmNjVmMjk0YTI5ODFjYmQ1YWQ2ZjNkYzYzYmY1IiwidGFnIjoiIn0%3D',
    'XSRF-TOKEN': 'eyJpdiI6ImJBVS9GWVpWcTNYUlBVaE1uWmhLYmc9PSIsInZhbHVlIjoidnZ2dEJYQnFGSWVqVWJmRGt6eHF5STJQZHFieEVNaWNNOTRSbkNkR01laFVxS1lsUG9heS9MTEhEVGNWUDVBVHl4RDljQVVLc3dpOW5wYTBGaEFvYXNoMmtYVng5KzZ6ZGxTYjhKNmN1YWpMUWIyNGhuZmFHcnlQQ05ybnF6T2EiLCJtYWMiOiJiOTFlYWU5M2E2YjdlZThmMmU3OGQ2NTQ3MDQxYWRhN2E5NjQ4MTdjZDE1YWZmNDNkN2Q0NTRmZWUyNjY0ZTY3IiwidGFnIjoiIn0%3D'
}

all_data = []

for page in range(1, 21):
    url = f'https://cargothai.tech/backoffice?limit=50&page={page}'
    r = requests.get(url, cookies=cookies)
    
    match = re.search(r'let containers = ({.*?});', r.text, re.DOTALL)
    if match:
        data = json.loads(match.group(1))
        records = data.get('data', [])
        all_data.extend(records)
        print(f"Page {page}: ได้ {len(records)} รายการ")
    else:
        print(f"Page {page}: ไม่เจอข้อมูล หยุดแล้ว")
        break

with open('containers.json', 'w', encoding='utf-8') as f:
    json.dump(all_data, f, ensure_ascii=False, indent=2)

print(f"\nรวม: {len(all_data)} รายการ บันทึกที่ containers.json")