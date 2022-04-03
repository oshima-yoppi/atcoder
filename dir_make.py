import os
import pathlib
import shutil

n = input("atcoder何番のフォルダを作成する？")
path = n
if os.path.exists(path):
    print("ディレクトリすでに存在しています。")
    bool = input("既存のディレクトリ削除してディレクトリ作り直す？[y/n]")
    if bool == "n":
        exit()
    else:
        shutil.rmtree(path)


os.makedirs(n)
li = ["/a.py", "/b.py", "/c.py", "/d.py", "/e.py", "/f.py"]
for i in li:
    f = pathlib.Path(n + i)
    f.touch()
print(f"ディレクトリ{path}を作成しました。")
