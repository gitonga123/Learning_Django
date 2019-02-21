<?php

function birthday_cake(array $arr)
{
    $new_array = array_count_values($arr);

    return max($new_array);
}

echo birthday_cake([18, 90, 90, 13, 90, 75, 90, 8, 90, 43]);
