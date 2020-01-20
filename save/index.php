

<html>
<head>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js">
<script type="text/javascript" src="jquery-1.9.0.min.js"></script>



</head>
<body>
<h1>SmartHome</h1>
<br>

<h1><div id="temp"></div></h1>
<br>
<form action="/templimit.php" method="post">

<input type="number" name="templimit" values="19">
<input type="submit" value="Submit">
</form>
<br>

<h2><div id="move"></div></h2>
</body>
</html>





<script type="text/javascript">
$(document).ready( function(){

	$('#temp').load('tempvisit.php');

	$('#move').load('movelist.php');

refresh();
});
 
function refresh()
{
	setTimeout( function() {

	 $('#temp').load('tempvisit.php');

	 $('#move').load('movelist.php');

refresh();
	}, 20000);
}
</script>
