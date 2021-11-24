/*
SQLyog v10.2 
MySQL - 5.5.5-10.1.21-MariaDB : Database - bookmall
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`bookmall` /*!40100 DEFAULT CHARACTER SET utf8 */;

/*Table structure for table `bookinfo` */

CREATE TABLE `bookinfo` (
  `isbn` varchar(13) NOT NULL,
  `title` varchar(200) NOT NULL,
  `author` text NOT NULL,
  `img` text NOT NULL,
  `stock` int(11) NOT NULL,
  `trade_price` int(11) NOT NULL,
  `retail_price` int(11) NOT NULL,
  `pub_date` date NOT NULL,
  `description` text NOT NULL,
  PRIMARY KEY (`isbn`),
  UNIQUE KEY `isbn` (`isbn`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `bookinfo` */

insert  into `bookinfo`(`isbn`,`title`,`author`,`img`,`stock`,`trade_price`,`retail_price`,`pub_date`,`description`) values ('2015620065151','网址编辑','dsds','/static/img/5.jpg',77,33,41,'2021-11-04','dsdsdsds'),('2020613225326','books1','sasas','/static/img/1.jpg',10,12,14,'2021-11-03','hello word'),('2020613225327','test2','jak','/static/img/2.jpg',22,22,12,'2021-11-11','21212dscsacscasc sa');

/*Table structure for table `cart` */

CREATE TABLE `cart` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `uid` int(11) DEFAULT NULL,
  `book_id` varchar(13) DEFAULT NULL,
  `quantity` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`),
  KEY `uid` (`uid`),
  KEY `book_id` (`book_id`),
  CONSTRAINT `cart_ibfk_1` FOREIGN KEY (`uid`) REFERENCES `user` (`id`),
  CONSTRAINT `cart_ibfk_2` FOREIGN KEY (`book_id`) REFERENCES `bookinfo` (`isbn`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8;

/*Data for the table `cart` */

insert  into `cart`(`id`,`uid`,`book_id`,`quantity`) values (12,1,'2020613225326',2),(14,1,'2020613225327',2);

/*Table structure for table `user` */

CREATE TABLE `user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(20) NOT NULL,
  `password` varchar(50) NOT NULL,
  `is_admin` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

/*Data for the table `user` */

insert  into `user`(`id`,`username`,`password`,`is_admin`) values (1,'customer1','p455w0rd',0),(2,'customer2','p455w0rd',0),(3,'admin','p455w0rd',1);

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
