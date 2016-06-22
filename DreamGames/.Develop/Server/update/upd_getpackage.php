<?php
	include '../php/dbconnector.php';
	include '../php/function.php';
	include '../php/global.php';
	$verList=array();
	$verlist=mysql_query("SELECT * FROM version WHERE buildVersion>'$_GET[buildVersion]' AND allowUpdate='1'");
	if($verlist){
		while($vl = mysql_fetch_array($verlist)){
			array_push($verList,"update_$vl[mainVersion].$vl[buildVersion].$vl[dateVersion].zip");
		}
		$verlistStr="";
		for($vi=0;$vi<count($verList);$vi++){
			$verlistStr=$verlistStr.$verList[$vi];
			if($vi!=count($verList)-1){
				$verlistStr=$verlistStr."|";
			}
		}
		echo $verlistStr;
	}else{
		echo -1;
	}
?>