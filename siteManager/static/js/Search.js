    $(document).ready(function () {

        var $b = $('#query_button'),$i = $('#selech_input');

        $i.keyup(function(e){
            if(e.keyCode == 13){
                $b.click();
            }
        });

        $b.click(function(){
            if($('input[name="keyword"]').val()==""){
                alert("搜索关键词不能为空");
                return false;
            }else{
                var keyword = $('input[name="keyword"]').val();
                window.location.href='detail/product/';
                //alert(keyword);
                return false;
            }
        });

    });