$(document).ready(function() {

    $('.btn').click(function() {
        console.log('hi');

        $.ajax({
            url: 'api/get_recent_articles/1',
            type: 'get',
            data: {

            },
            success: function(response) {
                console.log(response)
                
            }
        })

    });
});