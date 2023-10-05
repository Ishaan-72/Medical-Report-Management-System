
const signupButton = document.getElementById("sign-up");

const main = document.getElementById("main");
const createacct = document.getElementById("create-acct");


const returnBtn = document.getElementById("return-btn");



signupButton.addEventListener("click", function() {
    main.style.display = "none";
    createacct.style.display = "block";
    console.log("You clicked");
});

returnBtn.addEventListener("click", function() {
    main.style.display = "block";
    createacct.style.display = "none";
});