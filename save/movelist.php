<?php
$servername = "localhost";
$username = "root";
$password = "callheni";
$dbname = "DB_CPU";


$conn = new mysqli($servername, $username, $password, $dbname);

if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

$sql = "SELECT time  FROM move";
$result = $conn->query($sql);

if ($result->num_rows > 0) {
    // output data of each row
    while($row = $result->fetch_assoc()) {
        echo "mozgás időpontja: ". $row["time"]."<br>";
    }
} else {
    echo "0 results";
}
$conn->close();
?>