<?php
$host='localhost';
$user_name='root';
$password='lyf1995123';
$conn =mysql_connect($host,$user_name,$password);
if(!$conn)
{
	die('数据库连接失败： '.mysql_error());
}
$sql='select version();'
$result=mysql_query($sql);
if($num=mysql_num_rows($result)){
	$row=mysql_fetch_array($result);
	echo'<pre>'
	print($row);
}
mysql_close($conn);
?>
