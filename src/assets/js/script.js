jQuery(function ($) {
  'use strict';

  /* ----------------------------------------------------------- */
  /*  Fixed header on scroll
  /* ----------------------------------------------------------- */
  $(window).on('scroll', function () {
    var headerTopBar = $('.top-bar').outerHeight() || 0;
    var headerOneTopSpace = $('.header-one .logo-area').outerHeight() || 0;
    var headerOneElement = $('.header-one .site-navigation');

    if ($(window).scrollTop() > headerTopBar + headerOneTopSpace) {
      headerOneElement.addClass('navbar-fixed');
      $('.header-one').css('margin-bottom', headerOneElement.outerHeight());
    } else {
      headerOneElement.removeClass('navbar-fixed');
      $('.header-one').css('margin-bottom', 0);
    }

    // Counter Up Animation
    var oTop;
    if ($('.counterUp').length !== 0) {
      oTop = $('.counterUp').offset().top - window.innerHeight;
    }
    if ($(window).scrollTop() > oTop) {
      $('.counterUp').each(function () {
        var $this = $(this);
        if (!$this.hasClass('counted')) {
          $this.addClass('counted');
          var countTo = $this.attr('data-count');
          $({ countNum: $this.text() }).animate(
            { countNum: countTo },
            {
              duration: 1200,
              easing: 'swing',
              step: function () {
                $this.text(Math.floor(this.countNum));
              },
              complete: function () {
                $this.text(this.countNum);
              }
            }
          );
        }
      });
    }

    // Scroll to top button show/hide
    var scrollToTop = $('#back-to-top');
    if ($(window).scrollTop() >= 100) {
      scrollToTop.fadeIn();
    } else {
      scrollToTop.fadeOut();
    }
  });

  $(document).ready(function () {
    // Back to top click
    $('#back-to-top').on('click', function (e) {
      e.preventDefault();
      $('body,html').animate({ scrollTop: 0 }, 600);
      return false;
    });

    // Banner Carousel 1
    if ($('.banner-carousel.banner-carousel-1').length) {
      $('.banner-carousel.banner-carousel-1').slick({
        slidesToShow: 1,
        slidesToScroll: 1,
        autoplay: true,
        autoplaySpeed: 5000,
        dots: true,
        speed: 600,
        arrows: true,
        prevArrow: '<button type="button" class="carousel-control left" aria-label="carousel-control"><i class="fas fa-chevron-left"></i></button>',
        nextArrow: '<button type="button" class="carousel-control right" aria-label="carousel-control"><i class="fas fa-chevron-right"></i></button>'
      });
      if ($.fn.slickAnimation) {
        $('.banner-carousel.banner-carousel-1').slickAnimation();
      }
    }

    // Shuffle JS Filter & Masonry
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

    // Colorbox Popups for Projects
    if ($.fn.colorbox) {
      $('.gallery-popup').colorbox({
        rel: 'gallery-popup',
        transition: 'elastic',
        innerHeight: '550',
        maxWidth: '95%'
      });
    }

    // Smooth Scroll for Navigation Anchors
    $('a[href^="#"]:not([href="#"]):not([data-toggle])').on('click', function (e) {
      var target = $(this.getAttribute('href'));
      if (target.length) {
        e.preventDefault();
        var navHeight = $('.site-navigation').outerHeight() || 60;
        $('html, body').stop().animate({
          scrollTop: target.offset().top - navHeight
        }, 600);

        if ($('#navbar-collapse').hasClass('show')) {
          $('.navbar-toggler').click();
        }
      }
    });
  });
});