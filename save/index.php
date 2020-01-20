

<html>
<head>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js">
<script type="text/javascript" src="jquery-1.9.0.min.js"></script>
<link rel="stylesheet" type="text/css" href="asd.css" />

<title>SmartHome</title>

</head>
<body>
<h1>SmartHome</h1>
<br>
<br>

<div id="temp"></div>
<br>
<form action="/templimit.php" method="post">

<input type="number" name="templimit" values="19">
<input type="submit" value="Küldés">
</form>
<br>





<h2><div id="move"></div></h2>

<br>
<h3>
<div id="moveSelect"></div>
</h3>
<br>
<button id="moveButton">Riasztó be/ki kapcsolása</button>

<br>
<div id="moveOnOff"><div>
</body>
</html>
























<script type="text/javascript">
$(document).ready( function() {

	$('#moveButton').click( function(){

	$('#moveOnOff').load('moveOnOff.php');
	
});
});

</script>


<script type="text/javascript">
$(document).ready( function(){

	$('#temp').load('tempvisit.php');

	$('#move').load('movelist.php');

	$('#moveSelect').load('moveSelect.php');

refresh();
});
 
function refresh()
{
	setTimeout( function() {

	 $('#temp').load('tempvisit.php');

	 $('#move').load('movelist.php');
	 
	 $('#moveSelect').load('moveSelect.php');

refresh();
	}, 20000);
}
</script>
