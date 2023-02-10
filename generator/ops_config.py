import datetime
import os
from pathlib import Path

# basic info

CO_NAME = '快扫机器人'

start_time = '2018/01/01 00:00:00'
end_time = '2021/12/30 00:00:00'
time_format_str = '%Y/%m/%d HH:mm:ss'
date_format_str = '%Y/%m/%d'

# working calendar
workday_list = [1,2,3,4,5]

# 假期
holidy_list = []



# paths for data generation

abs_dir = os.path.abspath(__file__)

# get parent dir
par_dir = os.path.dirname(abs_dir)

# path_this_file = Path(abs_dir)
base_name = 'base'
BASE_DIR = os.path.join(os.path.dirname(par_dir), base_name)

generated_name = 'generated'
GE_DIR = os.path.join(os.path.dirname(par_dir), generated_name)


# path for basic operation data
BASE_INFO_PATH  = os.path.join(os.path.dirname(par_dir), '基础核心信息base_model_info.xlsx')

