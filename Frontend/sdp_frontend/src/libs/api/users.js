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


export const results_api = async (info) => {
  const token = window.sessionStorage.getItem('token');
  const data = {
    username : info.id,
    target : info.url,
    sub_path : "",
    scan_type :info.scan_type,
    vulnerability : info.vul,
    result_string : info.result_string,
    with_headers : info.with_headers,
    scan_session_id : info.scan_session_id
  }
  const response = await axios.post('/scan/query/', JSON.stringify(data), {headers: {"Content-Type": `application/json`,"Authorization": `Token ${token}`,}});
  return response.data;
};

export const targets_api = async () => {
  const token = window.sessionStorage.getItem('token');
  const id = window.sessionStorage.getItem('id');
  const data = {
    username : id,
    targets_only : true
  }
  const response = await axios.post('/scan/query/', JSON.stringify(data), {headers: {"Content-Type": `application/json`,"Authorization": `Token ${token}`,}});
  return response.data;
};

export const net_targets_api = async (info) => {
  const token = window.sessionStorage.getItem('token');
  const data = {
    username : info.id,
    target : info.url
  }
  const response = await axios.post('/netscan/target/', JSON.stringify(data), {headers: {"Content-Type": `application/json`,"Authorization": `Token ${token}`,}});
  return response.data;
};

export const net_results_api = async (info) => {
  const token = window.sessionStorage.getItem('token');
  const data = {
    username : info.username,
    scan_session_id : info.scan_session_id
  }
  const response = await axios.post('/netscan/result/', JSON.stringify(data), {headers: {"Content-Type": `application/json`,"Authorization": `Token ${token}`,}});
  return response.data;
};
