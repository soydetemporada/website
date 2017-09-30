var meses = {
  Ene: 0,
  Feb: 1,
  Mar: 2,
  Abr: 3,
  May: 4,
  Jun: 5,
  Jul: 6,
  Ago: 7,
  Sep: 8,
  Oct: 9,
  Nov: 10,
  Dic: 11
};
var mesesNuevos = {
  "01-Ene-2015": 0,
  "01-Feb-2015": 1,
  "01-Mar-2015": 2,
  "01-Abr-2015": 3,
  "01-May-2015": 4,
  "01-Jun-2015": 5,
  "01-Jul-2015": 6,
  "01-Ago-2015": 7,
  "01-Sep-2015": 8,
  "01-Oct-2015": 9,
  "01-Nov-2015": 10,
  "01-Dic-2015": 11
};

function graficaImportExport(container, path) {
  var width = $(container).width();
  var svg = d3.select(container).append('svg')
    .attr("width",width)
    .attr("height",350);

  var margin = {
      top: 20,
      right: 20,
      bottom: 30,
      left: 50
    },
    width = +svg.attr("width") - margin.left - margin.right,
    height = +svg.attr("height") - margin.top - margin.bottom,
    g = svg
      .append("g")
      .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

  var parseRow = function(d) {
    d.Mes = mesesNuevos[d.Mes];
    d.Importado = d.Importado;
    d.Exportado = d.Exportado;
    return d;
  };

  var xx = d3.scaleLinear().range([10, width]);
  var yy = d3.scaleLinear().range([height, 0]);

  var xaxis = d3
    .axisBottom(xx)
    .ticks(12)
    .tickFormat(function(d) {
      return Object.keys(meses)[d];
    });

  var lineImport = d3
    .line()
    .x(function(d) {
      return xx(d.Mes);
    })
    .y(function(d) {
      return yy(d.Importado);
    });

  var lineExport = d3
    .line()
    .x(function(d) {
      return xx(d.Mes);
    })
    .y(function(d) {
      return yy(d.Exportado);
    });

  d3.csv(path, parseRow, function(error, data) {
    mdata = data;
    if (error) throw error;
    maxImport = d3.max(data, function(d) {
      return parseInt(d.Importado);
    });
    maxExport = d3.max(data, function(d) {
      return parseInt(d.Exportado);
    });
    xx.domain([0, 11]);
    yy.domain([0, 1.1 * d3.max([maxImport, maxExport])]);

    // .tickFormat(d3.time.format("%B"))
    g
      .append("g")
      .attr("transform", "translate(0," + height + ")")
      .call(xaxis)
      .select(".domain")
      .remove();

    g
      .append("g")
      .call(d3.axisLeft(yy))
      .append("text") //texto
      .attr("fill", "#000")
      .attr("transform", "rotate(-90)")
      .attr("y", 6)
      .attr("dy", "0.71em")
      .attr("text-anchor", "end")
      .text("Toneladas");

    g
      .append("path")
      .data([data])
      .classed("line import", true)
      .transition()
      .attr("d", lineImport);

    g
      .append("path")
      .data([data])
      .classed("line export", true)
      .transition()
      .attr("d", lineExport);

    d3
      .selectAll("body")
      .append("div")
      .classed("d3-tooltip", true);
    /*** import label **/
    g
      .append("text")
      .text("Importación")
      .attr("transform", function() {
        return "translate(" + (xx(data[11].Mes)) + "," + 18 + ")";
      })
      .classed("textImport", true)
      .style("text-anchor", "end" );

    var element = g
      .selectAll("circle.dotImport") //g1 is the update section
      .data(data)
      .enter()
      .append("circle")
      .classed("dotImport ", true)
      .attr("cx", function(d) {
        return xx(d.Mes);
      })
      .attr("cy", function(d) {
        return yy(d.Importado);
      })
      .attr("r", 0)
      .on("mouseover", function(d) {
        var mouse = d3.mouse(this);
        var absPositionSvg = $("svg.import-export").position();
        $(".d3-tooltip").css("top", mouse[1] + absPositionSvg.top - 20 + "px");
        $(".d3-tooltip").css(
          "left",
          mouse[0] + absPositionSvg.left + 40 + "px"
        );
        $(".d3-tooltip").show();
        $(".d3-tooltip").html(d.Importado + " ton.");
      })
      .on("mouseout", function(d, i) {
        $(".d3-tooltip").hide();
        //    d3.select(this).select("circle")
      })
      .transition(300)
      .delay(500)
      .attr("r", 5);

    /*** export label **/
    g
      .append("text")
      .text("Exportación")
      .attr("transform", function() {
        return "translate(" + (xx(data[11].Mes)) + "," + 0 + ")";
      })
      .classed("textExport", true)
      .style("text-anchor", "end" );



    var element = g
      .selectAll("circle.dotExport") //g1 is the update section
      .data(data)
      .enter()
      .append("circle")
      .classed("dotExport ", true)
      .attr("cx", function(d) {
        return xx(d.Mes);
      })
      .attr("cy", function(d) {
        return yy(d.Exportado);
      })
      .attr("r", 0)
      .on("mouseover", function(d) {
        var mouse = d3.mouse(this);
        var absPositionSvg = $("svg.import-export").position();
        $(".d3-tooltip").css("top", mouse[1] + absPositionSvg.top - 20 + "px");
        $(".d3-tooltip").css(
          "left",
          mouse[0] + absPositionSvg.left + 40 + "px"
        );
        $(".d3-tooltip").show();
        $(".d3-tooltip").html(d.Exportado + " ton.");
      })
      .on("mouseout", function(d, i) {
        $(".d3-tooltip").hide();
        //    d3.select(this).select("circle")
      })
      .transition(300)
      .delay(500)
      .attr("r", 5);
  });


}

