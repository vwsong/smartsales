
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
    var ref = firebase.database().ref();


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

            $("input").each(function() {

                var id = $(this).attr('id');

                if (($(this).val()) === "") {
                    $(this).addClass("error");
                    val = 1
                }
                else if (id === 'inputAge' && (parseInt($(this).val()) > 99 || parseInt(($(this).val())) < 13)) {
                    $(this).addClass("error");
                    val = 1
                }
                else if (id === 'inputZip' && (parseInt($(this).val()) > 99999 || parseInt(($(this).val())) < 501)) {
                    $(this).addClass("error");
                    val = 1
                }
                else {
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
                .css('background-image', 'url("./img/items/' + mfItems[i] + '.jpg")')
                .css('background-size', 'cover');
        }

        for (i = 0; i < mItems.length; i++){
            $('#items-div')
                .append('<div class="item" id="div-'+ mItems[i] +'" data-selected="false"></div>');
            $('#div-' + mItems[i])
                .css('background-image', 'url("./img/items/men/' + mItems[i] + '.jpg")')
                .css('background-size', 'cover');
        }

        for (i = 0; i < fItems.length; i++){
            $('#items-div')
                .append('<div class="item" id="div-'+ fItems[i] +'" data-selected="false"></div>');
            $('#div-' + fItems[i])
                .css('background-image', 'url("./img/items/women/' + fItems[i] + '.jpg")')
                .css('background-size', 'cover')
        }
    }

    function sendDataToServer(){
        var customerID = 'CustID-' + generateDate();
        var age = $('#inputAge').val();
        var gender = $('#inputGender').find(':selected').data('id');
        var ethnicity = $('#inputEthnicity').find(':selected').data('id');
        var zip = $('#inputZip').val();
        var email = $('#inputEmail').val();

        var data = {};
        data[customerID] = {
            age: age,
            gender: gender,
            ethnicity: ethnicity,
            zip: zip,
            email: email,
            savedItems: clickedIDs
        };

        addCustomerToDB(data, customerID);
    }

    function addCustomerToDB(data, customerID){
        ref.child('users/')
            .update(data)
            .then(function(){
                addItemToDB(data, customerID);
            })
            .catch(function(error) {
                console.error(JSON.stringify(error));
                alert('Customer: Could not connect to the server. Please try again.');
            });
    }

    function addItemToDB(data, customerID){

        var savedItems = data[customerID].savedItems;
        var i = 0;

        savedItems.forEach(function(element){
            ref.child('items/' + element + '/interestedPersons/')
                .push(customerID)
                .then(function(){
                    i++;
                    if (i === savedItems.length) {
                        location.href = location.origin + location.pathname + "?success=true";
                    }
                }).catch(function(error) {
                    console.error(JSON.stringify(error));
                    alert('Item: Could not connect to the server. Please try again.');
                });
        });
    }

    function generateDate(){
        var date = new Date();
        var components = [
            date.getYear(),
            date.getMonth(),
            date.getDate(),
            date.getHours(),
            date.getMinutes(),
            date.getSeconds(),
            date.getMilliseconds()
        ];

        return components.join("");
    }

    // function addItemDataToDB(){
    //     for (var key in itemData){
    //         if (itemData.hasOwnProperty(key)){
    //             // "1"
    //             ref.child('items/ItemID-' + key + '/')
    //                 .update({
    //                     "price" : itemData[key]['price'],
    //                     "name" : itemData[key]['name']
    //                 })
    //                 .catch(function(error) {
    //                     console.error(JSON.stringify(error));
    //                     alert('Adding Item Info: Could not connect to the server. Please try again.');
    //                 });
    //         }
    //     }
    // }
});
