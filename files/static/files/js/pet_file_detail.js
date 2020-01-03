var firstTime = true

document.addEventListener('DOMContentLoaded', function() {
	adjustCheckboxes()
	resizeTextareas()
	adjustImgContainer()
	configEditButton()
})

function adjustCheckboxes() {
	var checkbox_castrated = document.getElementById('checkbox-castrated')
	var divElem = document.getElementById('castration-date-container')
	if (castrated == 'true') {
		checkbox_castrated.checked = 'true'
	} else {
		divElem.style.display = 'none'
	}

	id_castrated.addEventListener('click', function() {
		var divCheckbox = document.getElementById('castration-date-container')
		if (this.checked) divCheckbox.style.display = 'flex'
		else divCheckbox.style.display = 'none'
	})

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

function adjustImgContainer() {
	var container = document.getElementById('change-img-container')
	var div = document.createElement('div')
	div.id = 'clear-img-container'

	var input = document.getElementById('pet_img-clear_id')

	var labels = document.getElementsByTagName('LABEL'),
		lookup = {},
		i,
		label
	for (i = 0; i < labels.length; i++) {
		label = labels[i]
		if (document.getElementById(label.htmlFor)) {
			lookup[label.htmlFor] = label
		}
	}

	container.insertBefore(div, input)
	div.appendChild(lookup[input.id])
	div.appendChild(input)
}

function configEditButton() {
	document.getElementById('edit-btn').addEventListener('click', function() {
		var displayList = document.querySelectorAll('.set-display')
		var noDisplayList = document.querySelectorAll('.set-no-display')

		displayList.forEach(function(element) {
			element.classList.add('set-no-display')
			element.classList.remove('set-display')
		})

		noDisplayList.forEach(function(element) {
			element.classList.add('set-display')
			element.classList.remove('set-no-display')
		})

		var allergies_textarea = document.getElementById('allergies-textarea')
		var description_textarea = document.getElementById(
			'description-textarea'
		)
		var obs_textarea = document.getElementById('obs-textarea')

		var statusCheck = document.getElementById('status-check')
		if (statusCheck.classList.contains('set-display')) {
			allergies_textarea.classList.remove('textarea-container-row')
			description_textarea.classList.remove('textarea-container-row')
			obs_textarea.classList.remove('textarea-container-row')

			allergies_textarea.classList.add('textarea-container-col')
			description_textarea.classList.add('textarea-container-col')
			obs_textarea.classList.add('textarea-container-col')
		} else {
			allergies_textarea.classList.remove('textarea-container-col')
			description_textarea.classList.remove('textarea-container-col')
			obs_textarea.classList.remove('textarea-container-col')

			allergies_textarea.classList.add('textarea-container-row')
			description_textarea.classList.add('textarea-container-row')
			obs_textarea.classList.add('textarea-container-row')
		}
	})
}

$(function() {
	$('#data-form').submit(function(e) {
		if (document.getElementById('pet-id')) {
			document.getElementById('pet-id').value = pet_id
			document.getElementById('owner-id').value = owner_id
		} else {
			var petId = $('<input>')
				.attr('type', 'hidden')
				.attr('id', 'pet-id')
				.attr('name', 'pet_id')
				.val(pet_id)
			$('#data-form').append(petId)

			var ownerId = $('<input>')
				.attr('type', 'hidden')
				.attr('id', 'owner-id')
				.attr('name', 'owner_id')
				.val(owner_id)
			$('#data-form').append(ownerId)
		}

		$.post('/files/edit_file/', $(this).serialize(), function(data) {
			if (data['reload'] == true) location.reload()
		})
		e.preventDefault()
	})
})
