import cgi
import pickle as pkl
import numpy as np

form = cgi.FieldStorage()

age = int(form.getvalue('age'))
gender = int(form.getvalue('gender'))
temp = int(form.getvalue('temp'))
body_pain = int(form.getvalue('pain'))
runny_nose = int(form.getvalue('runny_nose'))
breath = int(form.getvalue('breath'))
nasal_congestion = int(form.getvalue('nasal'))
sore_throat = int(form.getvalue('throat'))
severity = int(form.getvalue('severity'))
contact = int(form.getvalue('contact'))

def load_file(path):
    file = open(path, 'rb')
    data = pkl.load(file)
    file.close()
    return data

onehot_1 = load_file('onehot_1.pkl')
onehot_2 = load_file('onehot_2.pkl')
onehot_3 = load_file('onehot_3.pkl')

minmax_transform = load_file('minmax.pkl')
model = load_file('covid_model.pkl')

gender_array = onehot_1.transform([[gender]]).toarray()
severity_array = onehot_2.transform([[severity]]).toarray()
contact_array = onehot_3.transform([[contact]]).toarray()

X = np.array([[age,temp,body_pain,runny_nose,breath, nasal_congestion, sore_throat]])
X = np.c_[X, gender_array, severity_array, contact_array]

X = minmax_transform.transform(X)
pred = model.predict(X)

if pred[0] == 0:
    msg = 'You are Tested Negative'
else:
    msg = 'You are Tested Positive, Consult a doctor'

print("""
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>Covid Testing App</h1>
    <hr>
    <h2>Prediction is : {}</h2>
</body>
</html>
""".format(msg))

