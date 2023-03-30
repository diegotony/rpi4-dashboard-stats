var grid = {
    view:"dashboard",
    id:"grid",
    gridColumns:4,
    gridRows:3,
    cellHeight:200,
    cellWidth:200,
    cells:[
      { view:"panel", x:0, y:0, dx:1, dy:1, 
       resize:true, css:"panel_drag_view", icon:false, body:{
         view:"chart", type:"pie", value:"#votes#", data:small_film_set
       }},
      { view:"panel", x:1, y:0, dx:2, dy:1,
       resize:true, css:"panel_drag_view", icon:false, body:{
         view:"chart", type:"spline", value:"#votes#", data:small_film_set
       }},
      { view:"panel", x:0, y:1, dx:1, dy:2,
       resize:true, css:"panel_drag_view", icon:false, body:{
         view:"list", template:"#votes#", data:small_film_set, scroll:false
       }},
      { view:"panel", type:"space", header:"Widget with header", 
       x:1, y:1, dx:3, dy:2, resize:true, body:{
         view:"datatable", autoConfig:true, data: small_film_set, scroll:false
       }}
    ]
  };
  
  webix.ui({
    view:"scrollview",
    scroll:"xy",
    body:grid
  });