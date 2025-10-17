import pandas as pd
import os 
import time

# def unzip_csv_gz(folder='raw_data', output_folder='data'):
#     os.makedirs(output_folder, exist_ok=True)

#     for i, filename in enumerate(os.listdir(folder)):
#         file_path=os.path.join(folder, filename)
#         print(file_path)

#         filename_clean=filename.split(".")[0]
#         file_outpath=os.path.join(output_folder,filename_clean+".csv")
#         print(file_outpath)

#         if not filename_clean in [fn.split('.')[0] for fn in os.listdir(output_folder)]:
#             df = pd.read_csv(file_path, compression='gzip', encoding='utf-8')
#             df.to_csv(file_outpath, index=False)
#             print(f"{i} ✔ {filename_clean} converted and saved in {output_folder}! \n")
#         else :
#             print(f"{i} {filename_clean} already exists in {output_folder}!\n")
#     return



def unzip_csv_gz(folder='raw_data', output_folder='data'):
    os.makedirs(output_folder, exist_ok=True)

    for i, filename in enumerate(os.listdir(folder)):
        file_path = os.path.join(folder, filename)

        # 只处理 .gz 文件
        if not filename.endswith('.gz'):
            print(f"{i} {filename} is not a gzip file, skipped.\n")
            continue

        filename_clean = os.path.splitext(filename)[0]  # 去掉 .gz
        file_outpath = os.path.join(output_folder, filename_clean)

        # 如果输出文件已存在，跳过
        if os.path.exists(file_outpath):
            print(f"{i} {filename_clean} already exists in {output_folder}!\n")
            continue

        try:
            df = pd.read_csv(file_path, compression='gzip', encoding='utf-8')
            df.to_csv(file_outpath, index=False)
            print(f"{i} ✔ {filename_clean} converted and saved in {output_folder}!\n")
        
        except Exception as e:
            print(f"{i} ❌ Error converting {filename}: {e}\n")
