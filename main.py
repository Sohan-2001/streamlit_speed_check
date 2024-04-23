
import streamlit as st
import speedtest

# Initialize the speedtest-cli
st.title("Internet Speed Monitor")

@st.cache
def get_speed():
    stt = speedtest.Speedtest()
    stt.get_best_server()
    download_speed = stt.download() / 1_000_000  # Convert to Mbps
    upload_speed = stt.upload() / 1_000_000  # Convert to Mbps
    return download_speed, upload_speed

download, upload = get_speed()

st.write(f"Download speed: **{download:.2f} Mbps**")
st.write(f"Upload speed: **{upload:.2f} Mbps**")