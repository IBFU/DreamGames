<?php
include("global.php");
$con = mysql_connect($db_addr,$db_user,$db_pswd);

mysql_query("set names '".$db_encoding."'",$con);
if (!$con){
	//die('Could not connect: ' . mysql_error());
	echo 'Could not connect db!';
}

mysql_select_db($db_name, $con);

//$plan = mysql_query("SELECT * FROM plan order by rate");
//$public = mysql_query("SELECT * FROM public order by rate");
//$result = mysql_query("SELECT * FROM result order by rate");
//$user = mysql_query("SELECT * FROM user order by rate");

//$child = mysql_query("SELECT * FROM child order by rate");
//$unit  = mysql_query("SELECT * FROM unit order by rate");
//$upload= mysql_query("SELECT * FROM upload order by rate");
?>