<?php
//static $SOPUrl = "http://itebeta.baidu.com:8102/webservice/UserService?wsdl";
//static $SOPUrl = "http://uuap.baidu.com:8086/webservice/UserService?wsdl";

//new interface
static $SOPUrlPosition = "http://itebeta.baidu.com:8102/ws/PositionRemoteService?wsdl";

//new interface
static $SOPUrl = "http://itebeta.baidu.com:8102/ws/UserRemoteService?wsdl";

$soapclient = new SoapClient($SOPUrl);

//SoapHeader
$soapheader = new SoapHeader("http://schemas.xmlsoap.org/wsdl/soap/","appKey","UICWSTestKey",false);
$soapclient->__setSoapHeaders(array($soapheader));

$workername = $argv[1];
$response = $soapclient->getUserByUsername(array('arg0'=>$workername));
$response2 = $soapclient->getSuperiorByUsername(array('arg0'=>$workername, 'arg1'=>1));

var_dump($response);
var_dump($response2);

var_dump($soapclient->__getFunctions());

//var_dump($soapclient->__getTypes());

/*
http://wiki.babel.baidu.com/twiki/bin/view/Com/BPIT/UIC%E6%8E%A5%E5%85%A5%E7%94%A8%E6%88%B7%E6%89%8B%E5%86%8C 
 */


?>
