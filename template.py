import os
from pathlib import Path
import logging

# Cấu hình logging: [YYYY-MM-DD HH:MM:SS,mmm] : Message
logging.basicConfig(level=logging.INFO, format='[%(asctime)s] : %(message)s:')

# Đặt tên dự án
project_name = 'textSummarizer'

# Lập danh sách file cần tạo
list_of_files = [
    '.github/workflow/.gitkeep', # duy trì thư mục 'workflow' ngay cả khi nó trống
    f'src/{project_name}/__init__.py', # Khởi tạo package
    f'src/{project_name}/components/__init__.py', # Khởi tạo compenents submodule để quản lý dự án
    f'src/{project_name}/utils/__init__.py', 
    f'src/{project_name}/utils/common.py', # Chứa các hàm tiện ích sử dụng trong dự án
    f'src/{project_name}/logging/__init__.py', # tổ chức và quản lý hệ thống ghi log của dự án hiệu quả
    f'src/{project_name}/config/__init__.py', 
    f'src/{project_name}/config/configuration.py', # chứa các cài đặt cấu hình: port, dir,... cho ứng dụng
    f'src/{project_name}/pipeline/__init__.py', # Khởi tạo pipeline
    f'src/{project_name}/entity/__init__.py', # Khởi tạo entity
    f'src/{project_name}/constants/__init__.py',
    'config/config.yaml', # Cấu hình file ở định dang yaml
    'app.py', # 
    'main.py', #
    'Dockerfile', #
    'requirements.txt', # Thư viện cần thiết cho mô hình
    'setup.py', 
    'research/trials.ipynb',
]

for filepath in list_of_files:
    # Chuyển filepath thành đối tượng Path
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath) # Lấy thư mục và tên file

    # Nếu tên file không có trong thư mục gôc
    if filedir != '':
        os.makedirs(filedir, exist_ok=True) # Tạo thư mục nếu nó chưa tồn tại 
        logging.info(f'Creating directory:{filedir} for the file {filename}') # tạo logging

    # Kiểm tra filepath xem có tồn tại hay trống không
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath, 'w') as f: # tạo file trống
            pass
            logging.info(f'Creating empty file: {filepath}')

    else:
        logging.info(f'{filename} is already exists') # nếu đã tồn tại tạo logging