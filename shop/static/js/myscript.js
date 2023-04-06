function showVal(x) {
    x = x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ',');
    document.getElementById('cur_price').innerText = x;
}




function status_of_shop_cart() {
    $.ajax({
        type: 'GET',
        url: '/orders/status_of_shop_cart/',
        success: function(res) {
            $("#indicator__value").text(res);
        }
    });
}
status_of_shop_cart()



function add_to_shop_cart(product_id, qty) {
    if (qty === 0) {
        qty = $('#product-quantity').val();
    }
    $.ajax({
        type: 'GET',
        url: '/orders/add_to_shop/',
        data: {
            product_id: product_id,
            qty: qty
        },
        success: function(res) {
            alert('کالای مورد نظر به سبد شما اضافه شد');
            status_of_shop_cart();
        }
    });
}

function delete_from_shop(product_id) {

    $.ajax({
        type: 'GET',
        url: '/orders/delete_from_shop/',
        data: {
            product_id: product_id,
        },
        success: function(res) {
            alert('کالای مورد نظر از سبد شما حذف شد');
            $("#show_shopcart").html(res)
            status_of_shop_cart();
        }
    });
}

function update_shop_cart() {
    var product_id_list = []
    var qty_list = []
    $("input[id^='qty-']").each(function(index) {
        product_id_list.push($(this).attr('id').slice(4));
        qty_list.push($(this).val())
    });
    console.log(product_id_list);
    console.log(qty_list);
    $.ajax({
        type: 'GET',
        url: '/orders/update_shop_cart/',
        data: {
            product_id_list: product_id_list,
            qty_list: qty_list
        },
        success: function(res) {
            $("#show_shopcart").html(res)
            status_of_shop_cart();

        }
    });

}

function ShowcreateCommentForm(productid, commentid, slug) {
    alert('hi')

    $.ajax({
        type: 'GET',
        url: '/csf/create_comment/' + slug,
        data: {
            productid: productid,
            commentid: commentid,
        },
        success: function(res) {
            $("#btn_" + commentid).hide();
            $("#comment_form_" + commentid).html(res);

        }
    });

}

function addScore(score, productid) {
    var starRatings = document.querySelectorAll('.fa-star');
    starRatings.forEach(element => {
        element.classList.remove('checked');
    });
    for (let i = 1; i <= score; i++) {
        const element = document.getElementById("star_" + i);
        element.classList.add('checked');
    }
    $.ajax({
        type: 'GET',
        url: '/csf/add_score/',
        data: {
            productid: productid,
            score: score,
        },
        success: function(res) {
            alert(res);

        }
    });
    starRatings.forEach(element => {
        element.classList.add("disable");
    });
}