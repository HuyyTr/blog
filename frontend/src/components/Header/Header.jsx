import React from "react";
import { Link } from "react-router-dom";

import { Layout, Menu } from "antd";

const menuItems = [
  { key: "home", title: "Home", path: "/" },
  { key: "about", title: "About", path: "/about" },
  { key: "contact", title: "Contact", path: "/contact" },
];

function Header(props) {
  return (
    <Layout>
      <Menu
        theme="dark"
        mode="horizontal"
        defaultSelectedKeys={[`${props.page}`]}
      >
        {menuItems.map((item) => (
          <Menu.Item key={item.key}>
            <Link to={item.path}>{item.title}</Link>
          </Menu.Item>
        ))}
      </Menu>
    </Layout>
  );
}

export default Header;
