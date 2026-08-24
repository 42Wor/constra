jQuery(function ($) {
  'use strict';

  /* ----------------------------------------------------------- */
  /*  Fixed header
  /* ----------------------------------------------------------- */
  $(window).on('scroll', function () {
    // fixedHeader on scroll
    function fixedHeader() {
      var headerTopBar = $('.top-bar').outerHeight() || 0;
      var headerOneTopSpace = $('.header-one .logo-area').outerHeight() || 0;
      var headerOneElement = $('.header-one .site-navigation');

      if ($(window).scrollTop() > headerTopBar + headerOneTopSpace) {
        $(headerOneElement).addClass('navbar-fixed');
        $('.header-one').css('margin-bottom', headerOneElement.outerHeight());
      } else {
        $(headerOneElement).removeClass('navbar-fixed');
        $('.header-one').css('margin-bottom', 0);
      }
    }
    fixedHeader();

    // Count Up
    function counter() {
      var oTop;
      if ($('.counterUp').length !== 0) {
        oTop = $('.counterUp').offset().top - window.innerHeight;
      }
      if ($(window).scrollTop() > oTop) {
        $('.counterUp').each(function () {
          var $this = $(this),
            countTo = $this.attr('data-count');
          $({
            countNum: $this.text()
          }).animate({
            countNum: countTo
          }, {
            duration: 1000,
            easing: 'swing',
            step: function () {
              $this.text(Math.floor(this.countNum));
            },
            complete: function () {
              $this.text(this.countNum);
            }
          });
        });
      }
    }
    counter();

    // scroll to top btn show/hide
    function scrollTopBtn() {
      var scrollToTop = $('#back-to-top'),
        scroll = $(window).scrollTop();
      if (scroll >= 50) {
        scrollToTop.fadeIn();
      } else {
        scrollToTop.fadeOut();
      }
    }
    scrollTopBtn();
  });

  $(document).ready(function () {
    // back to top
    function backToTop() {
      $('#back-to-top').on('click', function () {
        $('#back-to-top').tooltip('hide');
        $('body,html').animate({
          scrollTop: 0
        }, 800);
        return false;
      });
    }
    backToTop();

    // banner-carousel
    function bannerCarouselOne() {
      $('.banner-carousel.banner-carousel-1').slick({
        slidesToShow: 1,
        slidesToScroll: 1,
        autoplay: true,
        dots: true,
        speed: 600,
        arrows: true,
        prevArrow: '<button type="button" class="carousel-control left" aria-label="carousel-control"><i class="fas fa-chevron-left"></i></button>',
        nextArrow: '<button type="button" class="carousel-control right" aria-label="carousel-control"><i class="fas fa-chevron-right"></i></button>'
      });
      $('.banner-carousel.banner-carousel-1').slickAnimation();
    }
    bannerCarouselOne();

    // Shuffle js filter and masonry
    function projectShuffle() {
      if ($('.shuffle-wrapper').length !== 0) {
        var Shuffle = window.Shuffle;
        var myShuffle = new Shuffle(document.querySelector('.shuffle-wrapper'), {
          itemSelector: '.shuffle-item',
          sizer: '.shuffle-sizer',
          buffer: 1
        });
        $('input[name="shuffle-filter"]').on('change', function (evt) {
          var input = evt.currentTarget;
          if (input.checked) {
            myShuffle.filter(input.value);
          }
        });
        $('.shuffle-btn-group label').on('click', function () {
          $('.shuffle-btn-group label').removeClass('active');
          $(this).addClass('active');
        });
      }
    }
    projectShuffle();

    // media popup
    function mediaPopup() {
      $('.gallery-popup').colorbox({
        rel: 'gallery-popup',
        transition: 'slideshow',
        innerHeight: '500'
      });
    }
    mediaPopup();
  });
});