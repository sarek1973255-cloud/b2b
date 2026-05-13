import pandas as pd

def save_excel(data, filename="clients.xlsx"):
    df = pd.DataFrame(data)
    df.to_excel(filename, index=False)
    return filename
