var newBtn
var createBtn
var cancelBtn

document.addEventListener('DOMContentLoaded', function() {
	newBtn = document.getElementById('new')
	createBtn = document.getElementById('create-btn')
	cancelBtn = document.getElementById('cancel-btn')

	configEventListeners()
})

function configEventListeners() {
	newBtn.addEventListener('click', function() {
		document.getElementById('data-form').style.display = 'flex'
		document.getElementById('new').style.display = 'none'
	})

	cancelBtn.addEventListener('click', function() {
		document.getElementById('data-form').style.display = 'none'
		document.getElementById('new').style.display = 'flex'
	})
}

$(function() {
	$('.delete-btn').on('click', function() {
		var csrftoken = getCookie('csrftoken')
		if (confirm('¿Desea eliminar este registro del historial?') == true) {
			$.ajax({
				type: 'POST',
				url: '/files/delete_vaccination_history/',
				data: {
					vaccinationHistory_id: $(this).val(),
					csrfmiddlewaretoken: csrftoken
				},
				dataType: 'json',
				success: function reload() {
					location.reload()
				}
			})
		}
	})
})
