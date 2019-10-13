import pymzn 
   
# solns = pymzn.minizinc('prodPlan.mzn', 'prodPlanAuto.dzn', output_mode='dict')
# fpOut = open('prodScheduleAuto.dzn', 'a')
# fpOut.write("produce = " + str(solns[0]['produce']) + ";\n")
# fpOut.close()
# #print("produce = " + solns[0]['produce'] + ";\n")
# solns = pymzn.dict2dzn(solns[0])
# print("----------")
# print(solns)
# # fp = open('prodPlanOUTPUT.dzn', 'w')
# # fp.write(solns)
# # fp.close()
# # print("..received output from ProdPlan and saving it in a .dzn file!")   
# pass

# # import os
# # path = os.path.join("G:\\books","/train")
# # print(path)

solns = pymzn.minizinc('prodPlan.mzn', 'prodPlan.dzn', output_mode='dict')
print(solns[0])
print("-------------")
print(solns[0]['produce'])
