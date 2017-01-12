function updateBlogEdit(blogTitle,journeyTime,journeyTheme,blogSummary,blogMainCon) {
    	$("#id-blogedit-title").val(blogTitle);
        $("#id-blogedit-date").val("出发时间："+journeyTime);
        $("#id-blogedit-place").val("place");

        $(".blogedit-checkbox").children("input:eq("+journeyTheme+")").attr("checked",true);

        $("#id-blogedit-summary").val(blogSummary);
        $("#editor").html(blogMainCon);

    }
function updateTr(index,cityContent,spotContent){
    $("#routetable-input-"+index+"-1").val(cityContent);
    $("#routetable-input-"+index+"-2").val(spotContent);
}  
//增加行程单的条目
function addTr() {
        nowindex=$("#routetable-table-id tr").length-1;
        var newTr=$("<tr></tr>");
        newTr.attr("id","routetable-row-"+nowindex);
        $("#table-bottom-id").before(newTr);

        var dateTd=$("<td></td>");
        dateTd.addClass("routetable-date");
        dateTd.html("Day"+nowindex);
        dateTd.appendTo(newTr);

        var newItem_1=$("<td></td>");
        newItem_1.addClass("routetable-newitem");
        newItem_1.attr("onclick","openEditTxt("+nowindex+","+"1)");
        newItem_1.appendTo(newTr);

        var input_1=$("<input>");
        input_1.attr("type","text");
        input_1.attr("placeholder","新增");
        input_1.attr("readonly","readonly");
        input_1.attr("id","routetable-input-"+nowindex+"-1");
        input_1.appendTo(newItem_1);

        var newItem_2=$("<td></td>");
        newItem_2.addClass("routetable-newitem");
        newItem_2.attr("onclick","openEditTxt("+nowindex+","+"2)");
        newItem_2.appendTo(newTr);

        var input_2=$("<input>");
        input_2.attr("type","text");
        input_2.attr("placeholder","新增");
        input_2.attr("readonly","readonly");
        input_2.attr("id","routetable-input-"+nowindex+"-2");
        input_2.appendTo(newItem_2);

        var btnTd=$("<td></td>");
        btnTd.addClass("routetable-option");
            // btnTd.attr("onclick","clickTd("+nowindex+")");
        btnTd.appendTo(newTr);

        var btnImg=$("<img>");
        btnImg.attr("src","res/icons/remove.png");
        btnImg.attr("onclick","deleteOneItem("+nowindex+")");
        btnImg.appendTo(btnTd);
}
//删除行程单的某个条目
function deleteOneItem(num) {
    newNum=num;
    $(".routetable-table tr").each(function(index,element) {
        if(index>num&&index<$("#routetable-table-id tr").length-1){
            $(this).attr("id","routetable-row-"+newNum);
            $(this).children(':first').html("D"+newNum);
            $(this).children(':eq(1)').attr("onclick","openEditTxt("+newNum+","+"1)");
            $(this).children(':eq(1)').children('input').attr("id","routetable-input-"+newNum+"-1");
            $(this).children(':eq(2)').attr("onclick","openEditTxt("+newNum+","+"2)");
            $(this).children(':eq(2)').children('input').attr("id","routetable-input-"+newNum+"-2");
            $(this).children(':last').children('img').attr("onclick","deleteOneItem("+newNum+")");
            newNum++;
        }
            
    })
    $("#routetable-row-"+num).remove();
    
}
function openEditTxt(trNum,tdNum) {
    $('#insert-label').empty();
    $('.insert-route').show();
    var wordarray=$("#routetable-input-"+trNum+"-"+tdNum).val().split(";");
    for(var i=0;i<wordarray.length-1;i++)
    {
        addNewLabel(wordarray[i]);
    }
    $("#input-label").data("firstNum",trNum);
    $("#input-label").data("secondNum",tdNum);    
}
//删除某个地点/城市
function deleteLabel(num) {
    newNum=num;
    $("#insert-label span").each(function(index,element) {
        if(index>num-1){
            $(this).attr("id","Label-"+newNum);
            $(this).attr("onclick","deleteLabel("+newNum+")");
            newNum++;
        }
    })
    $("#Label-"+num).remove();
    
}

//增加标签函数
function addNewLabel(newTxt) {
    var newlabel=$("<span class='label' style='margin-right:10px;'></span>");
    nowindex=$("#insert-label span").length+1;
    newlabel.html(newTxt);
    newlabel.css("cursor","pointer");
    newlabel.attr("id","Label-"+nowindex);
    newlabel.attr("onclick","deleteLabel("+nowindex+")");
    newlabel.appendTo("#insert-label");
}
$(function() {
    //增加行程单一个条目
    $("#add-item-btn").click(function() {
    addTr();
    })
})
