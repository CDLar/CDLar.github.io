<?php
$myFile = fopen("tradeBlock.txt", "w");
$text = $_POST[newText];

fwrite($myFile, $text);

fclose($myFile);


?>
