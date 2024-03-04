// function updateAvatarPreview(part, filename) {
//     document.getElementById("avatar-preview-" + part).src = "emoji-assets/" + part + "/" + filename + ".png";
// }

class TabSwitcher {
    constructor(currentTab) {
        this.currentTab = currentTab;
    }
    switchTabAuto(tab) {
        console.log(tab)
        document.getElementById(this.currentTab).style.visibility = "hidden";
        document.getElementById(tab).style.visibility = "visible";
        this.currentTab = tab;
    }

    switchTabManual(currentTab, newTab) {
        // used when tab switch has been triggered by reload/a different script
        // as this.currentTab becomes de-synced
        document.getElementById(currentTab).style.visibility = "hidden";
        document.getElementById(newTab).style.visibility = "visible";
        this.currentTab = newTab;
    }
}

let shop = new TabSwitcher("shop-colour-tab");
// let pairsGame = new TabSwitcher("start-screen");
// let leaderboard = new TabSwitcher("total");