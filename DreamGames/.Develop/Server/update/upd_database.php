<?php
	include '../php/dbconnector.php';
	include '../php/function.php';
	include '../php/global.php';

	if($_GET['state']=='updversion'){
		$verlist=mysql_query("SELECT * FROM version WHERE mainVersion='$_GET[mainVersion]' AND buildVersion='$_GET[buildVersion]' AND dateVersion='$_GET[dateVersion]'");
		while($verexist = mysql_fetch_array($verlist)){
			echo "Exist version-$verexist[id]: $verexist[mainVersion].$verexist[buildVersion].$verexist[dateVersion] $verexist[versionName]";
			exit();
		}

		$addrs = mysql_query("INSERT INTO version VALUES(NULL,'$_GET[mainVersion]','$_GET[buildVersion]','$_GET[dateVersion]','$_GET[versionName]','0')");
		if($addrs){
			echo "Updated version: $_GET[mainVersion].$_GET[buildVersion].$_GET[dateVersion] $_GET[versionName]";
		}else{
			echo "Failed update version: $_GET[mainVersion].$_GET[buildVersion].$_GET[dateVersion] $_GET[versionName]";
		}
	}else if($_GET['state']=='applyupdate'){
		$verlist=mysql_query("SELECT * FROM version WHERE mainVersion='$_GET[mainVersion]' AND buildVersion='$_GET[buildVersion]' AND dateVersion='$_GET[dateVersion]'");
		while($verexist = mysql_fetch_array($verlist)){
			#echo "Exist version-$verexist[id]: $verexist[mainVersion].$verexist[buildVersion].$verexist[dateVersion] $verexist[versionName]";
			$addrs = mysql_query("UPDATE version SET allowUpdate='1' WHERE mainVersion='$_GET[mainVersion]' AND buildVersion='$_GET[buildVersion]' AND dateVersion='$_GET[dateVersion]'");
			echo "Applyed version: $_GET[mainVersion].$_GET[buildVersion].$_GET[dateVersion] $_GET[versionName]";
			exit();
		}
		echo "Failed apply version: $_GET[mainVersion].$_GET[buildVersion].$_GET[dateVersion] $_GET[versionName]";
	}else if($_GET['state']=='revokeupdate'){
		$verlist=mysql_query("SELECT * FROM version WHERE mainVersion='$_GET[mainVersion]' AND buildVersion='$_GET[buildVersion]' AND dateVersion='$_GET[dateVersion]'");
		while($verexist = mysql_fetch_array($verlist)){
			#echo "Exist version-$verexist[id]: $verexist[mainVersion].$verexist[buildVersion].$verexist[dateVersion] $verexist[versionName]";
			$addrs = mysql_query("UPDATE version SET allowUpdate='0' WHERE mainVersion='$_GET[mainVersion]' AND buildVersion='$_GET[buildVersion]' AND dateVersion='$_GET[dateVersion]'");
			echo "Revoked version: $_GET[mainVersion].$_GET[buildVersion].$_GET[dateVersion] $_GET[versionName]";
			exit();
		}
		echo "Failed revoke version: $_GET[mainVersion].$_GET[buildVersion].$_GET[dateVersion] $_GET[versionName]";
	}else{
		echo "Failed to do anything!";
		exit();
	}

?>