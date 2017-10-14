$(document).ready(function() {
  var calendario = null;
  moment().locale("es");

  $(".month").on("click", filterByMonth);
  $(".comunidad").on("change", filterProducts);
  $(".product-filter select").select2({
    placeholder: "Filtrar por producto",
    allowClear: true,
    minimumInputLength: 2
  });

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
    filterProducts();
    $items.show();
    $loader.hide();

  });

  function organizeProducts() {
    var $grid = $(".grid").isotope({
      itemSelector: ".portfolio-item",
      getSortData: {
        id: ".id parseInt",
        temporada: ".temporada parseInt",
        category: ".category",
      },
      percentPosition: true,
      masonry: {
        columnWidth: ".col-sm-2"
      },
      sortBy: ["temporada","category" ,"id"]
    });
    $grid.isotope("updateSortData").isotope();
  }
  function filterByMonth(e) {
    e.preventDefault();
    $(".month").removeClass("active");
    $(e.target).addClass("active");
    filterProducts();
  }

  function filterProducts() {
    var activeMonth = $(".month.active")
      .data("month")
      .trim();
    filterActive(activeMonth);
  }
  function filterActive(month) {
    month = month || $(".month.active").text();
    d3.csv("data/temporadas/calendario.csv", function(calendario) {
      for (var i = 0,id=1; i < calendario.length; i++,id++) {
        var product = $(".product-" + id);
        var season = $(".product-" + id + " .temporada");
        var icon = $(".product-"+id+" .icon-temporada");

        product.removeClass(
          "temporada inicio-temporada fin-temporada fuera-temporada fa-hourglass-half"
        );
        icon.removeClass("fa-hourglass-half");
        switch (calendario[i][month.toUpperCase()]) {
          case "X":
            product.addClass("en-temporada");
            season.text(1);
            break;
          //TODO remove
          case "Y":
          case "I":
            product.addClass("inicio-temporada");
            season.text(2);
            icon.addClass("fa-hourglass-half");
            break;
          case "F":
            product.addClass("fin-temporada");
            season.text(3);
            icon.addClass("fa-hourglass-half");
            break;
          default:
            product.addClass("fuera-temporada");
            season.text(4);
        }
      }
      organizeProducts();
    });
  }
});
