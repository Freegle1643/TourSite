(function ($) {
    $.fn.extend({
        searchMeme: function (options) {
            var settings = $.extend({ animationSpeed: 500, defaultText: '', button: 'green', buttonPlacement: 'right', onSearch: null, searchComplete: false }, options);
            return this.each(function () {
                var searchBox;
                var searchButton;
                var searchButtonIcon;
                if (settings.searchComplete) {
                    searchButtonIcon = $('.searchMeme-button-inner');
                    onSearchComplete();
                    return false;
                }
                //prepare markup
                var nav_search = $('<div class="nav_search-' + settings.button + '"><div class="searchMeme-button-' + settings.buttonPlacement + ' ' + settings.button + '-normal  searchMeme-round-' + settings.buttonPlacement + '"> ' +
                                '<div class="searchMeme-button-icon searchMeme-button-inner"></div></div> <div class="searchMeme-input-' + settings.buttonPlacement + '"></div></div>');
                $(this).before(nav_search);
                $('.searchMeme-input-' + settings.buttonPlacement + '', nav_search).append($(this));
                searchBox = $('.searchMeme-input-' + settings.buttonPlacement + ' input', nav_search);
                searchButton = $('.searchMeme-button-' + settings.buttonPlacement + '', nav_search);
                searchButtonIcon = $('.searchMeme-button-inner', searchButton);
                var w = 0; //width
                var p = 0; //padding
                var m = 0; //margin
                var suggestWrap = $('#id-submenu-search');
                var waterMark = settings.defaultText;
                w = searchBox.width();
                p = searchBox.css('padding-left');
                m = parseInt(w) + (parseInt(p) * 2);
                if (settings.buttonPlacement == 'left')
                    searchBox.css({ 'width': 0, paddingLeft: 0, paddingRight: 0 }).animate({ width: 0, paddingLeft: 0, paddingRight: 0 }, settings.animationSpeed);
                else
                    searchBox.css({ 'margin-left': m, paddingLeft: 0, paddingRight: 0 }).animate({ marginLeft: m, paddingLeft: 0, paddingRight: 0 }, settings.animationSpeed);
                searchBox.val(waterMark).addClass('searchMeme-water-mark');
                searchButton.hover(function () {
                    $(this).addClass('' + settings.button + '-hover');
                    $(this).removeClass('' + settings.button + '-normal');
                }, function () {
                    $(this).addClass('' + settings.button + '-normal');
                    $(this).removeClass('' + settings.button + '-hover')
                });
             searchButton.mouseenter(function () {
                    if (settings.buttonPlacement == 'left')
                        searchBox.addClass('searchMeme-water-mark').animate({ width: w, paddingLeft: p, paddingRight: p }, settings.animationSpeed);
                    else
                        searchBox.addClass('searchMeme-water-mark').animate({ marginLeft: 0, paddingLeft: 5, paddingRight: p }, settings.animationSpeed);
                }).click(function () { triggerSearch();return false; });

                //输入弹出下拉框
                $('input').bind('input propertychange', function() {
                    if ($(this).val() != '')
                        {$(this).addClass('searchMeme-water-mark');

                        //用户输入了东西 调用云搜进行检测
                        //在这里写Ajax请求拿到云搜返回的数据

                        //尝试解决Forbidden的问题：

                    function getCookie(name) {
                        var cookieValue = null;
                        if (document.cookie && document.cookie != '') {
                            var cookies = document.cookie.split(';');
                            for (var i = 0; i < cookies.length; i++) {
                                var cookie = jQuery.trim(cookies[i]);
                                // Does this cookie string begin with the name we want?
                                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                                    break;
                                }
                            }
                        }
                        return cookieValue;
                    }

                    var csrftoken = getCookie('csrftoken');

                    function csrfSafeMethod(method) {
                        // these HTTP methods do not require CSRF protection
                        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
                    }

                    $.ajaxSetup({
                        beforeSend: function (xhr, settings) {
                            var csrftoken = getCookie('csrftoken');
                            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                                xhr.setRequestHeader("X-CSRFToken", csrftoken);
                            }
                        }
                    });

                      var usercontent = $(this).val();

                    //用ajax把从前台获取到的搜索框中的内容发送到后台去
                    $.ajax({
                        url: '/yunsou/',
                        type: 'POST',
                        data: {searchTarget:usercontent},
                        dataType: 'html',
                        success: function (result) {
                            // alert('try yunsou success');
                            console.log("ready to replace");
                            $('#search-result-content').html(result);
                            t = $('#search-result-content').length;
                            console.log(t);
                            console.log("replace done");
                            console.log(result);
                        },
                        error: function (xhr, status, error) {
                            alert('!Error:' + error.message);
                        }
                    });

                    //展示下拉框
                        suggestWrap.show();
                    }
                    if ($(this).val() == '')
                        {$(this).addClass('searchMeme-water-mark');
                        suggestWrap.hide();
                    }
                });

                searchBox.keydown(function (e) {
                    if (e.which == 13) {
                        triggerSearch();
                    }
                }).click(function () { searchBox.removeClass('searchMeme-water-mark').val(''); return false; }).blur(function () {
                    if ($(this).val() != '')
                        {$(this).addClass('searchMeme-water-mark');
                        suggestWrap.show();
                    }
                    if ($(this).val() == '')
                        {$(this).addClass('searchMeme-water-mark');
                        suggestWrap.hide();
                    }
                });
                $(document).click(function (e) {
                    if (settings.buttonPlacement == 'left') {
                        searchBox.removeClass('searchMeme-water-mark').animate({ width: 0, paddingLeft: 0, paddingRight: 0 }, settings.animationSpeed, function () {
                            searchBox.val(waterMark).addClass('searchMeme-water-mark');
                        });
                    }
                    if(settings.buttonPlacement == 'right'&&searchBox.val() == "" && searchBox.val() == waterMark) {
                        searchBox.animate({ marginLeft: m, paddingLeft: 0, paddingRight: 0 }, settings.animationSpeed, function () {
                            searchBox.val(waterMark).addClass('searchMeme-water-mark');
                        });
                        suggestWrap.hide();
                    }
                });
                //点击搜索或者点击回车响应函数
                function triggerSearch() {
                    if (searchBox.val() != "" && searchBox.val() != waterMark) {
                        window.location.href='../destination2';
                    }
                }
               function onSearchComplete() {
                    searchButtonIcon.removeClass('searchMeme-button-searching');
                }
            });
        }
    });

})(jQuery);
