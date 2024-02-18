<!DOCTYPE html>
<html>
<body>

<?php
session_start();


$username = "";
$email    = "";
$Available_balance = "";
$errors = array(); 


$db = mysqli_connect('localhost', 'root', '', 'project');

if ($db->connect_error) {
    die("Connection failed: " . $db->connect_error);
}



$sql = "SELECT id, username, email,Available_balance, img FROM users";
$result = $db->query($sql);


if ($result->num_rows > 0) {
    
    while($row = $result->fetch_assoc()) {
        print "<br> id: ". $row["id"]. "<br> - Name: ". $row["username"]. "<br> - Email: " . $row["email"] . "<br> - Available_balance: ".$row["Available_balance"] ;
      print "<img src=\"".$row["img"]."\">";
     
    }
} else {
    print "0 results";
}



$db->close();   
        ?> 



</body>
</html>