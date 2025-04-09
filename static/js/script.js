// BaseURL = "http://127.0.0.1:5000/"
BaseURL = "https://htcs-5604ass2-2022s1.vercel.app/"
//BaseURL = "https://htcs5604ass2-2023s1.onrender.com/"

function isValidName(name){
    if (name.length === 0 || name.length > 30){
        alert("Invalid name")
        return false;
    }
    return true
}

function isValidPosition(position){
    if ((position == "Guard") || (position = "Forward") || (position == "Centre")){
        return true;
    }
    alert("Invalid position")
    return false
}

function isValidGamesPlayed(gamePlayed){
    if (Number(gamePlayed) >=0 && Number(gamePlayed) <= 200){
        return true
    }
    alert("Invalid Game Played")
    return false
}

function isValidTotalPoints(totalPoints){
    if (Number(totalPoints) >=0 && Number(totalPoints) <= 2000){
        return true
    }
    alert("Invalid Total Points")
    return false
}
