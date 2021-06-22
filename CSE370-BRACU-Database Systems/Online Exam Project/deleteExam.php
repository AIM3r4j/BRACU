<?php
include_once 'dbConnection.php';
session_start();
$eid=$_GET['eid'];

$sql="UPDATE exams SET active=0 WHERE exam_id='$eid';";
mysqli_query($con,$sql);
header('Location:exam.php');
?>