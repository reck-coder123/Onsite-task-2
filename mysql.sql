CREATE DATABASE IF NOT EXISTS `hirelogin` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `hirelogin`;
CREATE TABLE IF NOT EXISTS `Job`(
`id` int(65) NOT NULL auto_increment,
`nameA` varchar(50) NOT NULL,
`usernameA` varchar(50) NOT NULL,
`passwordA` varchar(50) NOT NULL,
`emailA` varchar(50) NOT NULL,
PRIMARY KEY (`id`) )ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS `New`(
`id` int(65) NOT NULL auto_increment,
`nameJ` varchar(50) NOT NULL,
`usernameJ` varchar(50) NOT NULL,
`passwordJ` varchar(50) NOT NULL,
`emailJ` varchar(50) NOT NULL,
PRIMARY KEY (`id`)
)ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS `info`(
`id` int(65) NOT NULL auto_increment,
`job` varchar(50) NOT NULL,
PRIMARY KEY (`id`))ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

use hirelogin;
alter table info add column description varchar(500) not null; 



CREATE TABLE IF NOT EXISTS `choose` (
`id` int(65) NOT NULL auto_increment,
`Name` varchar(50) NOT NULL,
`jprofile` varchar(100) NOT NULL ,
PRIMARY KEY (`id`)

)ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

use hirelogin;

show tables;
describe info;
