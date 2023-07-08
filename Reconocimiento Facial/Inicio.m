%% Inicio (carga de datos)
clc;
clear;
close all;

% Cargar una imagen de ejemplo
imagen = heifred('Ch1.heic');

% Sepearamos en los tres espectros
imgRojo = imagen(:,:,1);
imgVerde = imagen(:,:,2);
imgAzul = imagen(:,:,3);


% Lectura de la imagen .heic
% imagen = heifread(rutaImagen);

% Mostrar la imagen
imshow(imagen);