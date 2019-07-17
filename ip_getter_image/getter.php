 <?php
$fp = fopen('details.txt', 'w');
$info = "----------------------------\n";
$info .= "INFO ABOUT VISITOR:";
$info .= "HTTP_USER_AGENT: " . $_SERVER['HTTP_USER_AGENT'] . "\n";
$info .= "REMOTE_ADDR: " . $_SERVER['REMOTE_ADDR'] . "\n";
$info .= "HTTP_X_FORWARDED_FOR: " . ((isset($_SERVER['HTTP_X_FORWARDED_FOR']) || !empty($_SERVER['HTTP_X_FORWARDED_FOR'])) ? $_SERVER['HTTP_X_FORWARDED_FOR'] : "not set") . "\n";
$info .= "HTTP_CLIENT_IP: " . ((isset($_SERVER['HTTP_CLIENT_IP']) || !empty($_SERVER['HTTP_CLIENT_IP']))  ? $_SERVER['HTTP_CLIENT_IP'] : "not set") . "\n";
$info .= "\n";

fwrite($fp, $info);
fclose($fp);
?>


<?php
function load_png($imgname)
{
    $im = @imagecreatefrompng($imgname);

    
    if(!$im) // Is the image valid?
    {
        $im  = imagecreatetruecolor(150, 30); // If it's invalid, create a new image from scratch with the 
        $background_color = imagecolorallocate($im, 255, 255, 255);
        $text_color  = imagecolorallocate($im, 0, 0, 0);

        imagefilledrectangle($im, 0, 0, 150, 30, $background_color);

        // Error message
        imagestring($im, 1, 5, 5, 'Error loading ' . $imgname, $text_color);
    }

    return $im; // In any case return relevant image data
}

header('Content-Type: image/png');

$img = load_png('coolcat.png');

imagepng($img);
imagedestroy($img);
?>
