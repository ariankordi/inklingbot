<?php

/* Text to write */
mb_internal_encoding('UTF-8');
$txt = $argv[1] ?? exit();

$image = new Imagick();
$d = new ImagickDraw();
$color = new ImagickPixel('#0280ff');
$background = new ImagickPixel('none'); // Transparent
$openman = new Imagick(__DIR__ . '/open-man.png');

// Properties
$d->setFont(__DIR__ . '/open-font.ttf');
$d->setFontSize(48);
$d->setFontWeight(900);
$d->setFillColor($color);
$d->setTextKerning(-1.0);
$d->setTextAntialias(true);
$d->setTextEncoding('UTF-8');
$metrics = $image->queryFontMetrics($d, $txt);
$d->annotation(69, $metrics['ascender']+10, $txt);
$image->newImage($metrics['textWidth']+76, $metrics['textHeight']+10, $background);
$image->setImageFormat('png');
$image->compositeImage($openman, Imagick::COMPOSITE_MATHEMATICS, 0, 0);
$image->drawImage($d);

// Save image?
//echo base64_encode($image->getImageBlob());
file_put_contents(__DIR__ . '/open-py.png', $image);

$d->clear();
$d->destroy();
$image->clear();
$image->destroy();