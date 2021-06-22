<?php
	session_start();
	include_once 'dbConnection.php';
	include_once'header.php'; 	
?>
<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<meta http-equiv="X-UA-Compatible" content="IE=edge">
	<title>Past Exams</title>
	<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" crossorigin="anonymous">
</head>
<body>
	<div class="container-fluid" style="padding-top: 40px;padding-left: 20%">
	<table class="table table-sm table-bordered" style="width: 80%">
		<h3>List Of Past Exams</h3>
  		<thead class="table-dark">
  			<td>#</td>
  			<td>Exam</td>
    		<td>Name</td>
    		<td>Subject</td>
    		<td>subject_id</td>
    		<td>Class</td>
    		<td>Solution</td>
  		</thead>
  		<tbody>
	<?php
	$sql="SELECT E.exam_id,E.name ,S.name AS sname,E.subject_id,class,E.edate,E.duration FROM subject S JOIN exams E WHERE S.subject_id=E.subject_id AND E.active=0;";
	$result=mysqli_query($con,$sql);
	$check=mysqli_num_rows($result);
	$c=1;
	
	if($check!=0){
		while ($row=mysqli_fetch_array($result)) {
			$exam=$row['exam_id'];
				echo "<tr>
					<td>".$c++."</td>
					<td>".$row['exam_id']."</td>
					<td>".$row['name']."</td>
					<td>".$row['sname']."</td>
					<td>".$row['subject_id']."</td>
					<td>".$row['class']."</td>
					<td><form action='solution.php?' method='GET'>
					<input type='hidden' name='exam' value='".$exam."'></input>
					<input type='SUBMIT' value='View Solution'></form></td>
				</tr>";
		}
		echo "</table>";
	}else{
		echo "No Past Exams";
	}
	?>
	</tbody>
	</table>
</body>
</html>