import React, {useCallback, useState, useEffect } from 'react';
import {useSelector, useDispatch, shallowEqual} from 'react-redux';
import useWebSocket, { ReadyState } from 'react-use-websocket';

import {
    CCard,
    CCardBody,
    CRow,
    CCol,
    CCardHeader,
    CForm,
    CFormGroup,
    CLabel,
    CInput,
    CFormText,
    CCardFooter,
    CButton,
    CSpinner,
    CToaster,
    CToast,
    CToastHeader,
    CToastBody,
    CProgress,
    CSwitch,
    CCollapse,
    CListGroupItem,
    CDataTable,
    CFade,
    CBadge
  } from '@coreui/react'
  import CIcon from '@coreui/icons-react'
import * as loadingActions from 'src/store/modules/loading/actions';
import * as userActions from 'src/store/modules/user/actions';
  
  const fields = ['ip_address','port_number','port_protocol','port_status']

  const Netscan = () => {
    const dispatch = useDispatch();
    const [toast_Active,set_toast_Active] = useState(false)
    const [collapseMulti, setCollapseMulti] = useState([false, false, false])
    const [col1,setCol1] = useState(true)
    const [col2,setCol2] = useState(true)
    const [col3,setCol3] = useState(true)
    const [col4,setCol4] = useState(true)
    const [col5,setCol5] = useState(true)
    const [col6,setCol6] = useState(true)
    const [col7,setCol7] = useState(true)
    const [col8,setCol8] = useState(true)
    const [col9,setCol9] = useState(true)
    const [col10,setCol10] = useState(true)
    const [col11,setCol11] = useState(true)
    const [col12,setCol12]= useState(true)
    const [col13,setCol13] = useState(true)
    const [col14,setCol14] = useState(true)
    const [col15,setCol15] = useState(true)
    const [col16,setCol16] = useState(true)
    const [col17,setCol17] = useState(true)
    const [col18,setCol18] = useState(true)


    const {
      url,
      port_from,
      port_to,
      port_results,
      scan_rate,
      whois_flag,
      robot_flag,
      whois_results,
      robot_results,
      ip_addresses,
      process,
      console,
      loading,
      } = useSelector((state) => ({
        url: state.user.url,
        port_from : state.user.port_from,
        port_to : state.user.port_to,
        port_results : state.user.port_results,
        scan_rate : state.user.scan_rate,
        whois_flag : state.user.whois_flag,
        robot_flag : state.user.robot_flag,
        whois_results : state.user.whois_results,
        robot_results : state.user.robot_results,
        ip_addresses : state.user.ip_addresses,
        process : state.loading.process,
        console: state.loading.console,
        loading: state.loading.loading,
      }), shallowEqual)
    

    const {
      sendMessage,
      lastMessage,
      readyState,
    } = useWebSocket('ws://localhost:8000/ws/netscan/');

    const connectionStatus = {
      [ReadyState.CONNECTING]: 'Connecting',
      [ReadyState.OPEN]: 'Open',
      [ReadyState.CLOSING]: 'Closing',
      [ReadyState.CLOSED]: 'Closed',
      [ReadyState.UNINSTANTIATED]: 'Uninstantiated',
    }[readyState];

    useEffect(() => {
      if(lastMessage != null){
        const results = JSON.parse(lastMessage.data);
        if(results.whois){
          dispatch(userActions.set_whois_results(results.whois))
        }
        else if(results.robot){
          dispatch(userActions.set_robot_results(results.robot))
        }
        else if(results.collected_ip){
          dispatch(userActions.set_ip_addresses(results))
        }
        else if(results.port_number){
          dispatch(userActions.set_port_results(results))
        }
        else if(results.process){
          const process = parseFloat(results.process.split("%")[0])
          dispatch(loadingActions.set_process(process))
        }
        else if(results.message){
          dispatch(loadingActions.set_loading_console(results.message))
          if(results.message == "collecting whois information..."){
            setCollapseMulti([true,false,false]);
          }
          else if(results.message == "collecting robot.txt information..."){
            setCollapseMulti([false,true,false]);
          }
          else if(results.message == "collecting ip addresses..."){
            setCollapseMulti([false,false,true]);
          }
          else if(results.message == "all good"){
            setCollapseMulti([true,false,false]);
            set_toast_Active(true);
          }
        }
      }
    }, [lastMessage]);

    useEffect(() => {
      dispatch(userActions.set_port_from("0"));
      dispatch(userActions.set_port_to("65535"));
      dispatch(userActions.set_scan_rate("100"));
      return () => {
        dispatch(loadingActions.finishLoading());
        dispatch(userActions.reset_msg())
      };
    }, []);

    useEffect(() => {
      if(connectionStatus == 'Closed'){
        dispatch(loadingActions.finishLoading());
      }
    }, [connectionStatus]);
    
    useEffect(() => {
      if(toast_Active == true){
        setTimeout(() => {
          set_toast_Active(false)
        },5000)
      }
    },[toast_Active])

    const handleClickSendMessage = useCallback(() =>{
      if(url.length > 0 && port_from.length > 0 && port_to.length > 0){
        const token = sessionStorage.getItem('token');
        dispatch(loadingActions.startLoading());
        sendMessage(JSON.stringify({"token": `Token ${token}`,
                                    "target": url,
                                    "port_range": `${port_from}-${port_to}`,
                                    "rate": scan_rate,
                                    "whois_flag":whois_flag,
                                    "robot_flag":robot_flag
                                  }))
      }else{
        alert("양식 제대로")
      }
     }, [url,port_from,port_to,scan_rate,whois_flag, robot_flag]);
    
    const handleInputurl = (e) => {
      dispatch(userActions.set_url(e.target.value))
    }
    const handlePortFrom = (e) => {
      dispatch(userActions.set_port_from(e.target.value))
    }
    const handlePortTo = (e) => {
      dispatch(userActions.set_port_to(e.target.value))
    }
    const handleScanRate = (e) => {
      dispatch(userActions.set_scan_rate(e.target.value))
    }
    const handleWhois_flag = (e) => {
      dispatch(userActions.set_whois_flag(e.target.checked))
    }
    const handleRobot_flag = (e) => {
      dispatch(userActions.set_robot_flag(e.target.checked))
    }

     return (
      <>
        <CRow>
          <CCol sm = "12" md = "5">
            <CCard accentColor="primary">
              <CCardHeader>
                Network Scan
              </CCardHeader>
              <CCardBody>
                <CForm action="" method="post" encType="multipart/form-data" className="form-horizontal">
                  <CFormGroup row>
                    <CCol md="3">
                        <CLabel htmlFor="text-input">Target URL</CLabel>
                    </CCol>
                    <CCol xs="12" md="9">
                        <CInput id="text-input" name="text-input" placeholder="URL" onChange={handleInputurl}/>
                        <CFormText>ex) https://www.naver.com</CFormText>
                    </CCol>
                    </CFormGroup>
                    <CFormGroup row>
                    <CCol md="3">
                        <CLabel htmlFor="text-input">Port Range</CLabel>
                    </CCol>
                    <CCol xs="12" md="6">
                      <CRow>
                        <CCol><CInput id="text-input" name="text-input"  placeholder = {port_from} onChange={handlePortFrom}/></CCol>_
                        <CCol><CInput id="text-input" name="text-input" placeholder = {port_to} onChange={handlePortTo}/></CCol>
                      </CRow>
                    </CCol>
                    </CFormGroup>
                    <CFormGroup row>
                      <CCol md="3">
                          <CLabel htmlFor="text-input">Scan Rate</CLabel>
                      </CCol>
                      <CCol xs="12" md="3">
                          <CInput id="text-input" name="text-input" placeholder="Scan Rate" placeholder = {scan_rate} onChange = {handleScanRate}/>
                      </CCol>
                    </CFormGroup>
                    <CFormGroup row>
                      <CCol md="3">
                        <CLabel htmlFor="select">Whois Flag</CLabel>
                      </CCol>
                      <CCol xs="12" md="9">
                        <CSwitch className={'mx-1'} variant={'3d'} color={'primary'} defaultChecked onChange={handleWhois_flag}/>
                      </CCol>
                    </CFormGroup>
                    <CFormGroup row>
                      <CCol md="3">
                        <CLabel htmlFor="select">Robot Flag</CLabel>
                      </CCol>
                      <CCol xs="12" md="9">
                        <CSwitch className={'mx-1'} variant={'3d'} color={'primary'} defaultChecked onChange={handleRobot_flag}/>
                      </CCol>
                    </CFormGroup>
                </CForm>
              </CCardBody>
              <CCardFooter>
                <CButton type="button" size="sm" color="primary" onClick={handleClickSendMessage} style ={{marginBottom:'10px'}}
                  disabled={readyState !== ReadyState.OPEN || loading}><CIcon name="cil-scrubber" /> Scan
                </CButton>
                {loading && 
                <span>
                  <CSpinner color="primary" style={{width:'1.5rem', height:'1.5rem',marginLeft:'10px',marginRight:'10px'}}/>
                  <small style={{color:'red'}}>{console}</small>
                  <CProgress animated value={process} showPercentage className="mb-3"/>
                </span>
                }
              </CCardFooter>
            </CCard>
          </CCol>
          
          <CCol sm = "12" md="7">
            <CCard>
              <CCardHeader>
                <CButton color = {collapseMulti[0]? "dark":null} onClick={()=>{setCollapseMulti([true,false,false])}}>
                  <strong>Whois</strong></CButton>{' '}
                <CButton color = {collapseMulti[1]? "dark":null} onClick={()=>{setCollapseMulti([false,true,false])}}>
                  <strong>Robot</strong></CButton>{' '}
                <CButton color = {collapseMulti[2]? "dark":null} onClick={()=>{setCollapseMulti([false,false,true])}}>
                  <strong>IP address / Port</strong></CButton>{' '}
              </CCardHeader>
              <CCardBody style={{height:"600px",overflow: 'auto'}}>
                
                <CCollapse show={collapseMulti[0]}>
                  <CFade timeout ={300} in ={collapseMulti[0]}>

                    <CButton onClick={() => setCol1(!col1)}>
                      <span style={{fontWeight:"bold"}}>{col1?<CIcon size="sm" name="cilChevronDoubleUp"/>:<CIcon size="sm" name="cilChevronDoubleDown"/>}Domain Name</span>
                    </CButton>
                    <CCollapse show={col1} style={{marginLeft:'30px'}}>
                        {whois_results.domain_name && whois_results.domain_name.map((item,idx)=> <li key = {idx}>{item}</li>)}
                    </CCollapse>
                    <hr style={{width:"100%"}}/>

                    <CButton onClick={() => setCol2(!col2)}>
                      <span style={{fontWeight:"bold"}}>{col2?<CIcon size="sm" name="cilChevronDoubleUp"/>:<CIcon size="sm" name="cilChevronDoubleDown"/>}Registrar</span>
                    </CButton>
                    <CCollapse show={col2} style={{marginLeft:'30px'}}>
                        {whois_results.registrar && whois_results.registrar.map((item,idx)=> <li key = {idx}>{item}</li>)}
                    </CCollapse>
                    <hr style={{width:"100%"}}/>

                    <CButton onClick={() => setCol3(!col3)}>
                      <span style={{fontWeight:"bold"}}>{col3?<CIcon size="sm" name="cilChevronDoubleUp"/>:<CIcon size="sm" name="cilChevronDoubleDown"/>}Whois Server</span>
                    </CButton>
                    <CCollapse show={col3} style={{marginLeft:'30px'}}>
                        {whois_results.whois_server && whois_results.whois_server.map((item,idx)=> <li key = {idx}>{item}</li>)}
                    </CCollapse>
                    <hr style={{width:"100%"}}/>

                    <CButton onClick={() => setCol4(!col4)}>
                      <span style={{fontWeight:"bold"}}>{col4?<CIcon size="sm" name="cilChevronDoubleUp"/>:<CIcon size="sm" name="cilChevronDoubleDown"/>}Referral Url</span>
                    </CButton>
                    <CCollapse show={col4} style={{marginLeft:'30px'}}>
                        {whois_results.referral_url && whois_results.referral_url.map((item,idx)=> <li key = {idx}>{item}</li>)}
                    </CCollapse>
                    <hr style={{width:"100%"}}/>

                    <CButton onClick={() => setCol5(!col5)}>
                      <span style={{fontWeight:"bold"}}>{col5?<CIcon size="sm" name="cilChevronDoubleUp"/>:<CIcon size="sm" name="cilChevronDoubleDown"/>}Updated Date</span>
                    </CButton>
                    <CCollapse show={col5} style={{marginLeft:'30px'}}>
                        {whois_results.updated_date && whois_results.updated_date.map((item,idx)=> <li key = {idx}>{item}</li>)}
                    </CCollapse>
                    <hr style={{width:"100%"}}/>

                    <CButton onClick={() => setCol6(!col6)}>
                      <span style={{fontWeight:"bold"}}>{col6?<CIcon size="sm" name="cilChevronDoubleUp"/>:<CIcon size="sm" name="cilChevronDoubleDown"/>}Creation Date</span>
                    </CButton>
                    <CCollapse show={col6} style={{marginLeft:'30px'}}>
                        {whois_results.creation_date && whois_results.creation_date.map((item,idx)=> <li key = {idx}>{item}</li>)}
                    </CCollapse>
                    <hr style={{width:"100%"}}/>

                    <CButton onClick={() => setCol7(!col7)}>
                      <span style={{fontWeight:"bold"}}>{col7?<CIcon size="sm" name="cilChevronDoubleUp"/>:<CIcon size="sm" name="cilChevronDoubleDown"/>}Expiration Date</span>
                    </CButton>
                    <CCollapse show={col7} style={{marginLeft:'30px'}}>
                        {whois_results.expiration_date && whois_results.expiration_date.map((item,idx)=> <li key = {idx}>{item}</li>)}
                    </CCollapse>
                    <hr style={{width:"100%"}}/>

                    <CButton onClick={() => setCol8(!col8)}>
                      <span style={{fontWeight:"bold"}}>{col8?<CIcon size="sm" name="cilChevronDoubleUp"/>:<CIcon size="sm" name="cilChevronDoubleDown"/>}Name Servers</span>
                    </CButton>
                    <CCollapse show={col8} style={{marginLeft:'30px'}}>
                        {whois_results.name_servers && whois_results.name_servers.map((item,idx)=> <li key = {idx}>{item}</li>)}
                    </CCollapse>
                    <hr style={{width:"100%"}}/>

                    <CButton onClick={() => setCol9(!col9)}>
                      <span style={{fontWeight:"bold"}}>{col9?<CIcon size="sm" name="cilChevronDoubleUp"/>:<CIcon size="sm" name="cilChevronDoubleDown"/>}Status</span>
                    </CButton>
                    <CCollapse show={col9} style={{marginLeft:'30px'}}>
                        {whois_results.status && whois_results.status.map((item,idx)=> <li key = {idx}>{item}</li>)}
                    </CCollapse>
                    <hr style={{width:"100%"}}/>

                    <CButton onClick={() => setCol10(!col10)}>
                      <span style={{fontWeight:"bold"}}>{col10?<CIcon size="sm" name="cilChevronDoubleUp"/>:<CIcon size="sm" name="cilChevronDoubleDown"/>}Emails</span>
                    </CButton>
                    <CCollapse show={col10} style={{marginLeft:'30px'}}>
                        {whois_results.emails && whois_results.emails.map((item,idx)=> <li key = {idx}>{item}</li>)}
                    </CCollapse>
                    <hr style={{width:"100%"}}/>

                    <CButton onClick={() => setCol11(!col11)}>
                      <span style={{fontWeight:"bold"}}>{col11?<CIcon size="sm" name="cilChevronDoubleUp"/>:<CIcon size="sm" name="cilChevronDoubleDown"/>}Dnssec</span>
                    </CButton>
                    <CCollapse show={col11} style={{marginLeft:'30px'}}>
                        {whois_results.dnssec && whois_results.dnssec.map((item,idx)=> <li key = {idx}>{item}</li>)}
                    </CCollapse>
                    <hr style={{width:"100%"}}/>

                    <CButton onClick={() => setCol12(!col12)}>
                      <span style={{fontWeight:"bold"}}>{col12?<CIcon size="sm" name="cilChevronDoubleUp"/>:<CIcon size="sm" name="cilChevronDoubleDown"/>}Name</span>
                    </CButton>
                    <CCollapse show={col12} style={{marginLeft:'30px'}}>
                        {whois_results.name && whois_results.name.map((item,idx)=> <li key = {idx}>{item}</li>)}
                    </CCollapse>
                    <hr style={{width:"100%"}}/>

                    <CButton onClick={() => setCol13(!col13)}>
                      <span style={{fontWeight:"bold"}}>{col13?<CIcon size="sm" name="cilChevronDoubleUp"/>:<CIcon size="sm" name="cilChevronDoubleDown"/>}Org</span>
                    </CButton>
                    <CCollapse show={col13} style={{marginLeft:'30px'}}>
                        {whois_results.org && whois_results.org.map((item,idx)=> <li key = {idx}>{item}</li>)}
                    </CCollapse>
                    <hr style={{width:"100%"}}/>

                    <CButton onClick={() => setCol14(!col14)}>
                      <span style={{fontWeight:"bold"}}>{col14?<CIcon size="sm" name="cilChevronDoubleUp"/>:<CIcon size="sm" name="cilChevronDoubleDown"/>}Address</span>
                    </CButton>
                    <CCollapse show={col14} style={{marginLeft:'30px'}}>
                        {whois_results.address && whois_results.address.map((item,idx)=> <li key = {idx}>{item}</li>)}
                    </CCollapse>
                    <hr style={{width:"100%"}}/>

                    <CButton onClick={() => setCol15(!col15)}>
                      <span style={{fontWeight:"bold"}}>{col15?<CIcon size="sm" name="cilChevronDoubleUp"/>:<CIcon size="sm" name="cilChevronDoubleDown"/>}City</span>
                    </CButton>
                    <CCollapse show={col15} style={{marginLeft:'30px'}}>
                        {whois_results.city && whois_results.city.map((item,idx)=> <li key = {idx}>{item}</li>)}
                    </CCollapse>
                    <hr style={{width:"100%"}}/>

                    <CButton onClick={() => setCol16(!col16)}>
                      <span style={{fontWeight:"bold"}}>{col16?<CIcon size="sm" name="cilChevronDoubleUp"/>:<CIcon size="sm" name="cilChevronDoubleDown"/>}State</span>
                    </CButton>
                    <CCollapse show={col16} style={{marginLeft:'30px'}}>
                        {whois_results.state && whois_results.state.map((item,idx)=> <li key = {idx}>{item}</li>)}
                    </CCollapse>
                    <hr style={{width:"100%"}}/>

                    <CButton onClick={() => setCol17(!col17)}>
                      <span style={{fontWeight:"bold"}}>{col17?<CIcon size="sm" name="cilChevronDoubleUp"/>:<CIcon size="sm" name="cilChevronDoubleDown"/>}Zipcode</span>
                    </CButton>
                    <CCollapse show={col17} style={{marginLeft:'30px'}}>
                        {whois_results.zipcode && whois_results.zipcode.map((item,idx)=> <li key = {idx}>{item}</li>)}
                    </CCollapse>
                    <hr style={{width:"100%"}}/>

                    <CButton onClick={() => setCol18(!col18)}>
                      <span style={{fontWeight:"bold"}}>{col18?<CIcon size="sm" name="cilChevronDoubleUp"/>:<CIcon size="sm" name="cilChevronDoubleDown"/>}Country</span>
                    </CButton>
                    <CCollapse show={col18} style={{marginLeft:'30px'}}>
                        {whois_results.country && whois_results.country.map((item,idx)=> <li key = {idx}>{item}</li>)}
                    </CCollapse>
                    <hr style={{width:"100%"}}/>
                    
                  </CFade>                  
                </CCollapse>

                <CCollapse show={collapseMulti[1]}>
                  <CFade timeout ={300} in ={collapseMulti[1]}>
                    {robot_results.txt === "" ? <p>No Robots.txt on {robot_results.target}</p>: <p style = {{whiteSpace:"pre-wrap"}}>{robot_results.txt}</p>}
                   
                  </CFade>
                </CCollapse>

                <CCollapse show={collapseMulti[2]}>
                  <CFade timeout ={300} in ={collapseMulti[2]}>
                    <h4>IP Address</h4>
                    {ip_addresses.map((item,idx) => (
                          <CListGroupItem key={idx}>{item.collected_ip}</CListGroupItem>
                      ))}
                    <br/>
                    <h4>Open Ports</h4>
                    <CDataTable
                      items={port_results}
                      fields={fields}
                      hover
                      striped
                      bordered
                      size="sm"
                      scopedSlots = {
                        {'port_status':
                            (item)=>(
                            <td>
                                <CBadge color="primary">
                                  {item.port_status}
                                </CBadge>
                            </td>
                        )}
                        }
                    />
                  </CFade>
                </CCollapse>
                                                            
              </CCardBody>
            </CCard>
          </CCol>
        </CRow>
        <CToaster position="top-center" >
              <CToast
                show={toast_Active}
                autohide={3000}
                fade
              >
                <CToastHeader>
                  Notification
                </CToastHeader>
                <CToastBody>
                  Scanned Successfully!
                </CToastBody>
              </CToast>
        </CToaster>
      </>
    )
  }
  
  export default Netscan
  