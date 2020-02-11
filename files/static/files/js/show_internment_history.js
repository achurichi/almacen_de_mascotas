$(function() {
	$('.new-day-btn').on('click', function() {
		var csrftoken = getCookie('csrftoken')
		console.log($(this).attr('name'))
		$.ajax({
			type: 'POST',
			url: '/files/add_day_internment_history/',
			data: {
				internment_history_id: $(this).attr('name'),
				csrfmiddlewaretoken: csrftoken
			},
			dataType: 'json',
			success: function reload() {
				location.reload()
			}
		})
	})
})

$(function() {
	$('.delete-btn').on('click', function() {
		var csrftoken = getCookie('csrftoken')
		if (confirm('¿Desea eliminar este registro del historial?') == true) {
			$.ajax({
				type: 'POST',
				url: '/files/delete_day_internment_history/',
				data: {
					internmentDay: $(this).val(),
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
