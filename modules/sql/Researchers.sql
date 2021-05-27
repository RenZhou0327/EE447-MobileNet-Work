/*
 Navicat Premium Data Transfer

 Source Server         : tecent_cloud
 Source Server Type    : MySQL
 Source Server Version : 80023
 Source Host           : 127.0.0.1:3306
 Source Schema         : scholar

 Target Server Type    : MySQL
 Target Server Version : 80023
 File Encoding         : 65001

 Date: 27/05/2021 16:38:25
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for Researchers
-- ----------------------------
DROP TABLE IF EXISTS `Researchers`;
CREATE TABLE `Researchers`  (
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
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of Researchers
-- ----------------------------
INSERT INTO `Researchers` VALUES (
'159',
'Quanshi Zhang', 'http://qszhang.com/files/photo.png', 'Associate Professor', 'http://qszhang.com/', 'Shanghai Jiao Tong University', 'John Hopcroft Center for Computer Science', 'Currently, I am an associate professor at the Shanghai Jiaotong University. Before that, I received the B.S. degree in machine intelligence at the Peking University, China, in 2009. I obtained the M.Eng. degree and the Ph.D. degree at University of Tokyo, in 2011 and 2014, respectively, under the supervision of Prof. Ryosuke Shibasaki.  In 2014, I became a postdoctoral associate at the University of California, Los Angeles, under the supervision of Song-Chun Zhu.', 'http://qszhang.com/files/zqs.jpg', '\r\n05 Sep 1986', NULL, 'zqs1022@sjtu.edu.cn',
'{\"Mottos\": [\"Learn the hardcore knowledge is important\", \"My lectures would be useless if your future career is civil servants\", \"Do not cheat\"]}', '{\"ResearchInterest\": {\"robotics\": 10, \"data mining\": 10, \"computer vision\": 10, \"Interpretability\": 60, \"machine learning\": 10}}',
'{\"Awards\": {\"Journal Reviewer\": \"../../static/main_style/img/uploads/awards/award-02.png\", \"Workshop Co-chair\": \"../../static/main_style/img/uploads/awards/award-01.png\"}}',
'{\"Co_authors\": [{\"Co_authors_name\": \"Minglu Li (李明禄)\", \"Co_authors_title_and_institution\": \"Professor of Computer Science, Shanghai Jiao Tong University\"}, {\"Co_authors_name\": \"Yanmin Zhu\", \"Co_authors_title_and_institution\": \"Professor of CSE Department, Shanghai Jiao Tong University\"}, {\"Co_authors_name\": \"Guandong Xu, PhD\", \"Co_authors_title_and_institution\": \"Professor in Data Science, University of Technology Sydney\"}, {\"Co_authors_name\": \"Guangtao Xue\", \"Co_authors_title_and_institution\": \"Professor of Computer Science, Shanghai Jiao Tong University\"}, {\"Co_authors_name\": \"Longbing Cao\", \"Co_authors_title_and_institution\": \"University of Technology Sydney, Australia\"}, {\"Co_authors_name\": \"Yan Yao\", \"Co_authors_title_and_institution\": \"Shanghai Jiao Tong University\"}, {\"Co_authors_name\": \"hongzi zhu\", \"Co_authors_title_and_institution\": \"Shanghai Jiao Tong University\"}, {\"Co_authors_name\": \"Frédéric Le Mouël\", \"Co_authors_title_and_institution\": \"Full Professor, University of Lyon / INSA Lyon, INRIA CITI Lab\"}, {\"Co_authors_name\": \"Linpeng HUANG\", \"Co_authors_title_and_institution\": \"Shanghai Jiao Tong University\"}, {\"Co_authors_name\": \"Min-You Wu\", \"Co_authors_title_and_institution\": \"Computer Science, Shanghai Jiaotong University\"}, {\"Co_authors_name\": \"Jinjun Chen\", \"Co_authors_title_and_institution\": \"Professor and Deputy Institute Director, Swinburne University of Technology\"}, {\"Co_authors_name\": \"Yanchun Zhang\", \"Co_authors_title_and_institution\": \"Victoria University\"}]}',
'{\"Papers\": [{\"Paper_fig\": \"http://qszhang.com/files/icnn/top.jpg\", \"Paper_pdf\": \"https://arxiv.org/abs/1710.00935\", \"Paper_code\": \"https://github.com/zqs1022/interpretableCNN/\", \"Paper_name\": \"Interpretable Convolutional Neural Networks\", \"Paper_authors\": \"Quanshi Zhang, Ying Nian Wu, and Song-Chun Zhu\", \"Paper_cited_by\": \"26\", \"Paper_conference_and_year\": \"CVPR 2018\"}, {\"Paper_fig\": \"http://qszhang.com/files/explanatoryGraph/top.jpg\", \"Paper_pdf\": \"https://arxiv.org/abs/1708.01785\", \"Paper_code\": \"https://github.com/zqs1022/explanatoryGraph\", \"Paper_name\": \"Interpreting CNN Knowledge via an Explanatory Graph\", \"Paper_authors\": \"Quanshi Zhang, Ruiming Cao, Feng Shi, Ying Nian Wu, and Song-Chun Zhu\", \"Paper_cited_by\": \"32\", \"Paper_conference_and_year\": \"AAAI 2018\"}, {\"Paper_fig\": \"http://qszhang.com/files/transplant/transplant.jpg\", \"Paper_pdf\": \"https://arxiv.org/abs/1804.10272\", \"Paper_code\": \"\", \"Paper_name\": \"Network Transplanting\", \"Paper_authors\": \"Quanshi Zhang, Yu Yang, Ying Nian Wu, and Song-Chun Zhu\", \"Paper_cited_by\": \"18\", \"Paper_conference_and_year\": \"arXiv:1804.10272, 2018\"}]}',
'{\"Cited_graph\": [\"2012\", \"2013\", \"2014\", \"2015\", \"2016\", \"2017\", \"2018\", \"2019\", \"2020\", \"2021\", \"3\", \"6\", \"6\", \"7\", \"14\", \"11\", \"17\", \"33\", \"43\", \"18\"]}');

[{"Paper_name": "Social recommendation with strong and weak ties", "Paper_authors": "X Wang, W Lu, M Ester, C Wang, C Chen", "Paper_conference_and_year": "Proceedings of the 25th ACM International on Conference on Information and\u00a0\u2026, 2016", "Paper_cited_by": "101"}, {"Paper_name": "Friend recommendation with content spread enhancement in social networks", "Paper_authors": "Z Yu, C Wang, J Bu, X Wang, Y Wu, C Chen", "Paper_conference_and_year": "Information Sciences 309, 102-118, 2015", "Paper_cited_by": "83"}, {"Paper_name": "Learning personalized preference of strong and weak ties for social recommendation", "Paper_authors": "X Wang, SCH Hoi, M Ester, J Bu, C Chen", "Paper_conference_and_year": "Proceedings of the 26th International Conference on World Wide Web (WWW 2017\u00a0\u2026, 2017", "Paper_cited_by": "62"}, {"Paper_name": "Disentangled graph convolutional networks", "Paper_authors": "J Ma, P Cui, K Kuang, X Wang, W Zhu", "Paper_conference_and_year": "International Conference on Machine Learning, 4212-4221, 2019", "Paper_cited_by": "60"}, {"Paper_name": "Semi-supervised clustering in attributed heterogeneous information networks", "Paper_authors": "X Li, Y Wu, M Ester, B Kao, X Wang, Y Zheng", "Paper_conference_and_year": "Proceedings of the 26th International Conference on World Wide Web, 1621-1629, 2017", "Paper_cited_by": "47"}, {"Paper_name": "Recommending Groups to Users Using User-Group Engagement and Time-Dependent Matrix Factorization.", "Paper_authors": "X Wang, R Donaldson, C Nell, P Gorniak, M Ester, J Bu", "Paper_conference_and_year": "Proceedings of the Thirtieth AAAI Conference on Artificial Intelligence\u00a0\u2026, 2016", "Paper_cited_by": "44"}, {"Paper_name": "Interactive Social Recommendation", "Paper_authors": "X Wang, SCH Hoi, C Liu, M Ester", "Paper_conference_and_year": "Proceedings of the 2017 ACM on Conference on Information and Knowledge\u00a0\u2026, 2017", "Paper_cited_by": "18"}, {"Paper_name": "Prre: Personalized relation ranking embedding for attributed networks", "Paper_authors": "S Zhou, H Yang, X Wang, J Bu, M Ester, P Yu, J Zhang, C Wang", "Paper_conference_and_year": "Proceedings of the 27th ACM International Conference on Information and\u00a0\u2026, 2018", "Paper_cited_by": "15"}, {"Paper_name": "Discrete Social Recommendation", "Paper_authors": "C Liu, X Wang, T Lu, W Zhu, J Sun, SCH Hoi", "Paper_conference_and_year": "The Thirty-Third AAAI Conference on Artificial Intelligence (AAAI-19), 2019", "Paper_cited_by": "14"}, {"Paper_name": "Social recommendation with optimal limited attention", "Paper_authors": "X Wang, W Zhu, C Liu", "Paper_conference_and_year": "Proceedings of the 25th ACM SIGKDD International Conference on Knowledge\u00a0\u2026, 2019", "Paper_cited_by": "12"}, {"Paper_name": "Compositional Coding for Collaborative Filtering", "Paper_authors": "C Liu, T Lu, X Wang, Z Cheng, J Sun, CHS Hoi", "Paper_conference_and_year": "Proceedings of the 42nd International ACM SIGIR Conference on Research and\u00a0\u2026, 2019", "Paper_cited_by": "9"}, {"Paper_name": "Hahe: Hierarchical attentive heterogeneous information network embedding", "Paper_authors": "S Zhou, J Bu, X Wang, J Chen, C Wang", "Paper_conference_and_year": "arXiv preprint arXiv:1902.01475, 2019", "Paper_cited_by": "8"}, {"Paper_name": "Disentangled Self-Supervision in Sequential Recommenders", "Paper_authors": "J Ma, C Zhou, H Yang, P Cui, X Wang, W Zhu", "Paper_conference_and_year": "Proceedings of the 26th ACM SIGKDD International Conference on Knowledge\u00a0\u2026, 2020", "Paper_cited_by": "7"}, {"Paper_name": "Multimedia Intelligence: When Multimedia Meets Artificial Intelligence", "Paper_authors": "W Zhu, X Wang, W Gao", "Paper_conference_and_year": "IEEE Transactions on Multimedia, 2020", "Paper_cited_by": "6"}, {"Paper_name": "Perceptual visual reasoning with knowledge propagation", "Paper_authors": "G Li, X Wang, W Zhu", "Paper_conference_and_year": "Proceedings of the 27th ACM International Conference on Multimedia, 530-538, 2019", "Paper_cited_by": "5"}, {"Paper_name": "Cross-modal dual learning for sentence-to-video generation", "Paper_authors": "Y Liu, X Wang, Y Yuan, W Zhu", "Paper_conference_and_year": "Proceedings of the 27th ACM International Conference on Multimedia, 1239-1247, 2019", "Paper_cited_by": "5"}, {"Paper_name": "MEmoR: A Dataset for Multimodal Emotion Reasoning in Videos", "Paper_authors": "G Shen, X Wang, X Duan, H Li, W Zhu", "Paper_conference_and_year": "Proceedings of the 28th ACM International Conference on Multimedia, 493-502, 2020", "Paper_cited_by": "3"}, {"Paper_name": "Boosting Visual Question Answering with Context-aware Knowledge Aggregation", "Paper_authors": "G Li, X Wang, W Zhu", "Paper_conference_and_year": "Proceedings of the 28th ACM International Conference on Multimedia, 1227-1235, 2020", "Paper_cited_by": "3"}, {"Paper_name": "A Survey on Curriculum Learning", "Paper_authors": "X Wang, Y Chen, W Zhu", "Paper_conference_and_year": "IEEE Transactions on Pattern Analysis and Machine Intelligence, 2021", "Paper_cited_by": "2"}, {"Paper_name": "Hardware-Aware Transformable Architecture Search with Efficient Search Space", "Paper_authors": "Y Jiang, X Wang, W Zhu", "Paper_conference_and_year": "2020 IEEE International Conference on Multimedia and Expo (ICME), 1-6, 2020", "Paper_cited_by": "2"}]

INSERT INTO `Researchers` VALUES (160, 'Haiming Jin', 'https://jhc.sjtu.edu.cn/public/home/haimingjin/haimingjin.jpg', 'tenure-track assistant professor', NULL, NULL, NULL, 'cadcca', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 8);
INSERT INTO `Researchers` VALUES (161, 'Xinbing Wang', 'https://bkimg.cdn.bcebos.com/pic/8b82b9014a90f603dc1be7be3112b31bb151eda4?x-bce-process=image/resize,m_lfit,w_268,limit_1/format,f_jpg', 'Professor', NULL, NULL, NULL, 'cacadcsd', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 0);

SET FOREIGN_KEY_CHECKS = 1;
