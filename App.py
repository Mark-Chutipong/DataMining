from flask import Flask,render_template,request
import pickle
import pandas as pd
import sklearn
app = Flask(__name__)

def transform_ot(overtime):
    new_data =[]
    for i in overtime:
        if i == "Yes":
            new_data.append(1)
        else :
            new_data.append(0)
    return new_data

def transform_data(data):
    data['OverTime']=transform_ot(data['OverTime'])
    return data

def predict(new_data):
    result = ''
    filename ='/Users/chutipongpansantaveekun/Documents/Work/4th Year/1st Semmester/ITE-436 Data Mining/Project/projectRandomForest2.clf'
    clf8 = pickle.load(open(filename,'rb'))
    new_df = pd.DataFrame(new_data)
    result = clf8.predict(new_df)
    print(result)
    return 'Will Stay' if result[0] == 0 else 'Will Left' 

@app.route('/', methods=['POST','GET'])
def index():
    if request.method == "POST" :
        age = int(request.form['Age'])
        estat = int(request.form['EnvironmentSatisfaction'])
        jinvol = int(request.form['JobInvolvement'])
        jlevel = int(request.form['JobLevel'])
        jstat = int(request.form['JobSatisfaction'])
        mrate = int(request.form['MonthlyRate'])
        ot = request.form['OverTime']
        psh = int(request.form['PercentSalaryHike'])
        rstat = int(request.form['RelationshipSatisfaction'])
        totalyear = int(request.form['TotalWorkingYears'])
        wlb = int(request.form['WorkLifeBalance'])
        yearatcomp = int(request.form['YearsAtCompany'])
        yearwman = int(request.form['YearsWithCurrManager'])
        lastpro = int(request.form['YearsSinceLastPromotion'])


        try :
            new_data ={'Age':[age],'EnvironmentSatisfaction':[estat], 'JobInvolvement':[jinvol],
                       'JobLevel':[jlevel],'JobSatisfaction':[jstat],'MonthlyRate':[mrate],
                       'OverTime':[ot],'PercentSalaryHike':[psh],'RelationshipSatisfaction':[rstat],
                       'TotalWorkingYears':[totalyear],'WorkLifeBalance':[wlb],'YearsAtCompany':[yearatcomp],
                       'YearsSinceLastPromotion':[lastpro],'YearsWithCurrManager':[yearwman]}
            new_data = transform_data(new_data)
            result = predict(new_data)
            return render_template('index.html', result=result)
        except :
            return 'Error'
    else :
        return render_template('index.html', result='-----')

if __name__ == '__main__':
    app.run(debug=True)
