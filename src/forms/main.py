import streamlit as st
from dishka import Scope

from core.config import SecondaryService, create_dishka_container


def main():
    app_container = create_dishka_container(Scope.APP)

    st.set_page_config(layout="wide")

    st.header("Users")
    users = app_container.get(SecondaryService).get_all()
    st.table([res.model_dump() for res in users])


if __name__ == "__main__":
    main()
