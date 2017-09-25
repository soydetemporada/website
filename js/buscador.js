$(document).ready(function() {
  var calendario = null;
  moment().locale("es");

  $(".month").on("click", filterByMonth);
  $(".comunidad").on("change", filterProducts);

  filterProducts();

  function filterByMonth(e) {
    e.preventDefault();
    $(".month").removeClass("active");
    $(e.target).addClass("active");
    filterProducts();
  }
  function filterProducts() {
    var activeMonth = $(".month.active")
      .data('month')
      .trim();
    filterActive(activeMonth);
  }
  function filterActive(month) {
    month = month || $(".month.active").text();
    d3.csv("data/temporadas/calendario.csv", function(calendario) {
      for (var i = 0; i < calendario.length; i++) {
        var product = $("#product-" + calendario[i].ID + " .icon-temporada");
        var time = $("#product-" + calendario[i].ID + " .temporada");

        product.removeClass(
          "temporada inicio-temporada fin-temporada fuera-temporada fa-clock-o"
        );
        switch (calendario[i][month.toUpperCase()]) {
          case "X":
            product.addClass("en-temporada fa-clock-o");
            time.text(1);
            break;
          //TODO remove
          case "Y":
          case "I":
            product.addClass("inicio-temporada fa-clock-o");
            time.text(2);
            break;
          case "F":
            product.addClass("fin-temporada fa-clock-o");
            time.text(3);
            break;
          default:
            product.addClass("fuera-temporada fa-clock-o");
            time.text(4);
        }
      }
      var $grid = $(".grid").isotope({
        itemSelector: ".portfolio-item",
        getSortData: {
          id: ".id parseInt",
          temporada: ".temporada parseInt"
        },
        percentPosition: true,
        masonry: {
          // use element for option
          columnWidth: ".col-sm-2"
        },
        sortBy: ["temporada", "id"]
      });
      $grid.isotope("updateSortData").isotope();
    });
  }
  function loadData() {}
});
