$(document).ready(function(){
	var donde=$('.mitexto');
	var sizeFuenteOriginal=donde.css('font-size');
	//reset
	$(".reiFuente").click(function(){
		donde.css('font-size',sizeFuenteOriginal);
	});
	//+
	$(".aumFuente").click(function(){
		var sizeFuenteActual=donde.css('font-size');
		var sizeFuenteActualNum=parseFloat(sizeFuenteActual,10);
		var sizeFuenteNuevo=sizeFuenteActualNum*1.2;
		donde.css('font-size',sizeFuenteNuevo);
		return false;
	});
	//-
	$(".disFuente").click(function(){
		var sizeFuenteActual=donde.css('font-size');
		var sizeFuenteActualNum=parseFloat(sizeFuenteActual,10);
		var sizeFuenteNuevo=sizeFuenteActualNum*0.8;
		donde.css('font-size',sizeFuenteNuevo);
		return false;
	});

});
