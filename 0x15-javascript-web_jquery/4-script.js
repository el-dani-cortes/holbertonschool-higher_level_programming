/*
JavaScript script that toggles the class of the <header>
element when the user clicks on the tag DIV#toggle_header
*/
$('DIV#toggle_header').click(function () {
  if ($('header').hasClass('red')) {
    $('header').removeClass('red');
    $('header').addClass('green');
  } else {
    $('header').removeClass('green');
    $('header').addClass('red');
  }
});
