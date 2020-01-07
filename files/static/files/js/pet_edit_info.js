document.addEventListener('DOMContentLoaded', function() {
	adjustCheckboxes()
})

function adjustCheckboxes() {
	var divElem = document.getElementById('castration-date-container')
	if (castrated == 'false') {
		divElem.style.display = 'none'
	}

	id_castrated.addEventListener('click', function() {
		var divCheckbox = document.getElementById('castration-date-container')
		if (this.checked) divCheckbox.style.display = 'flex'
		else divCheckbox.style.display = 'none'
	})
}
