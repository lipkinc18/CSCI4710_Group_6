$(document).ready(function(){
	$('#display_button').click(function(){
		$.get( "/get_pickup", function( data ) {
		  // based on https://www.codebyamir.com/blog/populate-a-select-dropdown-list-with-json
		  var dropdown = $('#sel1');
		  
		  dropdown.empty();
		  dropdown.append('<option selected="true" disabled>Choose a Pickup</option>');
		  dropdown.prop('selectedIndex', 0);

		  js_obj = JSON.parse(data);
		  total_len = js_obj['all_pickups'].length;
		  
		  for (var i = 0; i < total_len; i++){
		  	dropdown.append('<option>'+js_obj['all_pickups'][i]['store']+'</option>');
		  }
		 
		});
	});
	$('#delete_button').click(function(){
		$.ajax({
			url: '/api/delete_user/'+$('#sel1').find(":selected").text(),
			type: 'MY_DELETE',
			success: function(log){
				console.log(log);
			}
		});
	});
});