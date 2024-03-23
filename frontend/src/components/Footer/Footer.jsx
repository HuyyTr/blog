import React from "react";
import { Layout } from "antd";

function Footer() {
  return <Layout style={footerStyle}>©2024 My blog</Layout>;
}

const footerStyle = {
  position: "fixed",
  left: 0,
  bottom: 0,
  width: "100%",
  backgroundColor: "#001529",
  color: "#fff",
  textAlign: "center",
  height: "20px", // Đặt chiều cao của footer
};

export default Footer;
