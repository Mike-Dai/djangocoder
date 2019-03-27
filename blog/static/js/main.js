function showPic(whichpic) {
	var source = whichpic.getAttribute("href");
	var placeholder = document.getElementById("placeholder");
	placeholder.setAttribute("src", source);
	return false;
}

function showPlaceholder() {
	var username = document.getElementById("username");
	username.setAttribute("placeholder", "username");
	username.setAttribute("height", "200px");
	var password = document.getElementById("password");
	password.setAttribute("placeholder", "password");
	password.setAttribute("height", "200px");
}

