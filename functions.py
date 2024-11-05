# 絕對路徑或相對路徑, windows 絕對路徑在字串前加 r"E:\...\..."
import os.path
import sys

FILEPATH = 'todos.txt'
def get_todos(file_route=FILEPATH):
    """ Read a text file and return the list
    of to-do item.
    """
    # 如果檔案不存在, 先新增
    if not os.path.exists(file_route):
        with open(file_route,'w',encoding='utf-8') as file:
            pass

    with open(file_route, 'r',encoding='utf-8') as file_local:
        todos_local = file_local.readlines()
    return todos_local


# below print will show documenting code
# print(help(get_todos))

# It would be show error: non-default parameter follows default parameter
# def write_todo(file_route='files/todos.txt',todos_args):
def write_todo(todos_args, file_route=FILEPATH):
    """ Write the to-do item list in the text file. """
    with open(file_route, 'w',encoding='utf-8') as file:
        file.writelines(todos_args)

#這個函式的目的是為了在不同的執行環境中（直接執行或打包後）
#都能正確獲取檔案的路徑，使得資源（如圖片、檔案等）能夠被順利加載。
def resource_path(relative_path):
    base_path=getattr(sys,'_MEIPASS', os.path.abspath(".."))
    return os.path.join(base_path,relative_path)

# below print will show documenting code
# print(help(write_todo))

# 測試從外部引入此module會發生什麼事
# print(__name__)
# module 被外部程式 引入後, 下方條件式內不會被執行。
# 只可以在這裡被執行。
if __name__ == "__main__":
    print("hello from functions")
    print(get_todos())
