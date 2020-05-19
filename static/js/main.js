function check() {
            var x = document.getElementById('password').innerHTML;
            var y = document.getElementById('re_password').innerHTML;
            if(x.value == y.value) {
                return true;
            }
            else {
                return false;
            }
        }
(function($) {

    $(".toggle-password").click(function() {

        $(this).toggleClass("zmdi-eye zmdi-eye-off");
        var input = $($(this).attr("toggle"));
        if (input.attr("type") == "password") {
          input.attr("type", "text");
        } else {
          input.attr("type", "password");
        }
      });

})(jQuery);