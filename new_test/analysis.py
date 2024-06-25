import pandas as pd
from fuzzywuzzy import fuzz
import os
import re
def macth_lines(truth_file,ocr_file):
    print("varifying data from", ocr_file)
    file1=open(truth_file,"r")
    ground_truth=file1.readlines()
    file2=open(os.path.join("../results",ocr_file),"r")
    hypothesis=file2.readlines()

    df=pd.DataFrame(columns=['REF', 'RESULT','percentage match'])
    n=1
    # print('sentences total lines = ', int(len(ground_truth)),' result total lines = ', int(len(hypothesis)))
    while n < int(len(ground_truth)):
        # print("line number:",n)
        match=fuzz.ratio(re.sub(' +',' ', hypothesis[n].strip()), re.sub(' +',' ',ground_truth[n].strip()))
        data=pd.DataFrame({'REF':[ground_truth[n]],'RESULT': [hypothesis[n]],'percentage match':[match]})
        df=pd.concat([df,data],ignore_index = True, axis = 0)
        n=n+1

    average_match = df['percentage match'].mean()
    print("Average match percentage = ", average_match)
    model_name=ocr_file.replace(".txt","_")
    file_name="../analysis/"+model_name+"analysis.csv"
    df.to_csv(file_name)
    return average_match


model_list=[]
for n in range(1,227):
    model_list.append("8Mdf_DER_"+str(n))

df=pd.DataFrame(columns=['Model name','percentage match'])
for model_name in model_list:
    print ("checking results by model ",model_name)
    match_percent=macth_lines("../sentences.txt",model_name+".txt")
    data=pd.DataFrame({'Model name':[model_name],'percentage match':[match_percent]})
    df=pd.concat([df,data],ignore_index = True, axis = 0)
df.to_csv("../anaylsis_summary.csv")