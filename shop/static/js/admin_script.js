$(document).ready(function() {
    var ListOfElements = $('select[id^="id_feature_pro-"][id$="-feature"]')

    $(ListOfElements).on('change', function() {
        f_id = $(this).val();
        dd1 = $(this).attr('id');
        dd2 = dd1.replace("-feature", "-filter_value");

        $.ajax({
            type: 'GET',
            url: "product/ajax_admin/?feature_id=" + f_id,
            success: function(res) {
                cols = document.getElementById(dd2);
                cols.options.length = 0;
                for (var k in res) {
                    cols.options.add(new Option(k, res[k]));
                }
            }
        });
    });
});