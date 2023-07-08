clc
clear
close all
% Definir el tamaño de las imágenes
imgSize = [32 32];

% Definir el número de imágenes por color
numImages = 1000;

% Crear imágenes de colores sólidos
redImages = 255 * ones(imgSize(1), imgSize(2), numImages, 'uint8');
greenImages = zeros(imgSize(1), imgSize(2), numImages, 'uint8');
blueImages = zeros(imgSize(1), imgSize(2), numImages, 'uint8');
yellowImages = cat(3, redImages, greenImages);
cyanImages = cat(3, greenImages, blueImages);
magentaImages = cat(3, redImages, blueImages);
orangeImages = cat(3, uint8(0.9 * redImages), uint8(0.5 * greenImages));
pinkImages = cat(3, uint8(0.9 * redImages), uint8(0.6 * greenImages), uint8(0.6 * blueImages));
brownImages = cat(3, uint8(0.6 * redImages), uint8(0.3 * greenImages), uint8(0.2 * blueImages));
purpleImages = cat(3, uint8(0.5 * redImages), uint8(0.2 * greenImages), uint8(0.5 * blueImages));

% Crear una categoría para cada color
redLabels = categorical(repmat({'red'}, numImages, 1));
greenLabels = categorical(repmat({'green'}, numImages, 1));
blueLabels = categorical(repmat({'blue'}, numImages, 1));
yellowLabels = categorical(repmat({'yellow'}, numImages, 1));
cyanLabels = categorical(repmat({'cyan'}, numImages, 1));
magentaLabels = categorical(repmat({'magenta'}, numImages, 1));
orangeLabels = categorical(repmat({'orange'}, numImages, 1));
pinkLabels = categorical(repmat({'pink'}, numImages, 1));
brownLabels = categorical(repmat({'brown'}, numImages, 1));
purpleLabels = categorical(repmat({'purple'}, numImages, 1));

% Concatenar las imágenes y etiquetas en un solo conjunto de datos
data = cat(3, redImages, greenImages, blueImages, yellowImages, cyanImages, magentaImages, orangeImages, pinkImages, brownImages, purpleImages);
labels = cat(1, redLabels, greenLabels, blueLabels, yellowLabels, cyanLabels, magentaLabels, orangeLabels, pinkLabels, brownLabels, purpleLabels);

% Mezclar el conjunto de datos
idx = randperm(numel(labels));
data = data(:, :, idx);
labels = labels(idx);