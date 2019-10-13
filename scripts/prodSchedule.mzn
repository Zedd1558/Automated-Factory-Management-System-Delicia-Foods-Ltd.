%_______________________________________________________________
%                                                               |
% Scheduling various stages of productions based on precedences |                                                               
%_______________________________________________________________|
%

include "globals.mzn";

int: nprocesses;
set of int: processes = 1..nprocesses;

int: nproducts;
set of int: products = 1..nproducts;

array[products] of int: produce;
array[products] of float: itemsPerBatch;
array[products] of string: productName;
array[products,processes] of int: duration;
array[products] of int: height = [ceil((produce[p]*1.0) / (itemsPerBatch[p]*1.0))|p in products];
array[processes] of string: processName;

array[processes] of int: maxNumOfBatches; % limitx

int: totalDuration = sum(i in products, j in processes)(duration[i,j]);

array[products,processes] of var 0..1000 : start;
array[products,processes] of var 0..1000: end;

var 1..totalDuration: span;

% handle the precedences
predicate prec(int:x , int: y, int: prod, array[int,int] of var int: s, array[int,int] of var int: d) = s[prod,x] + d[prod,x] <= s[prod,y];

constraint forall(prod in products)(
            forall(i,j in processes where j = i+1)
              ( prec(i,j,prod,start,duration) )
            );

% constraint prec(1,2,1,start,duration);
% constraint prec(2,3,1,start,duration);
% constraint prec(3,4,1,start,duration);
% constraint prec(4,5,1,start,duration);

% constraint prec(1,2,2,start,duration);
% constraint prec(2,3,2,start,duration);
% constraint prec(3,4,2,start,duration);
% constraint prec(4,5,2,start,duration);

% constraint prec(1,2,3,start,duration);
% constraint prec(2,3,3,start,duration);
% constraint prec(3,4,3,start,duration);
% constraint prec(4,5,3,start,duration);


constraint forall(prod in products) ( maximum(span, [end[prod,i]|i in processes] ) );
constraint forall(i in products, j in processes)(end[i,j] = start[i,j] + duration[i,j]); % end = start + duration;

constraint forall(proc in processes)
             ( cumulative( [start[i,proc]|i in products] , [duration[i,proc]|i in products] , height , maxNumOfBatches[proc]) );



solve minimize span;


% solve :: int_search(
% start ++ [span, maxNumOfBatches],
% % start ++ [makespan],
% first_fail,
% indomain_min,
% complete)
% % satisfy;
% minimize span;
% output ["total Duration:" ++ show(height)];