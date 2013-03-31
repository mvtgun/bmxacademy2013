$.Bundle = function (con, lin, hei, pos) {
    var content =  $(con);
    var link = $(lin);
    var height =  $(content).parent().height();
    var position = $(content).offset().top;

    this.getContent = function ()
    {
        return content;
    }
    this.getLink = function ()
    {
        return link;
    }
    this.getHeight = function ()
    {
        return height;
    }
    this.getPosition = function ()
    {
        return position;
    }

};