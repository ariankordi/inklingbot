<?php

/*
NnasClient by Arian Kordi
https://github.com/ariankordi

Licensed under GNU AGPLv3: https://choosealicense.com/licenses/agpl-3.0/
*/

class NnasClient {
    var $clientkey;
    var $clientkey_pass;
    var $host;
    var $account_id;
	var $account_passwd;
	var $platform_id;
	var $device_id;
	var $device_type;
	var $device_cert;
	var $serial_number;
	var $access_token;

	 /** new nnasClient('/etc/certificates/client_certificate_that_doesnt_need_password.pem');
     * OR... new nnasClient('/etc/certificates/client_certificate_that_needs_password.p12', 'alpine');
     */
    public function __construct($key) {
    $this->clientkey = $key;
    $this->clientkey_pass = (func_num_args() == 2 ? func_get_args()[1] : null);
    }

	private function xml_encode($mixed, $domElement=null, $DOMDocument=null) {
    if(is_null($DOMDocument)) {
        $DOMDocument = new DOMDocument;
        $DOMDocument->formatOutput = true;
        $this->xml_encode($mixed, $DOMDocument, $DOMDocument);
        return $DOMDocument->saveXML();
    } else {
        // To cope with embedded objects 
        if(is_object($mixed)) {
          $mixed = get_object_vars($mixed);
        }
        if(is_array($mixed)) {
            foreach($mixed as $index => $mixedElement) {
                if(is_int($index)) {
                    if($index === 0) {
                        $node = $domElement;
                    } else {
                        $node = $DOMDocument->createElement($domElement->tagName);
                        $domElement->parentNode->appendChild($node);
                    }
                } else {
                    $plural = $DOMDocument->createElement($index);
                    $domElement->appendChild($plural);
                    $node = $plural;
                    if (!(rtrim($index, 's') === $index)) {
                        $singular = $DOMDocument->createElement(rtrim($index, 's'));
                        $plural->appendChild($singular);
                        $node = $singular;
                    }
                }

                $this->xml_encode($mixedElement, $node, $DOMDocument);
            }
        } else {
            $mixed = is_bool($mixed) ? ($mixed ? 'true' : 'false') : $mixed;
            $domElement->appendChild($DOMDocument->createTextNode($mixed));
        }
    }
}
	
    public function nnasRequest($url) {
		$args = func_get_args();
			
	$httpheader = array(
'X-Nintendo-Platform-ID: ' . $this->platform_id,
'X-Nintendo-Device-Type: ' . $this->device_type,
'X-Nintendo-Device-ID: ' . $this->device_id,
'X-Nintendo-Serial-Number: ' . $this->serial_number,
'X-Nintendo-System-Version: 1200',
'X-Nintendo-Region: 2',
'X-Nintendo-Country: US',
'Accept-Language: en',
'X-Nintendo-Client-ID: ea25c66c26b403376b4c5ed94ab9cdea',
'X-Nintendo-Client-Secret: d137be62cb6a2b831cad8c013b92fb55',
'Accept: */*',
'X-Nintendo-API-Version: 0100',
'X-Nintendo-FPD-Version: 0000',
'X-Nintendo-Environment: L1',
'X-Nintendo-Title-ID: 000400100002C000',
'X-Nintendo-Unique-ID: 002C0',
'X-Nintendo-Application-Version: 0003',
'X-Nintendo-Device-Model: WUP',
'X-Nintendo-Device-Cert: ' . $this->device_cert,
);
if(!empty($this->access_token)) {
$httpheader[] = 'Authorization: Bearer ' . $this->access_token;
} if(isset($args[1])) {
$httpheader[] = 'Content-type: ' . (isset($args[2]) && $args[2] == 'xml' ? 'application/xml' : 'application/x-www-form-urlencoded');
}
	
            $ch = curl_init();
            $curl_array = array(
        CURLOPT_URL => $url, CURLOPT_SSL_VERIFYPEER => 0, CURLOPT_SSLCERT => $this->clientkey, CURLOPT_SSLCERTPASSWD => $this->clientkey_pass,CURLOPT_HEADER => true,
        CURLOPT_HTTPHEADER => $httpheader,
	    CURLOPT_RETURNTRANSFER => true,CURLOPT_FOLLOWLOCATION=> false,);
	    if(func_num_args() == 4) {
		if(!empty($args[3])) {
		        curl_setopt($ch, CURLOPT_CUSTOMREQUEST, $args[3]);
		}
	    $curl_array[CURLOPT_POST] = true;
		if($args[2] == 'xml') { $curl_array[CURLOPT_POSTFIELDS] = $this->xml_encode($args[1]); } else {
		$curl_array[CURLOPT_POSTFIELDS] = http_build_query($args[1]);
				}
	    }
	    curl_setopt_array($ch, $curl_array);
	    $response = curl_exec($ch);
	    $response_code = curl_getinfo($ch, CURLINFO_HTTP_CODE);
	    $content_type = curl_getinfo($ch, CURLINFO_CONTENT_TYPE);
        $body = substr($response, curl_getinfo($ch, CURLINFO_HEADER_SIZE));
        if($response_code != 200) {
            if($response_code == 500) {
            throw new Exception('Internal server error');
            }
            elseif($response_code == 405) {
            throw new Exception('Invalid method');
            }
            // other errors idk
        }
        if(!empty($body) && ($content_type == 'text/xml' || $content_type = 'application/xml')) {
        // parse xml if we are dealing with such
        $xml = new SimpleXMLElement($body);
        return $xml;
        }
        elseif($content_type == 'application/json') {
        // also parse json if we are doing that
        return json_decode($body);
        }
    // if none of the above is satisfied (return ends the function), then return body
    return $body;
    }

	public function setAccessToken() {
	$login = array('grant_type' => 'password', 'user_id' => $this->account_id, 'password' => $this->account_passwd,);
	$req = $this->nnasRequest('https://account.nintendo.net:443/v1/api/oauth20/access_token/generate', $login, 1, false);
	$token = "{$req->access_token->token}";
	$this->access_token = $token;
	return $token;
	}
	
	public function mappedIDs($input, $in_id = 'user_id', $out_id = 'pid') {
	$req = $this->nnasRequest('https://account.nintendo.net:443/v1/api/admin/mapped_ids?input_type=' . $in_id . '&output_type=' . $out_id . '&input=' . $input);
		if(empty($req->mapped_id->out_id)) {
		return false;
		}
	return $req;
	}
	
	public function getMiis($pids) {
	if(is_array($pids)) $pids = implode(',', $pids);
	$req = $this->nnasRequest('https://account.nintendo.net:443/v1/api/miis?pids=' . $pids);
		if(!isset($req->mii)) {
		return false;
		}
	return $req;
	}
	
	public function setMii($mii) {
	$mii_change = array('mii' => array('name' => 0, 'primary' => 'Y', 'data' => $mii));
	$req = $this->nnasRequest('https://account.nintendo.net:443/v1/api/people/@me/miis/@primary', $mii_change, 'xml', 'PUT');
	$req2 = $this->nnasRequest('https://account.nintendo.net:443/v1/api/people/@me/miis/@primary');
	$new_mii = "{$req2->data}";
	if($new_mii = $mii) {
	return true;
		} else {
		return false;
		}
	}

}