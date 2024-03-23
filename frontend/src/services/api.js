import axios from "axios";

const BASE_URL = process.env.REACT_APP_API_URL;

export const fetchData = async (entry_point) => {
  try {
    const response = await axios.get(`${BASE_URL}/${entry_point}`);
    return response.data;
  } catch (error) {
    throw new Error("Error fetching data");
  }
};
