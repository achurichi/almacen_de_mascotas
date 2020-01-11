$(function() {
	$('.delete-btn').on('click', function() {
		var csrftoken = getCookie('csrftoken')
		if (confirm('¿Desea eliminar esta ficha?') == true) {
			$.ajax({
				type: 'POST',
				url: '/files/delete_clinic_history/',
				data: {
					clinicHistory_id: $(this).val(),
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
