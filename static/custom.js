$(document).ready(function() {

	var count = photos.length;
	var i = 0;
  var j = 0;
  var speed = 1000;

(function(){
    $('#frameimg1').prepend('<img src="data:image/gif;base64,' + photos[0].image +  '" />');
}());
  
(function(){
      setInterval(function(){
          i++;
          if (i == count) { i = 0; }  

          j = i - 1;
          if (j == -1) { j = count; }

          $('#frameimg2').children().eq(0).remove();	
          $('#frameimg2').prepend('<img src="data:image/gif;base64,' + photos[i].image +  '" />');
          $('#currentCount').html(i+1);

          $('#frameimg1').children().eq(0).remove();
          $('#frameimg1').prepend('<img src="data:image/gif;base64,' + photos[j].image +  '" />');
          
			},speed);
  })($(this));

  





});