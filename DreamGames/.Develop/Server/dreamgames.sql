/*
Navicat MySQL Data Transfer

Source Server         : 138.128.217.186
Source Server Version : 50173
Source Host           : 138.128.217.186:3306
Source Database       : dreamgames

Target Server Type    : MYSQL
Target Server Version : 50173
File Encoding         : 65001

Date: 2016-06-22 19:03:07
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `version`
-- ----------------------------
DROP TABLE IF EXISTS `version`;
CREATE TABLE `version` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `mainVersion` varchar(255) DEFAULT NULL,
  `buildVersion` int(11) DEFAULT NULL,
  `dateVersion` varchar(255) DEFAULT NULL,
  `versionName` varchar(255) DEFAULT NULL,
  `allowUpdate` tinyint(4) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=gbk;

