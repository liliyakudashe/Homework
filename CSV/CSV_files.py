import csv


def write_holiday_cities(first_letter):
    visited_cities = set()
    want_to_visit = set()
    all_cities = set()
    first_city = None

    with open('travel_notes.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            name, visited, want = row[0], row[1].split(';'), row[2].split(';')
            if name.startswith(first_letter):
                visited_cities.update(visited)
                want_to_visit.update(want)
                all_cities.update(visited)
                all_cities.update(want)
                if not first_city:
                    first_city = sorted(all_cities)[0]

    not_visited = sorted(all_cities - visited_cities)
    want_to_visit_but_not_visited = sorted(want_to_visit - visited_cities)

    with open('holiday.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Посетили:'] + sorted(visited_cities))
        writer.writerow(['Хотят посетить:'] + sorted(want_to_visit))
        writer.writerow(['Никогда не были в:'] + not_visited)
        writer.writerow(['Следующим городом будет:'] + [first_city])


write_holiday_cities('L')