<?php

/* Text to write */
$text = $argv[1] ?? exit();

/* Create Imagick objects */
$image = new Imagick();
$draw = new ImagickDraw();
$color = new ImagickPixel('#000000');
$background = new ImagickPixel('none'); // Transparent

/* Font properties */
$draw->setFont('php-font.ttf');
$draw->setFontSize(200);
$draw->setFontWeight(900);
$draw->setStrokeColor('#fff');
$draw->setStrokeWidth(5);
$draw->setFillColor($color);
$draw->setStrokeAntialias(true);
$draw->setTextAntialias(true);
$draw->setTextEncoding('UTF-8');

/* Get font metrics */
$metrics = $image->queryFontMetrics($draw, $text);

/* Create text */
$draw->annotation(0, $metrics['ascender']+25, $text);

/* Create image */
$image->newImage($metrics['textWidth']+25, $metrics['textHeight'], $background);
$image->setImageFormat('png');
$image->drawImage($draw);

/* Save image */
file_put_contents('php-py.png', $image);

/* Clean up */
$draw->clear();
$draw->destroy();
$image->clear();
$image->destroy();