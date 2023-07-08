imgSize = [100,100];
numImages = 10;

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


images = cat(3, redImages, greenImages, blueImages, yellowImages, ...
              magentaImages, cyanImages, orangeImages, pinkImages, ...
              purpleImages, brownImages, blackImages, whiteImages);

labels = [ones(1,numImages), 2*ones(1,numImages), 3*ones(1,numImages), ...          
    4*ones(1,numImages), 5*ones(1,numImages), 6*ones(1,numImages), ...          
    7*ones(1,numImages), 8*ones(1,numImages), 9*ones(1,numImages), ...          
    10*ones(1,numImages), 11*ones(1,numImages), 12*ones(1,numImages)];
      
% Mix the images and labels randomly
randIdx = randperm(12*numImages);
images = images(:,:,randIdx);
labels = labels(randIdx);

% Split the dataset into training and testing sets
numTrainImages = ceil(0.8 * numImages * 12);
XTrain = images(:,:,1:numTrainImages);
YTrain = categorical(labels(1:numTrainImages));
XTest = images(:,:,numTrainImages+1:end);
YTest = categorical(labels(numTrainImages+1:end));
