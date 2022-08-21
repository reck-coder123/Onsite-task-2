CREATE DATABASE IF NOT EXISTS `hiretlogin` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `hiretlogin`;
CREATE TABLE IF NOT EXISTS `Jobs`(
`id` int(65) NOT NULL auto_increment,
`nameA` varchar(50) NOT NULL,
`username` varchar(50) NOT NULL,
`passwordA` varchar(50) NOT NULL,
`emailA` varchar(50) NOT NULL,
PRIMARY KEY (`id`) )ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS `News`(
`id` int(65) NOT NULL auto_increment,
`nameJ` varchar(50) NOT NULL,
`username` varchar(50) NOT NULL,
`passwordJ` varchar(50) NOT NULL,
`emailJ` varchar(50) NOT NULL,
PRIMARY KEY (`id`)
)ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS `infos`(
`id` int(65) NOT NULL auto_increment,
`job` varchar(50) NOT NULL,
`description` varchar(5000) NOT NULL,
PRIMARY KEY (`id`))ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS `chose` (
`id` int(65) NOT NULL auto_increment,
`Name` varchar(50) NOT NULL,
`jprofile` varchar(100) NOT NULL ,
PRIMARY KEY (`id`)

)ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
select * from Jobs;
