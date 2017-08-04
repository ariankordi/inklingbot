<?php

/* image URL */
mb_internal_encoding('UTF-8');
$argv[1] ?? exit();
if(substr($argv[1],0,4) != 'http') {
exit();
}
$handle = fopen( $argv[1] , 'rb');

$image = new Imagick();
$background = new ImagickPixel('none');
$php = new Imagick(__DIR__ . '/php.png');

$image->readImageFile($handle);
$image->setImageFormat('png');

$res = [$image->getImageWidth(), $image->getImageHeight()];
if($res[0] < 320 || $res[1] < 173) {
exit();
} else {
$d = $res[0] - 225;
$ds = $res[1] - 135;
}

$image->compositeImage($php, Imagick::COMPOSITE_ATOP, $d, $ds);

// Save image?
file_put_contents(__DIR__ . '/php-sp-py.png', $image);
echo 1;

$image->clear();
$image->destroy();