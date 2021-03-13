create database myData default character set utf8;

DROP TABLE IF EXISTS person;
CREATE TABLE IF NOT EXISTS person (
  id int(11) NOT NULL AUTO_INCREMENT,
  cin int(11) NOT NULL,
  nom varchar(40) NOT NULL,
  prenom varchar(40) NOT NULL,
  tel varchar(40) NOT NULL,
  email varchar(80) NOT NULL,
  PRIMARY KEY (id)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;



INSERT INTO person (id, cin, nom, prenom, tel, email) VALUES
(3, 1, 'zakaria', 'chafai', '0263542653', 'email@example.com'),
(4, 2, 'yassine', 'kamal', '098737874', 'email@expamle.com'),
(5, 3, 'salah', 'mobarik', '09878683', 'salah@gmail.com'),
(6, 6666, 'soufiane', 'ouamassi', '11111', 'souf@example.com'),
(7, 55, 'ss', 'tt', '333', 'rr'),
(8, 88, 'ss', 'tt', '333', 'rr'),
(9, 0, 'aaa', 'qqq', 'aaa', 'aaa'),
(10, 8789, 'boussidi', 'jamal', '7777', 'sss'),
(11, 44, 'mimouni', 'jawad', '8888', 'ooiu'),
(12, 22, 'attaa', 'mohamed', '888', 'qqq');
COMMIT;
