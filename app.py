from flask import Flask,render_template,request
import pickle
import os


app=Flask(__name__)



file=open('modell.pkl','rb')
clf=pickle.load(file)
file.close()

'''scores = {} # scores is an empty dict already

if os.path.getsize(target) > 0:      
    with open(target, "rb") as f:
        unpickler = pickle.Unpickler(f)
        # if file is not empty scores will be equal
        # to the value unpickled
        scores = unpickler.load()'''



@app.route('/' , methods=['GET','POST'])
def hello():
	if request.method == 'POST':
		myDict = request.form 
		Road=int(myDict['Road_Type'])
		Speed=int(myDict['Speed_limit'])
		Light=int(myDict['Light_Conditions'])
		Weather=int(myDict['Weather_Conditions'])
		Road_Surface=int(myDict['Road_Surface_Conditions'])
		Urban=int(myDict['Urban_or_Rural_Area'])
		input_features=[Road,Speed,Light,Weather,Road_Surface,Urban]
		infprob=clf.predict_proba([input_features])[0][1]
		print(infprob)

		if infprob > 0.5:
			return render_template('show.html',inf='Accident Severity Is Very High  {}'.format(infprob))
		else:
    		 return render_template('show.html',inf='Accident Severity Is Very Low {}'.format(infprob))
		

	return render_template('index.html')

	#return 'hello' + str(infprob)




if __name__ == '__main__':
	app.run(debug=True)