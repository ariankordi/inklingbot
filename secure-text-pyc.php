<?php

/* Text to write */
$txt = $argv[1] ?? exit();

$image = new Imagick();
$d = new ImagickDraw();
$color = new ImagickPixel('#178043');
$background = new ImagickPixel('none');
$hsts = new Imagick(__DIR__ . '/hsts.png');

// Properties
$d->setFont(__DIR__ . '/sc-font.ttf');
$d->setFontSize(28);
$d->setFontWeight(900);
$d->setFillColor($color);
$d->setTextAntialias(true);
$d->setTextEncoding('UTF-8');
$metrics = $image->queryFontMetrics($d, $txt);
$d->annotation(62, 43, $txt);
$image->newImage(278, 66, $background);
$image->compositeImage($hsts, Imagick::COMPOSITE_MATHEMATICS, 0, 0);
$image->setImageFormat('png');
$image->drawImage($d);

// Save image?
file_put_contents(__DIR__ . '/secure-py.png', $image);

$d->clear();
$d->destroy();
$image->clear();
$image->destroy();