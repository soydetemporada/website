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
  /*
  $(".product-filter select").on('select2:select', function (e) {
      console.log(e.params.data);
      var $grid = $(".grid").isotope({
        filter: function(){
          var id = parseInt($(this).find('.id').text());
          return id == e.params.data.id;
        }
      });
    });
    */

    $(".product-filter select").on('change.select2', function (e) {
      console.log("Unselecting");
      console.log($(e.target).val());
      var selected = parseInt($(e.target).val());
      if(selected){
        var $grid = $(".grid").isotope({
          filter: function(){
            var id = parseInt($(this).find('.id').text());
            return id == selected;
          }
        });
      }
      else{
        console.log("organizeProducts");
        var $grid = $(".grid").isotope({
          filter: "*"
        });
        organizeProducts();
      }
    });
  filterProducts();

  function organizeProducts(){
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
  }
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
        //var product = $("#product-" + calendario[i].ID + " .icon-temporada");
        var product = $("#product-" + calendario[i].ID);
        var time = $("#product-" + calendario[i].ID + " .temporada");

        product.removeClass(
          "temporada inicio-temporada fin-temporada fuera-temporada fa-clock-o"
        );
        switch (calendario[i][month.toUpperCase()]) {
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
      organizeProducts();
    });
  }
  function loadData() {}
});
