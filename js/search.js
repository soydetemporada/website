$(document).ready(function() {
  var calendar = null;
  moment().locale("es");

  // Initialize event handlers
  $(".month").on("click", filterByMonthHandler);

  $(".product-filter select").on("change.select2", function(e) {
    var selected = parseInt($(e.target).val());
    if (selected) {
      var $grid = $(".grid").isotope({
        filter: function() {
          var id = parseInt(
            $(this)
              .find(".id")
              .text()
          );
          return id == selected;
        }
      });
    } else {
      var $grid = $(".grid").isotope({
        filter: "*"
      });
      organizeProducts();
    }
  });

  $(".grid").imagesLoaded(function(){
    var $loader = $(".loader");
    var $items = $(".grid");
    $loader.show();
    $items.hide();
    filterProducts(true);
    $items.show();
    $loader.hide();

  });

  /**
  * Organize the product grid using isotope
  */
  function organizeProducts() {
    var $grid = $(".grid").isotope({
      itemSelector: ".product-item",
      getSortData: {
        id: ".id parseInt",
        season: ".season parseInt",
        category: ".category",
      },
      percentPosition: true,
      masonry: {
        columnWidth: ".col-sm-2"
      },
      sortBy: ["season","category" ,"id"]
    });
    $grid.isotope("updateSortData").isotope();
  }

  /**
  * Filter by month handler
  */
  function filterByMonthHandler(e) {
    e.preventDefault();
    $(".month").removeClass("active");
    $(e.target).addClass("active");
    filterProducts();
  }

  /**
  * Initialize the active month based on the browser date
  */
  function initializeActiveMonth(){
    $(".month").each(function(){
      var activeMonth = $(this).data('month').trim().toLowerCase();
      if(activeMonth +"." == moment().format("MMM")){
        $(this).addClass('active');
        filterActive(activeMonth);
        return;
      }
    });
  }
  /**
  * Filter products handler
  */
  function filterProducts(firstLoad) {
    var initActive = firstLoad || false;
    if(initActive){
      initializeActiveMonth();
    }
    else{
      var activeMonth = $(".month.active")
        .data("month")
        .trim();
      filterActive(activeMonth);
    }
  }

  /**
  * Filter products by active month
  * @param {string} month Active month
  */
  function filterActive(month) {
    month = month || $(".month.active").text();
    d3.csv("/data/seasons/calendario.csv", function(calendar) {
      for (var i = 0,id=1; i < calendar.length; i++,id++) {
        var product = $(".product-" + id);
        var season = $(".product-" + id + " .season");
        var icon = $(".product-"+id+" .icon-season");

        product.removeClass(
          "season start-of-season end-of-season out-of-season fa-hourglass-half"
        );
        icon.removeClass("fa-hourglass-half");
        switch (calendar[i][month.toUpperCase()]) {
          case "X":
            product.addClass("in-season");
            season.text(1);
            break;
          //TODO remove
          case "Y":
          case "I":
            product.addClass("start-of-season");
            season.text(2);
            icon.addClass("fa-hourglass-half");
            break;
          case "F":
            product.addClass("end-of-season");
            season.text(3);
            icon.addClass("fa-hourglass-half");
            break;
          default:
            product.addClass("out-of-season");
            season.text(4);
        }
      }
      organizeProducts();
    });
  }
});
