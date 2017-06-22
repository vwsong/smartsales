
$(document).ready(function(){

    // populateItems();
    setImageClickListener();

    /**
     * VARIABLES
     */
    var clickedIDs = [];

    /**
     * FUNCTIONS
     */
    function setImageClickListener(){
        $('.item').on('click', function(event){
            alert(event.target.id);

            // $('#div-' + event.target.id).append('' +
            //     '<img src="img/check.png" alt="check" class="checkMark"/>');
        });
    }

    function populateItems (){
        for (var i = 0; i < mfItems.length; i++){
            $('#items-div').append('' +
                '<div class="item" id="div-'+ mfItems[i] +'" data-selected="false">' +
                    '<img src="img/items/' + mfItems[i] + '.jpg" alt="itemImage" id="' + mfItems[i] + '"/>' +
                '</div>');
        }

        for (i = 0; i < mItems.length; i++){
            $('#items-div').append('' +
                '<div class="item" id="div-'+ mItems[i] +'" data-selected="false">' +
                '<img src="img/items/men/' + mItems[i] + '.jpg" alt="itemImage" id="' + mItems[i] + '"/>' +
                '</div>');
        }

        for (i = 0; i < fItems.length; i++){
            $('#items-div').append('' +
                '<div class="item" id="div-'+ fItems[i] +'" data-selected="false">' +
                '<img src="img/items/women/' + fItems[i] + '.jpg" alt="itemImage" id="' + fItems[i] + '"/>' +
                '</div>');
        }
    }
});




/*
    <div class="item">
        <img src="img/items/5870872.jpg" alt="5870872"/>
    </div>
 */