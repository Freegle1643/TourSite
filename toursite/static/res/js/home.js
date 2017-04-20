function selectfeaturedr() {
    document.getElementById("focusr-be-black").style.display="inline-block";
    document.getElementById("focusr-select-look").style.display="inline-block";
    document.getElementById("home-featuredr-text").style.display="none";
}

function unselectfeaturedr() {
    document.getElementById("focusr-be-black").style.display="none";
    document.getElementById("focusr-select-look").style.display="none";
    document.getElementById("home-featuredr-text").style.display="block";
}

function selectfeaturedl() {
    document.getElementById("focusl-be-black").style.display="inline-block";
    document.getElementById("focusl-select-look").style.display="inline-block";
    document.getElementById("home-featuredl-text").style.display="none";
    
}

function unselectfeaturedl() {
    document.getElementById("focusl-be-black").style.display="none";
    document.getElementById("focusl-select-look").style.display="none";
    document.getElementById("home-featuredl-text").style.display="block";
}

function blogRecommendAjax()
{
	// var userID=getCookie("userIDCookie");
    // //ajax传输热门游记,以及实现收藏功能
	// $.ajax({
	// 	url:"../blogs_blogsRecommend.action",
	// 	type:"post",
	// 	dataType:"json",
	// 	success:function(data){
	// 			for(var i=1;i<4;i++)
	// 			{
	// 				 var img="url(res/data/blogs/covers/"+data[i-1].b_ID+".jpg)";
	// 				$('#slide-img-'+i).css("background",img);
	// 				$('#slide-img-'+i).css("background-repeat","no-repeat");
	// 				$('#slide-img-'+i).css("background-size","cover");
	// 				$('#slide-txt-'+i+' h6').html(data[i-1].b_title);
	// 				$('#slide-abstract-'+i+' p').html(data[i-1].b_abstract);
	// 				$('#slide-readbtn-'+i).click(function () {
	// 					var str=$(this).attr('id');
	// 					location.href="blogdetails.html?blogID="+data[str[14]-1].b_ID;
	// 				})
	//
	// 				var destID=data[i-1].b_ID;
	//
	// 				feedsSearch(i,userID,destID,5);
	//
	// 				$('#slide-collectbtn-'+i).click(function () {
	// 					var str=$(this).attr('id');
	// 					var dest=data[str[17]-1].b_ID;
	// 					if($(this).html()!="已收藏"){
	// 					$(this).html("已收藏");
	// 					feedAjax(userID,dest,5);
	// 					addReadingList(data[str[17]-1].b_ID,data[str[17]-1].b_title,data[str[17]-1].b_abstract);
	// 					alert("收藏成功");
	// 					}
	// 					else{
	// 						$(this).html("加入收藏");
    	// 					disfeedAjax(userID,dest,5);
    	// 					alert("取消收藏成功");
	// 					}
	// 				})
	// 			}
	// 	},
	// 	error:function(){
	// 	}
	// });
}


$(function() {
	//游记滑动
    var $container=$('#slide-wrapper');
    var $img_1=$('#slide-img-1')
    var $img_2=$('#slide-img-2')
    var $img_3=$('#slide-img-3')
    var $txt_1=$('#slide-txt-1')
    var $txt_2=$('#slide-txt-2')
    var $txt_3=$('#slide-txt-3')
    var $prev=$('#btn-next');
    var $next=$('#btn-prev');
    var bool=false;
    var count=1;
    var timer;
    

    // $('#focusr-select-collect').click(function(){
    //     if($('#focusr-select-collect').html()=="加入关注")
    //     	$('#focusr-select-collect').html("已关注");
    //     else
    //     	$('#focusr-select-collect').html("加入关注");
    // })
    
    $('.slide-tbtn:eq(2)').click(function(){
        if(count==2){
            myanimate($img_2,$txt_2,$img_3,$txt_3,-$(window).width(),1000)
            count=3;
        }else if(count==1){
            myanimate($img_1,$txt_1,$img_3,$txt_3,-$(window).width(),1000)
            count=3;
        }

    })

    $('.slide-tbtn:eq(1)').click(function(){
        if(count==1){
            myanimate($img_1,$txt_1,$img_2,$txt_2,-$(window).width(),1000)
            count=2;
        }else if(count==3){
            myanimate($img_3,$txt_3,$img_2,$txt_2,$(window).width(),1000)
            count=2;
        }

    })

    $('.slide-tbtn:eq(0)').click(function(){
        if(count==2){
            myanimate($img_2,$txt_2,$img_1,$txt_1,$(window).width(),1000)
            count=1;
        }else if(count==3){
            myanimate($img_3,$txt_3,$img_1,$txt_1,$(window).width(),1000)
            count=1;
        }

    })

    function play() {
        timer=setInterval("$('#btn-next').click()",4000);
    }
    function stop() {
        clearInterval(timer);
    }

    
    function myanimate(img_1,txt_1,img_2,txt_2,offset,duration) {
        img_2.css("left",-offset);
        txt_2.css("left",-offset);
        img_1.animate({left:offset},duration);
        txt_1.animate({left:offset},duration);
        img_2.animate({left:0},duration,function(){bool=false});
        txt_2.animate({left:0},duration+500);
    }

    $next.click(function() {
        if(!bool){
            switch(count){
                case 1:
                    bool=true;
                    myanimate($img_1,$txt_1,$img_3,$txt_3,$(window).width(),1200);
                    count=3;
                    break;
                case 2:
                    bool=true;
                    myanimate($img_2,$txt_2,$img_1,$txt_1,$(window).width(),1200);
                    count=1;
                    break;
                case 3:
                    bool=true;
                    myanimate($img_3,$txt_3,$img_2,$txt_2,$(window).width(),1200);
                    count=2;
                    break;

        }

        }
    })

    $prev.click(function() {
        if(!bool){
            switch(count){
                case 1:
                    bool=true;
                    myanimate($img_1,$txt_1,$img_2,$txt_2,-$(window).width(),1200);
                    count=2;
                    break;
                case 2:
                    bool=true;
                    myanimate($img_2,$txt_2,$img_3,$txt_3,-$(window).width(),1200);
                    count=3;
                    break;
                case 3:
                    bool=true;
                    myanimate($img_3,$txt_3,$img_1,$txt_1,-$(window).width(),1200);
                    count=1;
                    break;

            }

        }
    })


    $container.mouseover(stop);
    $container.mouseout(play);
    play();

})