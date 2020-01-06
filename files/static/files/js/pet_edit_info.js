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
	})
})
