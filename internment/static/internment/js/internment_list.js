$(function() {
	$('.delete-btn').on('click', function() {
		var csrftoken = getCookie('csrftoken')
		if (confirm('¿Desea eliminar este registro de internación?') == true) {
			$.ajax({
				type: 'POST',
				url: '/internment/delete_internment/',
				data: {
					internmentHistory_id: $(this).val(),
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