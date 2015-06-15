<?php
$host='localhost';
$user_name='root';
$password='lyf1995123';
$conn =mysql_connect($host,$user_name,$password);
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
$time=$_post['time'];
$sql2='delete from todolist where time=' .$time. '';
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


