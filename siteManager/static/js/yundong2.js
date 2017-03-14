
//getByClass 获取Clsaa
function getByClass(oParent,sClass)
{
	var aEle=document.getElementsByTagName('*');   			//获取所有的元素

	var aResult=[]                                  		//传建一个空数组

	for(var i=0;i<aEle.length;i++)							// 把所有的元素循环
	{
		if(aEle[i].className==sClass)						// 如果第i个元素的className等于传进来的参数
		{
			aResult.push(aEle[i])							//就把选中的放到 aResult=[] 数组里面
		}
	}
	return aResult											//然后反馈出去
}

window.onload=function(){}

// 事件绑定 封装
function myAddEvent(obj,ev,fn)
{
	if(obj.attachEvent)
	{
		obj.attachEvent('on'+ev,fn)
	}
	else
	{
		oBtn.addEventListener(ev,fn)
	}
}

// 获取不在行间的样式
function getStyle(obj,name)
{
	if(obj.currentStyle)
	{
		return obj.currentStyle[name];
	}
	else
	{
		return getComputedStyle(obj,false)[name];
	}
}

function startMove(obj,json,fnEnd)                      		//fnEnd  函数
{
	clearInterval(obj.timer);         							//关闭当前DIV上的定时器

	obj.timer=setInterval(function()							//开启当前DIV上的定时器
	{
		var bStop=true;	     									//假设：所有的值都已经到了
		for(var attr in json)
		{
			var cur=0;
			if(attr=='opacity')
			{
				cur=parseFloat(getStyle(obj,attr))*100;
			}
			else
			{
				cur=parseFloat(getStyle(obj,attr));
			}
			var speed=(json[attr]-cur)/6;
			speed=speed>0?Math.ceil(speed):Math.floor(speed);  	//缓冲运动一定要给速度取整

			if(cur!=json[attr])
				bStop=false;
			if(attr=='opacity')
			{
				obj.style.filter='alpha(opacity:'+(cur+speed)+')';
				obj.style.opacity=(cur+speed)/100;
			}
			else
			{
				obj.style[attr]=cur+speed+'px';
			}
		}
			if(bStop)
			{
				clearInterval(obj.timer);
				if(fnEnd)fnEnd();
			}
	},30)
}


