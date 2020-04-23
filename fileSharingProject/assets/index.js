$(function(){
	var file_links = $(".row a");

	file_links.each(function(file_link) {
		var arr = $(this).attr('href').split('/');
		$(this).html(arr[arr.length-1])
	});

});