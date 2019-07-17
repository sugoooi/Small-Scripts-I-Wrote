<?php
header('Content-type: image/png');
$INFO = "----------------------------\n";
$info .= "INFO ABOUT VISITOR:";
$info .= "HTTP_USER_AGENT: " . $_SERVER['HTTP_USER_AGENT'] . "\n";
$info .= "REMOTE_ADDR: " . $_SERVER['REMOTE_ADDR'] . "\n";
$info .= "HTTP_X_FORWARDED_FOR: " . ((isset($_SERVER['HTTP_X_FORWARDED_FOR']) || !empty($_SERVER['HTTP_X_FORWARDED_FOR'])) ? $_SERVER['HTTP_X_FORWARDED_FOR'] : "not set") . "\n";
$info .= "HTTP_CLIENT_IP: " . ((isset($_SERVER['HTTP_CLIENT_IP']) || !empty($_SERVER['HTTP_CLIENT_IP']))  ? $_SERVER['HTTP_CLIENT_IP'] : "not set") . "\n";
$info .= "\n";
$file = fopen('details.txt', 'a');
fwrite($file, $info);
fclose($file);
imagepng(imagecreatefrompng('coolcat.png'));
?>