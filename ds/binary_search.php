<?php

# assumption no empty arrays
# parameters, Array, first side, last side, random pivot
function binarySearch(array $arr, int $l, int $r, int $x)
{
	  sort($arr);
    if ($r >= $l) {
    	  $mid = $l + ($r - $l)/2;

    	  if ($arr[$mid] == $x) {
    	  	  return $mid;
    	  }

    	  if ($arr[$mid] > $x) {
    	  	return binarySearch($arr, $l, $mid-1, $x);
    	  }


    	  // 
    	  return binarySearch($arr, $mid+1, $r, $x);
    }

    return -1;
}


// Driver Code 
$arr = [67, 567, 736, 838, 1900, 1910, 5748];
$n = count($arr); 
$x = 67; 
$result = binarySearch($arr, 0, $n - 1, $x); 
if(($result == -1)) 
echo "Element is not present in array"; 
else
echo "Element is present at index ". $result; 