function graficaImportExport(container, path) {
  var svg = d3.select(container),
    margin = { top: 20, right: 20, bottom: 30, left: 50 },
    width = +svg.attr("width") - margin.left - margin.right,
    height = +svg.attr("height") - margin.top - margin.bottom,
    g = svg
      .append("g")
      .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

  var parseTime = d3.timeParse("%d-%b-%Y");

  var x = d3.scaleTime().rangeRound([0, width]);
  var xaxis = d3.axisBottom(x);
  xaxis.tickFormat(d3.timeFormat("%b"));

  var y = d3.scaleLinear().rangeRound([height, 0]);
  var y2 = d3.scaleLinear().rangeRound([height, 0]);

  var line = d3
    .line()
    .x(function(d) {
      return x(d.Mes);
    })
    .y(function(d) {
      return y(d.Importado);
    });
    var line2 = d3
      .line()
      .x(function(d) {
        return x(d.Mes);
      })
      .y(function(d) {
        return y2(d.Exportado);
      });

  d3.csv(
    path,
    function(d) {
      d.Mes = parseTime(d.Mes);
      d.Importado = +d.Importado;
      d.Exportado = +d.Exportado;
      return d;
    },
    function(error, data) {
      if (error) throw error;
      console.log(data);
      x.domain(
        d3.extent(data, function(d) {
          return d.Mes;
        })
      );
      y.domain(
        d3.extent(data, function(d) {
          return d.Importado;
        })
      );
      y2.domain(d3.extent(data,function(d){return d.Exportado;}));

      g
        .append("g")
        .attr("transform", "translate(0," + height + ")")
        .call(xaxis)
        .select(".domain")
        .remove();

      g
        .append("g")
        .call(d3.axisLeft(y))
        .append("text")
        .attr("fill", "#000")
        .attr("transform", "rotate(-90)")
        .attr("y", 6)
        .attr("dy", "0.71em")
        .attr("text-anchor", "end")
        .text("Ton");

      g
        .append("path")
        .datum(data)
        .attr("fill", "none")
        .attr("stroke", "steelblue")
        .attr("stroke-linejoin", "round")
        .attr("stroke-linecap", "round")
        .attr("stroke-width", 1.5)
        .attr("d", line);

        g
          .append("g")
          .attr("transform", "translate("+(width)+",0)")
          .call(d3.axisLeft(y2))
          .append("text")
          .attr("fill", "#000")
          .attr("transform", "rotate(-90)")
          .attr("y", 6)
          .attr("dy", "0.71em")
          .attr("text-anchor", "end")
          .text("Ton");

        g
          .append("path")
          .datum(data)
          .attr('class','export')
          .attr("fill", "none")
          .attr("stroke", "red")
          .attr("stroke-linejoin", "round")
          .attr("stroke-linecap", "round")
          .attr("stroke-width", 1.5)
          .attr("d", line2);
    }
  );
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

    data = data.slice(0, 3);

    var x = d3
      .scaleLinear()
      .domain([0, d3.max(numbers)])
      .range([0, largoGrafico]);

    var enterSel = d3
      .select(container)
      .selectAll("div")
      .data(data)
      .enter()
      .append("div")
      .style("width", "0px");

    enterSel.text(function(d) {
      return d.Provincia + " " + d.Percent + "%";
    });
    enterSel
      .transition()
      .delay(0)
      .duration(1300)
      .style("width", function(d) {
        return x(d.Percent) + "px";
      })
      .delay(200)
      .style("color", colorTexto);
    //TODO poner el último a mano
  });
}

function cleanLatin(src){
  src = src.replace('á','a');
  src = src.replace('é','e');
  src = src.replace('í','i');
  src = src.replace('ó','o');
  src = src.replace('ú','u');
  src = src.replace('ñ','n');
  return src;
}
function updateCalendario(product,source){
  d3.csv(source+"/data/temporadas/calendario.csv", function(calendario) {
    product = cleanLatin(product);
    console.log(product);
    for (var i = 0,id=1; i < calendario.length; i++,id++) {
      if(calendario[i].PRODUCTO.toLowerCase() == product){
        console.log(calendario[i]);
        break;
      }
    }

  });
}
