from flask import Flask, render_template, request
import simplejson as json

from functions import connectToDB, aPlayers, allPlayers, deletePlayer, updatePlayer, insertAPlayer
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)
####html pages#####
@app.route('/')
def home():  # put application's code here
    return render_template('home.html')

@app.route('/searchplayerurl')
def searchplayerview():
    return render_template('searchplayer.html')

@app.route('/playersreporturl')
def playersreportview():
    return render_template('playersreport.html')

@app.route('/deleteplayerurl')
def deleteplayerview():
    return render_template('deleteplayer.html')

@app.route('/updateplayerurl')
def updateplayerview():
    return render_template('updateplayer.html')

@app.route('/addplayerurl')
def addplayerview():
    return render_template('addplayer.html')

####API functions####
@app.route('/searchplayer/<playerid>')
def searchAPlayer(playerid):
    cnx = connectToDB()
    player = aPlayers(cnx, playerid)
    if player is None:
        return None
    else:
        print(player.__dict__)
        return json.dumps(player.__dict__)
    cnx.close()

@app.route('/playersreport')
def playersreport():
    cnx = connectToDB()
    players = allPlayers(cnx)
    newPlayers = []
    for player in players:
        newPlayers.append(player.__dict__)
    return json.dumps(newPlayers)

@app.route('/deleteplayer/<playerid>')
def deleteAPlayer(playerid):
    cnx = connectToDB()
    deletePlayer(cnx, playerid)
    cnx.close()
    return json.dumps("Player " + str(playerid) + " has been deleted")

@app.route('/updateplayer', methods=['POST'])
def updatePlayerFun():
    data = request.form.to_dict()
    playerID = data['playerID']
    lastName = data['lastname']
    firstName = data['firstname']
    position = data['position']
    gamesPlayed = data['gamePlayed']
    totalPoints = data['totalPoints']
    cnx = connectToDB()
    updatePlayer(cnx, playerID, lastName, firstName, position, gamesPlayed, totalPoints)
    cnx.close()
    return json.dumps("Player " + lastName + " has been updated")

@app.route('/addplayer', methods=['POST'])
def addPlayerFun():
    data = request.form.to_dict()
    lastName = data['lastname']
    firstName = data['firstname']
    position = data['position']
    gamesPlayed = data['gamePlayed']
    totalPoints = data['totalPoints']
    cnx = connectToDB()
    insertAPlayer(cnx, lastName, firstName, position, gamesPlayed, totalPoints)
    cnx.close()
    return json.dumps("Player " + lastName + " has been add to database.")



if __name__ == '__main__':
    app.run()
