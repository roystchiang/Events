$(window).scroll(function() {
if ($(this).scrollTop() > 68){
    $('header').addClass("sticky");
    $('section#top').addClass("sticky");
  }
  else{
    $('header').removeClass("sticky");
    $('section#top').removeClass("sticky");
  }
});