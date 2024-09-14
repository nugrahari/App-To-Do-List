import axios from "axios";

// const url = "http://192.168.125.51:8000/";
const url = "http://localhost:8000/";

export const authAxios = axios.create({
    baseURL: url,
    timeout: 10000,
});
