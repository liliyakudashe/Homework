from datetime import datetime


class SuperDate(datetime):
    seasons = {
        1: "Winter",
        2: "Winter",
        3: "Spring",
        4: "Spring",
        5: "Spring",
        6: "Summer",
        7: "Summer",
        8: "Summer",
        9: "Autumn",
        10: "Autumn",
        11: "Autumn",
        12: "Winter"
    }

    def get_season(self):
        return self.seasons[self.month]

    def get_time_of_day(self):
        hour = self.hour
        if 6 <= hour < 12:
            return "Morning"
        elif 12 <= hour < 18:
            return "Day"
        elif 18 <= hour < 24:
            return "Evening"
        else:
            return "Night"


a = SuperDate(2024, 2, 22, 12)
print(a.get_season())
print(a.get_time_of_day())
