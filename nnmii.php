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

foreach(json_decode(json_encode($mii), true)['mii']['images']['image'] as $ass) {
if($ass['type'] == 'normal_face') {
	echo $ass['cached_url'];
	}
}