import streamlit as st
import functions


todos=functions.get_todos()
st.set_page_config(layout="wide")

def add_todo():
    # 取得表單值, 必須寫session_state抓表單key
    newdo=st.session_state["newitem"].strip()
    # 防止用戶輸入重複值, 出現 key重複 錯誤
    chk_rep=newdo+'\n'
    if chk_rep not in todos:
        todos.append(chk_rep)
    else:
        st.info("The same item.")
    functions.write_todo(todos)


st.title("Web ToDo App")
st.subheader("This is my todo app.")
st.write("This app is to increase your <u>productivity!</u>",
         unsafe_allow_html=True)

for index,chk_item in enumerate(todos):
    chk_value=st.checkbox(chk_item,key=chk_item)
    if chk_value:
        # 刪除所選項目
        todos.pop(index)
        functions.write_todo(todos)
        # 也必須刪除session
        del st.session_state[chk_item]
        # 因為項目有改, 必須重整整個form
        st.rerun()


st.text_input(label="Enter a todo: ",placeholder="Add new item...",
              key="newitem",on_change=add_todo)




# 可以直接在前端 看目前session的變化, 不用print:
#st.session_state

# 如何執行?
# 在Terminal 執行 streamlit run web.py