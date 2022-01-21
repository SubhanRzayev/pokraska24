$(function(){
    function hashTag (str){
        var hash = 0;
        if (str.length == 0) return hash;
        for (i = 0; i < str.length; i++) {
            char = str.charCodeAt(i);
            hash = ((hash<<5)-hash)+char;
            hash = hash & hash; // Convert to 32bit integer
        }
        return 'tag-'+Math.abs(hash);
    }
    
    var tag_links = $('.filter-item');
    var photos = $('.gallery_item');
    
    if(tag_links.length > 1){
        tag_links.each(function(idx, el){
            var tag = $(el);
            tag.bind('click', function(){
                var link = $(this);
                var hash = hashTag(link.text());
                var images = $('.gallery_item');
                images.hide();
                $('.gallery_item.'+hash).show();
                link.addClass('active').siblings().removeClass('active');
            });
        });
        
        photos.each(function(idx, el){
            var image = $(el);
            var tags = image.find('img').data('tags');
            if(!tags)
                return true;
                
            tags = tags.split('|');
            tags.forEach(function(tag){
                image.addClass(hashTag(tag));
            });
        });
        
        $('.filter-item').first().trigger('click');
    }
    else{
        photos.show();
        tag_links.hide();
    }
});