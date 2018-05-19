<?php

require_once __DIR__."/../vendor/autoload.php";

use Box\Spout\Reader\ReaderFactory;
use Box\Spout\Common\Type;

function clean_title($item){
  $item = str_replace(" ","_",$item);
  $item = str_replace("á","a",$item);
  $item = str_replace("é","e",$item);
  $item = str_replace("í","i",$item);
  $item = str_replace("ó","o",$item);
  $item = str_replace("ú","u",$item);
  $item = str_replace("ñ","n",$item);
  $item = str_replace(",","",$item);
  $item = strtolower($item);
  return $item;
}

function generate_recipe($fileName,$data){
  $recipe = "---\n";
  $recipe.="layout: recipe\n";
  $recipe.="css-id: recipes\n";
  $recipe.="title: {$data['title']}\n";
  $recipe.="---\n";
  return $recipe;
}
$source = __DIR__.'/../data/recipes.xlsx';
$target = __DIR__."/../_recipes/";
$target_data = __DIR__."/../_data/recipes/";

$reader = ReaderFactory::create(Type::XLSX); // for XLSX files

$reader->open($source);

$keys = ['id','category','title','ingredient_1','ingredient_2','ingredient_3','steps','source','url'];
foreach ($reader->getSheetIterator() as $sheet) {
    $rows = $sheet->getRowIterator();
    for ($rows->rewind(),$i=0; $rows->valid(); $rows->next(),$i++) {
        if($i==0) continue;
        try {
            $row = $rows->current();
            $row = array_combine($keys,$row);
            echo "Procesing {$row['title']}...\n";
            $title = clean_title($row['title']);
            // Generate recipe file
            $file_name = "{$target}/{$title}.markdown";
            $mr = fopen($file_name,'w');
            $recipe = generate_recipe($file_name,$row);
            fputs($mr,$recipe);
            fclose($mr);
            // Generate recipe data
            $file_name = "{$target_data}/{$title}.json";
            $mr = fopen($file_name,'w');
            $row['name']=ucfirst($row['title']);
            unset($row['title']);
            print_r($row);
            $recipe = json_encode($row,JSON_PRETTY_PRINT);
            $recipe = str_replace("\/","/",$recipe);
            fputs($mr,$recipe);
            fclose($mr);
            echo "DONE\n\n";
        } catch (Exception $exception) {
            continue;
        }

        # ...
    }
}

$reader->close();
