class Player:
    def __init__(self, PlayerID, LastName, FirstName, Position, GamesPlayed, TotalPoints):
        self.PlayerID = PlayerID
        self.LastName = LastName
        self.FirstName = FirstName
        self.Position = Position
        self.GamesPlayed = GamesPlayed
        self.TotalPoints = TotalPoints

    def setLastName(self, LastName):
        self.LastName = LastName

    def setFirstName(self, FirstName):
        self.FirstName = FirstName

    def setPosition(self, Position):
        self.Position = Position

    def setGamesPlayed(self, newGame):
        self.GamesPlayed = newGame

    def setTotalPoints(self, newPoints):
        self.TotalPoints = newPoints

