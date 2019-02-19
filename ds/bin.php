<?php

// binary search no look version :simley:
// Assumption list on n integers no strings

function binary_search(array $list, $left, $right, $item)
{
    sort($list);

    if ($right >= $left) {
        $mid = floor($left + (($right - $left)/2));

        if ($list[$mid] == $item) {
            return $mid;
        }

        if ($list[$mid] > $item) {
            return binary_search($list, $left, $mid-1, $item);
        }

        return binary_search($list, $mid+1, $right, $item);
    }

    return false;
}

$list = [67, 567, 736, 838, 1900, 1910, 5748];
$left = 0;
$right = count($list)-1;
$item = 67;
$result = binary_search($list, $left, $right, $item);
echo $result;
if ($result or $result == 0) {
    echo "{$item} found at index {$result}";
} else {
    echo "{$item} not found";
}
