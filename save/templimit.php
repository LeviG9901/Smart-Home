<?php
$servername = "localhost";
$username = "root";
$password = "callheni";
$dbname = "DB_CPU";


$conn = new mysqli($servername, $username, $password, $dbname);


if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}
$tl = $_POST["templimit"];
echo "Érték: ".$tl." C ";
$sql = "UPDATE test2 SET templimit=$tl WHERE id=12";

if ($conn->query($sql) === TRUE) {
    echo " .Hőmérséklet limit megváltoztatva";
} else {
    echo "Error updating record: " . $conn->error;
}

$conn->close();
?>