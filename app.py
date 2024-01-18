## Create a simple flask application where in we want to put some marks (3 subjects) thencalculate the average marks and give the result
## if the marks is less than 50 then mark the result as failed and if its greater than 50 then mark it as pass.

from flask import Flask, render_template, request, redirect, url_for

##create flask app
app=Flask(__name__)

@app.route('/success/<int:score>')
def success(score):
    return 'the score is '+ str(score)

@app.route('/fail/<int:score>')
def fail(score):
    return 'the person has failed and the score is '+ str(score)


@app.route('/calculate',methods=['POST','GET'])
def calculate():
    if request.method=='GET':
        return render_template('calculate.html')
    else:
        Maths=float(request.form['Maths'])
        science=float(request.form['science'])
        economics=float(request.form['economics'])

        average_marks=(Maths+science+economics)/3
        result=''
        if average_marks>=50:
            result='success'
        else:
            result='fail'
        
        return redirect(url_for(result,score=average_marks))

        #return render_template('result.html',results=average_marks)


if __name__=='__main__':
    app.run(debug=True)