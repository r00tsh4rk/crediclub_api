-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Servidor: localhost
-- Tiempo de generación: 09-12-2022 a las 07:19:53
-- Versión del servidor: 10.4.25-MariaDB
-- Versión de PHP: 7.4.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `crediclub`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `creditos`
--

CREATE TABLE `creditos` (
  `id_cliente` int(11) NOT NULL,
  `primer_nombre` varchar(50) NOT NULL,
  `apellido_pat` varchar(50) NOT NULL,
  `apellido_mat` varchar(50) NOT NULL,
  `fecha_nacimiento` varchar(11) NOT NULL,
  `rfc` varchar(10) NOT NULL,
  `ingresos_mensuales` bigint(20) NOT NULL,
  `dependientes` int(11) NOT NULL,
  `estatus_credito` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `creditos`
--

INSERT INTO `creditos` (`id_cliente`, `primer_nombre`, `apellido_pat`, `apellido_mat`, `fecha_nacimiento`, `rfc`, `ingresos_mensuales`, `dependientes`, `estatus_credito`) VALUES
(1, 'Josue', 'Ruiz', 'Chimal', '26-10-1992', 'RUCJ921026', 26000, 1, 'APROBADO'),
(2, 'Maria', 'Jimenez', 'López', '12-07-1978', 'JILM780712', 32000, 2, 'APROBADO'),
(4, 'Karla', 'Jiménez', 'Betancur', '12-12-1989', 'JIBK981212', 25000, 2, 'APROBADO'),
(8, 'Araceli', 'Rodríguez', 'López', '14-02-1993', 'RORA930214', 28999, 0, 'APROBADO'),
(11, 'Carlos', 'Quiróz', 'López', '19-01-1993', 'QULC930119', 34999, 2, 'APROBADO'),
(16, 'Alma Delia', 'Ricárdez', 'García', '15-04-1988', 'RIGA880415', 48000, 2, 'APROBADO'),
(17, 'Victor Manuel', 'Bautista', 'Méndez', '06-11-1991', 'BAMV911106', 16000, 2, 'APROBADO'),
(18, 'Carmen', 'Morales', 'Noriega', '18-06-1985', 'MONC850618', 70000, 4, 'APROBADO'),
(19, 'Luis Felipe', 'Tavares', 'Oriazabal', '03-08-1994', 'TAOL940803', 16000, 1, 'APROBADO'),
(20, 'Ernesto', 'Caballero', 'Carrizal', '18-03-1992', 'CACE920318', 16000, 4, 'NO APROBADO'),
(21, 'Isabel Andrea', 'Amaya', 'Pérez', '25-07-1992', 'AMPI920725', 13000, 2, 'NO APROBADO');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `creditos`
--
ALTER TABLE `creditos`
  ADD PRIMARY KEY (`id_cliente`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `creditos`
--
ALTER TABLE `creditos`
  MODIFY `id_cliente` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
