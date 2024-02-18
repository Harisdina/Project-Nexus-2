<?php 
  session_start(); 

  if (!isset($_SESSION['username'])) {
  	$_SESSION['msg'] = "You must log in first";
  	header('location: login.php');
  }
  if (isset($_GET['logout'])) {
  	session_destroy();
  	unset($_SESSION['username']);
  	header("location: login.php");
  }
  if (isset($_SESSION['Available_balance'])) {
    $_SESSION['Available_balance'];
    header('location: login.php');
}
?>
<!DOCTYPE html>
<html>
<head>
	<title>Food Delivery System</title>
    <meta charset="UTF-8">
	<link rel="stylesheet" type="text/css" href="style.css">
	<link rel="stylesheet" href="styles.css">
    <link href="https://storage.googleapis.com/alan-tutorial/web-sdk/styles.css" rel="stylesheet">
    

</head>
<body>

<div class="header">
	<h2>Home Page</h2>
</div>
            
<div class="content">
  	
  	<?php if (isset($_SESSION['success'])) : ?>
      <div class="error success" >
      	<h3>
          <?php 
          	echo $_SESSION['success']; 
          	unset($_SESSION['success']);
          ?>
      	</h3>
      </div>
  	<?php endif ?>

    

<?php
    if (isset($_SESSION['username'])) {
        echo "<p>Welcome <strong>{$_SESSION['username']}</strong></p>";

        if (isset($_SESSION['Available_balance'])) {
            $availableBalance = $_SESSION['Available_balance'];
            echo "Your Available Balance: $availableBalance";
        } else {
            echo "Your Available Balance is not set in this session";
        }

        echo '<p><a href="index.php?logout=1" style="color: red;">Logout</a></p>';
}
?>

</div>

    
</body>
</html>