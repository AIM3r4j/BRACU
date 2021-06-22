<?php
	session_start();
	include_once 'dbConnection.php';
	include_once'header.php';
	if(isset($_GET['d'])){
		echo "<script>
			alert('Questions have been added successfully');
		</script>";
	}
?>
<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<meta http-equiv="X-UA-Compatible" content="IE=edge">
	<title>Exams</title>
	<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" crossorigin="anonymous">
	<script src="js/exam.js" type="text/javascript" charset="utf-8" async defer></script>
</head>
<body>
	
	<div class="container-fluid" style="padding-top: 40px;padding-left: 20%">
	<table class="table table-sm table-bordered" style="width: 80%">
		<h3>List Of Exams</h3>
  		<thead class="table-dark">
  			<td>#</td>
  			<td>Exam</td>
    		<td>Name</td>
    		<td>Subject</td>
    		<td>subject_id</td>
    		<td>Class</td>
    		<td>Date</td>
    		<td>Duration(Minutes)</td>
  		</thead>
  		<tbody>
	<?php
	$sql="SELECT E.exam_id,E.name ,S.name AS sname,E.subject_id,class,E.edate,E.duration FROM subject S JOIN exams E WHERE S.subject_id=E.subject_id AND E.active=1;";
	$result=mysqli_query($con,$sql);
	$check=mysqli_num_rows($result);
	$c=1;
	if($check!=0){
		while ($row=mysqli_fetch_array($result)) {
				echo "<tr>
					<td>".$c++."</td>
					<td>".$row['exam_id']."</td>
					<td>".$row['name']."</td>
					<td>".$row['sname']."</td>
					<td>".$row['subject_id']."</td>
					<td>".$row['class']."</td>
					<td>".$row['edate']."</td>
					<td>".$row['duration']."</td>
				</tr>";
		}
		echo "</table>";
	}else{
		echo "No exams yet";
	}
	?>
	</tbody>
	</table>
	<button onclick="showCreateExam()" class="btn-primary">Create New Exam</button>

	<button onclick="showDeleteExam()" class="btn-primary">Delete Exam</button>


	<?php

	$sql="SELECT subject_id FROM subject;";
	$result=mysqli_query($con,$sql);
	?>
	<div id="createExam" style="display: none;"><br>
	<h5>Choose subject first:</h5>
	<form action="createExam.php" method="GET">
	<select name="esub" required>
		<?php
		while ($rows=mysqli_fetch_array($result)) {
				$subject=$rows['subject_id'];
				echo "<option value='$subject'>$subject</option>";	
			}
		?>
	</select>
	<input type="text" name="ename" placeholder="Exam Name" required>
	<input type="date" name="edate" placeholder="Date" required>
	<input type="int" name="eduration" placeholder="Duration in Minutes" required>
	<button type="SUBMIT" class="btn-outline-success">Create & Add questions</button>
	</form>
	
	<button onclick="hideCreateExam()" class="btn-warning">Cancel</button>
	

	<?php

	$sql="SELECT exam_id FROM exams WHERE active=1;";
	$result=mysqli_query($con,$sql);
	?>

	</div>
	<div id="deleteExam" style="display: none;"><br>
	<h5>Choose the exam you want to delete:</h5>
	<form action="deleteExam.php" method="GET">
	<select name="eid" required>
		<?php
		while ($rows=mysqli_fetch_array($result)) {
				$exam=$rows['exam_id'];
				echo "<option value='$exam'>$exam</option>";	
			}
		?>
	</select>
	<button type="SUBMIT" class="btn-outline-success">Confirm</button>
	</form>
	
	<button onclick="hideDeleteExam()" class="btn-warning">Cancel</button>
	
	</div>
	</div>
</body>
</html>