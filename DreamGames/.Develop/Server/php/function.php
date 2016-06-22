<?php
include("dbconnector.php");
include("global.php");

function getConfig($cn){
	$confinfo = mysql_query("SELECT cvalue FROM config where cname='".$cn."'");
	$confnumb = mysql_num_rows($confinfo);
	if($confnumb){
		$conf = mysql_fetch_array($confinfo);
		return $conf[0];
	}else{
		return -1;
	}
}

function setConfig($cn,$cv){
	$confset = mysql_query("UPDATE config SET cvalue='$cv' where cname='$cn'");
	if($confset){
		return 0;
	}else{
		return -1;
	}
}

function addConfig($cn,$cv){
	$confset = mysql_query("INSERT INTO config VALUES(NULL,'$cn','$cv')");
	if($confset){
		return 0;
	}else{
		return -1;
	}
}

function getMysqlError(){
	return mysql_errno().": ".mysql_error();
}

function ErrorLocation($eid){
	header("Location: /sorry.php?t=".$eid);
}

function ErrorLocationMsg($msg){
	header("Location: /sorry.php?o=".$msg);
}

function logFile($interface,$info){
	date_default_timezone_set('prc');
	$datetime = date("Y-m-d H:i:s");
	$date = date("Ymd");
	$RootDir = $_SERVER['DOCUMENT_ROOT'];
	$logFile =  $RootDir."_logs/log_".$interface."_".$date.".log";
	$ip = $_SERVER["REMOTE_ADDR"];
	if($ip=='127.0.0.1'){
		$country='本地';
		$province='本地';
		$city='本地';
	}else{
		$country = iconv('UTF-8','GBK//IGNORE',GetIpLookup($_SERVER["REMOTE_ADDR"])['country']);
		$province = iconv('UTF-8','GBK//IGNORE',GetIpLookup($_SERVER["REMOTE_ADDR"])['province']);
		$city = iconv('UTF-8','GBK//IGNORE',GetIpLookup($_SERVER["REMOTE_ADDR"])['city']);
	}
	$url = "http://".$_SERVER['SERVER_NAME']."".$_SERVER['REQUEST_URI'];
	$addrs = mysql_query("INSERT INTO logs VALUES(NULL,'$datetime','$ip','$country','$province','$city','$url','$info')");
	if($addrs){
		return true;
	}else{
		#echo "INSERT INTO logs VALUES(NULL,'$datetime','$ip','$url','$info')";
		return false;
	}
	//$logf = fopen($logFile, "w");
	//file_put_contents($logFile,$datetime." - ".$ip." - ".$url." - ".$info."\r\n",FILE_APPEND);
	//$myfile = fopen($logFile, "a");
	//fwrite($myfile, $datetime." - ".$ip." - ".$url." - ".$info."\r\n");
	//fclose();
}

function GetIp(){
	$realip = '';
	$unknown = 'unknown';
	if (isset($_SERVER)){
		if(isset($_SERVER['HTTP_X_FORWARDED_FOR']) && !empty($_SERVER['HTTP_X_FORWARDED_FOR']) && strcasecmp($_SERVER['HTTP_X_FORWARDED_FOR'], $unknown)){  
			$arr = explode(',', $_SERVER['HTTP_X_FORWARDED_FOR']);  
			foreach($arr as $ip){  
				$ip = trim($ip);  
				if ($ip != 'unknown'){  
					$realip = $ip;  
					break;  
				}  
			}  
		}else if(isset($_SERVER['HTTP_CLIENT_IP']) && !empty($_SERVER['HTTP_CLIENT_IP']) && strcasecmp($_SERVER['HTTP_CLIENT_IP'], $unknown)){  
			$realip = $_SERVER['HTTP_CLIENT_IP'];  
		}else if(isset($_SERVER['REMOTE_ADDR']) && !empty($_SERVER['REMOTE_ADDR']) && strcasecmp($_SERVER['REMOTE_ADDR'], $unknown)){  
			$realip = $_SERVER['REMOTE_ADDR'];  
		}else{  
			$realip = $unknown;  
		}  
	}else{  
		if(getenv('HTTP_X_FORWARDED_FOR') && strcasecmp(getenv('HTTP_X_FORWARDED_FOR'), $unknown)){  
			$realip = getenv("HTTP_X_FORWARDED_FOR");  
		}else if(getenv('HTTP_CLIENT_IP') && strcasecmp(getenv('HTTP_CLIENT_IP'), $unknown)){  
			$realip = getenv("HTTP_CLIENT_IP");  
		}else if(getenv('REMOTE_ADDR') && strcasecmp(getenv('REMOTE_ADDR'), $unknown)){  
			$realip = getenv("REMOTE_ADDR");  
		}else{  
			$realip = $unknown;  
		}  
	}  
	$realip = preg_match("/[\d\.]{7,15}/", $realip, $matches) ? $matches[0] : $unknown;  
	return $realip;  
}

function GetIpLookup($ip = ''){  
	if(empty($ip)){  
		$ip = GetIp();  
	}  
	$res = @file_get_contents('http://int.dpool.sina.com.cn/iplookup/iplookup.php?format=js&ip=' . $ip);  
	if(empty($res)){ return false; }  
	$jsonMatches = array();  
	preg_match('#\{.+?\}#', $res, $jsonMatches);  
	if(!isset($jsonMatches[0])){ return false; }  
	$json = json_decode($jsonMatches[0], true);  
	if(isset($json['ret']) && $json['ret'] == 1){  
		$json['ip'] = $ip;  
		unset($json['ret']);  
	}else{  
		return false;  
	}  
	return $json;  
}
?>