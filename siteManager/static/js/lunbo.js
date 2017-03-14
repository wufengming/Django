window.onload=function(){
	var q=document.getElementById('div2');
	var z=q.getElementsByTagName('ul')[0];
	var x=z.getElementsByTagName('li');

	z.innerHTML=z.innerHTML+z.innerHTML;

	z.style.width=x[0].offsetWidth*x.length+'px';   //以UL里面LI的个数乘以背个LI的宽来计算UL的宽
	
	
	function v(){										//如果 ul的左边距小于ul总宽度的一半； 那么 ul的左边等于0		
		if(z.offsetLeft<-z.offsetWidth/2)   	
		{
			z.style.left='0';
		}
		if(z.offsetLeft>0)								//如果 ul的左边距大于0 那么 ul的左边等于ul宽度的一半	
		{
			z.style.left=-z.offsetWidth/2+'px';	   
		}                                                
		z.style.left=z.offsetLeft-2+'px';		 // 加号向左移动 
		//z.style.left=z.offsetLeft-2+'px';		// 减号向右移动
		}
		
		
		timer=setInterval(v,30)    //定时器，30毫秒执行一次
		
								 
		q.onmouseover=function()   //定时器 .开关 鼠标进入移出
		{
			clearInterval(timer);
		}
		q.onmouseout=function()
		{
			timer=setInterval(v,30)
		}
}