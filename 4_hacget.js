var fs = require('fs');

function info() {
	fs.readFile('./4_hacget.json','utf8',function(err,data){
		if(err){
			//console.log('文件读取错误');
			return '文件读取错误';
		}else{
			//console.log(data);
			//return data;
			console.log('文件读取成功');
			
		}
	});	
}


/*
var data = fs.readFile('./4_hacget.json','utf8',function(err,data){
	if(err){
		console.log('文件读取错误');
	}else{
		//console.log(data);
		//return data;
		console.log('文件读取成功');
		

		var jdata = JSON.parse(data);
		console.log(typeof jdata);
		for(var key in jdata){
			console.log(key);
		}
	}
});
*/

function start() {
	var data = info();
}
start();
