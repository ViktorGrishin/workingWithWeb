import json

with open('scoring.json', 'r') as file:
    data = json.load(file)

result = 0
for group in data['scoring']:
    cost = group["points"] // len(group["required_tests"])
    for test in group["required_tests"]:
        test_result = input()
        if test_result == 'ok':
            result += cost

print(result)
