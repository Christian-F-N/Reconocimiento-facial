clear 
close all
clc
% Carga de la imagen
I = imread('linea.jpg');

% Conversión a espacio de color HSV
Ihsv = rgb2hsv(I);

% Segmentación de la imagen
bw = imbinarize(Ihsv(:,:,1));

% Identificación de las figuras en la imagen segmentada
[B,L] = bwboundaries(bw,'noholes');

% Iteración sobre las figuras identificadas
for k = 1:length(B)
    
    % Cálculo del área de la figura
    boundary = B{k};
    area = polyarea(boundary(:,2), boundary(:,1));
    
    % Extracción del color promedio de la figura
    [r, c] = find(L==k);
    color = mean(I(r,c,:),1);
    
    % Visualización de la información de la figura
    fprintf('Figura %d: Area = %0.2f, Color RGB = [%0.2f, %0.2f, %0.2f]\n', k, area, color(1), color(2), color(3));
end




