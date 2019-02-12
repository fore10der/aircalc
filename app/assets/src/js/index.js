import $ from "jquery";
import "bootstrap"
window.$ = $;
import 'slick-carousel';
// import './dropzoneloader.js'

let $status = $('.pager .pagenum')
let $uploadSlider = $('.upload_slider')
let $reportSlider = $('.report_slider')
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

if($reportSlider.length && !$emptymark.length){
  $reportSlider.on('afterChange',(event, slick, currentSlide, nextSlide)=>{
    let i = Math.floor(currentSlide/2)+1;
    $status.text(i);
  });
  $reportSlider.slick({
      dots: false,
      vertical: true,
      slidesToShow: 2,
      slidesToScroll: 2,
      verticalSwiping: true,
      prevArrow: $prev,
      nextArrow: $next,
    })
}