<?php
	include("global.php");
	include("dbconnector.php");
	session_start();
	if($_GET['op']=="login"){
		$usercheck = mysql_query("SELECT uid,password FROM user where uid='$_POST[j_username]' and password = '$_POST[j_password]'");
		$num = mysql_num_rows($usercheck);
		if($num){
			$row = mysql_fetch_array($usercheck);
			$Username = mysql_fetch_array(mysql_query("SELECT uid FROM user WHERE uid='$row[0]'"));
			$Name = mysql_fetch_array(mysql_query("SELECT name FROM user WHERE uid='$row[0]'"));
			$Level= mysql_fetch_array(mysql_query("SELECT level FROM user WHERE uid='$row[0]'"));
			if(intval($Level[0])>=1){
				if($Username[0]=="1"){
					$_SESSION['user']	= "Admin";
				}else{
					$_SESSION['user']	= $Username[0];
				}
				$_SESSION['uid']  = $Username[0];
				$_SESSION['uname']  = $Name[0];
				$_SESSION['level']  = $Level[0];
				header("Location: ../index.php");
			}else{
				echo "<script>alert('用户已被封禁，无法登录！'); history.go(-1);</script>";
			}
		}else{
			echo "<script>alert('用户名或密码不正确！'); history.go(-1);</script>";
		}
	}else if($_GET['op']=="quit"){
		unset($_SESSION['user']);
		unset($_SESSION['uname']);
		unset($_SESSION['level']);
		unset($_SESSION['uid']);
		header("Location: ../index.php");
	}else{
		if(!isset($_SESSION['user'])){
			echo "输入用户名和密码以登录！";
		}
	}
?>