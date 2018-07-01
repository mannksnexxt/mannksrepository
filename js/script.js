$('.nav-btn').on('click', function(e) {
	e.preventDefault();
	$('.navbar').toggleClass('navbar-active');
});

var translateWidth = 0;
var actual_slide = 1;
var slide_count = $('.slideshow').children().length;
var interval = 2000;
var navBtnId = 0;

$(document).ready(function () {
	var switchInterval = setInterval(nextSlide, interval);

	$('.viewport').hover(function(){
        clearInterval(switchInterval);
	},
	function() {
    	switchInterval = setInterval(nextSlide, interval);
	});

	$('.next-btn').click(function() {
        nextSlide();
    });

    $('.prev-btn').click(function() {
        prevSlide();
	});
	$('.slide-nav-btn').click(function() {
        navBtnId = $(this).index();

        if (navBtnId + 1 != actual_slide) {
            translateWidth = -$('.viewport').width() * (navBtnId);
            $('.slideshow').css({
                'transform': 'translate(' + translateWidth + 'px, 0)',
                '-webkit-transform': 'translate(' + translateWidth + 'px, 0)',
            });
            actual_slide = navBtnId + 1;
        }
});
});

function nextSlide() {
	if (actual_slide == slide_count || actual_slide <= 0 || actual_slide > slide_count) {
		$('.slideshow').css('transform', 'translate(0, 0)');
		actual_slide = 1;
	} else {
		translateWidth = -$('.viewport').width() * (actual_slide);
		$('.slideshow').css({
			'transform': 'translate(' + translateWidth + 'px, 0)',
            '-webkit-transform': 'translate(' + translateWidth + 'px, 0)',
		});
		actual_slide++;
	}
}

function prevSlide() {
    if (actual_slide == 1 || actual_slide <= 0 || actual_slide > slide_count) {
        translateWidth = -$('.viewport').width() * (slide_count - 1);
        $('.slideshow').css({
            'transform': 'translate(' + translateWidth + 'px, 0)',
            '-webkit-transform': 'translate(' + translateWidth + 'px, 0)',
        });
        actual_slide = slide_count;
    } else {
        translateWidth = -$('.viewport').width() * (actual_slide - 2);
        $('.slideshow').css({
            'transform': 'translate(' + translateWidth + 'px, 0)',
            '-webkit-transform': 'translate(' + translateWidth + 'px, 0)',
        });
        actual_slide--;
    }
}
