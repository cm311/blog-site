var page_num = 1;

$(document).ready(function() {

    
    $.ajax({
        url: 'api/get_recent_articles/' + page_num,
        type: 'get',
        data: {
        },

        success: function(response) {
            for (var key in response){
                console.log( key, response[key] );
                render_article(response[key], page_num);
            }

            

            var newer = '<a href="#' + (page_num - 1) + '" id="newer-link">newer</a>';
            var older = '<a href="#' + (page_num + 1) + '" id="older-link">older</a>';
            console.log(newer);
            document.getElementById('footer').innerHTML += newer;
            document.getElementById('footer').innerHTML += older;

            if(page_num == 1) {
                var newer = document.getElementById('newer-link').hidden = true;
            }

            $('#newer-link').click(function() {
                console.log('clikced newer');
                if(page_num == 1) {
                    document.getElementById('newer-link').hidden = true;
                }
            });
            
            $('#older-link').click(function() {
                console.log('clikced older');
                page_num += 1;
                    document.getElementById('newer-link').hidden = false;
            });
        }

    })
});



function render_article(article) {
    var element = document.getElementById('articles-main');
    var markup = '<div class="text"><h3 class="h4">' + article.article_title + '</h3><small class="date-posted">Posted on ' 
                + article.date + '</small><p><br>' + article.body + '</p></div>';
    element.innerHTML+= markup;
}