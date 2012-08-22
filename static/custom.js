$(document).ready(function() {

  var count = photos.length;
  var i = 0;
  var j = 0;
  var setSpeed = 300;
  var interval;

// load first img frame
  (function(){
    $('#frameimg1').html("");
    $('#frameimg1').prepend('<img src="data:image/gif;base64,' + photos[0].image +  '" />');
  }());

// create function to loop through img(s)  
  function makeTimeout() {
    if (setSpeed < 0) {
      i--;
      if (i == -1) { i = count-1; } // i range is 0..count-1, so when i==-1, set as count-1
      j = i + 1;
      if (j == count) { j = 0; } // j range is 0..count-1, so when j==count, set as 0
    } else {
      i++;
      if (i == count) { i = 0; } // i range is 0..count-1, so when i==count, then set as 0
      j = i - 1; 
      if (j == -1) { j = count-1; } // j range is 0..count-1, so when j==-1, then set as count-1
    }

    $('#frameimg2').children().eq(0).remove();  
    $('#frameimg2').prepend('<img src="data:image/gif;base64,' + photos[i].image +  '" />');

    $('#currentCount').html(i+1);

    $('#frameimg1').children().eq(0).remove();
    $('#frameimg1').prepend('<img src="data:image/gif;base64,' + photos[j].image +  '" />');

    interval = setTimeout(function() {
      makeTimeout(); 
    }, Math.abs(setSpeed));
  }

// start loop
  makeTimeout();


// initialize slider
  //$sliderValue="";
  $("#slider").slider({                   
      value: setSpeed,
      min: -1000,
      max: 1000,
      step: 100,
      change: function(event, ui) {
        clearTimeout(interval);
        setSpeed = ui.value;
        makeTimeout();
      }
  });






});