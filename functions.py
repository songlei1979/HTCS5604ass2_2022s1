import mysql.connector

from Player import Player


def connectToDB():
    """
    @return cnx: Object
    """
    try:
        cnx = mysql.connector.connect(
            user="gr5vdosuy02bdw37",
            password="s1kfs3zf2r81hvgp",
            host="s29oj5odr85rij2o.cbetxkdyhwsb.us-east-1.rds.amazonaws.com",
            database="iat7z0k6ucbsefeh"
        )
        return cnx
    except:
        print("not connected")
        return None


def allPlayers(cnx):
    """
    @param cnx: Object
    @return players: List
    """
    players = []
    cursor = cnx.cursor()
    cursor.execute("SELECT * FROM player")
    results = cursor.fetchall()
    for result in results:
        playID = result[0]
        lastname = result[1]
        firstname = result[2]
        position = result[3]
        gamesPlayed = result[4]
        totalPoints = result[5]
        player = Player(playID, lastname, firstname, position, gamesPlayed, totalPoints)
        players.append(player)
    return players


def printAPlayer(player):
    """
    @param player: object
    """
    player = player.__dict__
    print("Player ID: " + str(player["PlayerID"]))
    print("Lastname: " + player["LastName"])
    print("FirstName: " + player["FirstName"])
    print("Position: " + player["Position"])
    print("Games Played: " + str(player["GamesPlayed"]))
    print("Total Points: " + str(player["TotalPoints"]))
    print("#" * 20)


def aPlayers(cnx, playerID):
    """
    @param cnx: Object
    @return player: Object
    """
    player = None
    cursor = cnx.cursor()
    cursor.execute("SELECT * FROM player where playerID = " + playerID)
    results = cursor.fetchall()
    if len(results) == 1:
        for result in results:
            playID = result[0]
            lastname = result[1]
            firstname = result[2]
            position = result[3]
            gamesPlayed = result[4]
            totalPoints = result[5]
            player = Player(playID, lastname, firstname, position, gamesPlayed, totalPoints)
    return player


def displayPlayersReport():
    """
        This function integrated connectToDB() and allPlayers()
        There is no param and return
    """
    cnx = connectToDB()
    players = allPlayers(cnx)
    print("####Display Players Report####")

    for player in players:
        printAPlayer(player)
    cnx.close()


def isAInt(number):
    """
    @param number: Integer
    @return: Boolean
    """
    try:
        int(number)
        return True
    except:
        return False


def searchAPlayer(playerID):
    """
    @param playerID: Integer
    @return gotAPlayer: Boolean
    """
    gotAPlayer = False
    cnx = connectToDB()
    player = aPlayers(cnx, playerID)
    if player is None:
        print("There is no player ID " + str(playerID))
    else:
        printAPlayer(player)
        gotAPlayer = True
    cnx.close()
    return gotAPlayer


def showMenu():
    """
    """
    print("""
        1. Search Player
        2. Add a Player
        3. Delete a player
        4. Update a player
        5. Display players report
        6. Exit
    """)


def isValidChoice(choice):
    """
    @param choice: String
    @return valid: Bool
    """
    if choice in ["1", "2", "3", "4", "5", "6"]:
        return True
    return False


def isValidName(name):
    if 0 < len(name) <= 30:
        return True
    return False


def isValidPosition(position):
    if position in ["Guard", "Forward", "Centre"]:
        return True
    return False


def isValidInputNumber(number, minNum, maxNum):
    if minNum <= int(number) <= maxNum:
        return True
    return False


