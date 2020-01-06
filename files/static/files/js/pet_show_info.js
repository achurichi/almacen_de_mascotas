var globalResizeTimer = null

document.addEventListener('DOMContentLoaded', function() {
	adjustCheckboxes()
	resizeTextareas()
})

function adjustCheckboxes() {
	var checkbox_castrated = document.getElementById('checkbox-castrated')
	var divElem = document.getElementById('castration-date-container')
	if (castrated == 'true') {
		checkbox_castrated.checked = 'true'
	} else {
		divElem.style.display = 'none'
	}

	var checkbox_aggressive = document.getElementById('checkbox-aggressive')
	if (aggressive == 'true') {
		checkbox_aggressive.checked = 'true'
	}
}

function resizeTextareas() {
	var textareas = document.getElementsByClassName('large-text')
	Array.prototype.forEach.call(textareas, function(textarea) {
		textarea.style.height = '1px'
		textarea.style.height = textarea.scrollHeight + 'px'
	})
}

$(function() {
	$(window).resize(function() {
		if (globalResizeTimer != null) window.clearTimeout(globalResizeTimer)
		globalResizeTimer = window.setTimeout(function() {
			resizeTextareas()
		}, 50)
	})
})
