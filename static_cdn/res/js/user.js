function userfollowsselected(index) {
    var p1 = document.getElementById("id-user-follows-" + index);
    p1.style.color = "darkred";
    var p2 = document.getElementById("id-user-follows-" + index + index);
    p2.style.color = "darkred";
}

function userfollowsunselected(index) {
    var p1 = document.getElementById("id-user-follows-" + index);
    p1.style.color = "black";
    var p2 = document.getElementById("id-user-follows-" + index + index);
    p2.style.color = "#262626";
}

function newfastreading() {
    var oMask=document.createElement("div");
    var sHeight=document.documentElement.scrollHeight;
    var sWidth=document.documentElement.scrollWidth;
    var wWidth=document.documentElement.clientWidth;
    var wHeight=document.body.clientHeight;
    oMask.id="mask";
    oMask.style.height=sHeight + "px";
    oMask.style.widows=sWidth + "px";
    oMask.style.zIndex=102;
    document.body.appendChild(oMask);
    var oFastreading=document.createElement("div");
    oFastreading.id="fast-reading";
    oFastreading.innerHTML="<div class='close'id='fast-reading-close'></div><div class='user-myfeeds-content-time' style='top:16px;right:20%;'>30分钟前</div><div class='user-myfeeds-content-like' style='top:34px;right:20%;'><img  class='icons' src='res/icons/like.png' /><span>6m</span></div><div class='feed' style='margin-top:0;'><div class='feed-writer'><div class='head-and-likes'><img class='user-head-img' src='res/images/bali.jpeg'/></div><div class='feed-information'><h2>来自你关注的地点：<a class='fogPwdlink' href=''>巴厘岛</a></h2><a class='title' href=''>小长假来巴厘岛做一次瑜伽放松吧！</a></div><div class='feed-operate' style='float:left;'><img src='res/icons/user.png'/><span><a class='fogPwdlink' href=''>Howto颢豆</a></span><img src='res/icons/watched.png'/><span>213140/1221</span><img src='res/icons/spot.png'/><span><a class='fogPwdlink' href=''>巴厘岛</a></span></span></div></div><div class='feed-images'><video id='feed_video_01' src='res/images/feed_video_01.mp4' poster='res/images/feed_video_01_img.png' autoplay loop controls></video></div><div class='feed-text'><h6>SPORT TRAVEL</h6><h1 style='font-size: 25px;margin-bottom:16px;'>又学会了新技能</h1><p>一定要学好基本动作——和最喜爱的瑜伽大师Patrick Beach一起完成拜日式。</p></div><a class='a-select-01' href='#'>阅读全文</a><a class='a-select-01' href='#'>加入收藏</a><br/><textarea class='fast-comment' type='text' placeholder='快速发表您的简评'></textarea><br/><input type='submit' id='id-fast-submit' value='发表评论'/></div>";
    document.body.appendChild(oFastreading);
    oFastreading.style.display="block";
    // $("#fast-reading").fadeIn("100");
    // //Login的宽度高度

    var dFastreadingHeight=oFastreading.offsetHeight;
    var dFastreadingWidth=oFastreading.offsetWidth;
    oFastreading.style.left=(wWidth - dFastreadingWidth)/2 + "px";
    oFastreading.style.top=(wHeight - dFastreadingHeight)/2 + "px";
    document.body.appendChild(oFastreading);

    var oClose=document.getElementById("fast-reading-close");
    oMask.onclick=function() {
        $("#fast-reading").fadeOut(500,function() {
            document.body.removeChild(oMask);
            document.body.removeChild(oFastreading);
        });
        $("#mask").fadeOut(500,function(){
            document.body.removeChild(oMask);
            document.body.removeChild(oFastreading);
        });
    }

    oClose.onclick=function() {
        $("#fast-reading").fadeOut(500,function() {
            document.body.removeChild(oMask);
            document.body.removeChild(oFastreading);
        });
        $("#mask").fadeOut(500,function(){
            document.body.removeChild(oMask);
            document.body.removeChild(oFastreading);
        });
    }
}

