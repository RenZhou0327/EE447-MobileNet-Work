/*
 Navicat MySQL Data Transfer

 Source Server         : zr_local
 Source Server Type    : MySQL
 Source Server Version : 80021
 Source Host           : localhost:3306
 Source Schema         : scholar

 Target Server Type    : MySQL
 Target Server Version : 80021
 File Encoding         : 65001

 Date: 28/05/2021 07:34:45
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for researchers
-- ----------------------------
DROP TABLE IF EXISTS `researchers`;
CREATE TABLE `researchers`  (
  `ID` int NOT NULL,
  `Name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `Avatar` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `Title` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `HomePage` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `University` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `Lab` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `Bio` varchar(1000) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `Signature` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `DOB` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_bin NULL DEFAULT '',
  `Address` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `Email` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `Mottos` json NULL,
  `ResearchInterest` json NULL,
  `Awards` json NULL,
  `Co_authors` json NULL,
  `Papers` json NULL,
  `Cited_graph` json NULL,
  `Temperature` int NULL DEFAULT NULL,
  PRIMARY KEY (`ID`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of researchers
-- ----------------------------
INSERT INTO `researchers` VALUES (0, 'Quanshi Zhang', 'http://qszhang.com/files/photo.png', 'Associate Professor', 'http://qszhang.com/', 'Shanghai Jiao Tong University', 'John Hopcroft Center for Computer Science', 'Currently, I am an associate professor at the Shanghai Jiaotong University. Before that, I received the B.S. degree in machine intelligence at the Peking University, China, in 2009. I obtained the M.Eng. degree and the Ph.D. degree at University of Tokyo, in 2011 and 2014, respectively, under the supervision of Prof. Ryosuke Shibasaki.  In 2014, I became a postdoctoral associate at the University of California, Los Angeles, under the supervision of Song-Chun Zhu.', 'http://qszhang.com/files/zqs.jpg', '\r\n05 Sep 1986', NULL, 'zqs1022@sjtu.edu.cn', '{\"Mottos\": [\"Learn the hardcore knowledge is important\", \"My lectures would be useless if your future career is civil servants\", \"Do not cheat\"]}', '{\"ResearchInterest\": {\"robotics\": 10, \"data mining\": 10, \"computer vision\": 10, \"Interpretability\": 60, \"machine learning\": 10}}', '{\"Awards\": {\"Journal Reviewer\": \"../../static/main_style/img/uploads/awards/award-02.png\", \"Workshop Co-chair\": \"../../static/main_style/img/uploads/awards/award-01.png\"}}', '{\"Co_authors\": [{\"Co_authors_name\": \"Minglu Li (?????????)\", \"Co_authors_title_and_institution\": \"Professor of Computer Science, Shanghai Jiao Tong University\"}, {\"Co_authors_name\": \"Yanmin Zhu\", \"Co_authors_title_and_institution\": \"Professor of CSE Department, Shanghai Jiao Tong University\"}, {\"Co_authors_name\": \"Guandong Xu, PhD\", \"Co_authors_title_and_institution\": \"Professor in Data Science, University of Technology Sydney\"}, {\"Co_authors_name\": \"Guangtao Xue\", \"Co_authors_title_and_institution\": \"Professor of Computer Science, Shanghai Jiao Tong University\"}, {\"Co_authors_name\": \"Longbing Cao\", \"Co_authors_title_and_institution\": \"University of Technology Sydney, Australia\"}, {\"Co_authors_name\": \"Yan Yao\", \"Co_authors_title_and_institution\": \"Shanghai Jiao Tong University\"}, {\"Co_authors_name\": \"hongzi zhu\", \"Co_authors_title_and_institution\": \"Shanghai Jiao Tong University\"}, {\"Co_authors_name\": \"Fr??d??ric Le Mou??l\", \"Co_authors_title_and_institution\": \"Full Professor, University of Lyon / INSA Lyon, INRIA CITI Lab\"}, {\"Co_authors_name\": \"Linpeng HUANG\", \"Co_authors_title_and_institution\": \"Shanghai Jiao Tong University\"}, {\"Co_authors_name\": \"Min-You Wu\", \"Co_authors_title_and_institution\": \"Computer Science, Shanghai Jiaotong University\"}, {\"Co_authors_name\": \"Jinjun Chen\", \"Co_authors_title_and_institution\": \"Professor and Deputy Institute Director, Swinburne University of Technology\"}, {\"Co_authors_name\": \"Yanchun Zhang\", \"Co_authors_title_and_institution\": \"Victoria University\"}]}', '{\"Papers\": [{\"Paper_fig\": \"http://qszhang.com/files/icnn/top.jpg\", \"Paper_pdf\": \"https://arxiv.org/abs/1710.00935\", \"Paper_code\": \"https://github.com/zqs1022/interpretableCNN/\", \"Paper_name\": \"Interpretable Convolutional Neural Networks\", \"Paper_authors\": \"Quanshi Zhang, Ying Nian Wu, and Song-Chun Zhu\", \"Paper_cited_by\": \"26\", \"Paper_conference_and_year\": \"CVPR 2018\"}, {\"Paper_fig\": \"http://qszhang.com/files/explanatoryGraph/top.jpg\", \"Paper_pdf\": \"https://arxiv.org/abs/1708.01785\", \"Paper_code\": \"https://github.com/zqs1022/explanatoryGraph\", \"Paper_name\": \"Interpreting CNN Knowledge via an Explanatory Graph\", \"Paper_authors\": \"Quanshi Zhang, Ruiming Cao, Feng Shi, Ying Nian Wu, and Song-Chun Zhu\", \"Paper_cited_by\": \"32\", \"Paper_conference_and_year\": \"AAAI 2018\"}, {\"Paper_fig\": \"http://qszhang.com/files/transplant/transplant.jpg\", \"Paper_pdf\": \"https://arxiv.org/abs/1804.10272\", \"Paper_code\": \"\", \"Paper_name\": \"Network Transplanting\", \"Paper_authors\": \"Quanshi Zhang, Yu Yang, Ying Nian Wu, and Song-Chun Zhu\", \"Paper_cited_by\": \"18\", \"Paper_conference_and_year\": \"arXiv:1804.10272, 2018\"}]}', '{\"Cited_graph\": [\"2012\", \"2013\", \"2014\", \"2015\", \"2016\", \"2017\", \"2018\", \"2019\", \"2020\", \"2021\", \"3\", \"6\", \"6\", \"7\", \"14\", \"11\", \"17\", \"33\", \"43\", \"18\"]}', 10);
INSERT INTO `researchers` VALUES (1, 'Haiming Jin', 'https://jhc.sjtu.edu.cn/public/home/haimingjin/haimingjin.jpg', 'tenure-track assistant professor', NULL, NULL, NULL, 'cadcca', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 8);
INSERT INTO `researchers` VALUES (2, 'Xinbing Wang', 'https://www.cs.sjtu.edu.cn/Management/Upload/[User]9f2d943dc58c493fbe6d4c553abfdc16/201912293845931Csn4Z.jpg', 'Professor', NULL, NULL, NULL, 'cacadcsd', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 0);

SET FOREIGN_KEY_CHECKS = 1;
