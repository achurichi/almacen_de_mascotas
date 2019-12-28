var checkbox
var divCheckbox
var newButton
var searchButton
var newOwnerContainer
var existingOwnerContainer
var ownerData = []
var selectedOwnerId

document.addEventListener('DOMContentLoaded', function() {
	checkbox = document.getElementById('id_castrated')
	newButton = document.getElementById('new-button')
	searchButton = document.getElementById('search-button')
	newOwnerContainer = document.getElementById('new-owner-container')
	existingOwnerContainer = document.getElementById('existing-owner-container')
	divCheckbox = document.getElementById('castration-date-container')

	autocomplete(document.getElementById('owner-search'))

	checkbox.addEventListener('click', function() {
		var divCheckbox = document.getElementById('castration-date-container')
		if (this.checked) divCheckbox.style.display = 'flex'
		else divCheckbox.style.display = 'none'
	})

	newButton.addEventListener('click', function() {
		if (newButton.classList.contains('not-selected')) {
			newButton.classList.add('selected')
			newButton.classList.remove('not-selected')
			searchButton.classList.add('not-selected')
			searchButton.classList.remove('selected')
			document.getElementById('owner-search').style.display = 'none'
			clearOwnerInputs()

			document.getElementById('id_owner_name').readOnly = false
			document.getElementById('id_address').readOnly = false
			document.getElementById('id_phone_number_1').readOnly = false
			document.getElementById('id_phone_number_2').readOnly = false
			document.getElementById('id_phone_number_3').readOnly = false
		}
	})

	searchButton.addEventListener('click', function() {
		if (searchButton.classList.contains('not-selected')) {
			searchButton.classList.add('selected')
			searchButton.classList.remove('not-selected')
			newButton.classList.add('not-selected')
			newButton.classList.remove('selected')
			document.getElementById('owner-search').style.display = 'block'
			clearOwnerInputs()

			document.getElementById('id_owner_name').readOnly = true
			document.getElementById('id_address').readOnly = true
			document.getElementById('id_phone_number_1').readOnly = true
			document.getElementById('id_phone_number_2').readOnly = true
			document.getElementById('id_phone_number_3').readOnly = true
		}
	})

	function clearOwnerInputs() {
		document.getElementById('owner-search').value = ''
		document.getElementById('id_owner_name').value = ''
		document.getElementById('id_address').value = ''
		document.getElementById('id_phone_number_1').value = ''
		document.getElementById('id_phone_number_2').value = ''
		document.getElementById('id_phone_number_3').value = ''
	}

	function autocomplete(inp) {
		var currentFocus
		inp.addEventListener('input', function(e) {
			var a,
				b,
				i,
				val = this.value
			closeAllLists()
			if (!val) {
				return false
			}
			currentFocus = -1
			a = document.createElement('DIV')
			a.setAttribute('id', this.id + 'autocomplete-list')
			a.setAttribute('class', 'autocomplete-items')
			this.parentNode.appendChild(a)
			var matchOwners = ownerData
			for (i = 0; i < Object.keys(ownerData).length; i++) {
				if (
					ownerData['owner' + i.toString()].owner_name
						.substr(0, val.length)
						.toUpperCase() == val.toUpperCase()
				) {
					b = document.createElement('DIV')
					b.innerHTML =
						'<strong>' +
						ownerData['owner' + i.toString()].owner_name.substr(
							0,
							val.length
						) +
						'</strong>'
					b.innerHTML += ownerData[
						'owner' + i.toString()
					].owner_name.substr(val.length)
					b.innerHTML +=
						"<input type='hidden' value='" +
						ownerData['owner' + i.toString()].owner_name +
						"' id='" +
						'owner' +
						i.toString() +
						"'>"
					b.addEventListener('click', function(e) {
						selectedEl = this.getElementsByTagName('input')[0]
						inp.value = selectedEl.value
						document.getElementById('id_owner_name').value =
							matchOwners[selectedEl.id].owner_name
						document.getElementById('id_address').value =
							matchOwners[selectedEl.id].address
						document.getElementById('id_phone_number_1').value =
							matchOwners[selectedEl.id].phone_number_1
						document.getElementById('id_phone_number_2').value =
							matchOwners[selectedEl.id].phone_number_2
						document.getElementById('id_phone_number_3').value =
							matchOwners[selectedEl.id].phone_number_3
						selectedOwnerId = matchOwners[selectedEl.id].id
						closeAllLists()
					})
					a.appendChild(b)
				}
			}
		})
		inp.addEventListener('keydown', function(e) {
			var x = document.getElementById(this.id + 'autocomplete-list')
			if (x) x = x.getElementsByTagName('div')
			if (e.keyCode == 40) {
				currentFocus++
				addActive(x)
			} else if (e.keyCode == 38) {
				currentFocus--
				addActive(x)
			} else if (e.keyCode == 13) {
				e.preventDefault()
				if (currentFocus > -1) {
					if (x) x[currentFocus].click()
				}
			}
		})
		function addActive(x) {
			if (!x) return false
			removeActive(x)
			if (currentFocus >= x.length) currentFocus = 0
			if (currentFocus < 0) currentFocus = x.length - 1
			x[currentFocus].classList.add('autocomplete-active')
		}
		function removeActive(x) {
			for (var i = 0; i < x.length; i++) {
				x[i].classList.remove('autocomplete-active')
			}
		}
		function closeAllLists(elmnt) {
			var x = document.getElementsByClassName('autocomplete-items')
			for (var i = 0; i < x.length; i++) {
				if (elmnt != x[i] && elmnt != inp) {
					x[i].parentNode.removeChild(x[i])
				}
			}
		}
		document.addEventListener('click', function(e) {
			closeAllLists(e.target)
		})
	}
})

$(function() {
	$('#owner-search').keyup(function() {
		$.ajax({
			type: 'GET',
			url: '/files/search_owners/',
			data: {
				search_text: $('#owner-search').val(),
				csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
			},
			success: function searchSuccess(data) {
				ownerData = data
			},
			dataType: 'json'
		})
	})
})

$(function() {
	$('#data-form').on('submit', function() {
		var ownerOption = $('<input>')
			.attr('type', 'hidden')
			.attr('name', 'owner_option')
			.val(checkOwnerOption())
		$('#data-form').append(ownerOption)

		var ownerId = $('<input>')
			.attr('type', 'hidden')
			.attr('name', 'owner_id')
			.val(selectedOwnerId)
		$('#data-form').append(ownerId)
	})
})

function checkOwnerOption() {
	if (newButton.classList.contains('selected')) return 'True'
	else return 'False'
}
