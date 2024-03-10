import json

cats_dict = {
    'name': 'Pushin',
    'age': 1,
    'meals': [
        'Purina', 'Cat Chow', 'Hills'
    ],
    'owners': [
        {
            'first_name': 'Bill',
            'last_name': 'Gates'
        },
        {
            'first_name': 'Melinda',
            'last_name': 'Gates'
        }
    ]
}

with open('cats_and_owners_json.json', 'w') as file:
    json.dump(cats_dict, file, ensure_ascii=True)

