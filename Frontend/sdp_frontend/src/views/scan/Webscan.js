import React, {useCallback, useState, useEffect } from 'react';
import {useSelector, useDispatch, shallowEqual} from 'react-redux';
import useWebSocket, { ReadyState } from 'react-use-websocket';
import {
  CCard,
  CCardBody,
  CDataTable,
  CSpinner,
  CRow,
  CCol,
  CCardHeader,
  CButton,
  CCardFooter,
  CForm,
  CFormGroup,
  CFormText,
  CInput,
  CLabel,
  CSelect,
  CNav,
  CNavItem,
  CNavLink,
  CTabContent,
  CTabPane,
  CTabs,
  CProgress,
  CToaster,
  CToast,
  CToastHeader,
  CToastBody
} from '@coreui/react'
import CIcon from '@coreui/icons-react'
import * as loadingActions from 'src/store/modules/loading/actions';
import * as userActions from 'src/store/modules/user/actions';

const fields = ['vulnerability','result_string','url','sub_path', 'status']

const Webscan = () => {
  const [toast_Active,set_toast_Active] = useState(false)
  const dispatch = useDispatch();
  const {
    loading,
    url,
    url_list,
    reports,
    requests,
    responses,
    report,
    request,
    response,
    headers_string,
    fuzz,
    progress,
    total,
    } = useSelector((state) => ({
      loading: state.loading.loading,
      url : state.user.url,
      url_list : state.user.url_list,
      reports : state.user.reports,
      requests: state.user.requests,
      responses: state.user.responses,
      report: state.user.report,
      request: state.user.request,
      response: state.user.response,
      headers_string: state.user.headers_string,
      fuzz : state.user.fuzz,
      progress: state.loading.progress,
      total: state.loading.total,
    }), shallowEqual)

  const {
    sendMessage,
    lastMessage,
    readyState,
  } = useWebSocket('ws://localhost:8000/ws/scan/');

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
      if(results.urlList){
          dispatch(userActions.set_url_list(results.urlList))
          dispatch(loadingActions.add_total())
      }
      else if(results.reports){
        dispatch(userActions.set_results(results))
        dispatch(loadingActions.add_progress())
      }
      else if(results.message == "all good"){
        set_toast_Active(true);
        if(reports.length > 0){
          const req = requests.find((el) => el.id === reports[0].id);
          const res = responses.find((el) => el.id === reports[0].id);
          dispatch(userActions.set_request(req));
          dispatch(userActions.set_response(res));
          dispatch(userActions.set_report(reports[0]));
      }

      }
    }
  }, [lastMessage]);
  
  useEffect(() => {
    if(connectionStatus == 'Closed'){
      dispatch(loadingActions.finishLoading());
    }
  }, [connectionStatus]);
      
  useEffect(() => {
    return () => {
      dispatch(loadingActions.finishLoading());
      dispatch(userActions.reset_msg())
    };
  }, []);

  useEffect(() => {
    if(toast_Active == true){
      setTimeout(() => {
        set_toast_Active(false)
      },5000)
    }
  },[toast_Active])

  const handleClickSendMessage = useCallback(() =>{
    if(url.length > 0){
      const token = sessionStorage.getItem('token');
      dispatch(loadingActions.startLoading());
      sendMessage(JSON.stringify({"token": `Token ${token}`,
                                  "target": url,
                                  "fuzz": fuzz}))
    }else{
      alert("url제대로")
    }
   }, [url, fuzz]);
  
  const handleInputurl = (e) => {
    dispatch(userActions.set_url(e.target.value))
  }
  
  const handleInputfuzz = (e) => {
    dispatch(userActions.set_fuzz(e.target.value))
  }

  const handleRowclick = (e) =>{
    const req = requests.find((el) => el.id === e.id);
    const res = responses.find((el) => el.id === e.id);
    dispatch(userActions.set_request(req));
    dispatch(userActions.set_response(res));
    dispatch(userActions.set_report(e));
  }

  let res = []
  let req = []
  for (let [key, val] of Object.entries(headers_string)){
      res.push(<p key={key}><strong>{key}</strong> : {val}</p>);
    } 
  for (let [key, val] of Object.entries(request)){
      if (key !== "id"){
          req.push(<p key={key}><strong>{key}</strong> : {val}</p>);
        }
    } 

  return (
    <>
      <CRow>
            <CCol xs="10" md="5">
              <CCard>
                  <CCardHeader>
                  Web Scan
                  </CCardHeader>
                  <CCardBody>
                  <CForm action="" method="post" encType="multipart/form-data" className="form-horizontal">
                      <CFormGroup row>
                      <CCol md="3">
                          <CLabel htmlFor="text-input">Target URL</CLabel>
                      </CCol>
                      <CCol xs="12" md="9">
                          <CInput id="text-input" name="text-input" placeholder="URL"  onChange={handleInputurl}/>
                          <CFormText>ex) https://www.naver.com</CFormText>
                      </CCol>
                      </CFormGroup>
                      
                      <CFormGroup row>
                      <CCol md="3">
                          <CLabel htmlFor="select">Fuzz</CLabel>
                      </CCol>
                      <CCol xs="12" md="9">
                          <CSelect custom name="select" id="select" onChange = {handleInputfuzz}>
                          <option value="true">True</option>
                          <option value="false">False</option>
                          </CSelect>
                      </CCol>
                      </CFormGroup>
                  </CForm>
                  </CCardBody>
                  <CCardFooter>
                  <CButton type="button" size="sm" color="primary" onClick={handleClickSendMessage} 
                    disabled={readyState !== ReadyState.OPEN || loading}><CIcon name="cil-scrubber" /> Scan
                  </CButton>
                  </CCardFooter>
              </CCard>
              <CCard>
                <CCardHeader>
                  Url List
                </CCardHeader>
                <CCardBody style={{maxHeight:"100px",overflow: 'auto'}}>
                  <ul style={{listStyle : 'none'}}>
                   {url_list.map((url,idx) => (<li key={idx}><a href = {url} target="_blank" >{url}</a></li>))}
                  </ul>
                </CCardBody>
              </CCard> 
            </CCol>
            <CCol xs="10" md="7">
              <CCard style={{height:"440px",overflow: 'auto'}}>
                <CCardBody>
                  <CTabs>
                      <CNav variant="tabs">
                          <CNavItem>
                          <CNavLink>
                              Response
                          </CNavLink>
                          </CNavItem>
                          <CNavItem>
                          <CNavLink>
                              Request
                          </CNavLink>
                          </CNavItem>
                      </CNav>
                      <CTabContent>
                          <CTabPane>
                            {loading ? 
                            <div>
                              <CSpinner
                                color="primary"
                                style={{width:'4rem', height:'4rem', marginTop:"10%",marginLeft: '45%', marginBottom: '5%'}}/>  
                              <CProgress animated value={progress} max={total} showPercentage className="mb-3" />
                            </div> 
                            : 
                            <div>
                              <br/>
                              {report.url? <p><strong>Url</strong> : <a href = {report.url} target="_blank">{report.url}</a></p> : null}
                              {res}
                            </div>
                            }
                          </CTabPane>
                          <CTabPane>
                            {
                            loading ? 
                            <div>
                              <CSpinner
                                color="primary"
                                style={{width:'4rem', height:'4rem', marginTop:"10%",marginLeft: '45%', marginBottom: '5%'}}/>  
                              <CProgress animated value={progress} max={total} showPercentage className="mb-3" />
                            </div> 
                            :
                            <div>
                              <br/>
                              {report.url? <p><strong>Url</strong> : <a href = {report.url} target="_blank">{report.url}</a></p> : null}
                              {req}
                            </div>
                            }
                          </CTabPane>
                      </CTabContent>
                  </CTabs>
                  </CCardBody>
              </CCard>
            </CCol>
        </CRow>
    
      
      
      <CRow>
        <CCol xs="12" md="12">
          <CCard style={{maxHeight:"300px",overflow: 'auto'}}>
                <CCardBody>
                  <CDataTable
                  items={reports}
                  fields={fields}
                  hover
                  striped
                  bordered
                  pagination
                  size="sm"
                  onRowClick ={handleRowclick}
                  />
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
  );
};

export default Webscan