$(function() {
	$('.delete-btn').on('click', function() {
		var csrftoken = getCookie('csrftoken')
		if (
			confirm(
				'¿Desea eliminar esta ficha?\nSe eliminará la ficha de esta mascota junto con toda su información. También se eliminará la información del dueño en caso de que este no posea otras mascotas.'
			) == true
		) {
			$.ajax({
				type: 'POST',
				url: '/files/delete_file/',
				data: {
					pet_id: $(this).val(),
					csrfmiddlewaretoken: csrftoken
				},
				dataType: 'json',
				success: function deleteCard(data) {
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
