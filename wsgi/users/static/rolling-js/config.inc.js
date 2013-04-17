(function($){
	var imag=[];
	var link=[];
	var text=[];

  	imag[0]=encodeURIComponent("../static/rolling-img/1.jpg");
	link[0]=encodeURIComponent("http://www.google.com");
	text[0]="1";
  	imag[1]=encodeURIComponent("../static/rolling-img/2.jpg");
	link[1]=encodeURIComponent("http://www.google.com");
	text[1]="2";
  	imag[2]=encodeURIComponent("../static/rolling-img/3.jpg");
	link[2]=encodeURIComponent("http://www.google.com");
	text[2]="3";
  	imag[3]=encodeURIComponent("../static/rolling-img/4.jpg");
	link[3]=encodeURIComponent("http://www.google.com");
	text[3]="4";
 
	if(imag.length < 4){
	    for(var i=imag.length;i<4;i++){
          	imag[i]="../static/rolling-img/ad.jpg";
        	link[i]=encodeURIComponent("/");
        	text[i]="def";
	    }
	}
 	var pic_width=550;
	var pic_height=228;
	var stop_time=6000;
    makeSWF('FrontPageFocusShower','../static/rolling-js/focus.swf',{
		FlashVars : 'pics='+imag.join('|')+'&links='+link.join('|')+'&texts='+text.join('|')+'&stop_time='+stop_time+'',
		wmode: 'opaque',
		scale: 'noScale',
		quality: 'high',
		width : pic_width,
		height : pic_height
	});
})($);