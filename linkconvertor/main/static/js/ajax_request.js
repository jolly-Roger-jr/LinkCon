$('#serverror').toast({delay:5000});

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