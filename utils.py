

TABLE = {}

TABLE['Casualty Severity'] = {
    'code': [1, 2, 3],
    'label': ["Fatal", "Serious", "Slight"]
}

TABLE['Day_of_Week'] = {
    'code': [1, 2, 3, 4, 5, 6, 7],
    'label': ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
}

TABLE['Age Band'] = {
    'code': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
    'label': ['0-5', '6-10', '11-15', '16-20', '21-25', '26-35', '36-45', '46-55', '56-65', '66-75', '>75']
}

TABLE['Sex'] = {
    'code': [1, 2],
    'label': ['Male', "Female"]
}


def code2label(col, code):
    idx = TABLE[col]['code'].index(code)
    return TABLE[col]['label'][idx]
