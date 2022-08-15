$(window).scroll(function(){
    var scrl = $(window).scrollTop();
    if(scrl < 60)
        {
            $('.navbar').removeClass('fixedbar');
        }
    else{
        $('.navbar').addClass('fixedbar');
    }
});

