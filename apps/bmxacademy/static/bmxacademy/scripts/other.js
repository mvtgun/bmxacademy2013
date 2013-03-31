
function cur_pos() {
    return $(window).scrollTop();
}

function timeToScroll(from, to) {
    var speed = 0.5; // lower value means faster
    if (from > to) {
        return (from - to) * speed;
    } else {
        return (to - from) * speed;
    }
}

var program_links = $("a[href='index.html']");
var registrace_links = $("a[href='#registrace']");

// TODO
// alert($("html").offset().top);

$(program_links).click(function () {
    var to = 0;
    $('html, body').animate({
        scrollTop: to
    }, timeToScroll(cur_pos(), to));
    return false;
});

$(registrace_links).click(function () {
    var to =  1500;
    $('html, body').animate({
        scrollTop: to
    }, timeToScroll(cur_pos(), to));
    return false;
});