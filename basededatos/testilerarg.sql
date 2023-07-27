-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 27-07-2023 a las 20:36:49
-- Versión del servidor: 10.4.28-MariaDB
-- Versión de PHP: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `testilerarg`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `entrada_tela`
--

CREATE TABLE `entrada_tela` (
  `id_proveedor` int(11) NOT NULL,
  `id_tela` int(11) NOT NULL,
  `Tela` varchar(30) NOT NULL,
  `Metros` int(11) NOT NULL,
  `fecha_entrada` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `maquiladores`
--

CREATE TABLE `maquiladores` (
  `id_maquilador` int(11) NOT NULL,
  `nombre` varchar(30) NOT NULL,
  `Ape_pat` varchar(30) NOT NULL,
  `Ape_mat` varchar(30) NOT NULL,
  `Direccion` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `maquilero`
--

CREATE TABLE `maquilero` (
  `id_maquilero` int(11) NOT NULL,
  `nombre` varchar(30) NOT NULL,
  `Ape_pat` varchar(30) NOT NULL,
  `Ape_mat` varchar(30) NOT NULL,
  `Direccion` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `precios_productos`
--

CREATE TABLE `precios_productos` (
  `id_producto` int(11) NOT NULL,
  `talla` varchar(20) NOT NULL,
  `av_talla` int(11) NOT NULL,
  `precio` decimal(15,0) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `producto`
--

CREATE TABLE `producto` (
  `id_producto` int(11) NOT NULL,
  `Nombre_producto` varchar(30) NOT NULL,
  `Tipo_tela` varchar(30) NOT NULL,
  `talla` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `producto_a_procesar`
--

CREATE TABLE `producto_a_procesar` (
  `id_producto` int(11) NOT NULL,
  `id_proceso` int(11) NOT NULL,
  `Fecha_entrada` date NOT NULL,
  `Fecha_salida` date NOT NULL,
  `Fecha_estimada_entrega` date NOT NULL,
  `talla` varchar(20) NOT NULL,
  `id_usuario` int(11) NOT NULL,
  `id_maquilador` int(11) NOT NULL,
  `codigo_proceso` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `producto_entregar`
--

CREATE TABLE `producto_entregar` (
  `codigo_entrega` int(11) NOT NULL,
  `id_producto` int(11) NOT NULL,
  `Fecha_entrada` date NOT NULL,
  `talla` varchar(20) NOT NULL,
  `id_maquilador` int(11) NOT NULL,
  `id_maquilero` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `proveedor`
--

CREATE TABLE `proveedor` (
  `id_proveedor` int(11) NOT NULL,
  `nombre` varchar(30) NOT NULL,
  `Ape_pat` varchar(30) NOT NULL,
  `Ape_mat` varchar(30) NOT NULL,
  `Direccion` varchar(30) NOT NULL,
  `id_tela` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `puestos`
--

CREATE TABLE `puestos` (
  `id_puesto` int(11) NOT NULL,
  `Nombre_puesto` varchar(30) NOT NULL,
  `Maquinaria_a_cargo` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tipos_proceso`
--

CREATE TABLE `tipos_proceso` (
  `id_proceso` int(11) NOT NULL,
  `Proceso` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tipo_tela`
--

CREATE TABLE `tipo_tela` (
  `id_tela` int(11) NOT NULL,
  `Nombre_tela` varchar(30) NOT NULL,
  `Precio` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `username` varchar(50) NOT NULL,
  `password` varchar(256) NOT NULL,
  `email` varchar(100) NOT NULL,
  `first_name` varchar(50) DEFAULT '',
  `last_name` varchar(50) DEFAULT '',
  `role` varchar(50) NOT NULL DEFAULT 'customer',
  `image` varchar(100) DEFAULT ''
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `users`
--

INSERT INTO `users` (`id`, `username`, `password`, `email`, `first_name`, `last_name`, `role`, `image`) VALUES
(1, 'kion', 'pbkdf2:sha256:600000$N7IQWeguG1nVES8Z$a6d266b33773e7a701f529716bb0466e8b362ec1550c3bd48dd8100f84b3c181', 'kionsahernandez@gmail.com', '', '', 'customer', '');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuario`
--

CREATE TABLE `usuario` (
  `id_usuario` int(11) NOT NULL,
  `Tipo_usuario` varchar(30) NOT NULL,
  `Nombre` varchar(30) NOT NULL,
  `Ape_Pat` varchar(30) NOT NULL,
  `Ape_Mat` varchar(30) NOT NULL,
  `Direccion` varchar(30) NOT NULL,
  `id_puesto` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `entrada_tela`
--
ALTER TABLE `entrada_tela`
  ADD PRIMARY KEY (`id_proveedor`,`id_tela`),
  ADD KEY `id_tela` (`id_tela`);

--
-- Indices de la tabla `maquiladores`
--
ALTER TABLE `maquiladores`
  ADD PRIMARY KEY (`id_maquilador`);

--
-- Indices de la tabla `maquilero`
--
ALTER TABLE `maquilero`
  ADD PRIMARY KEY (`id_maquilero`);

--
-- Indices de la tabla `precios_productos`
--
ALTER TABLE `precios_productos`
  ADD PRIMARY KEY (`talla`),
  ADD KEY `id_producto` (`id_producto`);

--
-- Indices de la tabla `producto`
--
ALTER TABLE `producto`
  ADD PRIMARY KEY (`id_producto`);

--
-- Indices de la tabla `producto_a_procesar`
--
ALTER TABLE `producto_a_procesar`
  ADD PRIMARY KEY (`id_producto`,`id_proceso`),
  ADD KEY `id_proceso` (`id_proceso`),
  ADD KEY `id_usuario` (`id_usuario`),
  ADD KEY `id_maquilador` (`id_maquilador`),
  ADD KEY `talla` (`talla`);

--
-- Indices de la tabla `producto_entregar`
--
ALTER TABLE `producto_entregar`
  ADD PRIMARY KEY (`codigo_entrega`),
  ADD KEY `id_maquilero` (`id_maquilero`),
  ADD KEY `id_producto` (`id_producto`),
  ADD KEY `talla` (`talla`);

--
-- Indices de la tabla `proveedor`
--
ALTER TABLE `proveedor`
  ADD PRIMARY KEY (`id_proveedor`),
  ADD KEY `id_tela` (`id_tela`);

--
-- Indices de la tabla `puestos`
--
ALTER TABLE `puestos`
  ADD PRIMARY KEY (`id_puesto`);

--
-- Indices de la tabla `tipos_proceso`
--
ALTER TABLE `tipos_proceso`
  ADD PRIMARY KEY (`id_proceso`);

--
-- Indices de la tabla `tipo_tela`
--
ALTER TABLE `tipo_tela`
  ADD PRIMARY KEY (`id_tela`);

--
-- Indices de la tabla `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `usuario`
--
ALTER TABLE `usuario`
  ADD PRIMARY KEY (`id_usuario`),
  ADD KEY `id_puesto` (`id_puesto`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `maquiladores`
--
ALTER TABLE `maquiladores`
  MODIFY `id_maquilador` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `maquilero`
--
ALTER TABLE `maquilero`
  MODIFY `id_maquilero` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `producto`
--
ALTER TABLE `producto`
  MODIFY `id_producto` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `producto_entregar`
--
ALTER TABLE `producto_entregar`
  MODIFY `codigo_entrega` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `proveedor`
--
ALTER TABLE `proveedor`
  MODIFY `id_proveedor` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `puestos`
--
ALTER TABLE `puestos`
  MODIFY `id_puesto` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `tipos_proceso`
--
ALTER TABLE `tipos_proceso`
  MODIFY `id_proceso` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `tipo_tela`
--
ALTER TABLE `tipo_tela`
  MODIFY `id_tela` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `usuario`
--
ALTER TABLE `usuario`
  MODIFY `id_usuario` int(11) NOT NULL AUTO_INCREMENT;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `entrada_tela`
--
ALTER TABLE `entrada_tela`
  ADD CONSTRAINT `entrada_tela_ibfk_1` FOREIGN KEY (`id_tela`) REFERENCES `tipo_tela` (`id_tela`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `entrada_tela_ibfk_2` FOREIGN KEY (`id_proveedor`) REFERENCES `proveedor` (`id_proveedor`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `precios_productos`
--
ALTER TABLE `precios_productos`
  ADD CONSTRAINT `precios_productos_ibfk_1` FOREIGN KEY (`id_producto`) REFERENCES `producto` (`id_producto`) ON UPDATE CASCADE;

--
-- Filtros para la tabla `producto_a_procesar`
--
ALTER TABLE `producto_a_procesar`
  ADD CONSTRAINT `producto_a_procesar_ibfk_1` FOREIGN KEY (`id_producto`) REFERENCES `producto` (`id_producto`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `producto_a_procesar_ibfk_2` FOREIGN KEY (`id_proceso`) REFERENCES `tipos_proceso` (`id_proceso`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `producto_a_procesar_ibfk_3` FOREIGN KEY (`id_usuario`) REFERENCES `usuario` (`id_usuario`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `producto_a_procesar_ibfk_4` FOREIGN KEY (`id_maquilador`) REFERENCES `maquiladores` (`id_maquilador`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `producto_a_procesar_ibfk_5` FOREIGN KEY (`talla`) REFERENCES `precios_productos` (`talla`) ON UPDATE CASCADE;

--
-- Filtros para la tabla `producto_entregar`
--
ALTER TABLE `producto_entregar`
  ADD CONSTRAINT `producto_entregar_ibfk_1` FOREIGN KEY (`id_maquilero`) REFERENCES `maquilero` (`id_maquilero`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `producto_entregar_ibfk_2` FOREIGN KEY (`id_producto`) REFERENCES `producto` (`id_producto`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `producto_entregar_ibfk_3` FOREIGN KEY (`talla`) REFERENCES `precios_productos` (`talla`) ON UPDATE CASCADE;

--
-- Filtros para la tabla `proveedor`
--
ALTER TABLE `proveedor`
  ADD CONSTRAINT `proveedor_ibfk_1` FOREIGN KEY (`id_tela`) REFERENCES `tipo_tela` (`id_tela`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `usuario`
--
ALTER TABLE `usuario`
  ADD CONSTRAINT `usuario_ibfk_1` FOREIGN KEY (`id_puesto`) REFERENCES `puestos` (`id_puesto`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
