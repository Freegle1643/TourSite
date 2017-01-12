/**
 * @brief:登录界面各个输入框的监测与提醒与背景图片的实施切换
 * @param:null
 * @return:void
 * @author:高雨枫
 */
function check_txtName() {
    if (frmLogin.txtName.value.length == 0) {
        //alert("用户名不能为空");
        var txtName=document.getElementById("txtName");
        txtName.style.borderColor="red";
        var accWarning=document.getElementById("accWarning");
        accWarning.removeAttribute("hidden");
        //frmLogin.txtName.focus();
    }
}
function focus_txtName() {

    var txtName=document.getElementById("txtName");
    txtName.style.borderColor="#DFDFDF";
    var accWarning=document.getElementById("accWarning");
    accWarning.setAttribute("hidden",true);
}


function check_txtPwd() {
    if (frmLogin.txtPwd.value.length <= 6) {
        //alert("密码不能小于6位");
        //frmLogin.txtPwd.focus();
        var txtPwd=document.getElementById("txtPwd");
        txtPwd.style.borderColor="red";
        var pwdWarning=document.getElementById("pwdWarning");
        pwdWarning.removeAttribute("hidden");
        //frmLogin.txtPwd.value = null;
    }
}
function focus_txtPwd() {
    var txtPwd=document.getElementById("txtPwd");
    txtPwd.style.borderColor="#DFDFDF";
    var pwdWarning=document.getElementById("pwdWarning");
    pwdWarning.setAttribute("hidden",true);
}


function check_ctxtPwd() {
    if (frmLogin.ctxtPwd.value != frmLogin.txtPwd.value) {
        //alert("密码确认与密码不同");
        //frmLogin.ctxtPwd.focus();
        var ctxtPwd=document.getElementById("ctxtPwd");
        ctxtPwd.style.borderColor="red";
        var cpwdWarning=document.getElementById("cpwdWarning");
        cpwdWarning.removeAttribute("hidden");
        //frmLogin.ctxtPwd.value = null;
        //frmLogin.txtPwd.value = null;
    }
    else{
        var ctxtPwd=document.getElementById("ctxtPwd");
        ctxtPwd.style.borderColor="#DFDFDF";
        var cpwdWarning=document.getElementById("cpwdWarning");
        cpwdWarning.setAttribute("hidden",true);
    }
}
function focus_ctxtPwd() {
    var ctxtPwd=document.getElementById("ctxtPwd");
    ctxtPwd.style.borderColor="#DFDFDF";
    var cpwdWarning=document.getElementById("cpwdWarning");
    cpwdWarning.setAttribute("hidden",true);
}

function check_idtyCode() {
    if (frmLogin.idtyCode.value.length == 0) {
        //alert("验证码错误");
        //frmLogin.idtyCode.focus();
        var iptIdCode=document.getElementById("iptIdCode");
        iptIdCode.style.borderColor="red";
        var codeWarning=document.getElementById("codeWarning");
        codeWarning.removeAttribute("hidden");
        //frmLogin.idtyCode.value = null;
    }
}
function focus_idtyCode() {
    var iptIdCode=document.getElementById("iptIdCode");
        iptIdCode.style.borderColor="#DFDFDF";
        var codeWarning=document.getElementById("codeWarning");
        codeWarning.setAttribute("hidden",true);
}

function changeBg(){
	var bg_img=["res/images/register_backgroundimg_01.jpeg",
        "res/images/register_backgroundimg_02.jpeg",
        "res/images/register_backgroundimg_03.jpeg",
        "res/images/register_backgroundimg_04.jpeg",
        "res/images/register_backgroundimg_05.jpeg",
		"res/images/register_backgroundimg_06.jpeg"]//这里可以添加图片路径，每个路径用""包起来，每个路径之间用逗号分开，要在英文状态下输入符号。
       
    document.getElementById("Loginbody").style.background="url("+bg_img[Math.floor(Math.random()*(bg_img.length))]+")";
	document.getElementById("Loginbody").style.backgroundSize="cover";  //设置随机背景图，这里不用改。
	document.getElementById("Loginbody").style.backgroundAttachment="fixed";
	document.getElementById("Loginbody").style.fontFamily='"Microsoft YaHei",微软雅黑,"MicrosoftJhengHei",华文细黑,STHeiti,MingLiu';
}