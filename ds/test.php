<?php

// Complete the miniMaxSum function below.
function miniMaxSum($arr) {
    $sum = array();

    for($i =0; $i < count($arr); $i++) {
       $sum[] = array_sum($arr) - $arr[$i];
    }

     echo min($sum) ." " .max($sum);
}

(miniMaxSum([5, 5, 5, 5, 5]));
