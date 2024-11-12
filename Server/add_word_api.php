<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="add_word_api.css">
</head>
<body>
    <div class="container">
        <?php
            // Function to sanitize input data
            function sanitize_input($data) {
                $data = trim($data);
                $data = stripslashes($data);
                $data = htmlspecialchars($data);
                return $data;
            }

            // Check if all required input parameters are set
            if (!isset($_GET['originalWord']) || !isset($_GET['translation']) || !isset($_GET['name'])) {
                echo "<p class='error'>Error: Missing input parameters.</p>";
                exit;
            }

            // Sanitize input data
            $input = sanitize_input($_GET['originalWord']);
            $input2 = sanitize_input($_GET['translation']);
            $name = sanitize_input($_GET['name']);
            $metadata = 'T' . time();

            // Explode the input variable into an array of lines
            $lines = explode("\n", $input);
            $lines2 = explode("\n", $input2);

            // Check if the number of lines in both inputs is equal
            if (count($lines) !== count($lines2)) {
                // Throw an error if the counts are not equal
                echo "<p class='error'>Error: The number of lines in input variables is not equal.</p>";
                exit;
            }

            // Generate a unique ID for the file
            $id = uniqid();
            $filetosave = $id . $name . $metadata . "\n";

            // Iterate through each line and concatenate them
            foreach ($lines as $i => $line) {
                $thing = sanitize_input($line);
                $filetosave .= $thing . ";" . sanitize_input($lines2[$i]) . ";0;0\n";
            }

            // Save $filetosave to a file with the chosen ID as the filename
            $filename = $id . '.txt';
            if (file_put_contents($filename, $filetosave) === false) {
                echo "<p class='error'>Error: Failed to save data to file.</p>";
                exit;
            }

            // Append the ID to the "id.txt" file
            if (file_put_contents('id.txt', $id . ';' . $metadata . ';' . $name . PHP_EOL, FILE_APPEND) === false) {
                echo "<p class='error'>Error: Failed to append ID to 'id.txt' file.</p>";
                exit;
            }

            echo "<p class='message'>Your ID is: $id. It has been copied to your clipboard.</p>";
            if ($_GET['debug'] == 1) {
                echo($filetosave);
            }
        ?>
        <button class="button" onclick="copyBtn('<?php echo $id; ?>')">Copy ID</button>
        <p class="message">If you get a popup to allow access to the clipboard, click "Yes" because it's required to copy the ID.</p>
    </div>

    <script>
        function copyBtn(str) {
            navigator.clipboard.writeText(str);
        }
    </script>
</body>
</html>