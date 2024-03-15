let currentGame = null;
let isRegisteredSession= false;

levelVariables = [
    {"numOfSets": 3, "numToMatch": 2, "gridFormation": "auto auto auto",
        "maxExpectedTime": 18, "maxExpectedAttempts": 6, "difficultyWarning": ""},
    {"numOfSets": 4, "numToMatch": 2, "gridFormation": "auto auto auto auto",
        "maxExpectedTime": 24, "maxExpectedAttempts": 11, "difficultyWarning": ""},
    {"numOfSets": 6, "numToMatch": 2, "gridFormation": "auto auto auto auto",
        "maxExpectedTime": 35, "maxExpectedAttempts": 15, "difficultyWarning": ""},
    {"numOfSets": 8, "numToMatch": 2, "gridFormation": "auto auto auto auto",
        "maxExpectedTime": 60, "maxExpectedAttempts": 20, "difficultyWarning": ""},
    {"numOfSets": 9, "numToMatch": 2, "gridFormation": "auto auto auto auto auto auto",
        "maxExpectedTime": 90, "maxExpectedAttempts": 36, "difficultyWarning": ""},
    {"numOfSets": 6, "numToMatch": 3, "gridFormation": "auto auto auto auto auto auto",
        "maxExpectedTime": 120, "maxExpectedAttempts": 36, "difficultyWarning": "Enough of pairs - now match 3!"},
    {"numOfSets": 8, "numToMatch": 3, "gridFormation": "auto auto auto auto auto auto",
        "maxExpectedTime": 138, "maxExpectedAttempts": 42, "difficultyWarning": ""},
    {"numOfSets": 6, "numToMatch": 4, "gridFormation": "auto auto auto auto auto auto",
        "maxExpectedTime": 210, "maxExpectedAttempts": 50, "difficultyWarning": "Final level - time to match 4!"},
    {"difficultyWarning": ""}
];

// leave "normal" out of set because it's too similar to "long" and might lead to confusion for the player
let eyesSet = ["dot", "default", "confused"];
let mouthSet = ["uwu"];
let skinSet = ["earth", "pink", "purple", "sky_blue", "turquoise", "default_green"];

const gameplayScreen = document.getElementById("gameplay-screen");
const levelTransition = document.getElementById("level-transition");
const cardsGrid = document.getElementById("cards-grid");
const levelElem = document.getElementById("level");
const scoreElem = document.getElementById("score");
const attemptsElem = document.getElementById("attempts");
const timeElem = document.getElementById("time");
const numToMatchElem = document.getElementById("numToMatch");
const totalScoreElem = document.getElementById("total-score");
const difficultyWarningElem = document.getElementById("difficulty-warning");
const basePointsElem = document.getElementById("base-points");
const attemptsBonusElem = document.getElementById("attempts-bonus");
const timeBonusElem = document.getElementById("time-bonus");
const levelTotalElem = document.getElementById("level-total");
const scoreSummaryELem = document.getElementById("score-summary");

class Game {
   constructor() {
       this.level = 0;
       this.score = 0;
       this.totalScore = 0;
       this.attempts = 0;
       this.timeInS = 0;
       this.numOfSets = 3;
       this.numToMatch = 4;
       this.pointsPerCard = 5;
       this.remainingCards = 6;
       this.numFlippedThisTurn = 0;
       this.flippedCards = [null, null, null, null];
       this.scoreSummary = ""
       this.timer = function() {
           // this is a placeholder declaration
       }
       cardsGrid.addEventListener("click", (e) => {this.listenForCardFlip(e)});
       this.initLevel();
   }
    generateRandomEmoji() {
        let emoji = "";
        let index = Math.floor(Math.random() * 5);
        emoji += eyesSet[index] + "/";
        index = Math.floor(Math.random() * 6);
        emoji += mouthSet[index] + "/";
        index = Math.floor(Math.random() * 3);
        emoji += skinSet[index];
        return emoji;
    }
    updateScoreDisplay() {
        scoreElem.innerText = String(this.score);
    }
    showCardFront(cardBack) {
        cardBack.style = "visibility: hidden";
        cardBack.nextElementSibling.style = "visibility: visible";
		// add selected card to the list of cards flipped this turn
        this.flippedCards[this.numFlippedThisTurn] = cardBack.parentElement;
        this.numFlippedThisTurn ++;
    }
    hideCardFront(card) {
        card.firstElementChild.style = "visibility: visible";
        card.lastElementChild.style = "visibility: hidden";
    }

