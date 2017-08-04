<?php

/* Text to write */
mb_internal_encoding('UTF-8');
$txt = $argv[1] ?? exit();

$image = new Imagick();
$background = new ImagickPixel('none');
$d = new ImagickDraw();
$color = new ImagickPixel('#178043');
$hsts1 = new Imagick(__DIR__ . '/hsts-1.png');
$hsts2 = new Imagick(__DIR__ . '/hsts-2.png');
$stst = new Imagick(__DIR__ . '/stst.png');

// Properties
$image->newImage(2000, 66, $background);
$image->compositeImage($hsts1, Imagick::COMPOSITE_MATHEMATICS, 0, 0);
$d->setFont(__DIR__ . '/sc-font.ttf');
$d->setFontSize(28);
$d->setFontWeight(900);
$d->setFillColor($color);
$d->setTextAntialias(true);
$d->setTextEncoding('UTF-8');
$metrics = $image->queryFontMetrics($d, $txt);
$d->annotation(62, 43, $txt);
$len = $metrics['textWidth']+3;
$stst->scaleImage($len, 66);
$image->compositeImage($stst, Imagick::COMPOSITE_MATHEMATICS, 62, 0);
$image->compositeImage($hsts2, Imagick::COMPOSITE_MATHEMATICS, $len+62, 0);
$all_len = $hsts1->getImageWidth() + $stst->getImageWidth() + $hsts2->getImageWidth();

	$image->setImageExtent($all_len,66);

$image->setImageFormat('png');
$image->drawImage($d);

// Save image?
file_put_contents(__DIR__ . '/secure-py.png', $image);

$d->clear();
$d->destroy();
$image->clear();
$image->destroy();