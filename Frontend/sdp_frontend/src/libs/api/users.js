import axios from 'axios';
import {jsonHeader, urls, naverNewsHeader} from '../reqConf';


export const login_api = async (info) => {
  let data = {
    username : info.id,
    password : info.pw
  }
  const response = await axios.get('/auth/login/', {headers: {"Content-Type": `application/json`,}, params: data});
  return response.data;
};

export const register_api = async (info) => {
  let data = {
    username : info.id,
    password : info.pw
  }
  const response = await axios.post('/auth/login/', JSON.stringify(data), {headers: {"Content-Type": `application/json`,}});
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

export const results_api = async () => {
  const token = window.sessionStorage.getItem('token');
  console.log(token)
  const response = await axios.get('/api/url/',{headers: {"Content-Type": `application/json`,"Authorization": `Token ${token}`,}});
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