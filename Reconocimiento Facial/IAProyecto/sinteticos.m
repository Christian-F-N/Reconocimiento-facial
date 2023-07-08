clc
clear
close all

% Definir el tamaño de las imágenes
imgSize = [32 32];

% Definir el número de imágenes por color
numImages = 1000;

% Crear imágenes de colores sólidos
redImages = uint8(255 * repmat([1, 0, 0], [imgSize(1), imgSize(2), numImages]));
orangeImages = uint8(255 * repmat([1, 0.5, 0], [imgSize(1), imgSize(2), numImages]));
yellowImages = uint8(255 * repmat([1, 1, 0], [imgSize(1), imgSize(2), numImages]));
greenImages = uint8(255 * repmat([0, 1, 0], [imgSize(1), imgSize(2), numImages]));
blueImages = uint8(255 * repmat([0, 0, 1], [imgSize(1), imgSize(2), numImages]));
purpleImages = uint8(255 * repmat([0.5, 0, 0.5], [imgSize(1), imgSize(2), numImages]));
pinkImages = uint8(255 * repmat([1, 0, 1], [imgSize(1), imgSize(2), numImages]));
brownImages = uint8(255 * repmat([0.5, 0.25, 0], [imgSize(1), imgSize(2), numImages]));
greyImages = uint8(255 * repmat([0.5, 0.5, 0.5], [imgSize(1), imgSize(2), numImages]));
blackImages = uint8(255 * repmat([0, 0, 0], [imgSize(1), imgSize(2), numImages]));
whiteImages = uint8(255 * repmat([1, 1, 1], [imgSize(1), imgSize(2), numImages]));
beigeImages = uint8(255 * repmat([0.96, 0.96, 0.86], [imgSize(1), imgSize(2), numImages]));


% Crear una categoría para cada color
redLabels = categorical(repmat({'red'}, numImages, 1));
orangeLabels = categorical(repmat({'orange'}, numImages, 1));
yellowLabels = categorical(repmat({'yellow'}, numImages, 1));
greenLabels = categorical(repmat({'green'}, numImages, 1));
blueLabels = categorical(repmat({'blue'}, numImages, 1));
indigoLabels = categorical(repmat({'indigo'}, numImages, 1));
violetLabels = categorical(repmat({'violet'}, numImages, 1));
pinkLabels = categorical(repmat({'pink'}, numImages, 1));
brownLabels = categorical(repmat({'brown'}, numImages, 1));
grayLabels = categorical(repmat({'gray'}, numImages, 1));
blackLabels = categorical(repmat({'black'}, numImages, 1));
whiteLabels = categorical(repmat({'white'}, numImages, 1));

% Concatenar las imágenes y etiquetas en un solo conjunto

images = cat(3, redImages, orangeImages, yellowImages, greenImages, blueImages, indigoImages, violetImages, pinkImages, brownImages, grayImages, blackImages, whiteImages);
labels = [redLabels; orangeLabels; yellowLabels; greenLabels; blueLabels; indigoLabels; violetLabels; pinkLabels; brownLabels; grayLabels; blackLabels; whiteLabels];

% Mezclar las imágenes y las etiquetas
shuffledIndices = randperm(numImages * 12);
images = images(:,:,shuffledIndices);
labels = labels(shuffledIndices);

% Dividir en conjuntos de entrenamiento y prueba
numTrain = floor(0.8 * numImages * 12);
trainImages = images(:,:,1:numTrain);
trainLabels = labels(1:numTrain);
testImages = images(:,:,numTrain+1:end);
testLabels = labels(numTrain+1:end);
