from collections import OrderedDict

"""
Problem Statement:
Write a Python program to store football player information by team, 
track goals scored, and generate sorted results.

Requirements:
1. For each player, ask the user to enter:
   - First and last name
   - Team name
   - Jersey number
   - Number of goals scored
2. Goals must be a positive integer.
3. Store:
   - Teams and their players
   - Total goals per team
   - Total goals per player
4. After inputs, sort and display:
   - Teams alphabetically
   - Players alphabetically by last name
   - Players sorted by goals
   - Teams sorted by total goals
"""

class FootBall:
    def __init__(self):
        self.roster = {}              # {team: [[name, jersey], ...]}
        self.team_scores = {}         # {team: total_goals}
        self.alphabetical_players = [] # [[first, last], ...]
        self.player_goals = []        # [[name, goals], ...]
        
        self.read_inputs()
        self.process_data()

    def read_inputs(self):
        name = input("Enter player first and last name: ")
        team = input("Enter team name: ")
        jersey = input("Enter jersey number: ")
        goals = int(input("Enter number of goals: "))

        if goals < 0:
            print("Goals must be a positive number.")
            return self.read_inputs()

        # Add team if not present
        if team not in self.roster:
            self.roster[team] = [[name, jersey]]
            self.team_scores[team] = goals
        else:
            self.roster[team].append([name, jersey])
            self.team_scores[team] += goals

        # Store for alphabetical sorting
        first, last = name.split()
        self.alphabetical_players.append([first, last])

        # Store player goals
        self.player_goals.append([name, goals])

        proceed = input("Enter 1 to add another player, any other key to finish: ")
        if proceed == "1":
            self.read_inputs()

    def process_data(self):
        # Sort teams alphabetically
        self.roster = OrderedDict(sorted(self.roster.items()))

        # Sort players inside each team by jersey number
        for team in self.roster:
            self.roster[team].sort(key=lambda x: x[1])

        # Sort all players alphabetically by last name
        self.alphabetical_players.sort(key=lambda x: x[1])

        # Sort players by goals (highest first)
        self.player_goals.sort(key=lambda x: x[1], reverse=True)

        # Sort teams by total goals (highest first)
        self.sorted_team_scores = sorted(
            self.team_scores.items(), key=lambda x: x[1], reverse=True
        )

# Run program
obj = FootBall()
