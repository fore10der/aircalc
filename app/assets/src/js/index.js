import $ from "jquery";
window.$ = $;
import 'slick-carousel';

let $status = $('.pager .pagenum')
let $uploadSlider = $('.upload_slider')
let $prev = $('.pager .prev')
let $next = $('.pager .next')
let $emptymark = $('.is_empty')

if($uploadSlider.length && !$emptymark.length){
  $uploadSlider.on('afterChange',(event, slick, currentSlide, nextSlide)=>{
    let i = Math.floor(currentSlide/3)+1;
    $status.text(i);
  });
  $uploadSlider.slick({
      dots: false,
      vertical: true,
      slidesToShow: 3,
      slidesToScroll: 3,
      verticalSwiping: true,
      prevArrow: $prev,
      nextArrow: $next,
    })
}