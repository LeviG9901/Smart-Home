<?php
$servername = "localhost";
$username = "root";
$password = "callheni";
$dbname = "DB_CPU";


$conn = new mysqli($servername, $username, $password, $dbname);

if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

$sql = "SELECT szam ,templimit FROM test2";
$result = $conn->query($sql);

if ($result->num_rows > 0) {

    while($row = $result->fetch_assoc()) {
        echo "<h1>".$row["szam"]." C a hőmérséklet"."<br>"."<br>"."<h2>"."Jelenlegi maximális hőmérséklet beállítás:  ".$row["templimit"]."</h2>"."</h1>";
    }
} else {
    echo "0 results";
}
$conn->close();
?>
