% CODE ASSIGNMENT 3 PATTERN RECOGNITION

%% Feature selection
clear
load('featuresExtracted.mat');

% Ideal classification for train
trainLabels = double(Bds_labels(200*ones(7,1)));   % 100 samples per class, 5 classes
% Ideal classification for train
testLabels = double(Bds_labels(40*ones(7,1)));

% Normalization
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
[trainFeatures,a,b] = Bft_norm(trainFeatures,1);
N = size(testFeatures,1);
testFeatures = testFeatures.*(ones(N,1)*a) + ones(N,1)*b;

% Feature transformation
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
m = 200;
[trainFeatures, lambda, A, Xs, mx] = Bft_pca(trainFeatures, m);

B = A(:,1:m);
MXt = ones(length(testLabels),1)*mx;
X0t = testFeatures - MXt;
testFeatures = X0t*B;

% Clean de caracteristicas correlacionadas
% s = Bfs_clean(trainFeatures, 1);
% trainFeatures= trainFeatures(:, s);

% Selection
op.m = 70;
op.b.name = 'fisher';
op.show = 1;
s = Bfs_sfs(trainFeatures, trainLabels, op);
featureLabels = featureLabels(s,:);

save('selectedFeatures.mat', 'featureLabels', 's', 'trainLabels', 'trainFeatures', 'testFeatures');