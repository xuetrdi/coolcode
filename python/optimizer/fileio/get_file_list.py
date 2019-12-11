import os


def get_file_list(unprocess_file_dir, symbol="txt"):
  """根据提供的目录获取所有的符合规则的文件名列表

  Args:
    unprocess_file_dir: 待处理的文件所在的目录
  Return:
    文件路径列表
  """
  return map(lambda x: os.path.join(unprocess_file_dir, x),
             (filter(lambda x: x.endswith(symbol), os.listdir(unprocess_file_dir))))
