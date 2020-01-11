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
				success: function reload() {
					location.reload()
				}
			})
		}
	})
})
