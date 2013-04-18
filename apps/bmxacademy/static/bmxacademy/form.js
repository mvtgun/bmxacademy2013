function init_form(form_url, formid, submitid, domid){
    $(document).ready(function(){
        // $("input").keypress(function(e){
        //     console.log(e);
        //     if (e.which == 13) {
        //         form_request();
        //         return false;
        //     }
        // });

        done = function (data) {
            if(data.indexOf("redirect:") !== -1) document.location.href = data.split(":")[1];
            else {
                $(domid).html(data);
                $(submitid).click(form_request); 
            }
        }

        function form_request() {
            django_remote_ajax.post(form_url, done, $(formid).serialize());
        }

        django_remote_ajax.get(form_url, function (data) {
            $(domid).html(data);
            $(submitid).click(form_request);
        });
    });
}
