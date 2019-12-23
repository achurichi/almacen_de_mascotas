checkbox = document.getElementById('id_castrated')

document.addEventListener('DOMContentLoaded', function() {
	var divElem = document.getElementById('castration-date-container')
	divElem.style.display = 'none'
})

checkbox.addEventListener('click', function() {
	var divElem = document.getElementById('castration-date-container')
	if (this.checked) divElem.style.display = 'flex'
	else divElem.style.display = 'none'
})
