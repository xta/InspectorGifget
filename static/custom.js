$(document).ready(function() {

	var count = photos.length;
	var i = 0;

(function(){
    $('#frameimg1').prepend('<img src="data:image/gif;base64,' + photos[0].image +  '" />');
}());
  
(function(){
      setInterval(function(){
          $('#frameimg2').children().eq(0).remove();
          	i++;
          	if (i == count) {	i = 0; }  
          $('#frameimg2').prepend('<img src="data:image/gif;base64,' + photos[i].image +  '" />');
          $('#currentCount').html(i+1);
			},1000);
  })($(this));

  





});