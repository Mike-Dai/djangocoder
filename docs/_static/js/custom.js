var button = document.getElementById('post--pet');

button.onclick = function() {
	var parameters = document.getElementById('parameters');
	var responses = document.getElementById('responses');
	if (parameters.style.display !== 'none') {
		parameters.style.display = 'none';
	}
	else {
		parameters.style.display = 'block';
	}
	if (responses.style.display !== 'none') {
		responses.style.display = 'none';
	}
	else {
		responses.style.display = 'block';
	}
}