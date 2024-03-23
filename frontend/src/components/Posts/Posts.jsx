import React from "react";
import PostDetail from "../PostDetail/PostDetail";

function Posts(props) {
  return (
    <div>
      <ul>
        {props.data.map((item, index) => (
          <li key={index} style={{ marginBottom: 20 }}>
            <PostDetail index={index} item={item} />
          </li>
        ))}
      </ul>
    </div>
  );
}

export default Posts;
