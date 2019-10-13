
%________________________________________________________________________________________
%                                                                                        |
%  From given budget for resources, find out productions goal that gives maximum profit  |                                                               
%________________________________________________________________________________________|
%


int: nproducts;
set of int: products = 1..nproducts;

% upgrade- profit could be = sellingPrice - resources - productionCost
array[products] of int: profit;
array[products] of string: productName;
array[products] of int: itemsPerBatch;
array[products] of int: demand; % demand of every type of product
array[products] of int: penalty; % penalty of not being able to reach the demand
array[products] of var int: shortage; % demand - produce
array[products] of int: minimumProduce; % minimum number of each type of product we need to produce

%int: maxNumOfBatches; % maximum number of batches that can be processed simultaneously

int: maxNumOfBatches;

constraint  sum(i in products) ( produce[i] div itemsPerBatch[i])  <= maxNumOfBatches ;

constraint forall(p in products)((produce[p] >= minimumProduce[p]) );

int: nresources;
set of int: resources = 1..nresources;

int: budgetForResources;
array[resources] of int: resourceCost;
array[resources] of string: resourceName;

array[products, resources] of int: consumption;
constraint assert(forall(r in resources, p in products)
            (consumption[p,r] >= 0), "Error: negative consumption");
  
% upperlimits, uProduct, uResource
int: uProducts = max(p in products)
                    ( min(r in resources where consumption[p,r]>0)
                       (budgetForResources div (consumption[p,r]*resourceCost[r])) ) ;  
int: uResources = max(r in resources)(budgetForResources div resourceCost[r]);  
  
array[products] of var 0..uProducts : produce;
array[resources] of var 0..uResources : used;

constraint forall(r in resources)
              (used[r] = sum(p in products)(consumption[p,r]*produce[p]));

% we can't use resources within our budget for resources
constraint sum(r in resources)(used[r]*resourceCost[r]) <= budgetForResources;

% shortage is the amount of product we are short of demand
constraint forall(p in products)( shortage[p] = (bool2int(demand[p]>produce[p])) * (demand[p]-produce[p]) );

% obj is (profits - penalty for shortage)
var int: obj = sum(p in products)(profit[p]*produce[p]) - sum(p in products)(penalty[p]*shortage[p]);

solve maximize obj;

output [ show(productName[p]) ++ " = " ++ show(produce[p]) ++ ";\n" |
p in products ] ++
[ show(resourceName[r]) ++ " = " ++ show(used[r]) ++ ";\n" |
r in resources ] ++ ["obj:" ++ show(obj)];


% additional constraints : 
% every product should be produced in a certain amount
% produce mod itemsPerBatch should be minimum

% output [show(itemsPerBatch)];























