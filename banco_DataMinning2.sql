-- phpMyAdmin SQL Dump
-- version 4.7.9
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: 25-Jun-2018 às 01:50
-- Versão do servidor: 5.7.21
-- PHP Version: 7.0.29

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `t1_beta`
--

-- --------------------------------------------------------

--
-- Estrutura da tabela `filmes2`
--

DROP TABLE IF EXISTS `filmes2`;
CREATE TABLE IF NOT EXISTS `filmes2` (
  `urif` varchar(100) NOT NULL,
  `filme` varchar(100) NOT NULL,
  `imdb_rating` int(10) NOT NULL,
  `metacritic_rating` int(10) NOT NULL,
  `rottentomatoes_rating` int(10) NOT NULL,
  `ww_income` int(100) NOT NULL,
  `box_income` int(100) NOT NULL,
  `budget` int(100) NOT NULL,
  `franquia` varchar(10) NOT NULL,
  `ano` int(4) NOT NULL,
  PRIMARY KEY (`urif`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Extraindo dados da tabela `filmes2`
--

INSERT INTO `filmes2` (`urif`, `filme`, `imdb_rating`, `metacritic_rating`, `rottentomatoes_rating`, `ww_income`, `box_income`, `budget`, `franquia`, `ano`) VALUES
('http://www.imdb.com/title/tt0198781/', 'Monsters, Inc.', 81, 78, 96, 562816256, 34034168, 115000000, 'CONTROLE', 2001),
('http://www.imdb.com/title/tt0209144/', 'Memento', 85, 80, 92, 39723096, 23844220, 9000000, 'CONTROLE', 2000),
('http://www.imdb.com/title/tt0245429/', 'Spirited Away', 86, 96, 97, 274925095, 9855615, 15000000, 'CONTROLE', 2001),
('http://www.imdb.com/title/tt0253474/', 'The Pianist', 85, 85, 95, 120072577, 32519322, 35000000, 'CONTROLE', 2002),
('http://www.imdb.com/title/tt0266543/', 'Finding Nemo', 81, 90, 99, 940335536, 380529370, 94000000, 'CONTROLE', 2003),
('http://www.imdb.com/title/tt0107290/', 'Jurassic Park', 81, 68, 92, 920100000, 45299680, 63000000, 'CONTROLE', 1993),
('http://www.imdb.com/title/tt0109830/', 'Forrest Gump', 88, 82, 72, 677945399, 330000000, 55000000, 'CONTROLE', 1994),
('http://www.imdb.com/title/tt0110357/', 'The Lion King', 85, 83, 93, 987483777, 94240635, 45000000, 'CONTROLE', 1994),
('http://www.imdb.com/title/tt0120737/', 'The Lord of the Rings: The Fellowship of the Ring', 88, 92, 91, 871368364, 314000000, 93000000, 'CONTROLE', 2001),
('http://www.imdb.com/title/tt0167260/', 'The Lord of the Rings: The Return of the King', 89, 94, 93, 1118888979, 364000000, 94000000, 'CONTROLE', 2003),
('http://www.imdb.com/title/tt0167261/', 'The Lord of the Rings: The Two Towers', 87, 87, 95, 926287400, 339700000, 79000000, 'CONTROLE', 2002),
('http://www.imdb.com/title/tt0103064/', 'Terminator 2', 85, 75, 92, 520000000, 198116802, 100000000, 'CONTROLE', 1991),
('http://www.imdb.com/title/tt0080684/', 'Star Wars: Episode V - The Empire Strikes Back', 88, 82, 95, 538400000, 4548170, 18000000, 'CONTROLE', 1980),
('http://www.imdb.com/title/tt0086250/', 'Scarface', 83, 65, 82, 65884703, 656161, 25000000, 'CONTROLE', 1983),
('http://www.imdb.com/title/tt0088763/', 'Back to the Future', 85, 86, 96, 381109762, 2925880, 19000000, 'CONTROLE', 1985),
('http://www.imdb.com/title/tt0319061/', 'Big Fish', 80, 58, 76, 122919055, 66257002, 70000000, 'CONTROLE', 2003),
('http://www.imdb.com/title/tt0325980/', 'Pirates of the Caribbean: The Curse of the Black Pearl', 80, 63, 79, 655011224, 305343252, 140000000, 'CONTROLE', 2003),
('http://www.imdb.com/title/tt0338013/', 'Eternal Sunshine of the Spotless Mind', 83, 89, 93, 72258126, 34126138, 20000000, 'CONTROLE', 2004),
('http://www.imdb.com/title/tt0361748/', 'Inglourious Basterds', 83, 69, 88, 319131050, 120523073, 70000000, 'CONTROLE', 2009),
('http://www.imdb.com/title/tt0372784/', 'Batman Begins', 83, 70, 84, 374218673, 204100000, 150000000, 'CONTROLE', 2005),
('https://www.imdb.com/title/tt0371746/', 'Iron Man', 79, 79, 94, 585174222, 318298180, 140000000, 'MARVEL', 2008),
('http://www.imdb.com/title/tt0382932/', 'Ratatouille', 80, 96, 96, 623722818, 112408657, 150000000, 'CONTROLE', 2007),
('https://www.imdb.com/title/tt0458339/', 'Captain America: The First Avenger', 69, 66, 79, 370569774, 176636816, 140000000, 'MARVEL', 2011),
('https://www.imdb.com/title/tt0478970/', 'Ant-Man', 73, 64, 82, 519311965, 138002223, 130000000, 'MARVEL', 2015),
('http://www.imdb.com/title/tt0405094/', 'The Lives of Others', 84, 89, 92, 70000000, 11200000, 2000000, 'CONTROLE', 2006),
('https://www.imdb.com/title/tt0800080/', 'The Incredible Hulk', 68, 61, 67, 163712074, 134518390, 150000000, 'MARVEL', 2008),
('https://www.imdb.com/title/tt0800369/', 'Thor', 70, 57, 77, 449326618, 181015141, 150000000, 'MARVEL', 2011),
('http://www.imdb.com/title/tt0434409/', 'V for Vendetta', 82, 62, 73, 132511035, 70500000, 54000000, 'CONTROLE', 2005),
('https://www.imdb.com/title/tt0848228/', 'The Avengers', 81, 69, 92, 1519557910, 623279547, 220000000, 'MARVEL', 2012),
('http://www.imdb.com/title/tt0435761/', 'Toy Story 3', 83, 92, 99, 1066969703, 414984497, 200000000, 'CONTROLE', 2010),
('https://www.imdb.com/title/tt1211837/', 'Doctor Strange', 75, 72, 89, 677718395, 232630718, 166000000, 'MARVEL', 2016),
('https://www.imdb.com/title/tt1228705/', 'Iron Man 2', 70, 57, 73, 623933331, 312057433, 200000000, 'MARVEL', 2010),
('http://www.imdb.com/title/tt0440963/', 'The Bourne Ultimatum', 80, 85, 93, 442824138, 227400000, 70000000, 'CONTROLE', 2007),
('https://www.imdb.com/title/tt1300854/', 'Iron Man 3', 72, 62, 80, 1215439994, 408992272, 200000000, 'MARVEL', 2013),
('http://www.imdb.com/title/tt0454876/', 'Life of Pi', 79, 79, 87, 609016565, 103500000, 120000000, 'CONTROLE', 2012),
('https://www.imdb.com/title/tt1825683/', 'Black Panther', 75, 88, 97, 1343859226, 501105037, 200000000, 'MARVEL', 2018),
('http://www.imdb.com/title/tt0468569/', 'The Dark Knight', 90, 82, 94, 1004558444, 533316061, 185000000, 'CONTROLE', 2008),
('https://www.imdb.com/title/tt1843866/', 'Captain America: The Winter Soldier', 78, 70, 89, 714766572, 228636083, 170000000, 'MARVEL', 2014),
('http://www.imdb.com/title/tt0482571/', 'The Prestige', 85, 66, 75, 109676311, 53100000, 40000000, 'CONTROLE', 2006),
('https://www.imdb.com/title/tt1981115/', 'Thor: The Dark World', 70, 54, 66, 644571402, 206360018, 170000000, 'MARVEL', 2013),
('http://www.imdb.com/title/tt0758758/', 'Into the Wild', 81, 73, 82, 56255142, 18173360, 15000000, 'CONTROLE', 2007),
('https://www.imdb.com/title/tt2015381/', 'Guardians of the Galaxy', 81, 76, 91, 773328629, 270592504, 170000000, 'MARVEL', 2014),
('https://www.imdb.com/title/tt2250912/', 'Spider-Man: Homecoming', 75, 73, 92, 880166924, 334166825, 175000000, 'MARVEL', 2017),
('http://www.imdb.com/title/tt0796366/', 'Star Trek', 80, 82, 94, 385680446, 257704099, 150000000, 'CONTROLE', 2009),
('https://www.imdb.com/title/tt2395427/', 'Avengers: Age of Ultron', 74, 66, 75, 1405403694, 429113729, 280000000, 'MARVEL', 2015),
('http://www.imdb.com/title/tt0848228/', 'The Avengers', 81, 69, 92, 1519557910, 623279547, 220000000, 'CONTROLE', 2012),
('https://www.imdb.com/title/tt3498820/', 'Captain America: Civil War', 78, 75, 91, 1153304495, 408080554, 240000000, 'MARVEL', 2016),
('http://www.imdb.com/title/tt0892769/', 'How to Train Your Dragon', 81, 74, 98, 494878759, 216900000, 165000000, 'CONTROLE', 2010),
('https://www.imdb.com/title/tt3501632/', 'Thor: Ragnarok', 79, 74, 92, 853977126, 314971245, 180000000, 'MARVEL', 2017),
('https://www.imdb.com/title/tt3896198/', 'Guardians of the Galaxy Vol. 2', 77, 67, 83, 863756051, 389804217, 200000000, 'MARVEL', 2017),
('http://www.imdb.com/title/tt0903624/', 'The Hobbit: An Unexpected Journey', 79, 58, 65, 1021103568, 303001229, 250000000, 'CONTROLE', 2012),
('https://www.imdb.com/title/tt4154756/', 'Avengers: Infinity War', 88, 68, 83, 2004137049, 658903950, 300000000, 'MARVEL', 2018),
('http://www.imdb.com/title/tt0910970/', 'WALLÂ·E', 84, 95, 96, 521311860, 223749872, 180000000, 'CONTROLE', 2008),
('https://www.imdb.com/title/tt0372784/', 'Batman Begins', 83, 70, 84, 374218673, 204100000, 150000000, 'DC', 2005),
('https://www.imdb.com/title/tt0451279/', 'Wonder Woman', 75, 76, 92, 821847012, 412400625, 149000000, 'DC', 2017),
('http://www.imdb.com/title/tt1010048/', 'Slumdog Millionaire', 80, 86, 91, 377910544, 141243551, 15000000, 'CONTROLE', 2008),
('https://www.imdb.com/title/tt0468569/', 'The Dark Knight', 90, 82, 94, 1004558444, 533316061, 185000000, 'DC', 2008),
('http://www.imdb.com/title/tt1049413/', 'Up', 83, 88, 98, 735099082, 292979556, 175000000, 'CONTROLE', 2009),
('https://www.imdb.com/title/tt0770828/', 'Man of Steel', 71, 55, 55, 662845518, 291021565, 225000000, 'DC', 2013),
('https://www.imdb.com/title/tt0974015/', 'Justice League', 67, 45, 40, 657924295, 227032490, 500000000, 'DC', 2017),
('http://www.imdb.com/title/tt1201607/', 'Harry Potter and the Deathly Hallows: Part 2', 81, 87, 96, 1342000000, 381000185, 125000000, 'CONTROLE', 2011),
('https://www.imdb.com/title/tt1345836/', 'The Dark Knight Rises', 84, 78, 87, 1084939099, 448130642, 250000000, 'DC', 2012),
('http://www.imdb.com/title/tt1205489/', 'Gran Torino', 81, 72, 80, 269958228, 148055047, 33000000, 'CONTROLE', 2008),
('https://www.imdb.com/title/tt1386697/', 'Suicide Squad', 61, 40, 27, 745600054, 325021779, 176000000, 'DC', 2016),
('https://www.imdb.com/title/tt2975590/', 'Batman v Superman: Dawn of Justice', 66, 44, 27, 873260194, 293792936, 250000000, 'DC', 2016),
('http://www.imdb.com/title/tt1345836/', 'The Dark Knight Rises', 84, 78, 87, 1084939099, 448130642, 250000000, 'CONTROLE', 2012),
('http://www.imdb.com/title/tt1375666/', 'Inception', 88, 74, 86, 825532764, 292568851, 160000000, 'CONTROLE', 2010),
('http://www.imdb.com/title/tt1659337/', 'The Perks of Being a Wallflower', 80, 67, 86, 33400000, 14900000, 13000000, 'CONTROLE', 2012),
('http://www.imdb.com/title/tt1675434/', 'The Intouchables', 85, 57, 74, 426480871, 13179837, 13000000, 'CONTROLE', 2011),
('http://www.imdb.com/title/tt1853728/', 'Django Unchained', 84, 81, 87, 425368238, 162804648, 100000000, 'CONTROLE', 2012),
('http://www.imdb.com/title/tt0062622/', '2001: A Space Odyssey', 83, 82, 92, 68700000, 135620, 10500000, 'CONTROLE', 1968);

-- --------------------------------------------------------

--
-- Estrutura da tabela `filmes_controle`
--

DROP TABLE IF EXISTS `filmes_controle`;
CREATE TABLE IF NOT EXISTS `filmes_controle` (
  `urif` varchar(100) NOT NULL,
  PRIMARY KEY (`urif`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Extraindo dados da tabela `filmes_controle`
--

INSERT INTO `filmes_controle` (`urif`) VALUES
('http://www.imdb.com/title/tt0033467/'),
('http://www.imdb.com/title/tt0050083/'),
('http://www.imdb.com/title/tt0050825/'),
('http://www.imdb.com/title/tt0052357/'),
('http://www.imdb.com/title/tt0054215/'),
('http://www.imdb.com/title/tt0057012/'),
('http://www.imdb.com/title/tt0060196/'),
('http://www.imdb.com/title/tt0062622/'),
('http://www.imdb.com/title/tt0066921/'),
('http://www.imdb.com/title/tt0068646/'),
('http://www.imdb.com/title/tt0070047/'),
('http://www.imdb.com/title/tt0070511/'),
('http://www.imdb.com/title/tt0071562/'),
('http://www.imdb.com/title/tt0071853/'),
('http://www.imdb.com/title/tt0075148/'),
('http://www.imdb.com/title/tt0075314/'),
('http://www.imdb.com/title/tt0076759/'),
('http://www.imdb.com/title/tt0077416/'),
('http://www.imdb.com/title/tt0078748/'),
('http://www.imdb.com/title/tt0080684/'),
('http://www.imdb.com/title/tt0083658/'),
('http://www.imdb.com/title/tt0086190/'),
('http://www.imdb.com/title/tt0086250/'),
('http://www.imdb.com/title/tt0086879/'),
('http://www.imdb.com/title/tt0088763/'),
('http://www.imdb.com/title/tt0090605/'),
('http://www.imdb.com/title/tt0093058/'),
('http://www.imdb.com/title/tt0095016/'),
('http://www.imdb.com/title/tt0095765/'),
('http://www.imdb.com/title/tt0096283/'),
('http://www.imdb.com/title/tt0097576/'),
('http://www.imdb.com/title/tt0099685/'),
('http://www.imdb.com/title/tt0102926/'),
('http://www.imdb.com/title/tt0103064/'),
('http://www.imdb.com/title/tt0107290/'),
('http://www.imdb.com/title/tt0108052/'),
('http://www.imdb.com/title/tt0109830/'),
('http://www.imdb.com/title/tt0110357/'),
('http://www.imdb.com/title/tt0110413/'),
('http://www.imdb.com/title/tt0110912/'),
('http://www.imdb.com/title/tt0111161/'),
('http://www.imdb.com/title/tt0112573/'),
('http://www.imdb.com/title/tt0114369/'),
('http://www.imdb.com/title/tt0114709/'),
('http://www.imdb.com/title/tt0114814/'),
('http://www.imdb.com/title/tt0120382/'),
('http://www.imdb.com/title/tt0120586/'),
('http://www.imdb.com/title/tt0120689/'),
('http://www.imdb.com/title/tt0120737/'),
('http://www.imdb.com/title/tt0133093/'),
('http://www.imdb.com/title/tt0137523/'),
('http://www.imdb.com/title/tt0167260/'),
('http://www.imdb.com/title/tt0167261/'),
('http://www.imdb.com/title/tt0167404/'),
('http://www.imdb.com/title/tt0172495/'),
('http://www.imdb.com/title/tt0198781/'),
('http://www.imdb.com/title/tt0209144/'),
('http://www.imdb.com/title/tt0211915/'),
('http://www.imdb.com/title/tt0245429/'),
('http://www.imdb.com/title/tt0246578/'),
('http://www.imdb.com/title/tt0253474/'),
('http://www.imdb.com/title/tt0266543/'),
('http://www.imdb.com/title/tt0266697/'),
('http://www.imdb.com/title/tt0317248/'),
('http://www.imdb.com/title/tt0319061/'),
('http://www.imdb.com/title/tt0325980/'),
('http://www.imdb.com/title/tt0338013/'),
('http://www.imdb.com/title/tt0361748/'),
('http://www.imdb.com/title/tt0372784/'),
('http://www.imdb.com/title/tt0382932/'),
('http://www.imdb.com/title/tt0401792/'),
('http://www.imdb.com/title/tt0405094/'),
('http://www.imdb.com/title/tt0434409/'),
('http://www.imdb.com/title/tt0435761/'),
('http://www.imdb.com/title/tt0440963/'),
('http://www.imdb.com/title/tt0454876/'),
('http://www.imdb.com/title/tt0468569/'),
('http://www.imdb.com/title/tt0482571/'),
('http://www.imdb.com/title/tt0758758/'),
('http://www.imdb.com/title/tt0796366/'),
('http://www.imdb.com/title/tt0848228/'),
('http://www.imdb.com/title/tt0892769/'),
('http://www.imdb.com/title/tt0903624/'),
('http://www.imdb.com/title/tt0910970/'),
('http://www.imdb.com/title/tt1010048/'),
('http://www.imdb.com/title/tt1049413/'),
('http://www.imdb.com/title/tt1201607/'),
('http://www.imdb.com/title/tt1205489/'),
('http://www.imdb.com/title/tt1220719/'),
('http://www.imdb.com/title/tt1345836/'),
('http://www.imdb.com/title/tt1375666/'),
('http://www.imdb.com/title/tt1659337/'),
('http://www.imdb.com/title/tt1675434/'),
('http://www.imdb.com/title/tt1853728/');

-- --------------------------------------------------------

--
-- Estrutura da tabela `filmes_dc`
--

DROP TABLE IF EXISTS `filmes_dc`;
CREATE TABLE IF NOT EXISTS `filmes_dc` (
  `urif` varchar(100) NOT NULL,
  PRIMARY KEY (`urif`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Extraindo dados da tabela `filmes_dc`
--

INSERT INTO `filmes_dc` (`urif`) VALUES
('https://www.imdb.com/title/tt0372784/'),
('https://www.imdb.com/title/tt0451279/'),
('https://www.imdb.com/title/tt0468569/'),
('https://www.imdb.com/title/tt0770828/'),
('https://www.imdb.com/title/tt0974015/'),
('https://www.imdb.com/title/tt1345836/'),
('https://www.imdb.com/title/tt1386697/'),
('https://www.imdb.com/title/tt2975590/');

-- --------------------------------------------------------

--
-- Estrutura da tabela `filmes_m`
--

DROP TABLE IF EXISTS `filmes_m`;
CREATE TABLE IF NOT EXISTS `filmes_m` (
  `urif` varchar(100) NOT NULL,
  PRIMARY KEY (`urif`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Extraindo dados da tabela `filmes_m`
--

INSERT INTO `filmes_m` (`urif`) VALUES
('https://www.imdb.com/title/tt0371746/'),
('https://www.imdb.com/title/tt0458339/'),
('https://www.imdb.com/title/tt0478970/'),
('https://www.imdb.com/title/tt0800080/'),
('https://www.imdb.com/title/tt0800369/'),
('https://www.imdb.com/title/tt0848228/'),
('https://www.imdb.com/title/tt1211837/'),
('https://www.imdb.com/title/tt1228705/'),
('https://www.imdb.com/title/tt1300854/'),
('https://www.imdb.com/title/tt1825683/'),
('https://www.imdb.com/title/tt1843866/'),
('https://www.imdb.com/title/tt1981115/'),
('https://www.imdb.com/title/tt2015381/'),
('https://www.imdb.com/title/tt2250912/'),
('https://www.imdb.com/title/tt2395427/'),
('https://www.imdb.com/title/tt3498820/'),
('https://www.imdb.com/title/tt3501632/'),
('https://www.imdb.com/title/tt3896198/'),
('https://www.imdb.com/title/tt4154756/');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
