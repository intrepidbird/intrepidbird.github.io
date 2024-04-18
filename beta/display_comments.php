<?php
// Retrieve comments from file (or database)
$file = 'comments.txt';
$comments = file_get_contents($file);

// Display comments
echo nl2br($comments); // This will preserve line breaks in the comments
?>
