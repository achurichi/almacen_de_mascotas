var checkbox
var newButton
var searchButton
var newOwnerContainer
var existingOwnerContainer

document.addEventListener('DOMContentLoaded', function() {
	checkbox = document.getElementById('id_castrated')
	newButton = document.getElementById('new-button')
	searchButton = document.getElementById('search-button')
	newOwnerContainer = document.getElementById('new-owner-container')
	existingOwnerContainer = document.getElementById('existing-owner-container')

	var divElem = document.getElementById('castration-date-container')
	divElem.style.display = 'none'

	checkbox.addEventListener('click', function() {
		var divElem = document.getElementById('castration-date-container')
		if (this.checked) divElem.style.display = 'flex'
		else divElem.style.display = 'none'
	})

	newButton.addEventListener('click', function() {
		if (newButton.classList.contains('not-selected')) {
			newButton.classList.add('selected')
			newButton.classList.remove('not-selected')
			searchButton.classList.add('not-selected')
			searchButton.classList.remove('selected')

			newOwnerContainer.style.display = 'flex'
			existingOwnerContainer.style.display = 'none'
		}
	})

	checkbox.addEventListener('click', function() {
		var divElem = document.getElementById('castration-date-container')
		if (this.checked) divElem.style.display = 'flex'
		else divElem.style.display = 'none'
	})

	searchButton.addEventListener('click', function() {
		if (searchButton.classList.contains('not-selected')) {
			searchButton.classList.add('selected')
			searchButton.classList.remove('not-selected')
			newButton.classList.add('not-selected')
			newButton.classList.remove('selected')

			existingOwnerContainer.style.display = 'flex'
			newOwnerContainer.style.display = 'none'
		}
	})
})
