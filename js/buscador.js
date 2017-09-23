$(document).ready(function() {
  var comunidades = {};
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
    var activeMonth = $(".month.active").text();
    var activeProvince = $(".comunidad")
      .val()
      .toLowerCase();

    if (comunidades[activeProvince]) {
      filterActive(activeMonth, comunidades[activeProvince]);
    } else {
      loadData(activeProvince, filterActive);
    }
  }
  function filterActive(month, data) {
    month = month || $(".month.active").text();
    data =
      data ||
      comunidades[
        $(".comunidad")
          .val()
          .toLowerCase()
      ];
    month = month.toUpperCase();
    console.log("Filtrando por " + month);

    for (var i = 0; i < data.length; i++) {
      var product = $("#product-" + data[i].ID + " .fa-clock-o");
      var time = $("#product-" + data[i].ID + " .temporada");

      product.removeClass(
        "temporada inicio-temporada fin-temporada fuera-temporada"
      );
      switch (data[i][month.toUpperCase()]) {
        case "X":
          product.addClass("en-temporada");
          time.text(1);
          break;
        //TODO remove
        case "Y":
        case "I":
          product.addClass("inicio-temporada");
          time.text(2);
          break;
        case "F":
          product.addClass("fin-temporada");
          time.text(3);
          break;
        default:
          product.addClass("fuera-temporada");
          time.text(4);
      }
    }

    var $grid = $(".grid").isotope({
      itemSelector: ".portfolio-item",
      layoutMode: "fitRows",
      getSortData: {
        id: ".id parseInt",
        temporada: ".temporada parseInt"
      },
      sortBy: "temporada"
    });
    $grid.isotope("updateSortData").isotope();
  }
  function loadData(province, callback) {
    console.log("Cargando datos de " + province);
    d3.csv("data/temporadas/" + province + ".csv", function(data) {
      comunidades[province] = data;
      callback();
    });
  }
});
