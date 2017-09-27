
function graficaImportExport(container,path){
  var svg = d3.select(container),
    margin = {top: 20, right: 20, bottom: 30, left: 50},
    width = +svg.attr("width") - margin.left - margin.right,
    height = +svg.attr("height") - margin.top - margin.bottom,
    g = svg.append("g").attr("transform", "translate(" + margin.left + "," + margin.top + ")");


    var parseTime = d3.timeParse("%b");

    var x = d3.scaleTime()
        .rangeRound([0, width]);

var y = d3.scaleLinear()
    .rangeRound([height, 0]);

var line = d3.line()
    .x(function(d) { return x(d.Mes); })
    .y(function(d) { return y(d.Importado); });

d3.csv(path, function(d) {
  d.Mes = parseTime(d.Mes);
  d.Importado = +d.Importado
  d.Exportado = +d.Exportado;
  return d;
}, function(error, data) {
  if (error) throw error;
console.log(data)
  x.domain(d3.extent(data, function(d) { return d.Mes; }));
  y.domain(d3.extent(data, function(d) { return d.Importado; }));

  g.append("g")
      .attr("transform", "translate(0," + height + ")")
      .call(d3.axisBottom(x))
    .select(".domain")
      .remove();

  g.append("g")
      .call(d3.axisLeft(y))
    .append("text")
      .attr("fill", "#000")
      .attr("transform", "rotate(-90)")
      .attr("y", 6)
      .attr("dy", "0.71em")
      .attr("text-anchor", "end")
      .text("Price ($)");

  g.append("path")
      .datum(data)
      .attr("fill", "none")
      .attr("stroke", "steelblue")
      .attr("stroke-linejoin", "round")
      .attr("stroke-linecap", "round")
      .attr("stroke-width", 1.5)
      .attr("d", line);
});
}


function dibujaGrafico(container,ficheroDeDatos) {
    var colorTexto="#333"
    var largoGrafico=400;
    if(ficheroDeDatos===undefined)
         ficheroDeDatos="data/grafico.csv"

    d3.csv(ficheroDeDatos, function(error, data) {
        var mdata=data;
        var numbers=[]
        mdata.forEach(function(el){
            numbers.push(+el.Percent)
        })


        var x = d3.scaleLinear()
        .domain([0, d3.max(numbers)])
        .range([0, largoGrafico]);

        data = data.slice(0,3);

        var enterSel=d3.select(container)
          .selectAll("div")
            .data(data)
          .enter().append("div").style("width",'0px')

          enterSel.text(function(d) { return d.Provincia + " " + d.Percent + "%"; })
            enterSel.transition().delay(0).duration(1300)
            .style("width", function(d) { return x(d.Percent) + "px"; })
            .delay(200)
            .style('color',colorTexto)
            ;
        //TODO poner el último a mano
    });

}
