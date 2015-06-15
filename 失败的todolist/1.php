<?php
$host='localhost';
$user_name='root';
$password='lyf1995123';
$conn =mysql_connect($host,$user_name,$password);
$thing1=$_post['thing'];
$time1=$_post['time'];
if(!$conn)
{
	die('数据库连接失败： '.mysql_error());
}
mysql_select_db('test');
$sql="insert into todolist set thing='" . $thing1 ."',time='" . $time1 ."'";
mysql_query($sql)
?>
<html>
<head>
<title> </title>
</head>
<center>
<table width="75%" border="0" cellpadding="0" cellspacing="1">
<tr>
<td><div align="center">计划任务</div></td>
<td><div align="center">完成时间</div></td>
</tr>
<?php
$sql2='select* from todolist';
$result=mysql_query($sql2);
if($num=mysql_num_rows($result)){
	while($row=mysql_fetch_array($result,MYSQL_ASSOC))
	{
		?>
		<tr>
		<td>&nbsp;<?php echo $row['thing'];?> &nbsp;</td>
		<td>&nbsp;<?php echo $row['time'];?> &nbsp;</td>
		</tr>
		<?php
	}
}
mysql_close($conn);
?>
</table>
</body>
</center>
</html>

