let questionNum = 0;
let questionList = document.querySelectorAll(".question-panel");
console.log(questionList);

function isAnswered(question) {
    // check that one of the question's answers has been selected
    let answerList = question.querySelectorAll("fieldset > div > input");
    console.log(answerList);
    let i = 0;
    answered = false;
    while (answered == false && i < answerList.length)
    {
        if (answerList[i].checked == true) {
            answered = true;
        }
        i++;
    }
    console.log(answered)
    return answered;
}

function nextQuestion() {
    currQuestion = questionList[questionNum];
    // ensure that the current question has been answered before proceeding
    if (isAnswered(currQuestion)) {
        // hide current question and display next one
        currQuestion.style.visibility = "hidden";
        questionNum++;
        if (questionNum == questionList.length -1) {
            // remove "next" button for last question
            let nextButton = document.querySelector("#next-q-button");
            nextButton.style.display = "none";
        }
        questionList[questionNum].style.visibility = "visible";
    } else {
        // TODO add "no answer" error message
    }      
}