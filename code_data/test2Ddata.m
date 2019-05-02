
%% README
% Make sure to put the image sequence and the tracking data in the same
% folder with this matlab file.
% WARNING : all the files will be overwritten, please make a backup before
% use this program.

%% CLEANUP
clc;    % Clear the command window.w
close all;  % Close all figures (except those of imtool.)
imtool close all;  % Close all imtool figures.
clear all;  % Erase all existing variables.


%% MAIN FUNCTION
% myFolder = 'C:\Users\hchyu\Dropbox\dance motion data test\Image Sequences'; % Specify the folder where the files are
% imageSqPrefix = 'Tarian Zapin-Gerak asas langkah maju undur 45_'; % Change this string to your image sequence
trackingData = '9_Fast Song 05.data'; % Change this string to your tracking data
% trackingData = 'newMat.data'
% writerObj = VideoWriter('Test.avi'); %Video Writer function 
% open(writerObj);

% filePattern = fullfile(myFolder, '*.jpg'); % Change to whatever pattern you need.
myfolder =  'E:\codes\BU\Mycodes\motion\FastSong_Man_5';
theFiles = dir('FastSong_Man_5\*.jpg');

%% IMAGE WRITER
Prefix = fullfile(myfolder,theFiles(1).name(1:end-8));
[Tracking2D, delimeter] = importdata(trackingData); %2D skeleton data;

A = Tracking2D(10:109,:);
% [rowa,cola]=find(A==0);
A1 = Tracking2D(1:100,:);
% [rowa1,cola1]=find(A1==0);
Tracking2D(1:100,:) = interpolation(A,A1);

% A = Tracking2D(1:109,:);
% A1 = Tracking2D(20:128,:);
% Tracking2D(20:128,:) = interpolation(A,A1);
% 
% A = Tracking2D(1:120,:);
% A1 = Tracking2D(41:160,:);
% Tracking2D(41:160,:) = interpolation(A,A1);
% 
% A = Tracking2D(1:130,:);
% A1 = Tracking2D(61:190,:);
% Tracking2D(61:190,:) = interpolation(A,A1);
% 
% A = Tracking2D(1:130,:);
% A1 = Tracking2D(71:200,:);
% Tracking2D(71:200,:) = interpolation(A,A1);
% 
% A = Tracking2D(1:130,:);
% A1 = Tracking2D(81:210,:);
% Tracking2D(81:210,:) = interpolation(A,A1);
% 
% A = Tracking2D(1:130,:);
% A1 = Tracking2D(91:220,:);
% Tracking2D(91:220,:) = interpolation(A,A1);
% 
% A = Tracking2D(1:130,:);
% A1 = Tracking2D(101:230,:);
% Tracking2D(101:230,:) = interpolation(A,A1);
% 
% A = Tracking2D(1:130,:);
% A1 = Tracking2D(111:240,:);
% Tracking2D(111:240,:) = interpolation(A,A1);
% 
% A = Tracking2D(1:130,:);
% A1 = Tracking2D(121:250,:);
% Tracking2D(121:250,:) = interpolation(A,A1);
% 
% A = Tracking2D(1:150,:);
% A1 = Tracking2D(111:260,:);
% Tracking2D(111:260,:) = interpolation(A,A1);
% 
% A = Tracking2D(1:150,:);
% A1 = Tracking2D(121:270,:);
% Tracking2D(121:270,:) = interpolation(A,A1);
% 
% A = Tracking2D(1:150,:);
% A1 = Tracking2D(131:280,:);
% Tracking2D(131:280,:) = interpolation(A,A1);
% 
% A = Tracking2D(1:160,:);
% A1 = Tracking2D(131:290,:);
% Tracking2D(131:290,:) = interpolation(A,A1);
% 
% A = Tracking2D(1:160,:);
% A1 = Tracking2D(141:300,:);
% Tracking2D(141:300,:) = interpolation(A,A1);
% 
% A = Tracking2D(1:200,:);
% A1 = Tracking2D(111:310,:);
% Tracking2D(111:310,:) = interpolation(A,A1);
% 
% A = Tracking2D(1:200,:);
% A1 = Tracking2D(121:320,:);
% Tracking2D(121:320,:) = interpolation(A,A1);
% 
% A = Tracking2D(1:200,:);
% A1 = Tracking2D(131:330,:);
% Tracking2D(131:330,:) = interpolation(A,A1);
% 
% A = Tracking2D(1:200,:);
% A1 = Tracking2D(141:340,:);
% Tracking2D(141:340,:) = interpolation(A,A1);
% 
% A = Tracking2D(1:200,:);
% A1 = Tracking2D(151:350,:);
% Tracking2D(151:350,:) = interpolation(A,A1);
% 
% A = Tracking2D(1:200,:);
% A1 = Tracking2D(161:360,:);
% Tracking2D(161:360,:) = interpolation(A,A1);
% 
% A = Tracking2D(1:200,:);
% A1 = Tracking2D(171:370,:);
% Tracking2D(171:370,:) = interpolation(A,A1);
% 
% A = Tracking2D(1:250,:);
% A1 = Tracking2D(131:380,:);
% Tracking2D(131:380,:) = interpolation(A,A1);
% 
% A = Tracking2D(1:250,:);
% A1 = Tracking2D(141:390,:);
% Tracking2D(141:390,:) = interpolation(A,A1);
% 
% A = Tracking2D(1:250,:);
% A1 = Tracking2D(151:400,:);
% Tracking2D(151:400,:) = interpolation(A,A1);
% 
% A = Tracking2D(1:250,:);
% A1 = Tracking2D(161:410,:);
% Tracking2D(161:410,:) = interpolation(A,A1);
% 
% A = Tracking2D(1:250,:);
% A1 = Tracking2D(171:420,:);
% Tracking2D(171:420,:) = interpolation(A,A1);
% 
% A = Tracking2D(1:250,:);
% A1 = Tracking2D(181:430,:);
% Tracking2D(181:430,:) = interpolation(A,A1);
% 
% A = Tracking2D(1:250,:);
% A1 = Tracking2D(191:440,:);
% Tracking2D(191:440,:) = interpolation(A,A1);
% 
% A = Tracking2D(1:250,:);
% A1 = Tracking2D(201:450,:);
% Tracking2D(201:450,:) = interpolation(A,A1);
% 
% A = Tracking2D(1:250,:);
% A1 = Tracking2D(211:460,:);
% Tracking2D(211:460,:) = interpolation(A,A1);
% 
% A = Tracking2D(1:250,:);
% A1 = Tracking2D(221:470,:);
% Tracking2D(221:470,:) = interpolation(A,A1);
% 
% A = Tracking2D(1:250,:);
% A1 = Tracking2D(231:480,:);
% Tracking2D(231:480,:) = interpolation(A,A1);
% 
% A = Tracking2D(1:300,:);
% A1 = Tracking2D(191:490,:);
% Tracking2D(191:490,:) = interpolation(A,A1);
% 
% A = Tracking2D(1:300,:);
% A1 = Tracking2D(end-299:end,:);
% Tracking2D(end-299:end,:) = interpolation(A,A1);

