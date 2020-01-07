var globalResizeTimer = null

document.addEventListener('DOMContentLoaded', function() {
	resizeTextareas()
})

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
