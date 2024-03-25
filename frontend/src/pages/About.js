import React from "react";
import Header from "../components/Header/Header";
import Footer from "../components/Footer/Footer";

function About() {
  return (
    <div>
      <Header page="about" />
      <div style={{ marginTop: 50 }}>About Page</div>
      <Footer />
    </div>
  );
}

export default About;
