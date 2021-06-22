<?php
session_start();
$_SESSION['admin']="admin";
include_once 'dbConnection.php';
include_once'header.php';
?>
<!DOCTYPE html>
<html>
<head>
	<title>DASHBOARD</title>
</head>
<body>
	<h3 style="padding: 50px">Welcome, Admin.</h5>
	<h5 style="padding-left: 50px">Use the navigation bar to roam through your desired features.</h3>

</body>
</html>