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
		var deletefile = $(this)
		deletefile.parent().html("deleting <div class='spinner-border spinner-border-sm text-danger'></div>")

		$.ajax({
                type: "get",
                url: "/file/deleteFile",
                data: {"filename": deletefile.attr('id')},
                success: function(data){
                	$('.body_for_ajax').html( $(data).filter('.body_for_ajax').html() )
					console.log(deletefile.parent())
                },
                error: function(e){
                    alert("something went wrong while deleting file");
                }
        });
	});

});