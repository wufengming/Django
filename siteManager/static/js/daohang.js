var q1=document.getElementById('q');
var li1=q1.getElementsByTagName('li');

var urls = ['index', 'news', 'about', 'product', 'plan', 'case', 'league', 'joinus']
var url = window.location.href;
var selectLI = 0;

var oD=q1.getElementsByTagName('div');
var oP=q1.getElementsByTagName('p');

for(var i=0;i<li1.length;i++)
{
	//当前页被选中
	if (url.indexOf(urls[i]) >= 0)
	{
		selectLI = i;
		oD[i].style.color='#669535'
		oD[i].style.right = '100px';
		li1[i].style.background='#000'
		oP[i].className = oP[i].className + "-1"
		oD[i].style.background='#000'
		oD[i].style.fontWeight='bold'
	}
	else {
        oD[i].style.color='#fff'
    }

	li1[i].index=i
	li1[i].onmouseover=function()
	{
		if (selectLI != this.index) {
            startMove(oD[this.index], {right: -80});
            selectLI = -1
        }
	}

	li1[i].onmouseout=function()
	{
		startMove(oD[this.index],{right:100});
	}


	oP[i].index=i
	oD[i].index = i
	oP[i].onclick=function()
	{
		oD[this.index].style.color='#669535'
		oD[this.index].style.fontWeight='bold'
		this.className = this.className + '-1'
		//oD[this.index].style.right = '-80px';
	}

	oD[i].onclick=function()
	{
		this.style.color='#669535'
		this.style.fontWeight='bold'
		oP[this.index].className = oP[this.index].className + '-1'
	}
}
