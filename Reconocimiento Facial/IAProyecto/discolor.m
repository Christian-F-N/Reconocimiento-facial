%%ejemplo de código para reducir el tamaño de la imagen o dividirla en partes más pequeñas y procesarlas por separado para reconocer figuras y extraer sus colores en matlab
% Load the image
clear 
close all
clc
I = imread('rgb2.png');

% Resize the image
I = imresize(I, [300 300]);

% Split the image into smaller parts
numOfRows = 3;
numOfCols = 3;
[rows, cols, ~] = size(I);
rowBlockSize = floor(rows/numOfRows);
colBlockSize = floor(cols/numOfCols);

% Loop through each block and process it
for r = 1:numOfRows
    for c = 1:numOfCols
        rowStart = (r-1)*rowBlockSize + 1;
        rowEnd = rowStart + rowBlockSize - 1;
        colStart = (c-1)*colBlockSize + 1;
        colEnd = colStart + colBlockSize - 1;
        block = I(rowStart:rowEnd, colStart:colEnd, :);
        
        % Code to process the block goes here
        color = mean(block(:),1);
    end
end