$(function () {
    //获取class为caname的元素 
    $("#user-user-name").mouseover(function () {
        $("#user-user-name").css("color", "darkred");
        $("#user-user-name").css("cursor", "pointer");
    });

    $("#user-user-name").mouseout(function () {
        $("#user-user-name").css("color", "black");
    });

    $("#user-user-briefidtion").mouseover(function () {
        $("#user-user-briefidtion").css("color", "darkred");
        $("#user-user-briefidtion").css("cursor", "pointer");
    });

    $("#user-user-briefidtion").mouseout(function () {
        $("#user-user-briefidtion").css("color", "black");
    });

    $("#user-user-name").click(function () {
        var td = $(this);
        var txt = td.text();
        var input = $("<input class='change-user-name' type='text'value='" + txt + "'/>");
        td.html(input);
        input.click(function () { return false; });
        //获取焦点 
        input.trigger("focus");
        //文本框失去焦点后提交内容，重新变为文本 
        input.blur(function () {
            var newtxt = $(this).val();
            //判断文本有没有修改 
            if (newtxt != txt) {
                td.html(newtxt);
                /* 
                var caid = $.trim(td.prev().text()); 
                //ajax异步更改数据库,加参数date是解决缓存问题 
                var url = "res/common/Handler2.ashx?caname=" + newtxt + "&caid=" + caid + "&date=" + new Date(); 
                //使用get()方法打开一个一般处理程序，data接受返回的参数（在一般处理程序中返回参数的方法 context.Response.Write("要返回的参数");） 
                //数据库的修改就在一般处理程序中完成 
                $.get(url, function(data) { 
                if(data=="1") 
                { 
                alert("该类别已存在！"); 
                td.html(txt); 
                return; 
                } 
                alert(data); 
                td.html(newtxt); 
                }); 
                */
            }
            else {
                td.html(newtxt);
            }
        });
    });

    $("#user-user-briefidtion").click(function () {
        var td = $(this);
        var txt = td.text();
        var input = $("<input class='change-user-briefidtion' type='text'value='" + txt + "'/>");
        td.html(input);
        input.click(function () { return false; });
        //获取焦点 
        input.trigger("focus");
        //文本框失去焦点后提交内容，重新变为文本 
        input.blur(function () {
            var newtxt = $(this).val();
            //判断文本有没有修改 
            if (newtxt != txt) {
                td.html(newtxt);
                /* 
                var caid = $.trim(td.prev().text()); 
                //ajax异步更改数据库,加参数date是解决缓存问题 
                var url = "res/common/Handler2.ashx?caname=" + newtxt + "&caid=" + caid + "&date=" + new Date(); 
                //使用get()方法打开一个一般处理程序，data接受返回的参数（在一般处理程序中返回参数的方法 context.Response.Write("要返回的参数");） 
                //数据库的修改就在一般处理程序中完成 
                $.get(url, function(data) { 
                if(data=="1") 
                { 
                alert("该类别已存在！"); 
                td.html(txt); 
                return; 
                } 
                alert(data); 
                td.html(newtxt); 
                }); 
                */
            }
            else {
                td.html(newtxt);
            }
        });
    });

});

$(function () {
    //上传头像
    $("#id-user-head").mouseover(function () {
        $("#id-user-head-click-change").css("opacity", "1");
    });

    $("#id-user-head").mouseout(function () {
        $("#id-user-head").css("color", "black");
        $("#id-user-head-click-change").css("opacity", "0");
    });


    var $editor = $('.image-editor');
    $editor.cropit();

    $('.export').click(function () {
        // Get cropping information
        var imgSrc = $editor.cropit('imageSrc');
        var offset = $editor.cropit('offset');
        var zoom = $editor.cropit('zoom');
        var previewSize = $editor.cropit('previewSize');
        var exportZoom = $editor.cropit('exportZoom');

        var img = new Image();
        img.src = imgSrc;

        // Draw image in original size on a canvas
        var originalCanvas = document.createElement('canvas');
        originalCanvas.width = previewSize.width / zoom;
        originalCanvas.height = previewSize.height / zoom;
        var ctx = originalCanvas.getContext('2d');
        ctx.drawImage(img, offset.x / zoom, offset.y / zoom);

        // Use pica to resize image and paint on destination canvas
        var zoomedCanvas = document.createElement('canvas');
        zoomedCanvas.width = previewSize.width * exportZoom;
        zoomedCanvas.height = previewSize.height * exportZoom;
        pica.resizeCanvas(originalCanvas, zoomedCanvas, {
            // Pica options, see https://github.com/nodeca/pica
        }, function (err) {
            if (err) { return console.log(err); }

            // Resizing completed
            // Read resized image data
            var picaImageData = zoomedCanvas.toDataURL();
            var $picaImg = $('<img src="' + picaImageData + '" />');

            // Compare to original canvas export
            var canvasImageData = $editor.cropit('export');
            var $canvasImg = $('<img src="' + canvasImageData + '" />');

            // Render on page
            $('<div />').css('margin', '20px 0').append($picaImg, $canvasImg).appendTo('body');
        });
    });
});