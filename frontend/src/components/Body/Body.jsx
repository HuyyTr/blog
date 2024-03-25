import { React, useState, useEffect } from "react";
import Posts from "../Posts/Posts";
import PostDetail from "../PostDetail/PostDetail";
import { fetchData } from "../../services/api";

const Body = (props) => {
  const [data, setData] = useState(null);
  useEffect(() => {
    const fetchDataFromApi = async () => {
      let entry_point;
      if (typeof props.slug === "undefined") {
        entry_point = "post/";
      } else {
        entry_point = "post/?slug=" + props.slug;
      }
      try {
        const result = await fetchData(entry_point);
        console.log("data: ", result);
        setData(result.results);
      } catch (error) {
        console.error("Error fetching data: ", error.message);
      }
    };

    fetchDataFromApi();
  }, [props.slug]);

  return (
    <div>
      {typeof props.slug === "undefined" ? (
        data ? (
          <Posts data={data} />
        ) : (
          <p>Loading ...</p>
        )
      ) : data ? (
        <PostDetail index="0" item={data[0]} />
      ) : (
        <p>Loading ...</p>
      )}
    </div>
  );
};

export default Body;
