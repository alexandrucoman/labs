 <style type="text/css">
 body{
 	background: #FF6699;
 	padding:100px;
 	padding-top: 0px;
 }
 #result{
 	margin: 50px;
 	font-size: 20px;
 }
 </style>
 
 <h2>Enter an equation: </h2> <br>
 <form action="index.php" method = 'POST'>
  First member: <input type="text" name="firstMember"> 
  Second member: <input type="text" name="secondMember">
  = <input type="text" name="resultMember">
  <input type="submit" value="Submit">
</form> 
<div id = "result">
<?php
	function resolveEquation($firstMember, $secondMember, $resultMember){

		$result = ($resultMember - $secondMember )/$firstMember;
		return $result;
	}
	if(isset($_POST)){
		$firstMember = intval($_POST["firstMember"]); 
		$secondMember = intval($_POST["secondMember"]);
		$resultMember = intval($_POST["resultMember"]);
		echo 'Result is: ';
		echo resolveEquation($firstMember,$secondMember,$resultMember);
	}


?>
</div>