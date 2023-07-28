import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder

pitch_data = pd.read_csv('mlbpitchdata.csv') 

y = pitch_data.Pitch
pitch_features = ['Velocity', 'Spin Rate', 'Horizontal', 'Vertical']
X = pitch_data[pitch_features]

label_encoder = LabelEncoder()
y = label_encoder.fit_transform(y)

model = RandomForestClassifier()
model.fit(X, y)

Velocity = float(input('Enter the value for Velocity (mph): '))
SpinRate = float(input('Enter the value for Spin Rate: '))
Horizontal = float(input('Enter the value for Horizontal Break: '))
Vertical = float(input('Enter the value for Vertical Break: '))

input_data = [[Velocity, SpinRate, Horizontal, Vertical]]
predicted_class = model.predict(input_data)
predicted_class = label_encoder.inverse_transform(predicted_class)

predicted_probabilities = model.predict_proba(input_data)
class_labels = label_encoder.classes_
probabilities = dict(zip(class_labels, predicted_probabilities[0]))


print(f'The predicted class for the input values [{Velocity}, {SpinRate}, {Horizontal}, {Vertical}] is: {predicted_class[0]}')
print('Predicted Class Probabilities:')
for class_label, probability in probabilities.items():
    print(f'{class_label}: {int(probability*100)}%')