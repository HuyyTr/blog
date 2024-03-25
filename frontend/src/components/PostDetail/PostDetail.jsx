import React from "react";
import { Link } from "react-router-dom";

const PostDetail = (props) => {
  return (
    <div>
      <div>{props.item.title}</div>
      <Link to={"/post/" + props.item.slug}>
        <img src={props.item.image} alt={"image" + props.index} />
      </Link>
      <div dangerouslySetInnerHTML={{ __html: props.item.html_content }} />
      <div>{props.item.excerpt}</div>
    </div>
  );
};

export default PostDetail;
