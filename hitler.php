<?php

$argv[1] ?? exit();
if(substr($argv[1],0,4) != 'http') {
exit();
}
$handle = fopen( $argv[1] , 'rb');

$image = new Imagick(__DIR__ . '/hitler-getty.jpg');
$background = new ImagickPixel('none');
$image2 = new Imagick();

$image2->readImageFile($handle);
$image2->setImageFormat('png');
$image2->scaleImage(128, 128);
$image->compositeImage($image2, Imagick::COMPOSITE_ATOP, 622, 97);

$image->setImageFormat('png');

// Save image?
file_put_contents(__DIR__ . '/hitler-py.png', $image);

$image->clear();
$image->destroy();