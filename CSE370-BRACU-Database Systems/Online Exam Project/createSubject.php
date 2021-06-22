<?php
include_once 'dbConnection.php';
session_start();

$admin=$_SESSION['admin'];
$name=ucfirst($_GET['sname']);
$class=$_GET['sclass'];
$sid=strtoupper(substr($name,0,3)).$class;
$sql="INSERT INTO subject(subject_id,name,class,admin_id) VALUES ('$sid','$name','$class','$admin');";
mysqli_query($con,$sql);
header('Location:subject.php');
?>