    resetForNextTurn() {
        for (let i = 0; i < this.numToMatch; i++) {
            this.hideCardFront(this.flippedCards[i]);
        }
        this.numFlippedThisTurn = 0;
        this.flippedCards = [null, null, null, null];
    }

    timerFunction() {
        this.timeInS++;
        let minutes = String(Math.floor(this.timeInS / 60));
        let seconds = String(this.timeInS - minutes * 60);
        if (seconds.length == 1) {
            seconds = "0" + seconds;
        }
        timeElem.innerHTML = minutes + ":" + seconds;
    }
    initLevel() {
        // set up new level variables
        this.level = cardLevel; // Initialize this.level with cardLevel
        let currentLevelVars = levelVariables[this.level]; // Using cardLevel as the index
        this.level++;
        this.numOfSets = currentLevelVars.numOfSets;
        this.numToMatch = currentLevelVars.numToMatch;
        if (this.numToMatch == 3) {
            this.pointsPerCard = 10;
        } else if (this.numToMatch == 4) {
            this.pointsPerCard = 20;
        }
        this.remainingCards = this.numOfSets * this.numToMatch;
        // update elements to fit level
        levelElem.innerText = "Level: " + String(this.level);
        numToMatchElem.innerText = "Match: " + String(this.numToMatch);
        cardsGrid.style.gridTemplateColumns = currentLevelVars.gridFormation;
        // generate cards
        let cards = [];
        for (let i = 0; i < this.numOfSets; i++) {
            let newCard = this.generateRandomEmoji();
            // prevent inclusion of identical card sets
            while (cards.includes(newCard)) {
                newCard = this.generateRandomEmoji();
            }
            for (let n = 0; n < this.numToMatch; n++) {
                cards.push(newCard);
            }
        }
        // randomly add cards to grid
        let numToPlace = this.remainingCards;
        for (let i = 0; i < this.remainingCards; i++) {
            let cardIndex = Math.floor(Math.random() * numToPlace);
            // fetch randomly selected card and remove from selection pool
            let card = String(cards.splice(cardIndex, 1));
            card = card.split("/");
            let cardElem = document.createElement("div");
            cardElem.className = "card";
            cardElem.innerHTML = "\t<span class=\"back\" style=\"visibility: visible\"></span>\n" +
                "\t<div class=\"front\" style=\"visibility: hidden\">\n" +
                "\t\t<img class=\"stacked-emoji-eyes\" src=\"emoji-assets/eyes/" + card[0] + ".png\">\n" +
                "\t\t<img class=\"stacked-emoji-mouth\" src=\"emoji-assets/mouth/" + card[1] + ".png\">\n" +
                "\t\t<img class=\"stacked-emoji-skin\" src=\"emoji-assets/skin/" + card[2] + ".png\">\n" +
                "\t</div>\n</div>";
            cardsGrid.appendChild(cardElem);
            numToPlace--;
        }
        // reset level-specific HUD elements
        this.score = 0
        this.updateScoreDisplay()
        this.attempts = 0
        attemptsElem.innerText = String(0);
        this.timeInS = 0;
        this.timer = setInterval(function() {currentGame.timerFunction.call(currentGame)}, 1000);
    }
    listenForCardFlip(e){
        let elem = e.target;
        if (elem.className == "back" && this.numFlippedThisTurn < this.numToMatch) {
            this.showCardFront(elem);
            if (this.numFlippedThisTurn == this.numToMatch) {
                this.endTurn();
            }
        }
    }
    endLevel() {
        clearInterval(this.timer);
        // remove this level's cards from the grid
        cardsGrid.innerText = "";
        // calculate and add score bonuses
        let attemptsBonus = (levelVariables[this.level-1].maxExpectedAttempts - this.attempts) * 10;
        if (attemptsBonus < 0) {
            attemptsBonus = 0;
        }
        let timeBonus = (levelVariables[this.level-1].maxExpectedTime - this.timeInS) * 5;
        if (timeBonus < 0) {
            timeBonus = 0;
        }
        // format level transition text
        difficultyWarningElem.innerText = levelVariables[this.level].difficultyWarning;
        basePointsElem.innerHTML = "<span style='font-weight:bold'>\t" + this.score + "</span> base points";
        this.score += attemptsBonus + timeBonus;
        this.totalScore += this.score;
        totalScoreElem.innerText = this.totalScore;
        attemptsBonusElem.innerHTML = "<span style='font-weight:bold'>\t" + String(attemptsBonus) + "</span> attempts bonus";
        timeBonusElem.innerHTML = "<span style='font-weight:bold'>\t" + String(timeBonus) + "</span> time bonus";
        levelTotalElem.innerText = "Level Total: " + this.score;
        // update score summary if playing in registered session
        if (isRegisteredSession == true) {
            this.scoreSummary += String(this.score) + "/";
        }
        // show level transition after slight delay
        setTimeout(function () {
            gameplayScreen.style.visibility = "hidden";
            levelTransition.style.visibility = "visible";
        }, 100)
    }
    endGame() {
        // send score summary to form for php access
        this.scoreSummary += String(this.totalScore);
        scoreSummaryELem.value = this.scoreSummary;
        // format end screen text
        document.getElementById("final-score").innerText = "Final score: " + this.totalScore;
    }
    endTurn() {
		// check if flipped cards match by fetching and comparing their emoji components
        let successfulMatch = true;
        let cardFront = null;
		// 0 = eyes, 1 = mouth, 2 = skin
        let nextCardFrontCollection = this.flippedCards[0].lastElementChild.children;
        let nextCardFront = [nextCardFrontCollection.item(0).src,
            nextCardFrontCollection.item(1).src,
            nextCardFrontCollection.item(2).src];

        for(let i = 0; i < this.numToMatch-1; i++) {
            cardFront = nextCardFront;
            nextCardFrontCollection = this.flippedCards[i+1].lastElementChild.children;
            nextCardFront = [nextCardFrontCollection.item(0).src,
                nextCardFrontCollection.item(1).src,
                nextCardFrontCollection.item(2).src];

            if (! (cardFront[0] == nextCardFront[0]
                && cardFront[1] == nextCardFront[1]
                && cardFront[2] == nextCardFront[2])) {
                successfulMatch = false;
                break;
            }
        }
        // update hud sidebar
        this.attempts++;
        attemptsElem.innerText = String(this.attempts);
        if (successfulMatch == true) {
            this.score += this.pointsPerCard * this.numToMatch;
            this.updateScoreDisplay();
            this. numFlippedThisTurn = 0;
            this.flippedCards = [null, null, null, null];
            this.remainingCards -= this.numToMatch;
            if (this.remainingCards == 0) {
                if (this.level < 8) {
                    this.endLevel();
                } else {
                    if (isRegisteredSession == true) {
                        document.getElementById("level-transition-exit").innerHTML =
                            '<button onClick="currentGame.endGame();' +
                            'pairsGame.switchTabManual(\'level-transition\', \'end-screen\')">All done!'
                    } else {
                        document.getElementById("level-transition-exit").innerHTML =
                            '<h2>Thanks for playing!</h2>'
                    }
                    this.endLevel();
                }
            }
        } else {
            // delay to allow player to see the card designs before resetting
            setTimeout(function () {currentGame.resetForNextTurn.call(currentGame)}, 800);
        }
    }
}

function initNewGame() {
    // store reference to new game to allow referencing in anonymous functions
    currentGame = new Game()
}

function setAsRegistered() {
    isRegisteredSession = true;
}

