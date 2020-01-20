<?php
$servername = "localhost";
$username = "root";
$password = "callheni";
$dbname = "DB_CPU";

$conn = new mysqli($servername, $username, $password, $dbname);

if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

$sql = "SELECT movesensor FROM test2";
$result = $conn->query($sql);

$row = $result->fetch_assoc();
//echo "asd".$row["movesensor"];

if($row["movesensor"]==0){
	echo "Riasztó kikapcsolva";
}

if($row["movesensor"]==1){
	echo "Riasztó bekapcsolva";
}



$conn->close();
?>
