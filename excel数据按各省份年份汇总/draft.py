import pandas as pd
#读入整理好的数据
excel_file = pd.read_excel(r'C:\Users\chu yuanyue\Desktop\乔老师发的\人口、gdp\人口、gdp汇总_copy.xlsx', sheet_name=None)
regions = []

for _, sheet_data in excel_file.items():
    old_regions = sheet_data.iloc[0:, 0].unique()
    regions = [string.strip() for string in old_regions]

for region in regions:
    file_data = None
    flag = 0
    for sheet_name, sheet_data in excel_file.items():
        grouped_data = sheet_data.groupby('地区')
        for group_name, group_data in grouped_data:
            group_name = group_name.strip()
            if group_name != region:
                continue
            if flag == 0:
                file_data = pd.DataFrame(columns=sheet_data.columns)
                flag = 1
            file_data = pd.concat([file_data, group_data])
            file_data.iloc[-1, 0] = sheet_name
            continue
    file_data.rename(columns={'地区': '年份'}, inplace=True)
    file_name = f'{region}.xlsx'
    file_data.to_excel(file_name, index=False)