import os
from box.exceptions import BoxValueError # xử lý các lỗi liên quan đến giá trị không hợp lệ trong Box object
import yaml # đọc và ghi các tệp YAML
from textSummarizer.logging import logger
from ensure import ensure_annotations #kiểm tra kiểu dữ liệu và chú thích hàm
from box import ConfigBox #quản lý cấu hình và dữ liệu
from pathlib import Path 
from typing import Any #Any được sử dụng khi kiểu dữ liệu không được biết trước


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """Đọc tệp YAML và trả về dữ liệu trong ConfigBox

    Args:
        path_to_yaml (str): Đường dẫn đến tệp YAML

    Raises:
        ValueError: Nếu tệp YAML trống
        e: tệp trống

    Returns:
        ConfigBox: đối tượng ConfigBox chứa dữ liệu từ tệp YAML
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file) # Đọc nội dung tệp yaml
            logger.info(f"yaml file: {path_to_yaml} loaded successfully") # Ghi log thông báo đọc yaml thành công
            return ConfigBox(content) # Trả về đối tượng ConfigBox chứa thông tin vừa đọc từ tệp yaml
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e


@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """Tạo danh sách các thư mục

    Args:
        path_to_directories (list): Danh sách đường dẫn của các thư mục
        ignore_log (bool, optional): 
    """
    for path in path_to_directories: 
        os.makedirs(path, exist_ok=True) # Tạo thư mục nếu chưa tồn tại
        if verbose:
            logger.info(f"created directory at: {path}") # Ghi log thông báo đã tạo dir


@ensure_annotations
def get_size(path: Path) -> str:
    """Lấy kích thước tệp (đơn vị KB)

    Args:
        path (Path): đường dẫn của file

    Returns:
        str: size in KB
    """
    size_in_kb = round(os.path.getsize(path)/1024) # Lấy kích thước tệp và chia cho 1024 để chuyển đơn vị KB
    return f"~ {size_in_kb} KB" # Trả về kích thước tệp dưới dạng chuỗi, làm tròn và đơn vị KB