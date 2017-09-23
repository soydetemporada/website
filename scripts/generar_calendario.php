<?php

$source = __DIR__ ."/../data/temporadas/";

$files = scandir($source);

$ignore = [".","..",".DS-Store","calendario.csv"];
$target = [];
foreach($files as $file){
  if(in_array($file,$ignore)) continue;
  $csv = array_map('str_getcsv', file($source.$file));
  foreach($csv as $line){
    if($line[0]=='ID') continue;
    if(!array_key_exists($line[0],$target)){
      $target[$line[0]]=$line;
    }
    else{
      $current = $target[$line[0]];
      foreach($line as $index=>$col){
        if(!empty($col)){
          $current[$index]=$col;
        }
      }
      $target[$line[0]]=$current;
    }
  }
}
$mr = fopen($source."calendario.csv", "w");
fputs($mr,"ID,PRODUCTO,ENE,FEB,MAR,ABR,MAY,JUN,JUL,AGO,SEP,OCT,NOV,DIC\n");
foreach($target as $row){
  fputs($mr,implode(",",$row)."\n");
}
