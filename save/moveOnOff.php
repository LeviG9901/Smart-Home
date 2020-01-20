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

if($row["movesensor"]==0){
	
$sql = "UPDATE test2 SET movesensor=1 WHERE id=12";

$conn->query($sql);

}




if($row["movesensor"]==1){
	
$sql = "UPDATE test2 SET movesensor=0 WHERE id=12";

$conn->query($sql);

}

$conn->close();
?>