figure(1); 
% for i = 0 : length(theFiles)-1
for i = 0 : 99
    imageFile = strcat(Prefix, sprintf('%04d',i), '.jpg');
%    fullFileName = fullfile(myFolder, imageFile);
    %fprintf(1, 'Now reading %s\n', fullFileName);
    thisFrame = imread(imageFile);
    warning('off', 'Images:initSize:adjustingMag');
    imshow(thisFrame);
    
    skeleton = Tracking2D(i+1,:);
    y = skeleton(1:3:end);
    x = skeleton(2:3:end);

    %% Plot key_points
    hold on
    % Draw bones
    line([y(1), y(2)], [x(1), x(2)], 'Color', 'b', 'LineWidth', 3); % 0-1
    line([y(2), y(3)], [x(2), x(3)], 'Color', [1 0.9 0], 'LineWidth', 3); % 1-2
    line([y(3), y(4)], [x(3), x(4)], 'Color', [1 0.8 0], 'LineWidth', 3); % 2-3
    line([y(4), y(5)], [x(4), x(5)], 'Color', [1 1 0], 'LineWidth', 3); % 3-4
    line([y(2), y(6)], [x(2), x(6)], 'Color', [1 0.7 0], 'LineWidth', 3); % 1-5
    line([y(6), y(7)], [x(6), x(7)], 'Color', [0.8 1 0], 'LineWidth', 3); % 5-6
    line([y(7), y(8)], [x(7), x(8)], 'Color', 'g', 'LineWidth', 3); % 6-7
    line([y(2), y(9)], [x(2), x(9)], 'Color', [0 0.8 0.2], 'LineWidth', 3); % 1-8
%     line([y(15), y(9)], [x(15), x(9)], 'Color', [0 1 0.5], 'LineWidth', 3); % 8-9
    line([y(9), y(10)], [x(9), x(10)], 'Color', [0 1 0], 'LineWidth', 3); % 8-9
    line([y(10), y(11)], [x(10), x(11)], 'Color', [0 1 0.3], 'LineWidth', 3); % 9-10
    line([y(11), y(12)], [x(11), x(12)], 'Color', [0 0.8 1], 'LineWidth', 3); % 1-11
    line([y(9), y(13)], [x(9), x(13)], 'Color', [0 0.5 1], 'LineWidth', 3); % 11-12
    line([y(13), y(14)], [x(13), x(14)], 'Color', [0 0 1], 'LineWidth', 3); % 12-13
    line([y(14), y(15)], [x(14), x(15)], 'Color', [0 1 0.5], 'LineWidth', 3); % 8-11
    
    % Draw Key points
    plot(y,x,'r*' )
% Print the figure with the plotted point
%    print(gcf,'-djpeg',strcat('test', sprintf('%04d',i), '.jpg'));
    hold off
    Frames(i+1) = getframe(gcf);
end

movie(Frames);

% function Astar=interpolation(A,A1)
% 
% [num,jnum]=size(A);
% meanA = sum(A,1)/num;
% A = A - repmat(meanA,num,1);
% A0=A;
% 
% zeroentry = find(A1==0);
% if ~isempty(zeroentry)
%     [row,col]= find(A1==0);
%     A0(row,col) = 0;
% 
%     tmp = A1*0;
%     tmp(row,col)=1;
% 
%     meanA1 = sum(A1,1)./(ones(1,jnum).*num-sum(tmp,1));
%     A1 = A1 - repmat(meanA1,num,1);
%     A1(row,col) = 0;
% 
%     [u,d,v] = svd(A'*A);
%     [u0,d0,v0] = svd(A0'*A0);
%     T = u0'*u;
%     [u1,d1,v1] = svd(A1'*A1);
%     Astar = A1*u1*T*u';
% 
%     A1(row,col)=Astar(row,col);
%     A1=A1 + repmat(meanA1,num,1);
% end
% Astar=A1;
% %A1()
% 
% end


