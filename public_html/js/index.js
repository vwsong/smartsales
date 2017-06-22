
$(document).ready(function(){

    showSuccessAlert();
    populateItems();
    setImageClickListener();
    setSubmitListener();
    setJumboCloseListener();

    /**
     * VARIABLES
     */
    var clickedIDs = [];

    /**
     * FUNCTIONS
     */
    function showSuccessAlert(){
        if (getQueryParam('success') === 'true'){
            $('.alert').removeClass('hidden');
        }
    }

    function setImageClickListener(){
        $('.item').on('click', function(event){
            var clickedItem = $('#' + event.target.id);

            if (clickedItem.parent().attr('data-selected') === 'true' || typeof clickedItem.attr('data-selected') === 'undefined'){
                clickedItem.parent()
                    .html('')
                    .attr('data-selected', 'false');
                var index = clickedIDs.indexOf(event.target.id.replace('check-', ''));
                if (index > -1) {
                    clickedIDs.splice(index, 1);
                }
            } else {
                clickedItem
                    .html('<img src="img/check.png" alt="check" class="checkMark" id="check-'+ event.target.id.replace('div-', '') +'"/>')
                    .attr('data-selected', 'true');
                clickedIDs.push('ItemID-' + event.target.id.replace('div-', ''));
            }
        });
    }

    function getQueryParam(param) {
        location.search.substr(1)
            .split("&")
            .some(function(item) { // returns first occurence and stops
                return item.split("=")[0] === param && (param = item.split("=")[1])
            });
        return param
    }

    function setSubmitListener(){

        $('#submitBtn').on('click', function(){
            var val = 0;

            $("input").each(function(){
                if (($(this).val()) === ""){
                    $(this).addClass("error");
                    val = 1
                }
                else{
                    $(this).removeClass("error");
                }
            });

            // if you want to check select fields
            $("select").each(function(){
                if (($(this).val()) === ""){
                    $(this).addClass("error");
                    val = 1
                }
                else{
                    $(this).removeClass("error");
                }
            });

            if (val === 1) {
                alert('Please fix the fields.');
            } else if (clickedIDs.length === 0){
                alert('Please select an item.');
            } else {
                sendDataToServer();
            }
        });
    }

    function setJumboCloseListener(){
        $('#dismiss-jumbo').on('click', function(){
            $('#jumbotron-div').remove();
        });
    }

    function populateItems (){
        for (var i = 0; i < mfItems.length; i++){
            $('#items-div')
                .append('<div class="item" id="div-'+ mfItems[i] +'" data-selected="false"></div>');
            $('#div-' + mfItems[i])
                .css('background-image', 'url("/smart-sales/public_html/img/items/' + mfItems[i] + '.jpg")')
                .css('background-size', 'cover');
        }

        for (i = 0; i < mItems.length; i++){
            $('#items-div')
                .append('<div class="item" id="div-'+ mItems[i] +'" data-selected="false"></div>');
            $('#div-' + mItems[i])
                .css('background-image', 'url("/smart-sales/public_html/img/items/men/' + mItems[i] + '.jpg")')
                .css('background-size', 'cover');
        }

        for (i = 0; i < fItems.length; i++){
            $('#items-div')
                .append('<div class="item" id="div-'+ fItems[i] +'" data-selected="false"></div>');
            $('#div-' + fItems[i])
                .css('background-image', 'url("/smart-sales/public_html/img/items/women/' + fItems[i] + '.jpg")')
                .css('background-size', 'cover')
        }
    }

    function sendDataToServer(){
        var customerID = new Date().valueOf();
        var age = $('#inputAge').val();
        var gender = $('#inputGender').find(':selected').data('id');
        var ethnicity = $('#inputEthnicity').find(':selected').data('id');
        var zip = $('#inputZip').val();

        var data = {
            customerID : 'CustID-' + customerID,
            age: age,
            gender: gender,
            ethnicity: ethnicity,
            address: zip,
            savedItems: clickedIDs
        };

        // $.post("https://qtpmimexld.localtunnel.me/api/subscribe", data, function(res){
        //         alert("Thank you!");
        //         location.href = "/smart-sales/?success=true";
        //     })
        //     .fail(function(err){
        //         console.error(JSON.stringify(err));
        //         alert('Could not connect to the server. Please try again.');
        //     });

        $.ajax({
            url: 'https://qtpmimexld.localtunnel.me/api/subscribe',
            type: 'POST',
            contentType: 'application/json',
            data: data,
            success: function(res){
                alert("Thank you!");
                location.href = "/smart-sales/?success=true";
            },
            error: function(err){
                alert(JSON.stringify(err));
                alert('Could not connect to the server. Please try again.');
            }
        });
    }
});
