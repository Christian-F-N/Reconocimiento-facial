clc
clear
close all
% Definir el tamaño de las imágenes
imgSize = [100, 100,3];

% Definir el número de imágenes por color
numImages = 100;

% Creación de imágenes sintéticas de colores
redImages = uint8(255 * repmat([1, 0, 0], [imgSize(1), imgSize(2), numImages]));
orangeImages = uint8(255 * repmat([1, 0.5, 0], [imgSize(1), imgSize(2), numImages]));
yellowImages = uint8(255 * repmat([1, 1, 0], [imgSize(1), imgSize(2), numImages]));
greenImages = uint8(255 * repmat([0, 1, 0], [imgSize(1), imgSize(2), numImages]));%%
blueImages = uint8(255 * repmat([0, 0, 1], [imgSize(1), imgSize(2), numImages]));
purpleImages = uint8(255 * repmat([0.5, 0, 0.5], [imgSize(1), imgSize(2), numImages]));
pinkImages = uint8(255 * repmat([1, 0, 1], [imgSize(1), imgSize(2), numImages]));
brownImages = uint8(255 * repmat([0.5, 0.25, 0], [imgSize(1), imgSize(2), numImages]));
greyImages = uint8(255 * repmat([0.5, 0.5, 0.5], [imgSize(1), imgSize(2), numImages]));
blackImages = uint8(255 * repmat([0, 0, 0], [imgSize(1), imgSize(2), numImages]));
whiteImages = uint8(255 * repmat([1, 1, 1], [imgSize(1), imgSize(2), numImages]));
beigeImages = uint8(255 * repmat([0.96, 0.96, 0.86], [imgSize(1), imgSize(2), numImages]));

% Creación de etiquetas de colores
redLabels = repmat(categorical({'red'}), [numImages, 1]);
orangeLabels = repmat(categorical({'orange'}), [numImages, 1]);
yellowLabels = repmat(categorical({'yellow'}), [numImages, 1]);
greenLabels = repmat(categorical({'green'}), [numImages, 1]);
blueLabels = repmat(categorical({'blue'}), [numImages, 1]);
purpleLabels = repmat(categorical({'purple'}), [numImages, 1]);
pinkLabels = repmat(categorical({'pink'}), [numImages, 1]);
brownLabels = repmat(categorical({'brown'}), [numImages, 1]);
greyLabels = repmat(categorical({'grey'}), [numImages, 1]);
blackLabels = repmat(categorical({'black'}), [numImages, 1]);


% Crear una matriz para almacenar todas las imágenes sintéticas
images = cat(3, redImages, greenImages, blueImages, ...
              yellowImages, purpleImages, pinkImages, ...
              brownImages, greyImages, blackImages, ...
              whiteImages, orangeImages, beigeImages);

% Crear un vector para almacenar las etiquetas de cada imagen
labels = [ones(1,numImages), 2*ones(1,numImages), 3*ones(1,numImages), ...          
    4*ones(1,numImages), 5*ones(1,numImages), 6*ones(1,numImages), ...          
    7*ones(1,numImages), 8*ones(1,numImages), 9*ones(1,numImages), ...          
    10*ones(1,numImages), 11*ones(1,numImages), 12*ones(1,numImages)];
      
% Mezcla las imágenes y las etiquetas al azar.
randIdx = randperm(12*numImages);
images = images(:,:,randIdx);
labels = labels(randIdx);

% Dividir el conjunto de datos en conjuntos de entrenamiento y prueba
numTrainImages = ceil(0.8 * numImages * 12);
XTrain = images(:,:,1:numTrainImages);
YTrain = categorical(labels(1:numTrainImages));
XTest = images(:,:,numTrainImages+1:end);
YTest = categorical(labels(numTrainImages+1:end));

%%
layers = [
    imageInputLayer(imgSize)
    
    convolution2dLayer(3,8,'Padding','same')
    batchNormalizationLayer
    reluLayer
    
    maxPooling2dLayer(2,'Stride',2)
    
    convolution2dLayer(3,16,'Padding','same')
    batchNormalizationLayer
    reluLayer
    
    maxPooling2dLayer(2,'Stride',2)
    
    convolution2dLayer(3,32,'Padding','same')
    batchNormalizationLayer
    reluLayer
    
    fullyConnectedLayer(12)
    softmaxLayer
    classificationLayer];

options = trainingOptions('sgdm', ...
    'InitialLearnRate',0.01, ...
    'MaxEpochs',4, ...
    'Shuffle','every-epoch', ...
    'ValidationData',{XTest,YTest}, ...
    'ValidationFrequency',30, ...
    'Verbose',false, ...
    'Plots','training-progress');

net = trainNetwork(XTrain,YTrain,layers,options);


YPred = classify(net,XTest);
accuracy = mean(YPred == YTest);

%%
% Supongamos que tenemos una matriz de 100 imágenes de 300 x 960, llamada "images"
numImages = 960;
numRows = 100;
numCols = 300;
% Primero debemos convertir las imágenes a un formato vectorial
imagesVector = reshape(XTrain, [numRows * numCols, numImages]);
% Luego, podemos transponer la matriz para tener cada fila representando una imagen
imagesMatrix = imagesVector';