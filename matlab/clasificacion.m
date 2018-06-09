% CODE ASSIGNMENT 3 PATTERN RECOGNITION

%% Feature transformation
clear
load('selectedFeatures.mat');

% Classification
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
clear b
k = 0;
k=k+1;b(k).name = 'libsvm';   b(k).options.kernel = '-t 0';     b(k).string = 'SVM';
k=k+1;b(k).name = 'lda';   b(k).options.p = [];         b(k).string = 'LDA';            
k=k+1;b(k).name = 'knn';   b(k).options.k = 7;          b(k).string = 'KNN';           
k=k+1;b(k).name = 'nnglm'; b(k).options. method = 3; b(k).options.iter = 10;           b(k).string = 'ANN';            

opc = b;
ds = Bcl_structure(trainFeatures(:,s),trainLabels,testFeatures(:,s),opc);                                  

% Evaluation of Performance
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
testLabels = double(Bds_labels(40*ones(7,1)));   % 40 samples per class, 7 classes

op.strat=1; op.b = b; op.v = 10; op.show = 1; op.c = 0.95;     % 10 groups cross-validation

p1 = Bev_crossval(trainFeatures(:, s),trainLabels,op);

p = Bev_performance(ds,testLabels);

for i=1:length(b)
    fprintf('%15s = %6.2f%%\n',b(i).string,p(i)*100);
end

%%
% Plot confusion matrix
% Convert this data to a [numClasses x 6] matrix
targets = zeros(7,280);
outputs = zeros(7,280);
targetsIdx = sub2ind(size(targets), transpose(testLabels), 1:280);
outputsIdx = sub2ind(size(outputs), transpose(ds(:, 1)), 1:280);
targets(targetsIdx) = 1;
outputs(outputsIdx) = 1;
% Plot the confusion matrix for a 3-class problem
% Bio_showconfusion(
plotconfusion(targets,outputs)

h = gca;
h.XTickLabel = {'Clase 1','Clase 2','Clase 3','Clase 4', 'Clase 5', 'Clase 6', 'Clase 7', ''};
h.YTickLabel = {'Clase 1','Clase 2','Clase 3','Clase 4', 'Clase 5', 'Clase 6', 'Clase 7', ''};
h.YTickLabelRotation = 90;