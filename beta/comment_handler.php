<?php
// Retrieve form data
$name = $_POST['name'];
$comment = $_POST['comment'];

// Append comment to a file (you can use a database instead)
$file = 'comments.txt';
$current = file_get_contents($file);
$current .= "Name: $name\nComment: $comment\n\n";
file_put_contents($file, $current);

// Redirect back to the HTML page
header("Location: index.html");
exit();
?>
