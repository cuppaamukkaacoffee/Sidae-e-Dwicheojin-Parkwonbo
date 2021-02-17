import axios from 'axios';
import {jsonHeader, urls, naverNewsHeader} from '../reqConf';


export const login_api = async (info) => {
  let data = {
    username : info.id,
    password : info.pw
  }
  const response = await axios.post('/auth/login/',JSON.stringify(data) ,{headers: {"Content-Type": `application/json`,}});
  return response.data;
};

export const register_api = async (info) => {
  let data = {
    username : info.id,
    password : info.pw
  }
  const response = await axios.post('/auth/register/', JSON.stringify(data), {headers: {"Content-Type": `application/json`,}});
  return response.data;
};

export const urlCheck_api = async (url) => {
  let data = {
    url : url
  }
  const token = window.sessionStorage.getItem('token');
  console.log(token)
  const response = await axios.post('/api/url/', JSON.stringify(data), {headers: {"Content-Type": `application/json`,"Authorization": `Token ${token}`,}});
  return response.data;
};

export const results_api = async (info) => {
  const id = window.sessionStorage.getItem('id'); 
  const token = window.sessionStorage.getItem('token');
  const data = {
    username : id,
    target : info.url,
    sub_path : "",
    vulnerability : info.vul,
    result_string : ""
  }
  const response = await axios.post('/scan/query/', JSON.stringify(data), {headers: {"Content-Type": `application/json`,"Authorization": `Token ${token}`,}});
  return response.data;
};

export const results_detail_api = async (id) => {
  const token = window.sessionStorage.getItem('token');
  console.log(token)
  const response = await axios.get(`/api/url/${id}`,{headers: {"Content-Type": `application/json`,"Authorization": `Token ${token}`,}});
  return response.data;
};


export const results_delete_api = async (id) => {
  const token = window.sessionStorage.getItem('token');
  console.log(token)
  const response = await axios.delete(`/api/url/${id}`,{headers: {"Content-Type": `application/json`,"Authorization": `Token ${token}`,}});
  return response.data;
};