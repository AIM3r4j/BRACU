<?php
	include_once 'dbConnection.php';
	if(isset($_GET['n'])){
		$eid=$_GET['eid'];
	}else if(!isset($_GET['n'])){
		$eid=rand(100000,999999);
		$name=ucfirst($_GET['ename']);
		$subject=$_GET['esub'];
		$edate=$_GET['edate'];
		$duration=$_GET['eduration'];

		$sql="INSERT INTO exams(exam_id,subject_id,name,edate,duration,active) VALUES ('$eid','$subject','$name','$edate','$duration','1');";
		mysqli_query($con,$sql);
	}
	
	include_once 'header.php';
	session_start();
?>
<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<meta http-equiv="X-UA-Compatible" content="IE=edge">
	<title>Create Questions</title>
	<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" crossorigin="anonymous">
</head>
<body>
	<form action="addQuestions.php" method="GET" id="form" style="padding: 100px; padding-top: 40px; padding-bottom: 40px">
		<input type="hidden" name="eid" value="<?php echo $eid; ?>">
		<h5>Insert all the informations correctly:</h5>
		<input class="form-control" type="text" name="q" placeholder="Question text" required>
		<h5>Set the options for the question:</h5>
		<input class="form-control" type="text" name="o1" placeholder="Option-1 text" required>
		<input class="form-control" type="text" name="o2" placeholder="Option-2 text" required>
		<input class="form-control" type="text" name="o3" placeholder="Option-3 text" required>
		<input class="form-control" type="text" name="o4" placeholder="Option-4 text" required><br>
		<h5>Choose the correct option:</h5>
		<select name="co" required>
			<option value="option_1">Option-1</option>
			<option value="option_2">Option-2</option>
			<option value="option_3">Option-3</option>
			<option value="option_4">Option-4</option>
		</select><br>
		<button class="btn-outline-success" type="SUBMIT">Confirm & Next</button>
	</form>

	<form action="exam.php" method="GET" style="padding-left: 100px">
		<input name="d" type="hidden" value="0">
		<h5>If you are done adding questions, press the done button</h5>
		<button class="btn-success" type="SUBMIT">Done</button>	
	</form>
	
</body>
</html>