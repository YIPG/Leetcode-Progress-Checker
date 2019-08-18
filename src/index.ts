import axios from "axios";

type Data = {
  user_name?: string;
};

const getLeetcodeInfo = async () => {
  try {
    const res = await axios("https://leetcode.com/api/problems/algorithms/");
    console.log(res.data);
  } catch (error) {
    console.error(error);
  }
};

getLeetcodeInfo();
