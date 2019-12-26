document.addEventListener('DOMContentLoaded', function() {
	adjustCheckbox()
	resizeTextareas()
})

function adjustCheckbox() {
	var checkbox = document.getElementById('checkbox-castrated')
	var divElem = document.getElementById('castration-date-container')

	if (castrated == 'true') {
		checkbox.checked = 'true'
	} else {
		divElem.style.display = 'none'
	}
}

function resizeTextareas() {
	var textareas = document.getElementsByClassName('large-text')
	Array.prototype.forEach.call(textareas, function(textarea) {
		textarea.style.height = '1px'
		textarea.style.height = textarea.scrollHeight - 4 + 'px'
	})
}
