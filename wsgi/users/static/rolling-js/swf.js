var makeSWF = function(idname,path,params,breturn){
    breturn = breturn || false;
	var defaultp = {
		width: 600,
		height: 400,
		movie: path,
		allowfullscreen : false,
		scale : 'exactfit',
		wmode : 'transparent',
		play : 0,
		loop : -1,
		quality : 'high',
		allowscriptaccess : 'always',
		bgcolor : '#ffffff',
		align : 'middle',
		swremote : '',
		seamlesstabbing : '1',
		profile : '0',
		profileaddress : '',
		profileport : '',
		base : '',
		allownetworking : 'all'
	};
	if(params != undefined) for(var k in params){
		defaultp[k] = params[k];
	}
	params = defaultp;
	var info = '';
	var str = '<object id="'+idname+'" name="'+idname+'" classid="clsid:d27cdb6e-ae6d-11cf-96b8-444553540000" codebase="http://fpdownload.macromedia.com/pub/shockwave/cabs/flash/swflash.cab#version=8,0,0,0" width="'+params.width+'" height="'+params.height+'" align="'+params.align+'">';
	for(key in params){
	    if(params[key] == null) continue;
		str += '<param name="'+key+'" value="'+params[key]+'">';
	}
	str += '<embed src="'+params['movie']+'" id="'+idname+'" name="'+idname+'" type="application/x-shockwave-flash" pluginspage="http://www.macromedia.com/go/getflashplayer"';
	for(key in params){
	    if(params[key] == null) continue;
		if(!/^(FlashVars|wmode|scale|quality|bgcolor|width|height|align|allowScriptAccess)$/i.test(key)) continue;
		str += ' '+key+'="'+params[key]+'"';
	}
	str += ' />';
	str += info + '</object>';
	if(breturn) return str;
	document.writeln(str);
};

var getSWFObj = function(name){
	return ((navigator.appName.indexOf("Microsoft") != -1) ? window[name] : document[name]);
};
var getSWFObjRef = function(name){
	return ((navigator.appName.indexOf("Microsoft") != -1) ? window[name] : document.getElementById(name));
};

var swfMovieIsLoaded = function(theMovie){
if(typeof(theMovie) != "undefined"){
  return theMovie.PercentLoaded() == 100;
}else{
  return false;
}
};
