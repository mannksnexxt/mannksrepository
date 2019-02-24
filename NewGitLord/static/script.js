$(function() {
    $('.repository').on('click', function() {
        window.location.replace('/repositories/' + $(this).attr('name'));
    });

    $('.toggle-form').on('click', function() {
        $('.hidden-form').toggleClass('active-form');
        $(this).toggleClass('to-close');
    });
    // 
    // $('.branch').on('click', function() {
    //     window.location.replace('')
    // });
});