function dibujaGrafico(container, ficheroDeDatos) {
  var colorTexto = "#333";
  var largoGrafico = $(container).width();
  if (ficheroDeDatos === undefined) ficheroDeDatos = "data/grafico.csv";

  d3.csv(ficheroDeDatos, function(error, data) {
    var mdata = data;
    var numbers = [];
    mdata.forEach(function(el) {
      numbers.push(+el.Percent);
    });

    //data = data.slice(0, 3);

    var x = d3
      .scaleLinear()
      .domain([0, 100])
      .range([0, largoGrafico - 10]);
    var arrayColores = ["#A83232", "#C25C30", "#D98236", "#D9A036"];
    var enterSel = d3
      .select(container)
      .selectAll("div.grafica-barras")
      .data(data)
      .enter()
      .append("div")
      .style("width", function(d) {
        return x(d.Percent) + "px";
      })
      .style("opacity", 0)
      .style("background-color", function(d, i) {
        return arrayColores[i];
      })
      .classed("grafica-barras", true);

    var enterSelText = d3
      .select(container)
      .selectAll("div.grafica-texto")
      .data(data)
      .enter()
      .append("div")
      .classed("grafica-texto", true)
      .style("width", function(d) {
        return x(d.Percent) + "px";
      })
      .style("opacity", 0);
    enterSelText
      .transition()
      .delay(1000)
      .style("opacity", 1);

    enterSelText.text(function(d) {
      return d.Provincia + " " + d.Percent + "%";
    });
    enterSelText.style("writing-mode", function(d) {
      if (x(d.Percent < 20)) return "vertical-rl";
      else "horizontal-tb";
    });
    enterSel
      .transition()
      .delay(0)
      .duration(1000)
      .delay(100)
      .style("opacity", 1);

  });
}

function isOverflown(element) {
  return (
    element.scrollHeight > element.clientHeight ||
    element.scrollWidth > element.clientWidth
  );
}

function cleanLatin(src) {
  src = src.replace("á", "a");
  src = src.replace("é", "e");
  src = src.replace("í", "i");
  src = src.replace("ó", "o");
  src = src.replace("ú", "u");
  src = src.replace("ñ", "n");
  return src;
}

function updateCalendario(product, source) {
  $("#product-page li").removeClass(
    "en-temporada inicio-temporada fin-temporada"
  );
  d3.csv(source + "/data/temporadas/calendario.csv", function(calendario) {
    product = cleanLatin(product);
    for (var i = 0, id = 1; i < calendario.length; i++, id++) {
      if (calendario[i].PRODUCTO.toLowerCase() == product) {
        $("#product-page .month").each(function(index, item) {
          $item = $(item);
          switch (calendario[i][$item.data("month").toUpperCase()]) {
            case "Y":
              $item.closest("li").addClass("inicio-temporada");
              break;
            case "X":
              $item.closest("li").addClass("en-temporada");
              break;
          }
        });
        break;
      }
    }
  });
}

function tiempoCultivo(producto,container,path){
  // Dimensions
  var contWidth = $(container).width(),
      margin = { top: 10, right: 10, bottom: 10, left: 5 },
      width = contWidth - margin.left - margin.right,
      height = 70 - margin.top - margin.bottom;


  // Initialize svg
  var svg = d3.select(container).selectAll('svg')
      .data([{}]).enter()
      .append('svg')
      .attr('width', width + margin.right + margin.left)
      .attr('height', height + margin.top + margin.bottom);

  // External group
  var chartWrapper = svg.selectAll('g.chartWrapper')
      .data([{}]).enter()
      .append('g')
      .attr('class', 'chartWrapper')
      .attr('transform', 'translate(' + margin.left + ',' + margin.top + ')');

  var xScale = d3.scaleBand()
    .domain(d3.range(12))
    .range([margin.left, width - margin.right])
    .padding(.3);


  d3.csv(path, function(datos) {
    var meses = datos
      .filter(function(d) { return d.PRODUCTO.toLowerCase() == producto; })[0].MESES;
    meses = meses != 'NA' ? +meses : 0;
    console.log(meses);

    chartWrapper.selectAll('.time-line')
      .data(d3.range(12))
      .enter()
      .append('line')
      .attr('class', 'time-line')
      .classed('high', function(d, i) {
        return i < meses ? true : false; })
      .attr('x1', function(d, i) { return xScale(i); })
      .attr('y1', height/2)
      .attr('x2', function(d, i) { return xScale(i) + xScale.bandwidth(); })
      .attr('y2', height/2)
      .style('stroke', function(d, i) { return i < meses ? '#89BC10' : '#D8D8D8'; })
      .style('stroke-linecap', 'round')
      .style('stroke-width', 6);

    chartWrapper.selectAll('.time-line-label')
      .data([meses])
      .enter()
      .append('text')
      .attr('x', xScale(0))
      .attr('y', height/2 + 30)
      .text(function(d) { if(d==0){ return "Sin información";}else{return d + ' meses';} })

  });
}
