$(function(){
	var file_links = $(".row a");

	file_links.each(function(file_link) {
		var arr = $(this).attr('href').split('/');
		$(this).html(arr[arr.length-1])
	});

	// $('.search_submit').click(function() {
	// 	console.log("clicked")
	// 	var lecturer = $("#inlineFormInput")
	// 	var tags = $("#inlineFormInputGroup")
	// 	console.log(lecturer.val(), tags.val())
	// 	if(lecturer.val() != ""){
	// 		console.log("serch on lecturer");
	// 	}
	// 	else if(tags.val() != ""){
	// 		console.log("serch on tags");
	// 	}
	// 	else{
	// 		console.log("serch on year");
	// 	}
	// });
	
	$(".fa-trash-alt").click(function() {
		console.log($(this).attr('id'))
		$.ajax({
                type: "get",
                url: "/file/deleteFile",
                data: {"filename": $(this).attr('id')},
                success: function(data){
                	location.reload();
                },
                error: function(e){
                    alert("something went wrong while deleting file");
                }
        });
	});

});