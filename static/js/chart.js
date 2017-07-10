
//Below Code is for the GettysBurg address chart
data_piechart=[{"key": "Serie 1", "values": [{"value": 3, "label": "us"}, {"value": 3, "label": "great"}, {"value": 3, "label": "people"}, {"value": 3, "label": "dead"}, {"value": 8, "label": "we"}, {"value": 3, "label": "shall"}, {"value": 4, "label": "dedicated"}, {"value": 3, "label": "they"}, {"value": 5, "label": "nation"}]}];

nv.addGraph(function() {
    var chart = nv.models.pieChart();
    chart.margin({top: 30, right: 60, bottom: 20, left: 60});
    var datum = data_piechart[0].values;

    chart.color(d3.scale.category20c().range());

    chart.tooltipContent(function(key, y, e, graph) {
        var x = String(key);
        var y =  String(y)  + ' count';

        tooltip_str = '<center><b>'+x+'</b></center>' + y;
        return tooltip_str;
    });

    chart.showLabels(true);
    chart.donut(false);
    chart.showLegend(true);

    chart
        .x(function(d) { return d.label })
        .y(function(d) { return d.value });

    chart.width(450);
    chart.height(450);

    d3.select('#piechart svg')
            .datum(datum)
            .transition().duration(500)
            .attr('width', 450)
            .attr('height', 450)
            .call(chart);
});

//Code for I have a dream chart
dream_piechart = [{"key": "Serie 1", "values": [{"value": 11, "label": "day"}, {"value": 32, "label": "be"}, {"value": 13, "label": "with"}, {"value": 20, "label": "freedom"}, {"value": 21, "label": "we"}, {"value": 17, "label": "our"}, {"value": 11, "label": "dream"}, {"value": 12, "label": "ring"}]}];

nv.addGraph(function() {
  var chart = nv.models.pieChart();
  chart.margin({top: 30, right: 60, bottom: 20, left: 60});
  var datum = dream_piechart[0].values;

  chart.color(d3.scale.category20c().range());

  chart.tooltipContent(function(key, y, e, graph) {
      var x = String(key);
      var y =  String(y)  + ' count';

      tooltip_str = '<center><b>'+x+'</b></center>' + y;
        return tooltip_str;
      });
      
      chart.showLabels(true);
      chart.donut(false);
      chart.showLegend(true);

      chart
        .x(function(d) { return d.label })
        .y(function(d) { return d.value });

      chart.width(450);

      chart.height(450);


      d3.select('#dream_piechart svg')
            .datum(datum)
            .transition().duration(500)
            .attr('width', 450)
            .attr('height', 450)
            .call(chart);
});

//Code For Military-Industry Speech
military_piechart = [{"values": [{"value": 10, "label": "my"}, {"value": 9, "label": "military"}, {"value": 16, "label": "we"}, {"value": 18, "label": "be"}, {"value": 27, "label": "our"}, {"value": 9, "label": "peace"}, {"value": 16, "label": "with"}, {"value": 10, "label": "you"}, {"value": 9, "label": "balance"}], "key": "Serie 1"}];

nv.addGraph(function() {
    var chart = nv.models.pieChart();
    chart.margin({top: 30, right: 60, bottom: 20, left: 60});
    var datum = military_piechart[0].values;
    
    chart.color(d3.scale.category20c().range());

    chart.tooltipContent(function(key, y, e, graph) {
      var x = String(key);
          var y =  String(y)  + ' count';

          tooltip_str = '<center><b>'+x+'</b></center>' + y;
          return tooltip_str;
          });
    
    chart.showLabels(true);
    chart.donut(false);
    chart.showLegend(true);

    chart
      .x(function(d) { return d.label })
      .y(function(d) { return d.value });

    chart.width(450);

    chart.height(450);

    d3.select('#military_piechart svg')
          .datum(datum)
          .transition().duration(500)
          .attr('width', 450)
          .attr('height', 450)
          .call(chart);
});