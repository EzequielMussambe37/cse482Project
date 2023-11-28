CREATE TABLE IF NOT EXISTS `preferences` (
`SteamID`   varchar(64)     NOT NULL        COMMENT 'User Steam ID',
`Tags`      varchar(256)    DEFAULT NULL    COMMENT 'Preferred Tags',
PRIMARY KEY(`SteamID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT 'Preferences of the user';