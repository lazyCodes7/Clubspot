jQuery(document).ready(function ($) {
    $("#btnSubmit").click(function() {
        console.log("button click");
        let csv_file = $("#csv_file").prop("files")[0];
        var data = new FormData();
        data.append("file",csv_file);
       // If you want to add an extra field for the FormData
       //  data.append("CustomField", "This is some extra data, testing");

       // disabled the submit button
        $("#btnSubmit").prop("disabled", true);

        $.ajax({
            type: "POST",
            enctype: 'multipart/form-data',
            url: "https://attendanceai.herokuapp.com/behaviour",
            data: data,
            processData: false,
            contentType: false,
            cache: false,
            timeout: 800000,
            success: function (data) {
                console.log(data);
                for (var key in data) {
                    if (data.hasOwnProperty(key)) {
                        let res = JSON.parse(data[key]);
                        Plotly.newPlot(key, res["data"], res['layout']);
                    }
                }
                $("#btnSubmit").prop("disabled", false);

            },
            error: function (e) {
                $("#output").text(e.responseText);
                console.log("ERROR : ", e);
                $("#btnSubmit").prop("disabled", false);

            }
        });
    });
});