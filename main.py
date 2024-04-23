
import streamlit as st
import speedtest

# Initialize the speedtest-cli
st.title("@MASK Speed Monitor")


def get_speed():
    stt = speedtest.Speedtest(secure=True)
    stt.get_servers(servernames)
    ping=sst.results.ping
    download_speed = stt.download() / (1024**2)  # Convert to Mbps
    upload_speed = stt.upload() / (1024**2)  # Convert to Mbps
    return download_speed, upload_speed, ping

download, upload, ping = get_speed()

st.write(f"Download speed: **{download:.2f} Mbps**")
st.write(f"Upload speed: **{upload:.2f} Mbps**")
st.write(f"Ping: **{ping}")
