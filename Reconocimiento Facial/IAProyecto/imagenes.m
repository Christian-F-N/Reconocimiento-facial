clear
clc
close all;
% Define la carpeta que contiene las imágenes
image_folder = 'images';

% Obtiene la lista de archivos en la carpeta
image_files = dir(fullfile(image_folder, '*.jpg'));

% Crea un cell array para almacenar las imágenes
images = cell(1, length(image_files));

% Lee las imágenes y las almacena en el cell array
for i = 1:length(image_files)
image_path = fullfile(image_folder, image_files(i).name);
images{i} = imread(image_path);
end

% Almacena el cell array de imágenes en un archivo .mat
save('images_dataset.mat', 'images');
load('images_dataset.mat');