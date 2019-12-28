$(function() {
	$('.delete-btn').on('click', function() {
		var csrftoken = getCookie('csrftoken')
		// Acá tiene que ir un botón para confirmar la eliminación de la ficha
		$.ajax({
			type: 'POST',
			url: '/files/delete_file/',
			data: {
				pet_id: $(this).val(),
				csrfmiddlewaretoken: csrftoken
			},
			dataType: 'json',
			success: function deleteCard(data) {
				var elem = document.getElementById('card-' + data['pet_id'])
				elem.parentNode.removeChild(elem)
			}
		})
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
