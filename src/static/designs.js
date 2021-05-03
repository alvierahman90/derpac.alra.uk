
function vote(e) {
	console.log(this.dataset.id)
	unvoteAll()
	el = this
	votePOSTRequest(this.dataset.id, function (){
		el.getElementsByClassName("vote_text")[0].innerHTML = "thanks!"
		el.classList.add('voted')
	})
}

function unvoteAll() {
	[...document.getElementsByClassName("design")].forEach( el => {
		el.classList.remove('voted')
		p = el.getElementsByClassName("vote_text")[0]
		if (p.innerHTML == "thanks!") p.innerHTML = ":("
		else p.innerHTML = "vote me!"
	})
}

function votePOSTRequest(design, callback) {
	var xhttp = new XMLHttpRequest();
	  xhttp.onreadystatechange = function() {
		if (this.readyState == 4 && this.status == 200) callback()
	}
	xhttp.open("GET", "/designs/vote/" + design, true);
	xhttp.send()
}

[...document.getElementsByClassName("design")].forEach( el =>
	el.addEventListener('click', vote)
)
