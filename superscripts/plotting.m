cwd=cd;
cd data
clc
clear all
close all

Data = {'AzoCAM-B3LYPwater','AzoCAM-B3LYPwaternoroot','LaurdanB3LYPtail','LaurdanB3LYPwatertail'};

q=size(Data);
for a = [1:q(2)]
    A=csvread([Data{a}, '.csv'],2,0);

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

x=A(:,1);
v=[2:4;5:7];

for i=1:2
    figure()
    hold on
    grid on
    grid minor
    B=A(:,v(i,:));
    Bsave{i}=B;
    for ii=B
        y=ii;
        plot(x(~isnan(y)),y(~isnan(y)),'LineWidth',2)
        
        indexmin = find(min(y) == y); 
        xmin = x(indexmin); 
        ymin = y(indexmin);
        indexmax = find(max(y) == y);
        xmax = x(indexmax);
        ymax = y(indexmax);
        
        strmin = ['Min = ',num2str(ymin(1)), ' at ', num2str(xmin(1))];
        %text(0,ymin(1),strmin,'HorizontalAlignment','left');

        strmax = ['Max = ',num2str(ymax(1)),' at ', num2str(xmax(1))];
        %text(120,ymax(1),strmax,'HorizontalAlignment','right');
        
        strmax = ['Diff = ',num2str(ymax(1)-ymin(1))];
        %text(170,ymax(1),strmax,'HorizontalAlignment','right');
    end
    xlabel('Degrees')
    if i == 1
        ylabel([' eV'])
    elseif i == 2
        ylabel([' Kcal/mol'])
    end
    legend('GS','S1','T1')
    set(gca,'Color',[0.9 0.9 0.9]);
    title([Data{a}]);
end

end
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%