def verifyInputPlayerData():
    ## 1. lastname
    isNotValidName = True
    while isNotValidName:
        lastname = input("please input lastname: ")
        if isValidName(lastname):
            isNotValidName = False
        else:
            print("please input a valid lastname")

    ## 2. firstname
    isNotValidName = True
    while isNotValidName:
        firstname = input("please input firstname: ")
        if isValidName(firstname):
            isNotValidName = False
        else:
            print("please input a valid firstname")

    ## 3. Position
    isNotValidPosition = True
    while isNotValidPosition:
        position = input("please input position (Guard, Forward, Centre): ")
        if isValidPosition(position):
            isNotValidPosition = False
        else:
            print("please input a valid position (Guard, Forward, Centre)")

    ## 4. GamesPlayed
    isNotValidGamesPlayed = True
    while isNotValidGamesPlayed:
        gamesPlayed = input("please input games played (0-200): ")
        if isAInt(gamesPlayed):
            if isValidInputNumber(gamesPlayed, 0, 200):
                isNotValidGamesPlayed = False
        else:
            print("please input a valid games played (0-200)")

    ## 5. totalPoints
    isNotValidTotalPoints = True
    while isNotValidTotalPoints:
        totalPoints = input("please input total points (0-2000)")
        if isAInt(totalPoints):
            if isValidInputNumber(totalPoints, 0, 2000):
                isNotValidTotalPoints = False
        else:
            print("please input a valid total points")

    return lastname, firstname, position, gamesPlayed, totalPoints


def insertAPlayer(cnx, LastName, FirstName, Position, GamesPlayed, TotalPoints):
    try:
        cursor = cnx.cursor()
        sql = "INSERT INTO player VALUES " \
              "(Null, '" + LastName + "', '" + FirstName + "', " \
                                                           "'" + Position + "', " + str(GamesPlayed) + ", " + str(
            TotalPoints) + ");"
        cursor.execute(sql)
        cnx.commit()
        print(LastName + " has been inserted into database")
        return True
    except:
        return False


def deletePlayer(cnx, playerID):
    cursor = cnx.cursor()
    sql = "Delete from player where playerID = " + playerID
    cursor.execute(sql)
    cnx.commit()
    print("player " + playerID + " has been deleted from database")


def updatePlayer(cnx, playerID, LastName, FirstName, Position, GamesPlayed, TotalPoints):
    cursor = cnx.cursor()
    sql = "UPDATE player SET " \
          "lastname='" + LastName + "'," \
          "firstname='" + FirstName + "'," \
          "position='" + Position + "'," \
          "gamesPlayed=" + GamesPlayed + "," \
          "totalPoints=" + TotalPoints + " " \
          "WHERE playerID= " + playerID
    cursor.execute(sql)
    cnx.commit()
    print("player " + playerID + " has been updated in database")


###### Final Integrated Functions #########
def integrated_searchPlayer():
    """
        This function integrated all units functions for search player
    """
    gotAPlayer = False
    while gotAPlayer == False:
        playerID = input("Please input a player ID: ")
        if isAInt(playerID):
            gotAPlayer = searchAPlayer(playerID)
        else:
            print("Please inter a number")


def integrated_insertPlayer():
    """
        This function integrated all units functions for insert a player
    """
    notInserted = True
    while notInserted:
        lastname, firstname, position, gamesPlayed, totalPoints = verifyInputPlayerData()
        cnx = connectToDB()
        insertAPlayer(cnx, lastname, firstname, position, gamesPlayed, totalPoints)
        cnx.close()
        notInserted = False


def integrated_deletePlayer():
    isNotValidPlayerID = True
    while isNotValidPlayerID:
        playerID = input("please input a player ID: ")
        if isAInt(playerID):
            cnx = connectToDB()
            player = aPlayers(cnx, playerID)
            if player is not None:
                deletePlayer(cnx, playerID)
                cnx.close()
                isNotValidPlayerID = False
            else:
                print("player ID is not exist")
        else:
            print("please input a valid player ID.")


def integrated_updatePlayer():
    isNotValidPlayerID = True
    while isNotValidPlayerID:
        playerID = input("please input a player ID: ")
        if isAInt(playerID):
            cnx = connectToDB()
            player = aPlayers(cnx, playerID)
            if player is not None:
                lastname, firstname, position, gamesPlayed, totalPoints = verifyInputPlayerData()
                updatePlayer(cnx, playerID, lastname, firstname, position, gamesPlayed, totalPoints)
                cnx.close()
                isNotValidPlayerID = False
            else:
                print("player ID is not exist")
        else:
            print("please input a valid player ID.")


def selectAfunction(option):
    if option == "1":
        integrated_searchPlayer()
    elif option == "2":
        integrated_insertPlayer()
    elif option == "3":
        integrated_deletePlayer()
    elif option == "4":
        integrated_updatePlayer()
    elif option == "5":
        displayPlayersReport()
    elif option == "6":
        exit()
