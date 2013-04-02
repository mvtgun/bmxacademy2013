$(document).ready(function () {

var tablet = false;

if (/Android|webOS|iPad|iPod|BlackBerry/i.test(navigator.userAgent)) {
    tablet = true;
    $(document).touchwipe({
        wipeUp: function() { scroller.Prev();},
        wipeDown: function() { scroller.Next();},
        min_move_x: 20,
        min_move_y: 20
    });
}



if($(window).height() < 900)
{
    $("#head").attr("class","small");
    $("#head").parent().css("width","225px");

}


$('#one').ContentSlider({
    width: '910px',
    height: '300px',
    speed: 200,
    easing: 'easeOutQuad'
});

$('#three').VideoSlider({
    width: '930px',
    height: '270px',
    speed: 200,
    easing: 'easeOutQuad'

});

var scroll = true;

var callbackScroll = $.Callbacks();
callbackScroll.add(scrollManip)

function scrollManip() {
    scroll = false;
    setTimeout(function () {
        scroll = true;
    }, 800);
}

var scroller = new $.Scroller(
    [
        new $.Bundle("div#top", "a[href='#top']"),
        new $.Bundle("div#about", "a[href='#about']"),
        new $.Bundle("div#news", "a[href='#news']"),
        new $.Bundle("div#gallery", "a[href='#gallery']"),
        new $.Bundle("div#video", "a[href='#video']"),
        new $.Bundle("div#partners", "a[href='#partners']"),
        new $.Bundle("div#contact", "a[href='#contact']"),
        new $.Bundle("div#register", "a[href='#register']")
    ],tablet
);

$('body').on('click', '.down', function () {
    scroller.Next();
    return false;
});

$('body').on('click', '.up', function () {
    scroller.Prev();
    return false;
});

scroller.setUp();

disable_scroll();

$(document).mousewheel(function (event, delta) {
    if (delta == -1) if (scroll) {
        callbackScroll.fire();
        scroller.Next();
    }
    if (delta == 1) if (scroll) {
        callbackScroll.fire();
        scroller.Prev();
    }
});

$(window).bind('orientationchange', function(event) {

    if($(window).height() < 900)
    {
        $("#head").attr("class","small");
        $("#head").parent().css("width","225px");
    } else
    {
        $("#head").attr("class","large");
        $("#head").parent().css("width","225px");
    }
    scroller.toActual();
});

$(document).keydown(function (event) {
    if (event.which == 40 && scroll) {
        callbackScroll.fire();
        scroller.Next();
    }
    if (event.which == 38 && scroll) {
        callbackScroll.fire();
        scroller.Prev();
    }
});

scroller.detectPositionDown();
scroller.toActual();

setInterval(function(){
    if (window.location.hash == "#register") { /* set_position(5958)*/ }
}, 10)

});