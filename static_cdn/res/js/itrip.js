window.onload=
function(){
    
    var oDivr = document.getElementById("float-r");
    Hr = 0,
    Yr = oDivr
    while (Yr) {Hr += Yr.offsetTop; Yr = Yr.offsetParent}
    window.onscroll = function()
    {
        var sr = document.body.scrollTop || document.documentElement.scrollTop;
        if(sr>H) {
            oDivr.style = "position:fixed;top:10;";
        } else {
            oDivr.style = "";
        }
    };
    var oDiv = document.getElementById("float-l");
    H = 0,
    Y = oDiv
    while (Y) {H += Y.offsetTop; Y = Y.offsetParent}
    window.onscroll = function()
    {
        var s = document.body.scrollTop || document.documentElement.scrollTop;
        if(s>H) {
            oDiv.style = "position:fixed;top:10;";
        } else {
            oDiv.style = "";
        }
    };
}