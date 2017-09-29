<<<<<<< HEAD

var meses={
    'Enero':0,'Febrero':1,'Marzo':2,'Abril':3,'Mayo':4,'Junio':5,'Julio':6,'Agosto':7,'Septiembre':8,'Octubre':9,'Noviembre':10,'Diciembre':11
}

function graficaImportExport(container,path){
      var svg = d3.select(container),
        margin = {top: 20, right: 20, bottom: 30, left: 50},
        width = +svg.attr("width") - margin.left - margin.right,
        height = +svg.attr("height") - margin.top - margin.bottom,
        g = svg.append("g").attr("transform", "translate(" + margin.left + "," + margin.top + ")");
        //var parseTime = d3.timeParse("%b");

    var parseRow=function(d) {
          d.Mes = meses[d.Mes]
          d.Importado = d.Importado
          d.Exportado = d.Exportado;
          return d;
    }

    var xx = d3.scaleLinear().range([10, width]);
    var yy = d3.scaleLinear().range([ height,0]);

    var xaxis=  d3.axisBottom(xx).ticks(12).tickFormat(function(d){
        return Object.keys(meses)[d]
    })
    //.ticks(d3.timeMonths).tickSize(16, 0)
    //.tickFormat(d3.timeFormat("%B"));
//    xaxis.tickValues(Object.keys(meses));//.tickFormat(d3.timeFormat("%m"));
    var lineImport = d3.line()
      .x(function(d) {  return xx(d.Mes); })
      .y(function(d) { return yy(d.Importado); });

      var lineExport = d3.line()
        .x(function(d) { return xx(d.Mes); })
        .y(function(d) {  return yy(d.Exportado); });

    d3.csv(path, parseRow,function(error, data) {
            mdata=data
          if (error) throw error;
          maxImport=d3.max(data,function(d){return parseInt(d.Importado)})
          maxExport=d3.max(data,function(d){return parseInt(d.Exportado)})
          xx.domain([0,11]);
          yy.domain([0,1.1*d3.max([maxImport, maxExport])]);

          // .tickFormat(d3.time.format("%B"))
          g.append("g")
              .attr("transform", "translate(0," + height + ")")
              .call(xaxis )
            .select(".domain")
              .remove();

          g.append("g")
             .call(d3.axisLeft(yy))
            .append("text") //texto
              .attr("fill", "#000")
              .attr("transform", "rotate(-90)")
              .attr("y", 6)
              .attr("dy", "0.71em")
              .attr("text-anchor", "end")
              .text("Toneladas");


          g.append("path")
              .data([data])
              .classed("line import",true).transition()
              .attr("d", lineImport);

          g.append("path")
              .data([data])
              .classed("line export",true).transition()
              .attr("d", lineExport);

              d3.selectAll("body").append("div")
              .classed('d3-tooltip',true);
/*** import label **/
        g.append("text").text("Importación").attr("transform", function(){
            return "translate(" + xx(data[1].Mes) + "," + (yy(data[11].Importado) -20) + ")";
        })

        var g1 = g.selectAll("g.dotImport") //g1 is the update section
              .data(data)

        var element = g1.enter().append("g").attr("transform", function(d) {
            return "translate(" + xx(d.Mes) + "," + yy(d.Importado) + ")";
        })
        element.classed("dotImport ", true);
        element.append("svg:circle")
        .attr('r',4)


/*** export label **/
        g.append("text").text("Exportación").attr("transform", function(){
            return "translate(" + xx(data[1].Mes) + "," + (yy(data[11].Exportado) -20) + ")";
        })
        var g1 = g.selectAll("g.dotExport") //g1 is the update section
              .data(data)

        var element = g1.enter().append("g").attr("transform", function(d) {
            return "translate(" + xx(d.Mes) + "," + yy(d.Exportado) + ")";
        })
        element.classed("dotExport", true);
        element.append("svg:circle")
        .attr('r',0)
        .transition(300).delay(500)
        .attr('r',5)

        element.on("mouseover", function(d,i) {
/*
            $(".d3-tooltip").css('top',d3.mouse(svg)[1]+"px")
            $(".d3-tooltip").css('left',d3.mouse(svg)[0]+"px")

            $(".d3-tooltip").show();
            $(".d3-tooltip").html(d.Exportado);*/



        })

        element.on("mouseout", function(d,i) {
            $(".d3-tooltip").hide();
        //    d3.select(this).select("circle")
        })



    });
=======
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
>>>>>>> 9b02e0ef1b50e5b72d32187ab5b69104b26da0ce
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
