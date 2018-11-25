import pandas as pd
import bayespy as bp

data = pd.read_csv("heart_disease_data1.csv")
heart_disease = pd.DataFrame(data)
#print(heart_disease)

from pgmpy.models import BayesianModel
from pgmpy.estimators import MaximumLikelihoodEstimator,BayesianEstimator
model = BayesianModel([('age','Lifestyle'),('Gender','Family'),('Gender','Lifestyle'),('Family','diet'),('diet','cholestrol'),('Lifestyle','cholestrol'),('heartdisease','diet'),('heartdisease','cholestrol')])
model.fit(heart_disease,estimator=BayesianEstimator)
from pgmpy.inference import VariableElimination
HeartDisease_infer=VariableElimination(model)

print('For age Enter Super Senior Citizen:0 ,Senior citize:1,Middle age:2, Youth: 3, Teen:4')
print('For Gender Enter Male:0, Female :1')
print('For Family History Enter Yes:1, No:0')
print('For diet Enter high:0, Medium:1')
print('For lifestyle Enter Athlete:0, Active:1, Moderate:2, Sedetary:3')
print('For Cholestrol Enter High:0, BoderLine:1, Normal:2')
q=HeartDisease_infer.query(variables=['heartdisease'],evidence={'age':int(input('Enter Age :')),'Gender':int(input('Enter Gender :')),'Family':int(input('Enter Family_History :')),'diet':int(input('Enter diet :')),'Lifestyle':int(input('Enter lifestyle :')),'cholestrol':int(input('Enter cholestrol :'))})
print(q['heartdisease'])
