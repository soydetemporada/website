<?php

$source = __DIR__."/../_products/";
$target = __DIR__."/../_data/products/";

function parse_line($line){
  return array_map('trim',explode(":",$line));
}
$files = scandir($source);

$ignore = [".",".."];
$properties = ["name","img","category","description"];
foreach ($files as $file) {
  if(in_array($file,$ignore)) continue;
  $product = array_fill_keys($properties,'');
  $product_name = str_replace(".markdown","",$file);
  $file = array_map('parse_line', file($source.$file));
  foreach($file as $props){
    list($name,$value) = $props;
    $name = ($name=='descripcion') ? 'description' : $name;
    $name = ($name=='title')? 'name':$name;
    if(in_array($name,$properties)){
      $product[$name]=str_replace('"','',$value);
    }
  }
  if(empty($product['name'])){
    $product['name']=ucwords($product_name);
  }
  echo "Processing $product_name\n";
  $mr = fopen($target.$product_name.".json","w");
  fputs($mr,json_encode($product,JSON_PRETTY_PRINT));
}
