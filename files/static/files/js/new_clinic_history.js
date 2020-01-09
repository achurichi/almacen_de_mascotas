$(function() {
	$('#add_more').click(function() {
		var form_idx = $('#id_form-TOTAL_FORMS').val()
		$('#form_set').append(
			$('#empty_form')
				.html()
				.replace(/__prefix__/g, form_idx)
				.replace('form_id', 'form-' + form_idx + '-row')
				.replace('btn_id', 'form-' + form_idx + '-btn')
		)
		$('#id_form-TOTAL_FORMS').val(parseInt(form_idx) + 1)
	})
})

$(function() {
	$(document).on('click', '.delete-btn', function() {
		$(this)
			.parents('.no_error')
			.remove()
		return false
	})
})
