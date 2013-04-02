$.Scroller = function (pos, tab) {

    var positions = pos;
    var actual = 0;
    var downer = 0;
    var tablet = tab;


    var onMove = $.Callbacks();
    onMove.add(hideArrow);


    var onStop = $.Callbacks();
    onStop.add(showArrow);


    this.detectPositionDown = function() {
        if(actual == positions.count -1) return;
        var current = $(window).scrollTop();

        for (i = 0; i < positions.length; i++) {
            if(actual == positions.count -1) return;

            if(current >= positions[actual+1].getPosition())
            {
                actual++;
            }
        }
    }

    this.detectPositionUp = function() {
        if(actual == 0) return;
        var current = $(window).scrollTop();

        for (i = 0; i < positions.length; i++) {
            if(actual == 0) return;

            if(current <= positions[actual-1].getPosition())
            {
                actual--;
            }
        }
    }



    function hideArrow() {
        $(".menu").fadeOut(100);
        $("a[href='#next']").fadeOut(100);
        $("a[href='#prev']").fadeOut(100);
    }

    function showArrow() {
        $(".menu").fadeIn(400);

        var down = $("a#position-button");

        if (actual == 0) {
            $(down).attr("href", "#next");
            $(down).attr("class", "down");
        }

        if (actual == positions.length - 1) {
            $(down).attr("href", "#prev");
            $(down).attr("class", "up");
        }

        $(down).fadeIn(400);
    }

    this.getOnMoveCallback = function () {
        return onMove;
    }

    this.getOnStopCallback = function () {
        return onStop;
    }

    this.Next = function () {
        this.detectPositionDown();
        if (actual + 1 < positions.length)
            actual++;
        else
            return;
        this.toActual();
    }

    this.Prev = function () {
        this.detectPositionUp();
        if (actual - 1 >= 0)
            actual--;
        else
            return;
        this.toActual();
    }

    this.toActual = function () {
        if (!tablet) {
            this.scrollTo(positions[actual].getPosition() - (($(window).height() - positions[actual].getHeight()) / 2) - 35);
        }
        else {
            this.scrollTo(positions[actual].getPosition() - (($(window).height() - positions[actual].getHeight()) / 2) - 120);
        }
    }

    this.getPositions = function () {
        return positions;
    }

    this.getPosition = function (i) {
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
        if (this.timeToScroll(this.currentPosition(), to) == 0) return;

        onMove.fire();
        $('html, body').animate({
            scrollTop: to
        }, this.timeToScroll(this.currentPosition(), to), "swing", this.getOnStopCallback().fire);
    }

    this.setUp = function () {
        for (var i = 0; i < positions.length; i++)
            this.registerBundle(i);

    }

    this.registerBundle = function (i) {
        var scroller = this;
        $(positions[i].getLink()).click(function () {
            actual = i;
            scroller.toActual();
            return false;
        });
    }

};

