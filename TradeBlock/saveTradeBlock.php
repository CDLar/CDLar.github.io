<?php
$myFile = fopen("TradeBlock/tradeBlock.txt", "w");
$text = $_POST[newText];

fwrite($myFile, $text);

fclose($myFile);


?>