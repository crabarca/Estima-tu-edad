% CODE ASSIGNMENT 3 PATTERN RECOGNITION
%%
clt;
NTraining = 1400;
NTest = 280;
trainingImg = cell(NTraining, 1);
testImg = cell(NTest, 1);
trainFeatures = [];
testFeatures = [];
featureLabels = [];

path = '/home/cristobal/Dropbox/U/Patrones/Tareas/T3/fotos/';

l = 1;
for i = 1:7
    for j = 1:200
        filename = [path 'face_' sprintf('%03d', i) '_' sprintf('%05d', j) '.png'];
        fprintf("Opening training file img %d/%d\n", i,j);
        trainingImg{l} = imread(filename);
        l = l + 1;
    end
end

l = 1;
for i = 1:7
    for j = 201:240
        filename = [path 'face_' sprintf('%03d', i) '_' sprintf('%05d', j) '.png'];
        fprintf("Opening test file img %d/%d\n", i, j);
        testImg{l} = imread(filename);
        l = l + 1;
    end
end

% LBP
lbpop.vdiv = 4;
lbpop.hdiv = 4;
lbpop.semantic = 0;
lbpop.samples = 16;
lbpop.mappingtype = 'u2';
buff = [];
for i = 1: NTraining
    [X, Xn] = Bfx_lbp(trainingImg{i}, [], lbpop);
    buff = [buff; X];
    fprintf("Extracting LBP %i \n", i);

end
trainFeatures = [trainFeatures, buff];
buff = [];
for i = 1: NTest
    [X, Xn] = Bfx_lbp(testImg{i}, [], lbpop);
    buff = [buff; X];
    fprintf("Extracting LBP %i \n", i);
end
testFeatures = [testFeatures, buff];
featureLabels = [featureLabels; Xn];


% GABOR
options.Lgabor  = 8;                 % number of rotations       
options.Sgabor  = 5;                 % number of dilations (scale)
options.fhgabor = 4;                 % highest frequency of interest
options.flgabor = 0.1;               % lowest frequency of interest
options.Mgabor  = 21;                % mask size
options.show    = 0;        

buff = [];
for i = 1: NTraining
    resized = imresize(trainingImg{i}, 0.5);
    [X, Xn] = Bfx_gabor(resized,  options);
    buff = [buff; X];
    fprintf("Extracting gabor %i \n", i);

end
trainFeatures = [trainFeatures, buff];
buff = [];
for i = 1: NTest
    resized = imresize(testImg{i}, 0.5);
    [X, Xn] = Bfx_gabor(resized, options);
    buff = [buff; X];
    fprintf("Extracting gabor %i \n", i);
end
testFeatures = [testFeatures, buff];
featureLabels = [featureLabels; Xn];

% HOG
hogoptions.nj = 5;
hogoptions.ni = 5;
hogoptions.B = 10;
hogoptions.show = 0;

buff = [];
for i = 1:NTraining
    [X, Xn] = Bfx_hog(trainingImg{i}, hogoptions);
    buff = [buff; X];
    fprintf("Extracting HOG %i \n", i);
end
trainFeatures = [trainFeatures, buff];
buff = [];
for i = 1:NTest
    [X, Xn] = Bfx_hog(testImg{i}, hogoptions);
    buff = [buff; X];
    fprintf("Extracting HOG %i \n", i);
end
testFeatures = [testFeatures, buff];
featureLabels = [featureLabels; Xn];

% Haralick
hoptions.dharalick = 1;
hoptions.show = 0;
buff = [];
for i = 1: NTraining
    [X, Xn] = Bfx_haralick(trainingImg{i}, hoptions);
    buff = [buff; X];
    fprintf("Extracting haralick %  i \n", i);

end
trainFeatures = [trainFeatures, buff];
buff = [];
for i = 1: NTest
    [X, Xn] = Bfx_haralick(testImg{i}, hoptions);
    buff = [buff; X];
    fprintf("Extracting haralick %i \n", i);
end
testFeatures = [testFeatures, buff];
featuresLabels = [featureLabels; Xn];

save('featuresExtracted.mat','trainFeatures', 'testFeatures', 'featureLabels');



