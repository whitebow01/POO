<?php
$host = "localhost";
$user = "root";
$pass = "carlos123";
$dbname = "empresa2";

try {
    $con = new PDO("mysql:host=$host;dbname=$dbname", $user, $pass);
    $con->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $ex) {
    die($ex->getMessage());
}

$sql1 = "select * from ventafact";
$stmt = $con->prepare($sql1);
$stmt->execute();
$registros = array();

while ($row = $stmt->fetch(PDO::FETCH_ASSOC)) {
    $registros[] = $row;
}

echo json_encode($registros);
?>
