/*!
 * Start Bootstrap - Freelancer Bootstrap Theme (http://startbootstrap.com)
 * Code licensed under the Apache License v2.0.
 * For details, see http://www.apache.org/licenses/LICENSE-2.0.
 */

// jQuery for page scrolling feature - requires jQuery Easing plugin
$(function() {
  $(".page-scroll a").bind("click", function(event) {
    var $anchor = $(this);
    $("html, body")
      .stop()
      .animate(
        {
          scrollTop: $($anchor.attr("href")).offset().top
        },
        1500,
        "easeInOutExpo"
      );
    event.preventDefault();
  });
});

// Floating label headings for the contact form
$(function() {
  $("body")
    .on("input propertychange", ".floating-label-form-group", function(e) {
      $(this).toggleClass(
        "floating-label-form-group-with-value",
        !!$(e.target).val()
      );
    })
    .on("focus", ".floating-label-form-group", function() {
      $(this).addClass("floating-label-form-group-with-focus");
    })
    .on("blur", ".floating-label-form-group", function() {
      $(this).removeClass("floating-label-form-group-with-focus");
    });
});

// Contact form processing
$(function() {
  if (window.location.hash) {
    if (window.location.hash == "#error") {
      $("#contact .alert-danger").show();
    } else if (window.location.hash == "#success") {
      $("#contact .alert-success").show();
    }
  }
});
// select2
$(function(){
  $(".product-filter select").select2({
    allowClear: true,
    minimumInputLength: 2
  });
})

// Closes the Responsive Menu on Menu Item Click
$(".navbar-collapse ul li a").click(function() {
  $(".navbar-toggle:visible").click();
});

$(function(){
  moment().locale("es");
  $(".month").each(function(){
    var activeMonth = $(this).data('month').trim().toLowerCase();
    if(activeMonth +"." == moment().format("MMM")){
      $(this).addClass('active');
      return;
    }
  });
  $("#lang").on('change',function(){
    selected = $(this).val();
    location.href = location.origin + selected;
  });
});
