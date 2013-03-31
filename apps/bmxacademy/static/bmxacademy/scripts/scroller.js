$.Scroller = function (pos) {

    var positions = pos;
    var actual = 0;


    var onMove = $.Callbacks();
    onMove.add( hideArrow );

    var onStop = $.Callbacks();
    onStop.add( showArrow );


    function hideArrow () {
        $("#menu").fadeOut(100);
        $("#head").fadeOut(100);
        $("#lista").fadeOut(100);
        $("a[href='#next']").fadeOut(100);

    }

    function showArrow () {
        $('#menu').css("top", positions[actual].getPosition());
        $("#menu").fadeIn(400);
        $("#head").fadeIn(400);
        $("#lista").fadeIn(400);
        if(actual != positions.length -1 ) $("a[href='#next']").fadeIn(400);
    }

    this.getOnMoveCallback = function () {
        return onMove;
    }

    this.getOnStopCallback = function () {
        return onStop;
    }

    this.Next = function () {
        if (actual + 1 < positions.length)
            actual++;
        else
            return;
        this.toActual();
    }

    this.Prev = function () {
        if (actual - 1 >= 0)
            actual--;
        else
            return;
        this.toActual();
    }

    this.toActual = function () {
        this.scrollTo(positions[actual].getPosition()-(($(window).height()-positions[actual].getHeight())/2)-35);
    }

    this.getPositions = function ()
    {
        return positions;
    }

    this.getPosition = function (i)
    {
        return positions[i];
    }


    this.setActualPosition = function (pos) {
        actual = pos;
    }

    this.getActualPosition = function () {
        return (positions[actual].getPosition());
    }


    this.currentPosition = function () {
        return $(window).scrollTop();
    }

    this.timeToScroll = function (from, to) {
        var speed = 0.5; // lower value means faster
        if (from > to) {
            return (from - to) * speed;
        } else {
            return (to - from) * speed;
        }
    }

    this.scrollTo = function (to) {
        var scroller = this;
        // target is current
        if(timeToScroll(this.currentPosition(), to) == 0) return;

        onMove.fire();
        $('html, body').animate({
            scrollTop: to
        }, this.timeToScroll(this.currentPosition(), to),"swing", this.getOnStopCallback().fire);
    }

    this.setUp = function ()
    {
        for (var i = 0; i < positions.length; i++)
            this.registerBundle(i);

    }

    this.registerBundle = function (i) {
        var scroller = this;
        $(positions[i].getLink()).click(function (){
            actual = i;
            scroller.scrollTo(positions[actual].getPosition()-(($(window).height()-positions[actual].getHeight())/2)-35);
            return false;
        });
    }

};

