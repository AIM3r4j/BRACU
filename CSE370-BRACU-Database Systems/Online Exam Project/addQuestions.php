<?php
include_once 'dbConnection.php';
session_start();
$eid=$_GET['eid'];
$qid=rand(100000,999999);
$q=$_GET['q'];
$o1=$_GET['o1'];
$o2=$_GET['o2'];
$o3=$_GET['o3'];
$o4=$_GET['o4'];
$co=$_GET['co'];
$sql="INSERT INTO questions(qid,question,option_1,option_2,option_3,option_4,c_option,exam_id) VALUES('$qid','$q','$o1','$o2','$o3','$o4','$co','$eid');";
mysqli_query($con,$sql);
header('Location:createExam.php?n=0&eid='.$eid);
?>