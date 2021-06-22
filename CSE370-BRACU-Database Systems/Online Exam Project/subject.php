<?php
session_start();
include_once 'dbConnection.php';

include_once 'header.php';
?>
<!DOCTYPE html>
<html>
<head>
	<title>Subjects</title>
	<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" crossorigin="anonymous">
	<script src="js/subject.js"></script>
</head>
<body>
	<div class="container-fluid" style="padding-top: 40px;padding-left: 30%">
	<table class="table table-sm table-bordered" style="width: 50%">
		<h3>List Of Subjects</h3>
  		<thead class="table-dark">
  			<td>#</td>
  			<td>Subject_id</td>
    		<td>Name</td>
    		<td>Class</td>
    		<td>Created by</td>
  		</thead>
  		<tbody>
	<?php
	$sql="SELECT * FROM subject;";
	$result=mysqli_query($con,$sql);
	$check=mysqli_num_rows($result);
	$c=1;
	if($check!=0){
		while ($row=mysqli_fetch_array($result)) {
				echo "<tr>
					<td>".$c++."</td>
					<td>".$row['subject_id']."</td>
					<td>".$row['name']."</td>
					<td>".$row['class']."</td>
					<td>".$row['admin_id']."</td>
				</tr>";
		}
		echo "</table>";
	}else{
		echo "No subjects yet";
	}
	?>
	</tbody>
	</table>
	<button onclick="showCreateSubject()" class="btn-primary">Create New Subject</button>

	<div id="createSubject" style="display: none;">
	<form action="createSubject.php" method="GET">
	<input type="text" name="sname" placeholder="Subject Name" required>
	<input type="int" name="sclass" placeholder="Class" required>
	<button type="SUBMIT" class="btn-outline-success">Confirm</button>
	</form>
	
	<button onclick="hideCreateSubject()" class="btn-warning">Cancel</button>
	
	</div>
	</div>
	
	
</body>
</html>