import pandas as pd
from tkinter import filedialog

try:
    file = filedialog.askopenfilename(initialdir='./xlsx',title='파일선택', filetypes=(('excel files','*.xlsx'),('all files','*.*')))
    df = pd.read_excel(file, header=None)
    string = list(filter(lambda x: x != "nan", map(str, df[0].tolist())))
    data = sorted(string)
    pd.DataFrame(data).to_excel(file, index=False, header=False)
except PermissionError as e:
    if "[Errno 13]" in str(e):
        print("파일이 열려있거나 디렉토리에 띄어쓰기가 있습니다. 파일을 닫거나 띄어쓰기를 빼보세요.")
