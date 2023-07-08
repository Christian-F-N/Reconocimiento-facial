%% Inicio (carga de datos)
clc;
clear;
close all;
imagenOriginal1 = imread('ch2.jpg');
imagenOriginal = imread('ch2.jpeg');
imagenOriginal2 = imread('ch2.png');
%% Mostrar la imagen original
% figure(1);
% imshow(imagenOriginal);
% title('Imagen original');
%% separa los spectros
imgRojo = imagenOriginal(:,:,1);
imgVerde = imagenOriginal(:,:,2);
imgAzul = imagenOriginal(:,:,3);
figure();
imshow(imgVerde);

imgRojo1 = imagenOriginal1(:,:,1);
imgVerde1 = imagenOriginal1(:,:,2);
imgAzul1 = imagenOriginal1(:,:,3);
figure();
imshow(imgAzul1);
imgRojo2 = imagenOriginal2(:,:,1);
imgVerde2 = imagenOriginal2(:,:,2);
imgAzul2 = imagenOriginal2(:,:,3);
figure();
imshow(imgRojo2);