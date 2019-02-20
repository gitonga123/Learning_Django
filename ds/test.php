<?php

function sum_small(array $arr)
{
    arsort($arr);
    $min_value = array_shift($arr);
    $sum_min = array_sum($arr);
    array_unshift($arr, $min_value);
    array_pop($arr);
    $sum_max = array_sum($arr);
    echo $sum_max . "\n";
    echo $sum_min . "\n";
    return $sum_max + $sum_min;
}

echo "Sum -->" . sum_small([1, 2, 3, 4, 5, 6, 7]);
