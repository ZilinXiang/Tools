import os
from pdf2image import convert_from_path

def fnameList(path, list_name, suffix='.pdf'):
    for file in os.listdir(path):
        file_path = os.path.join(path, file)
        if os.path.isdir(file_path):
            fnameList(file_path, list_name)
        else:
            if suffix in file_path:
                list_name.append(file_path)

def mkdir(path):
    folder = os.path.exists(path)
    if not folder:
        os.makedirs(path)
        return path+'/'
    else:
        return path+'/'

def pdf2Img(fpdf, f='png', dpi=100):
    fdir = os.path.dirname(os.path.abspath(fpdf))
    name = os.path.abspath(fpdf).split('/')[-1].split('.')[0]
    fdir = fdir+'/conver_figs'
    fdir = mkdir(fdir)

    
    pages = convert_from_path(fpdf, dpi)
    if len(pages) > 1:
        dir_name = mkdir(fdir + name)
        flag = 1
    else:
        flag = 0
    for page in pages:
        if flag:
            page.save(dir_name + str(flag) + '.' + f, f)
            flag += 1
        else:
            page.save(fdir + name +'.'+ f, f)
        

# 指定文件夹（包含要转化的PDF文件）
loc = '/home/zilin/Desktop/dudu'
flist = []
fnameList(loc, flist, '.pdf')
if len(flist) == 0:
    print("--------------------------------------------")
    print("!!!  In the folder: " + loc + ", No .pdf file exist.      ")
    print("--------------------------------------------")
    exit(1)
for item in flist:
        pdf2Img(item)
print("--------------------------------------------")
print("***     All .pdf file are converted!     ***")
print("--------------------------------------------")
