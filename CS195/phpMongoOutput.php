
<?php
    //set Uniform Resource Identifier
    $uri = "mongodb://DrakeStudent:abc123@ds031912.mongolab.com:31912/drake_environmental_science";
    //set when to timeout connection to client
    $options = array("connectTimeoutMS" => 30000);
    //connect to mongoDB
    $client = new MongoClient($uri, $options);

    //select database
    $db = $client->selectDB('drake_environmental_science');
    //lets you store pics, so get pics this way too
    $gridfs = $db->getGridFS();


    //select collection
    //names of collections: testdocs
    $collection = new MongoCollection($db, 'testdocs');

    //get variables 
    $month = $_POST['month'];
    $day = $_POST['day'];
    $year = $_POST['year'];
    $date = $year . "-" . $month . "-" . $day; 

    //search for date
    $dateQuery = array('date' => $date);
    $result = array();
    $picResult = array();

    $id = null;
    //finds all data that aren't pictures
    $cursor = $collection->find($dateQuery);
    foreach($cursor as $doc) {
        //var_dump($doc);
        array_push($result,$doc);

        //finds all pictures for a specific date
        
        $id = $doc['_id'];
        $picCursor = $gridfs->find(array('recordID'=>$id);
        foreach($picCursor as $doc) {
            array_push($picResult,$doc);

        }
    }

    function cleanData(&$str)
    {
        $str = preg_replace("/\t/", "\\t", $str);
        $str = preg_replace("/\r?\n/", "\\n", $str);
        if(strstr($str, '"')) $str = '"' . str_replace('"', '""', $str) . '"';
    }

    // filename for download
    $filename = "website_data_" . date('Ymd') . ".xls";

    header("Content-Disposition: attachment; filename=\"$filename\"");
    header("Content-Type: application/vnd.ms-excel");

    $flag = false;
    //switch this to $result for actual result, $test_array to test the code
    foreach($result as $row) {
        if(!$flag) {
            // display field/column names as first row
            echo implode("\t", array_keys($row)) . "\r\n";
            $flag = true;
        }
        array_walk($row, 'cleanData');
        echo implode("\t", array_values($row)) . "\r\n";
    }

    header("Content-Type: image/jpeg");
    echo $picResult->getBytes();

    exit;

?>
