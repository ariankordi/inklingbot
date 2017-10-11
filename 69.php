<?php

$argv[1] ?? exit();
if(substr($argv[1],0,4) != 'http') {
exit();
}
$handle = fopen( $argv[1] , 'rb');

$image = new Imagick(__DIR__ . '/69f.png');
$background = new ImagickPixel('none');
$image2 = new Imagick();

$image2->readImageFile($handle);
$image2->setImageFormat('png');
$image2->scaleImage(282, 412);
$image->compositeImage($image2, Imagick::COMPOSITE_ATOP, 29, 16);

$image->setImageFormat('png');

// Save image?
file_put_contents(__DIR__ . '/69-py.png', $image);

$image->clear();
$image->destroy();