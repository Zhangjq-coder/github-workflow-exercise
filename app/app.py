from collections import defaultdict
from typing import List

def dedupe_header(columns: List[str]) -> List[str]:
    """
    Make header column names unique by appending numeric suffixes to duplicates.
    
    Rules:
    - The first occurrence of a name is kept as-is.
    - The 2nd, 3rd, ... occurrences of the same name get ".1", ".2", ... appended.
      (This mirrors how tools like pandas disambiguate duplicate column labels.)
    - Order is preserved exactly as given.
    - Input is a list of strings (column names); output is a same-length list.
    
    Example:
    ["id", "name", "id", "name", "name"] -> ["id", "name", "id.1", "name.1", "name.2"]
    """
    seen_counts = defaultdict(int)
    result: List[str] = []
    
    for col in columns:
        count = seen_counts[col]
        if count == 0:
            result.append(col)
        else:
            result.append(f"{col}.{count}")
        seen_counts[col] += 1
    
    return result

def add_numbers(a: float, b: float) -> float:
    """
    添加两个数字并返回结果
    
    Args:
        a (float): 第一个数字
        b (float): 第二个数字
    
    Returns:
        float: 两个数字的和
    """
    return a + b

if __name__ == "__main__":
    # 示例用法
    columns = ["id", "name", "id", "name", "name"]
    print(f"原始列名: {columns}")
    print(f"去重后列名: {dedupe_header(columns)}")
    
    # 测试加法功能
    result = add_numbers(5.0, 3.0)
    print(f"5.0 + 3.0 = {result}")