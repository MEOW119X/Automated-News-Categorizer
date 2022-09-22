import pandas as pd

def count_values(df , columns='label'):
    """Counting the total numbers of the specific lebel"""
    
    label = []
    u_names = []
    count = []
    for i in df[columns]:
        label.append(i)
    for names in label:
        if names not in u_names:
            names = str(names)
            u_names.append(names)
    for num in u_names:
        count.append(label.count(num))
    return pd.DataFrame({'Label': u_names, 'Numbers': count})


if __name__ == '__main__':
    pass