$('#serverror').toast({delay:5000});

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            if(cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');
function csrfSafeMethod(method) {
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});


$("#ajax_request_btn").click(function () {
    $.ajax({
        type:"POST",
        url:"convert",
        data: {
            'original_url': $("#original_url_input").val(),
        },
        dataType: "json",
        cache: false,

        success: function (data) {
            $("#linkForm").trigger("reset");
            $("#form-errors-container").hide();
            $("#shortLinkContainer").html(data["shortlink_url"]);
            $("#shortLinkContainer").show();
            if (data["duplicate"]) {
                $("#duplicateLinkNotice").show();
            } else {
                $("#duplicateLinkNotice").hide();
            }
        },

        error: function (xhr, options, thrownError) {
            var errorContainer = $("#form-errors-container");
            if (xhr.responseJSON && xhr.responseJSON["error"]) {
                error = xhr.responseJSON["error"];
                errorContainer.html(error);
                errorContainer.show();
            } else {
                $('#serverror').toast("show");
            }

            $("#shortLinkContainer").hide();
            $("#duplicateLinkNotice").hide();
        }
    });
});