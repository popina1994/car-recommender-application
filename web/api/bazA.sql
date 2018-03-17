-- phpMyAdmin SQL Dump
-- version 4.1.14
-- http://www.phpmyadmin.net
--
-- Host: 127.0.0.1
-- Generation Time: Aug 22, 2017 at 01:11 PM
-- Server version: 5.6.17
-- PHP Version: 5.5.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `cvecara2017`
--
CREATE DATABASE IF NOT EXISTS `cvecara2017` DEFAULT CHARACTER SET latin1 COLLATE latin1_swedish_ci;
USE `cvecara2017`;

-- --------------------------------------------------------

--
-- Table structure for table `buketi`
--

DROP TABLE IF EXISTS `buketi`;
CREATE TABLE IF NOT EXISTS `buketi` (
  `id_narudzbine` int(11) NOT NULL,
  `id_cvet` int(11) NOT NULL,
  `cvet_komada` int(11) NOT NULL,
  PRIMARY KEY (`id_narudzbine`,`id_cvet`),
  KEY `id_cvet` (`id_cvet`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `buketi`
--

INSERT INTO `buketi` (`id_narudzbine`, `id_cvet`, `cvet_komada`) VALUES
(1, 1, 7),
(2, 1, 3),
(2, 3, 2),
(3, 5, 3),
(3, 6, 1),
(4, 1, 4),
(5, 3, 1),
(6, 2, 1),
(7, 2, 1);

-- --------------------------------------------------------

--
-- Table structure for table `cvet`
--

DROP TABLE IF EXISTS `cvet`;
CREATE TABLE IF NOT EXISTS `cvet` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'auto_increment identifikator',
  `naziv` varchar(32) COLLATE utf8_unicode_ci NOT NULL,
  `trenutna_kolicina` int(11) NOT NULL,
  `cena` double NOT NULL,
  `slika` varchar(32) COLLATE utf8_unicode_ci NOT NULL COMMENT 'putanja do slike',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci AUTO_INCREMENT=7 ;

--
-- Dumping data for table `cvet`
--

INSERT INTO `cvet` (`id`, `naziv`, `trenutna_kolicina`, `cena`, `slika`) VALUES
(1, 'ruЕѕa', 15, 180.5, 'rose.jpg'),
(2, 'ljiljan', 18, 160, 'ljiljan.jpg'),
(3, 'orhideja', 10, 225, 'orhidea.jpg'),
(4, 'hrizantema', 10, 190, 'hrizantema.jpg'),
(5, 'crveni gerber', 0, 200, 'gerber.jpg'),
(6, 'suncokret', 7, 155, 'suncokret.jpg');

-- --------------------------------------------------------

--
-- Table structure for table `korisnici`
--

DROP TABLE IF EXISTS `korisnici`;
CREATE TABLE IF NOT EXISTS `korisnici` (
  `korisnickoime` varchar(32) COLLATE utf8_unicode_ci NOT NULL,
  `lozinka` varchar(32) COLLATE utf8_unicode_ci NOT NULL,
  `ime` varchar(16) COLLATE utf8_unicode_ci NOT NULL,
  `prezime` varchar(16) COLLATE utf8_unicode_ci NOT NULL,
  `tip` tinyint(4) NOT NULL COMMENT '0-naruДЌilac, 1-kurir',
  PRIMARY KEY (`korisnickoime`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `korisnici`
--

INSERT INTO `korisnici` (`korisnickoime`, `lozinka`, `ime`, `prezime`, `tip`) VALUES
('drasko', 'sifra123', 'DraЕѕen', 'DraЕЎkoviД‡', 0),
('joca', 'sifra123', 'Jovan', 'JovanoviД‡', 1),
('maja', 'sifra123', 'Maja', 'VukasoviД‡', 0),
('pera', 'sifra123', 'Pera', 'PeriД‡', 1),
('sanja', 'sifra123', 'Sanja', 'DelДЌev', 0),
('zika', 'sifra123', 'ЕЅika', 'Е uЕЎtran', 0);

-- --------------------------------------------------------

--
-- Table structure for table `kuriri`
--

DROP TABLE IF EXISTS `kuriri`;
CREATE TABLE IF NOT EXISTS `kuriri` (
  `kurir` varchar(32) COLLATE utf8_unicode_ci NOT NULL,
  `opstina` int(11) NOT NULL,
  PRIMARY KEY (`kurir`,`opstina`),
  KEY `opstina` (`opstina`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `kuriri`
--

INSERT INTO `kuriri` (`kurir`, `opstina`) VALUES
('pera', 1),
('pera', 2),
('joca', 3),
('pera', 3),
('joca', 4),
('pera', 4),
('joca', 5),
('joca', 6),
('joca', 7);

-- --------------------------------------------------------

--
-- Table structure for table `narudzbina`
--

DROP TABLE IF EXISTS `narudzbina`;
CREATE TABLE IF NOT EXISTS `narudzbina` (
  `ident` int(11) NOT NULL AUTO_INCREMENT,
  `osoba_za_isporuku` varchar(32) COLLATE utf8_unicode_ci NOT NULL,
  `adresa_za_isporuku` varchar(64) COLLATE utf8_unicode_ci NOT NULL,
  `opstina` int(11) NOT NULL,
  `broj_kartice` varchar(16) COLLATE utf8_unicode_ci NOT NULL,
  `narucilac` varchar(32) COLLATE utf8_unicode_ci NOT NULL,
  `kurir_preuzeo` varchar(32) COLLATE utf8_unicode_ci DEFAULT NULL,
  `isporuceno` datetime DEFAULT NULL,
  PRIMARY KEY (`ident`),
  KEY `narucilac` (`narucilac`,`kurir_preuzeo`),
  KEY `narucilac_2` (`narucilac`),
  KEY `opstina` (`opstina`),
  KEY `kurir_preuzeo` (`kurir_preuzeo`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci AUTO_INCREMENT=8 ;

--
-- Dumping data for table `narudzbina`
--

INSERT INTO `narudzbina` (`ident`, `osoba_za_isporuku`, `adresa_za_isporuku`, `opstina`, `broj_kartice`, `narucilac`, `kurir_preuzeo`, `isporuceno`) VALUES
(1, 'Jasna J.', 'Bulevar Nikole Tesle 123', 5, '4234123412341234', 'drasko', 'joca', '2017-08-22 10:06:00'),
(2, 'Sanja D.', 'Bulevar kralja Aleksandra 333', 4, '3445234513452345', 'drasko', 'joca', NULL),
(3, 'Sanja D.', 'Bulevar kralja Aleksandra 73', 8, '4321123400005431', 'sanja', 'pera', NULL),
(4, 'Jelena D.', 'Bulevar Nikole Tesle 73', 6, '3030313132323333', 'zika', 'joca', NULL),
(5, 'Stanka M.', 'Kraljice Natalije 37', 1, '5534223985242847', 'sanja', 'pera', '2017-03-08 11:15:00'),
(6, 'Jelica P.', 'Bulevar kralja Aleksandra 73', 8, '5295347589379523', 'drasko', 'pera', '2017-03-08 10:10:14'),
(7, 'Marija P.', 'Bulevar kralja Aleksandra 73', 8, '5295347589379523', 'drasko', 'pera', '2017-03-08 10:10:17');

-- --------------------------------------------------------

--
-- Table structure for table `opstina`
--

DROP TABLE IF EXISTS `opstina`;
CREATE TABLE IF NOT EXISTS `opstina` (
  `id_opstine` int(11) NOT NULL AUTO_INCREMENT,
  `naziv` varchar(32) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`id_opstine`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci AUTO_INCREMENT=10 ;

--
-- Dumping data for table `opstina`
--

INSERT INTO `opstina` (`id_opstine`, `naziv`) VALUES
(1, 'Stari grad'),
(2, 'Savski venac'),
(3, 'VraДЌar'),
(4, 'Zvezdara'),
(5, 'Zemun'),
(6, 'Novi Beograd'),
(7, 'VoЕѕdovac'),
(8, 'Palilula');

--
-- Constraints for dumped tables
--

--
-- Constraints for table `buketi`
--
ALTER TABLE `buketi`
  ADD CONSTRAINT `buketi_ibfk_2` FOREIGN KEY (`id_cvet`) REFERENCES `cvet` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `buketi_ibfk_1` FOREIGN KEY (`id_narudzbine`) REFERENCES `narudzbina` (`ident`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `kuriri`
--
ALTER TABLE `kuriri`
  ADD CONSTRAINT `kuriri_ibfk_2` FOREIGN KEY (`opstina`) REFERENCES `opstina` (`id_opstine`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `kuriri_ibfk_1` FOREIGN KEY (`kurir`) REFERENCES `korisnici` (`korisnickoime`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `narudzbina`
--
ALTER TABLE `narudzbina`
  ADD CONSTRAINT `narudzbina_ibfk_1` FOREIGN KEY (`opstina`) REFERENCES `opstina` (`id_opstine`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `narudzbina_ibfk_2` FOREIGN KEY (`narucilac`) REFERENCES `korisnici` (`korisnickoime`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `narudzbina_ibfk_3` FOREIGN KEY (`kurir_preuzeo`) REFERENCES `korisnici` (`korisnickoime`) ON DELETE CASCADE ON UPDATE CASCADE;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;