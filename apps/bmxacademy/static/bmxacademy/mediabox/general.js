window.addEvent("load", function () {

        mediaActualGalleryIndex = 0;
        mediaOldGalleryIndex = 0;
        mediaGalleryArray = $$("#fotogalerie #in > div");
        mediaGalleryArray.setStyles({top: 3800, "z-index": 1});
        mediaGalleryArray[mediaActualGalleryIndex].setStyles({top: 0, "z-index": 2});

        set();

        $$("#in > div > a > img").each(function (e, d) {
            e.store("initPosX", e.getStyle("left").toInt());
            e.store("initPosY", e.getStyle("top").toInt());
            e.set("morph", {duration: 700, transition: Fx.Transitions.Quint.easeOut})
        });

     

    $$(".prepinani .prev, .prepinani .next").set("tween", {
        duration: 400, transition: Fx.Transitions.Quint.easeOut, unit: "%"}).addEvents({mouseenter: function () {
            this.tween("background-position", "50% 100%")
        }, mouseleave: function () {
            this.tween("background-position", "50% 0%")
        }, click: function (d) { 
  
            if (this.retrieve("enabled") == false) {
                return
            }
            $$(".prepinani .prev, .prepinani .next").store("enabled", false);
            c(this);

        }}).store("enabled", true);

    function c(d) {
        mediaOldGalleryIndex = mediaActualGalleryIndex;
        switch (d.get("class")) {
            case"next":
                mediaActualGalleryIndex++;
                break;
            case"prev":
                mediaActualGalleryIndex--;
                break
        }
        if (mediaActualGalleryIndex > (mediaGalleryArray.length - 1)) {
            mediaActualGalleryIndex = 0
        }
        if (mediaActualGalleryIndex < 0) {
            mediaActualGalleryIndex = (mediaGalleryArray.length - 1)
        }


        b()
    }

    function b() {

        mediaGalleryArray[mediaOldGalleryIndex].getElements("a img").each(function (e, d) {
            randomMoveX = Math.floor((Math.random() * 300)) - 150;
            randomMoveY = Math.floor((Math.random() * 300)) - 150;
            newY = e.retrieve("initPosY") + randomMoveY;
            newX = e.retrieve("initPosX") + randomMoveX;
            e.morph({opacity: 0, top: newY, left: newX});                    
        });
        mediaGalleryArray[mediaActualGalleryIndex].setStyles({top: 0, opacity: 1, "z-index": 2});

        set();

        mediaGalleryArray[mediaActualGalleryIndex].getElements("a img").each(function (e, d) {
            randomMoveX = Math.floor((Math.random() * 300)) - 150;
            randomMoveY = Math.floor((Math.random() * 300)) - 150;

            //alert(e.retrieve("initPosY"));

            newY = e.retrieve("initPosY") + randomMoveY;
            newX = e.retrieve("initPosX") + randomMoveX;
            e.setStyles({top: newY, left: newX});

            e.morph({opacity: 1, top: e.retrieve("initPosY"), left: e.retrieve("initPosX")})
        });

        (function () {
            mediaGalleryArray[mediaOldGalleryIndex].setStyles({top: 3800, "z-index": 1});
            mediaGalleryArray[mediaOldGalleryIndex].getElements("a img").each(function (e, d) {
                //e.setStyles({top: e.retrieve("initPosY"), left: e.retrieve("initPosX"), opacity: 0})
            })
        }).delay(700);

        (function () {
            $$(".prepinani .prev, .prepinani .next").store("enabled", true)
        }).delay(800)
    }

    function set() {
        var t    = 0;
        var left = 0;
        var i    = 0;
        mediaGalleryArray[mediaActualGalleryIndex].getElements("a img").each(function (e, d) {            
            newY = t;
            newX = left;
            e.setStyles({ top: newY, left: newX });   

            e.store("initPosX", newX);
            e.store("initPosY", newY);

            left += 160;

            i++;

            if(i%6 == 0 && i != 0) {
                t   += 160;
                left = 0;
                i = 0;
            }
        });
    }

});

  