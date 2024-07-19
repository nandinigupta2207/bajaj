import pandas as pd
df=pd.read_csv("/content/DataEngineeringQ2.csv")

df.info()

df['consultationData__medicines__medicineName'].value_counts().iloc[2:3]

df['consultationData__medicines__isActive'].value_counts(normalize=True) * 100

df["patientDetails__lastName"].info()

df["patientDetails__firstName"].info()

df["patientDetails__birthDate"].info()

df["patientDetails__gender"].info()
df['patientDetails__gender'].fillna(df['patientDetails__gender'].mode()[0], inplace=True)
df["patientDetails__gender"].info()
(df['patientDetails__gender'].value_counts(normalize=True) * 100)['F']

from datetime import datetime
from dateutil.relativedelta import relativedelta

def calculate_age(birth_date_str):
  if pd.isna(birth_date_str):
    return None
  try:
    birth_date = datetime.strptime(birth_date_str, '%Y-%m-%d')
    today = datetime.now()
    age = relativedelta(today, birth_date).years
    return age
  except ValueError:
    return None

df['age'] = df['patientDetails__birthDate'].apply(calculate_age)

# Categorizing
def categorize_age(age):
  if age is None:
    return None
  elif age >= 0 and age <= 12:
    return 'Child'
  elif age >= 13 and age <= 19:
    return 'Teen'
  elif age>= 20 and age <= 59:
    return 'Adult'
  else:
    return 'Senior'

df['ageGroup'] = df['age'].apply(categorize_age)
adult_count = df['ageGroup'].value_counts()['Adult']
print(adult_count)


def is_valid_indian_mobile(phone_number):
  if not isinstance(phone_number, str):
    return False
  if len(phone_number) != 10:
    return False
  if not phone_number.isdigit():
    return False
  if not phone_number.startswith(('6', '7', '8', '9')):
    return False
  return True

df['isValidMobile'] = df['phoneNumber'].apply(is_valid_indian_mobile)
df.info()

valid_phone_count = df['isValidMobile'].value_counts()['True']
print(valid_phone_count)
