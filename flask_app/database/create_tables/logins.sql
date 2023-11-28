CREATE TABLE IF NOT EXISTS `logins` (
`SteamID`   varchar(64)    NOT NULL    COMMENT 'The Steam ID of the user',
`Username`  varchar(64)    NOT NULL        COMMENT 'The username of the user',
`Password` varchar(64)     NOT NULL        COMMENT 'The password of the user',
PRIMARY KEY (`SteamID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT 'User login information (Basic Login until OpenID)';