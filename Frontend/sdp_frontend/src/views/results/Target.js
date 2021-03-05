import {useCallback, useEffect} from 'react';
import {useSelector, useDispatch, shallowEqual} from 'react-redux';
import React from 'react'
import {
  CBadge,
  CDataTable,
  CButton,
  CLink
  
} from '@coreui/react'
import * as userActions from 'src/store/modules/user/actions';
import history from "src/utils/history";

const fields = ['target','timestamp','xss','sqli','open_redirect','windows_directory_traversal','linux_directory_traversal','lfi','rfi','rce_linux','rce_php','ssti']
  
  
  
const Target = () => {
  const dispatch = useDispatch();

  const {
    targets
    } = useSelector((state) => ({
    targets : state.user.targets,
    }), shallowEqual)

  useEffect(() => {
    dispatch(userActions.targets_check())
    return () => {
      dispatch(userActions.reset_msg());
    };
  }, []);
  
  const xss_click = (id) => {
    history.push({
      pathname: "/vulnerabilities",
      state: {id:id, vul: "XSS"}
    });
  }

  const sqli_click = (id) => {
    history.push({
      pathname: "/vulnerabilities",
      state: {id:id, vul: "SQL Injection"}
    });
  }
  
  const or_click = (id) => {
    history.push({
      pathname: "/vulnerabilities",
      state: {id:id, vul: "Open Redirect"}
    });
  }
  const wdt_click = (id) => {
    history.push({
      pathname: "/vulnerabilities",
      state: {id:id, vul: "Windows Directory Traversal"}
    });
  }
  const ldt_click = (id) => {
    history.push({
      pathname: "/vulnerabilities",
      state: {id:id, vul: "Linux Directory Traversal"}
    });
  }
  const lfi_click = (id) => {
    history.push({
      pathname: "/vulnerabilities",
      state: {id:id, vul: "LFI Check"}
    });
  }
  const rfi_click = (id) => {
    history.push({
      pathname: "/vulnerabilities",
      state: {id:id, vul: "RFI Check"}
    });
  }
  const rl_click = (id) => {
    history.push({
      pathname: "/vulnerabilities",
      state: {id:id, vul: "RCE Linux Check"}
    });
  }
  const rp_click = (id) => {
    history.push({
      pathname: "/vulnerabilities",
      state: {id:id, vul: "RCE PHP Check"}
    });
  }
  const ssti_click = (id) => {
    history.push({
      pathname: "/vulnerabilities",
      state: {id:id, vul: "SSTI Check"}
    });
  }

  return (
    <>
      <CDataTable
        items={targets}
        fields={fields}
        bordered
        striped
        size="sm"
        scopedSlots = {{
          'target':
            (item)=>(
              <td>
                <CLink 
                  style={{color: 'red'}} 
                  to={{
                    pathname: "/vulnerabilities",
                    state: {id:item.id}
                  }}
                >
                  {item.target}
                </CLink>
              </td>
            ),
          'xss':(item)=>(
            <td><CButton onClick = {()=>{xss_click(item.id);}} disabled={!item.xss}><CBadge shape="pill" color="danger">{item.xss}</CBadge></CButton></td>
          ),
          'sqli':(item)=>(
            <td><CButton onClick = {()=>{sqli_click(item.id);}} disabled={!item.sqli}><CBadge shape="pill" color="warning">{item.sqli}</CBadge></CButton></td>
          ),
          'open_redirect':(item)=>(
            <td><CButton onClick = {()=>{or_click(item.id);}} disabled={!item.open_redirect}><CBadge shape="pill" color="info">{item.open_redirect}</CBadge></CButton></td>
          ),
          'windows_directory_traversal':(item)=>(
            <td><CButton onClick = {()=>{wdt_click(item.id);}} disabled={!item.windows_directory_traversal}><CBadge shape="pill" color="primary">{item.windows_directory_traversal}</CBadge></CButton></td>
          ),
          'linux_directory_traversal':(item)=>(
            <td><CButton onClick = {()=>{ldt_click(item.id);}} disabled={!item.linux_directory_traversal}><CBadge shape="pill" color="secondary">{item.linux_directory_traversal}</CBadge></CButton></td>
          ),
          'lfi':(item)=>(
            <td><CButton onClick = {()=>{lfi_click(item.id);}} disabled={!item.lfi}><CBadge shape="pill" color="success">{item.lfi}</CBadge></CButton></td>
          ),
          'rfi':(item)=>(
            <td><CButton onClick = {()=>{rfi_click(item.id);}} disabled={!item.rfi}><CBadge shape="pill" color="light">{item.rfi}</CBadge></CButton></td>
          ),
          'rce_linux':(item)=>(
            <td><CButton onClick = {()=>{rl_click(item.id);}} disabled={!item.rce_linux}><CBadge shape="pill" color="dark">{item.rce_linux}</CBadge></CButton></td>
          ),
          'rce_php':(item)=>(
            <td><CButton onClick = {()=>{rp_click(item.id);}} disabled={!item.rce_php}><CBadge shape="pill" color="info">{item.rce_php}</CBadge></CButton></td>
          ),
          'ssti':(item)=>(
            <td><CButton onClick = {()=>{ssti_click(item.id);}} disabled={!item.ssti}><CBadge shape="pill" color="warning">{item.ssti}</CBadge></CButton></td>
          ),
          
      
            
        }}
      />
      

    </>
  )
}

export default Target
