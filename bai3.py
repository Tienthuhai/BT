
class Player:
    def __init__(self, name: str, endurance: int, sprint: int, dribble: int, passing: int, shooting: int):
        self.__name = name
        self.__endurance = endurance
        self.__sprint = sprint
        self.__dribble = dribble
        self.__passing = passing
        self.__shooting = shooting

   
    def get_name(self):
        return self.__name

    def get_stats(self):
        return {
            "Endurance": self.__endurance,
            "Sprint": self.__sprint,
            "Dribble": self.__dribble,
            "Passing": self.__passing,
            "Shooting": self.__shooting
        }

    
    def __str__(self):
        stats = self.get_stats()
        stats_info = "\n".join([f"{key}: {value}" for key, value in stats.items()])
        return f"Player: {self.__name}\n{stats_info}\n"


class Team:
    def __init__(self, name: str, rating: int):
        self.__name = name
        self.__rating = rating
        self.__players = {}

    
    def get_name(self):
        return self.__name

    def get_rating(self):
        return self.__rating

    def get_players(self):
        return list(self.__players.values())

    
    def add_player(self, player: Player):
        if player.get_name() in self.__players:
            return f"Player {player.get_name()} has already joined"
        self.__players[player.get_name()] = player
        return f"Player {player.get_name()} joined team {self.__name}"

    
    def remove_player(self, player_name: str):
        if player_name in self.__players:
            removed_player = self.__players.pop(player_name)
            return removed_player
        return f"Player {player_name} not found"

    
    def __str__(self):
        players_info = "\n".join([str(player) for player in self.get_players()])
        return f"Team: {self.__name}\nRating: {self.__rating}\nPlayers:\n{players_info}"


player1 = Player("Tien", 80, 90, 85, 75, 88)
player2 = Player("Tung", 78, 85, 90, 80, 92)
team = Team("MU", 90)
print(team.add_player(player1)) 
print(team.add_player(player2))  
print(team)
print(team.remove_player("Tien")) 
print(team.remove_player("Unknown Player"))  
print(team)
