%_______________________________________________________________
%_______________________________________________________________|
%                                                               |
% Assignment of workers to different processes for next N days  |                                                               
%_______________________________________________________________|
%_______________________________________________________________|
%

include "globals.mzn";

int: nDays;
set of int: days = 1..nDays;

int: nprocesses;
set of int: processes = 1..nprocesses;

int: nworkers;
set of int: workers = 1..nworkers;

array[processes] of string: processName;
array[processes] of int: minimumWorkers;

array[workers] of string: workerName;

array[processes, workers] of int: ability;

array[workers,days] of var processes : assignment;   % the goal is to find this array - the assignment of each worker for a particular day to a process. 


% in a day, each process must have a minimum number of workers
constraint forall(d in days)
           (  global_cardinality_low_up( [assignment[w,d]|w in workers], [p|p in processes], [m| m in minimumWorkers], [nworkers| m in minimumWorkers] )  );


% don't want one worker to do the same job for three consecutive days... so that workers are not bored
constraint forall(p in processes)
            ( forall(w in workers, d in 1..nDays-2)
              ( (assignment[w,d]=p /\ assignment[w,d+1]=p ) -> (assignment[w,d+2]!=p) )
              );

array[processes] of int: maxAbility = [sum(w in workers)(ability[p,w]) | p in processes ];

int: totalMaxAbility = nDays*(sum(p in processes)(maxAbility[p])) ;

% we want as many as trained/able workers for a particular job
var 0..totalMaxAbility: obj;
constraint obj = sum( w in workers, d in days)( ability[assignment[w,d] ,w]);
           
solve maximize obj;

output  ["\n[format : process => day]\n"] ++
        [ if d == 1 then "\n" ++ show(workerName[w])++ "\n" else " " endif
        ++ show(assignment[w,d]) ++ " => "++ show(d) ++", "|
         w in 1..nworkers, d in 1..nDays ]
         ++  ["\nobj:" ++ show(obj)];

%___________________________________________________________________________________________
% omitted constraints -- replaced with globals cardinality functions and other optimizations

% array[workers,processes] of var int: count = forall(w in workers)(
%                                                       forall(p in processes)(
%                                                             sum(d in days)(bool2int(assignment[w,d] = p) )
%                                                         ));


% constraint forall(w  in workers,p in processes)( (count[w,p]>=0 ) -> (ability[p,w]=1) );

% array[days, processes] of var int: count;
% constraint  forall(d in days)
%             ( forall( p in processes) 
%             ( count[d,p] = sum( w in workers)(assignment[w,d]=p) )); 

% constraint forall(d in days)
%           ( forall( p in processes) 
%             ( count[d,p] >= minimumWorkers[p] ) );
% output ["obj:" ++ obj];

% solve :: int_search(
% obj,
% first_fail,
% indomain_min,
% complete)
% maximize obj;