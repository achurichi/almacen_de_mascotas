var newBtn
var createBtn
var cancelBtn

document.addEventListener('DOMContentLoaded', function() {
	newBtn = document.getElementById('new-product')
	createBtn = document.getElementById('create-btn')
	cancelBtn = document.getElementById('cancel-btn')

	configEventListeners()
})

function configEventListeners() {
	newBtn.addEventListener('click', function() {
		document.getElementById('data-form').style.display = 'flex'
		newBtn = 'none'
	})

	cancelBtn.addEventListener('click', function() {
		document.getElementById('data-form').style.display = 'none'
		newBtn = 'flex'
	})
}

$(function() {
	$('.delete-btn').on('click', function() {
		var csrftoken = getCookie('csrftoken')
		if (confirm('¿Desea eliminar este producto?') == true) {
			$.ajax({
				type: 'POST',
				url: '/sales/delete_product/',
				data: {
					product_db_id: $(this).val(),
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
