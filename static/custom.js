$(document).ready(function() {
	var numItems = $('.frame').length;
	$('span#totalCount').html(numItems);

	current = 1; // set initial counter start
	$('span#currentCount').html(current);

	$(".frame").hide().filter(":first").show();





});