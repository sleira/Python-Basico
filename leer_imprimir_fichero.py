filepath = "C:\PythonScripts\kk.txt"
with open(filepath) as fp:
    for i, line in enumerate(fp):
        if i >= 10:
            print(fp.read())