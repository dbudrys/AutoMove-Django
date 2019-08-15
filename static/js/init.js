/*
(function($){
  $(function(){

    $('.sidenav').sidenav();

  }); // end of document ready
})(jQuery); // end of jQuery name space
*/


// Initializing 
$(document).ready(function(){
  
  $('.sidenav').sidenav();

  $('.parallax').parallax();

  $('.materialboxed').materialbox();

  $('.scrollspy').scrollSpy();

  $('.fixed-action-btn').floatingActionButton();

  $('.modal').modal();
  
  $('.carousel').carousel();

  $('select').formSelect();

});


/* Scroll to top when arrow up clicked BEGIN */
/* Use scrollspy to make action button to scroll to the top */
/* Must set wanted button to display: none; */
$(window).scroll(function() {
  var height = $(window).scrollTop();
  if (height > 200) {
      $('.fixed-action-btn').fadeIn();
  } else {
      $('.fixed-action-btn').fadeOut();
  }
});


/*
  jQuery succes TOAST message when form was successfully sent
*/
$(document).ready(function() {
  if ( $('#success_toast').length ) //If checking if the element exists, use .length
      M.toast({html: 'Žinutė Sėkmingai Išsiųsta!', classes: 'rounded green', displayLength: 7000})
});


