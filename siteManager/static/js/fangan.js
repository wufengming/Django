var t2=document.getElementById('t2');
var t6=document.getElementById('zhezhao2');
var azHui=document.getElementById('sannong1');
var azHui1=document.getElementById('licai1');
var azHui2=document.getElementById('gonghui1')
var czHui3=document.getElementById('box1');
var oTc1=document.getElementById('tc1');
var input2=oTc1.getElementsByTagName('input');
var zXc1=document.getElementById('zxc1');
var oLi3=document.getElementById('li3');
var oLi2=oLi3.getElementsByTagName('li');
var zi3=document.getElementById('input1');
var zi5=document.getElementById('txt2');

//方案
for(var i=0;i<oLi2.length;i++)
{
	oLi2[i].onclick=function()
	{
		for(var i=0;i<oLi2.length;i++)
		{
			oLi2[i].style.backgroundColor=''
		}
		this.style.backgroundColor='#16b693';
	}
}

for(var i=0;i<input2.length;i++)
{
	input2[i].onclick=function()
	{
		for(var i=0;i<input2.length;i++)
		{
			at7()
		}
	}
}
zXc1.onclick=function(){
	at8()
}
function at7(){
	czHui3.style.display='block'
	startMove(czHui3,{top:0})
}
function at8(){
		startMove(czHui3,{top:-1100},function(){
		czHui3.style.display='none'	
	})
}
//遮罩页
 function ccv1(){
	t6.style.animation='zhe 1s';
	t6.style.animationFillMode='forwards';
}
setTimeout(ccv1,1000)