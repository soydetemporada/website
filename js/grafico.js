


function dibujaGrafico(container,ficheroDeDatos) {
    var colorTexto="#333"
    var largoGrafico=400;
    console.log(ficheroDeDatos);
    if(ficheroDeDatos===undefined)
         ficheroDeDatos="data/grafico.csv"

    d3.csv(ficheroDeDatos, function(error, data) {
        var mdata=data;
        var numbers=[]
        mdata.forEach(function(el){
            numbers.push(+el.Percent)
        })

        console.log(numbers);

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
