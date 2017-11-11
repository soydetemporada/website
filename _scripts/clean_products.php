<?php

$source = __DIR__."/../_products.old/";
$target = __DIR__."/../_products/";

function parse_line($line){
  return array_map('trim',explode(":",$line));
}
$files = scandir($source);

$ignore = [".",".."];
$properties = ["title","layout"];
foreach ($files as $file) {
  if(in_array($file,$ignore)) continue;
  $product=["---"];
  $product_name = $file;
  $file = array_map('parse_line', file($source.$file));
  foreach($file as $props){
    list($name,$value) = $props;
    if(in_array($name,$properties)){
      $product[]="$name: $value";
    }
  }
  $product[]="---";
  echo "Processing $product_name\n";
  $mr = fopen($target.$product_name,"w");
  fputs($mr,implode("\n",$product));

}
