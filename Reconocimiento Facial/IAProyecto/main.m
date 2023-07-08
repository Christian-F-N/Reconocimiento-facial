clc; clear; close all; 
dataset = readmatrix("heart.csv");

y = dataset(:,end); 
dataset = normalize(dataset(:,1:end-1)); 
dataset = [dataset y]; 

x = dataset(:, 1:end-1); 


[m,n] = size(dataset) ;
P = 0.80 ;
idx = randperm(m);



training = dataset(idx(1:round(P*m)),:) ; 

testing = dataset(idx(round(P*m)+1:end),:) ; 

testing_ = testing(:,1:end-1);

idx_0 = find(training(:,end) == 0); 
idx_1 = find(training(:,end) == 1); 

ts_training = tsne(training); 
gscatter(ts_training(:,1),ts_training(:,2),training(:,end)); 


predictions = knnAlgo(testing_, training, 3); 

acum = 0; 
for i = 1 : length(testing)
    if predictions(i,end) == testing(i,end)
        acum = acum + 1; 
    end
end

accuracy = acum/length(testing); 


