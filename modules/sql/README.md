## Researchers

CREATE TABLE `Researchers` (
  `ID` int NOT NULL,
  `Name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `Avatar` varchar(255) DEFAULT NULL,
  `Title` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `HomePage` varchar(255) DEFAULT NULL,
  `University` varchar(255) DEFAULT NULL,
  `Lab` varchar(255) DEFAULT NULL,
  `Bio` varchar(1000) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `Signature` varchar(255) DEFAULT NULL,
  `DOB` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_bin DEFAULT '',
  `Address` varchar(255) DEFAULT NULL,
  `Email` varchar(255) DEFAULT NULL,
  `Mottos` json DEFAULT NULL,
  `ResearchInterest` json DEFAULT NULL,
  `Awards` json DEFAULT NULL,
  `Co_authors` json DEFAULT NULL,
  `Papers` json DEFAULT NULL,
  `Cited_graph` json DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

## user

CREATE TABLE `user` (
  `id` int(10) unsigned zerofill NOT NULL DEFAULT '0000000000',
  `password` varchar(255) DEFAULT NULL,
  `username` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
