$(document).ready(function() {
  $('#access-denied-message').fadeIn();

  $(document).on('click', '#close-button', function() {
    $('#access-denied-message').fadeOut();
  });

  setTimeout(function() {
  $('#access-denied-message').fadeOut();
  }, 5000);

});

