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

// $(function() {
// 	$(document).ready(function() {
// 		$.fn.datepicker.default.language = 'it'
// 	})
// })

// $(function() {
// 	$(document).ready(function() {
// 		$('.datepicker').datepicker()
// 	})
// })

$(function() {
	$('.delete-btn').on('click', function() {
		var csrftoken = getCookie('csrftoken')
		if (confirm('¿Desea eliminar esta vacuna?') == true) {
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

function getCookie(name) {
	// Permite obtener el token de django
	var cookieValue = null
	if (document.cookie && document.cookie != '') {
		var cookies = document.cookie.split(';')
		for (var i = 0; i < cookies.length; i++) {
			var cookie = jQuery.trim(cookies[i])
			if (cookie.substring(0, name.length + 1) == name + '=') {
				cookieValue = decodeURIComponent(
					cookie.substring(name.length + 1)
				)
				break
			}
		}
	}
	return cookieValue
}
