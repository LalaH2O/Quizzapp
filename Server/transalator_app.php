<?php
    $id = $_GET['id'];
    $search = $_GET['download_list'];
    $out = '';

    if($id != '' and isset($_GET['id'])){
        if isset($_GET['json']){
            $filename = $id . '.json';
        }else{
        $filename = $id . '.txt';
        }
        // Check if the file exists
        if (file_exists($filename)) {
            // Open the file for reading
            $file = fopen($filename, "r");

            // Check if the file was opened successfully
            if ($file) {
                // Read and echo the content of the file line by line
                while (!feof($file)) {
                    $out .= fgets($file) . "\n";
                }

                // Close the file
                fclose($file);
            } else {
                echo "Failed to open the file.";
            }
        } else {
            echo "File does not exist.";
        }
    } elseif(isset($_GET['download_list'])){
        if (file_exists('id.txt')) { // Check if the file exists
            $file = fopen('id.txt', 'r');
            $content = fread($file, filesize('id.txt')); // Read the content of the file
            $out .= $content; // Echo the content
            fclose($file); // Close the file
        } else {
            echo "File does not exist.";
        }
    }else{
        exit('1');
    }
?>

<html>
    <head>
        <meta utf-8>
    </head>
    <body>
        <p>
            <? echo $out; ?>
        </p>
    </body>
</html>