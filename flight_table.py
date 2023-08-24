from prettytable import PrettyTable

class FlightTableList:
    def __init__(self, location, team1, team2, timing):
        self.location = location
        self.team1 = team1
        self.team2 = team2
        self.timing = timing

class FlightTableDatabase:
    def __init__(self):
        self.matches = []

    def add_match(self, match):
        self.matches.append(match)

    def list_matches_by_team(self, team_name):
        return [match for match in self.matches if team_name.lower() in (match.team1.lower(), match.team2.lower())]

    def list_matches_by_location(self, location_name):
        return [match for match in self.matches if location_name.lower() == match.location.lower()]

    def list_matches_by_timing(self, timing_name):
        return [match for match in self.matches if timing_name.lower() == match.timing.lower()]

    def get_all_matches(self):
        return self.matches

def main():
    match_db = FlightTableDatabase()

    match_db.add_match(FlightTableList("Mumbai", "India", "Sri Lanka", "DAY"))
    match_db.add_match(FlightTableList("Delhi", "England", "Australia", "DAY-NIGHT"))
    match_db.add_match(FlightTableList("Chennai", "India", "South Africa", "DAY"))
    match_db.add_match(FlightTableList("Indore", "England", "Sri Lanka", "DAY-NIGHT"))
    match_db.add_match(FlightTableList("Mohali", "Australia", "South Africa", "DAY-NIGHT"))
    match_db.add_match(FlightTableList("Delhi", "India", "Australia", "DAY"))

    while True:
        print("Choose a search parameter:")
        print("1. List of all the matches of a Team")
        print("2. List of Matches on a Location")
        print("3. List of Matches based on timing")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            team_name = input("Enter the team name: ")
            team_matches = match_db.list_matches_by_team(team_name)
            display_matches(team_matches)

        elif choice == '2':
            location_name = input("Enter the location: ")
            location_matches = match_db.list_matches_by_location(location_name)
            display_matches(location_matches)

        elif choice == '3':
            timing_name = input("Enter the timing: ")
            timing_matches = match_db.list_matches_by_timing(timing_name)
            display_matches(timing_matches)

        elif choice == '4':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please select a valid option.")

def display_matches(matches):
    table = PrettyTable()
    table.field_names = ["Match Location", "Team 01", "Team 02", "Timing"]

    for match in matches:
        table.add_row([match.location, match.team1, match.team2, match.timing])

    print(table)

if __name__ == "__main__":
    main()