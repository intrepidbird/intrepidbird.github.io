<?php

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Process posted comment
    // Insert comment into database or store in a file
    // Return appropriate response
} elseif ($_SERVER["REQUEST_METHOD"] == "GET") {
    // Retrieve comments from database or file
    // Return comments as JSON
}

?>
