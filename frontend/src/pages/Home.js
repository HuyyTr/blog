import React from "react";
import { useParams } from "react-router-dom";
import Body from "../components/Body/Body";
import Header from "../components/Header/Header";
import Footer from "../components/Footer/Footer";

function Home() {
  let params = useParams();
  return (
    <div>
      <Header page="home" />
      <div>Home Page</div>
      <Body slug={params.slug} />
      <Footer />
    </div>
  );
}

export default Home;
