function disableSelection(target){
    if (typeof target.onselectstart!="undefined") //For IE 
    	target.onselectstart=function(){return false}
    else if (typeof target.style.MozUserSelect!="undefined") //For Firefox
    	target.style.MozUserSelect="none"
    else //All other route (For Opera)
    	target.onmousedown=function(){return false}
    target.style.cursor = "default"
}

$(function() {
    
    // short block
    $('.js_toggle_text_btn').on('click', function(e){
        e.preventDefault();
        $(this).closest('.short_block').find('.short_content').toggleClass('hidden');
        if($(this).text() == 'Показать полностью'){
            $(this).text('Скрыть');
        } else{
            $(this).text('Показать полностью');
        }
    })

    
    
    //disableSelection($('body')[0]);
    
    var user = detect.parse(navigator.userAgent);
    if(user.browser.version < 10 && user.browser.family == 'Safari'){
        $('body').addClass('footer_no_down');
    }
    //lazyload картинок
    lazyload();
    // $('.lazyload').each(function(){
    //     $(this).attr('src', $(this).attr('data-src'));
    // });
    
	// прижать футер если не работают флексы
	function fixedFooter(){
		if($('html').hasClass('no-flexbox')){
			var bodyHeight = $('body').outerHeight(),
				 windowHeight = $(document).outerHeight(),
				 mainHeight = $('.main').outerHeight();
				 
			if(bodyHeight < windowHeight) {
				var mainAddHeight = windowHeight - bodyHeight;
				$('.main').css('height', mainHeight + mainAddHeight);
			}
		}
	}
	fixedFooter();
    
    //no dragging img
	$("img, a").on("dragstart", function(event) { event.preventDefault(); });
    
    //response table
    $(".text_edit").not( ".contants-block" ).find('table').wrap("<div class='table-wrap'></div>");
    
    //фиксированный header и мобильное меню
    var headerHeight = $('header:not(.fixed)').outerHeight();
    function onResize() {
        headerHeight = $('header:not(.fixed)').outerHeight();
    };
    var doit;
    doit = setTimeout(onResize, 400);
    
    window.onresize = function() {
      clearTimeout(doit);
      doit = setTimeout(onResize, 400);
    };
    
    $(window).scroll(function () {
        if ($(this).scrollTop() > headerHeight) {
            $('.header-fix').addClass('fixed');
        } else if ($(this).scrollTop() < headerHeight) {
            $('.header-fix').removeClass('fixed');
        }
    });
    
    //mobile menu
    $('#mob-menu-list').mmenu({
        navbar : {
            title: 'Меню'
        }
    });
    var api = $("#mob-menu-list").data( "mmenu" );
    
    api.bind( "openPanel:finish", function( $panel ) {
        $('footer').addClass('when_menu_open');
        //console.log('open');
    });
    api.bind( "closePanel", function( $panel ) {
        $('footer').removeClass('when_menu_open');
        //console.log('close');
    });
    
    //mask on input phone
	$('[name="phone"]').mask("+7(999) 999-99-99");
    
    //animate placeholder
    var show = 'show';

    $('input, textarea').on('checkval', function () {
        var label = $(this).next('label');
        if(this.value !== '') {
            label.addClass(show);
        } else {
            label.removeClass(show);
        }
    }).on('keyup', function () {
        $(this).trigger('checkval');
    });
    
    
    //btn-menu header
    $('.nav-icon1').click(function (e) {
        e.preventDefault();
        $(this).toggleClass('open');
        $('.mob-menu').fadeToggle(500);
        $('body').toggleClass('no-scroll');
    });
    
    //form-styler
    $('input, select').styler();
    
    //lazy youtube
    ( function() {

        var youtube = document.querySelectorAll( ".youtube" );
        
        for (var i = 0; i < youtube.length; i++) {
            
            var source = "https://img.youtube.com/vi/"+ youtube[i].dataset.embed +"/0.jpg";
            
            var image = new Image();
                    image.src = source;
                    image.addEventListener( "load", function() {
                        youtube[ i ].appendChild( image );
                    }( i ) );
            
                    youtube[i].addEventListener( "click", function() {
    
                        var iframe = document.createElement( "iframe" );
    
                                iframe.setAttribute( "frameborder", "0" );
                                iframe.setAttribute( "allowfullscreen", "" );
                                iframe.setAttribute( "src", "https://www.youtube.com/embed/"+ this.dataset.embed +"?rel=0&showinfo=0&autoplay=1" );
    
                                this.innerHTML = "";
                                this.appendChild( iframe );
                    } );    
        };
        
    } )();
    
    //carousel
    $('.top-carousel').addClass('owl-carousel').owlCarousel({
        loop: false,
        margin: 24,
        lazyLoad:true,
        nav: false,
        navText: [],
        navClass: ['arrow-left', 'arrow-right'],
        dots: true,
        items:3,
        responsive:{
            0:{
                items:1,
                nav: false
            },
            560:{
                items:1,
                nav: false
            },
            767:{
                items:1,
                nav: false
            },
            992:{
                items:1,
                nav: false
            },
            1200:{
                items:1,
                nav: false
            }
        }
    });
    
    //mob menu scroll about window height
    if ($(window).height() < 565) {
        $('.mm-listview > li.phone-wp, .mm-listview > li.adress-wp').addClass('min_size');
    } else {
        $('.mm-listview > li.phone-wp, .mm-listview > li.adress-wp').removeClass('min_size');
    }
    
    $(window).on('resize', function () {
        if ($(window).height() < 565) {
            $('.mm-listview > li.phone-wp, .mm-listview > li.adress-wp').addClass('min_size');
        } else {
            $('.mm-listview > li.phone-wp, .mm-listview > li.adress-wp').removeClass('min_size');
        }
    });
    $( window ).on( "orientationchange", function( event ) {
        if ($(window).height() < 565) {
            $('.mm-listview > li.phone-wp, .mm-listview > li.adress-wp').addClass('min_size');
        } else {
            $('.mm-listview > li.phone-wp, .mm-listview > li.adress-wp').removeClass('min_size');
        }
    });
    
    //fancybox init
    $('.fancybox').fancybox({
        'autoScale': true,
        'touch': false,
        'transitionIn': 'elastic',
        'transitionOut': 'elastic',
        'speedIn': 500,
        'speedOut': 300,
        'autoDimensions': true,
        'centerOnScroll': true
    });

});

$(window).load(function() {

	$(".loader_inner").fadeOut();
	$(".loader").delay(400).fadeOut("slow");

});