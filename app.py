import streamlit as st

from bear_marriage.data import read_points
from bear_marriage.find_pairs import connect_points
from bear_marriage.plotting_utils import plot_pairs_plotly

st.header("Bear Marriage Application")

with st.sidebar:
    st.header("Load your Data")

    file = st.file_uploader(label="Upload your data", type="txt")
    if file is None:
        st.info("file is not uploaded yet")
    else:
        st.success("successfully loaded")
    
    # choose method
    method = st.selectbox(
        label="Select method for finding pairs",
        options=["line", "hull", "both"]
    )

    build = st.button("Build")
    
    
# parse data
if file is not None and build:
    points = read_points(file)
    
    st.subheader("First 5 of you loaded points:")
    st.write(points[:5])

    # calculate
    if method in ["hull", "both"]:
        pairs = connect_points(points, method="hull")
        # output
        st.subheader("Result Vizualization")
        fig = plot_pairs_plotly(pairs)
        st.plotly_chart(fig)
    if method in ["line", "both"]:
        pairs = connect_points(points, method="line")
        # output
        st.subheader("Result Vizualization")
        fig = plot_pairs_plotly(pairs)
        st.plotly_chart(fig)
    
    st.subheader("First 5 of bear pairs:")
    st.write(pairs[:5])