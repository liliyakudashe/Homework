import json


def employees_rewrite(sort_type):
    valid_keys = {'firstName', 'lastName', 'department', 'salary'}
    if sort_type not in valid_keys:
        raise ValueError('Bad key for sorting')

    with open('employees.json', 'r') as file:
        data = json.load(file)

    sorted_data = sorted(data['employees'], key=lambda x: x[sort_type])

    with open(f'employees_{sort_type}_sorted.json', 'w') as file:
        json.dump({'employees': sorted_data}, file, indent=2)


employees_rewrite('lastName')
