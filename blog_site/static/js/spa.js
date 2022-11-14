var page_num = 1;


function change_page(direction) {
    page_num += direction
    console.log('changing page to' + page_num);
    $('#articles-main').empty();
    $.ajax({
        url: 'api/get_recent_articles/' + page_num,
        type: 'get',
        data: {
        },

        success: function(response) {
            articles = []
            for (var key in response){
                articles.push(render_article(response[key]));
            }

            articles.reverse();
            for(var i=0; i < articles.length; i++) {
                var element = document.getElementById('articles-main');
                element.innerHTML+= articles[i];
            }

            if ($('#articles-main div').length < 5) {
                $('#older-link').attr('hidden', true);
            }
            else {
                $('#older-link').attr('hidden', false)
            }
        }
    });

    if(page_num == 1) {
        $('#newer-link').attr('hidden', true);
    }
    else {
        $('#newer-link').attr('hidden', false);
    }
}   


$(document).ready(function() {
    if(page_num == 1) {
        $('#newer-link').attr('hidden', true);
    }

    $.ajax({
        url: 'api/get_recent_articles/' + page_num,
        type: 'get',
        data: {
        },

        success: function(response) {
            articles = []
            for (var key in response){
                articles.push(render_article(response[key]));
            }

            articles.reverse();
            for(var i=0; i < articles.length; i++) {
                var element = document.getElementById('articles-main');
                element.innerHTML+= articles[i];
            }

            if ($('#articles-main div').length < 5) {
                $('#older-link').attr('hidden', true);
            }
        }
    });
});




function render_article(article) {
    //var element = document.getElementById('articles-main');
    var markup = '<div class="text"><h3 class="h4">' + article.article_title + '</h3><small class="date-posted">Posted on ' 
                + article.date + '</small><p><br>' + article.body + '</p></div>';
    //element.innerHTML+= markup;
    return markup
}

function render_search_results(data) {
    console.log('in this funciton at least');
}