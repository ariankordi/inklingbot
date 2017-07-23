<?php
if(!isset($argv[1])) {
exit('n');
}
require_once('nnasclient.php');
$nnas = new NnasClient('illegal.p12', 'alpine');

$mapped = $nnas->mappedIds($argv[1]);
if(!$mapped) {
exit('n');
}
$pid = +"{$mapped->mapped_id->out_id}";
$mii = $nnas->getMiis($pid);
if(!$mii) {
exit('n');
}
echo "{$mii->mii->images->image[4]->cached_url}";