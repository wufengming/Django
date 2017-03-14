var t3=document.getElementById('t3');
var t7=document.getElementById('zhezhao3');
var bzHui=document.getElementById('sannong2');
var bzHui1=document.getElementById('licai2');
var bzHui2=document.getElementById('gonghui2')
var dzHui3=document.getElementById('box2');
var oTc2=document.getElementById('tc2');
var input3=oTc2.getElementsByTagName('input');
var zXc2=document.getElementById('zxc2');
var oLi5=document.getElementById('li5');
var oLi3=oLi5.getElementsByTagName('li');
var zi3=document.getElementById('input1');

//案列
for(var i=0;i<oLi3.length;i++)
{
	oLi3[i].onclick=function()
	{
		for(var i=0;i<oLi3.length;i++)
		{
			oLi3[i].style.backgroundColor=''
		}
		this.style.backgroundColor='#16b693';
	}
}
for(var i=0;i<input3.length;i++)
{
	input3[i].onclick=function()
	{
		for(var i=0;i<input3.length;i++)
		{
			at9()
		}
	}
}

function at9(){
	dzHui3.style.display='block'
	startMove(dzHui3,{top:0})
}
function at10(){
		startMove(dzHui3,{top:-1100},function(){
		dzHui3.style.display='none'	
	})
}

zXc2.onclick=function(){
	at10()
}

setTimeout(tt,1000)
function tt1(){
startMove(zi2,{opacity:100})
}
setTimeout(tt1,2000)
function tt2(){
startMove(zi3,{opacity:100})
}
setTimeout(tt2,2500)
//遮罩页
 function ccv1(){
	t7.style.animation='zhe 1s';
	t7.style.animationFillMode='forwards';
}
setTimeout(ccv1,1000)



