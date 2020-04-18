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
	$('#select_buttom').click(function(){
		$.ajax({
			url: '/accept_pickup/'+$('#sel1').find(":selected").text(),
			type: 'MY_PICK',
			success: function(log){
				console.log(log);
			}
		});
	});

});

