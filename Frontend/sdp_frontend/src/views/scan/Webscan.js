import React, {useCallback, useRef, useEffect } from 'react';
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
  CListGroupItem,
  CListGroup,
  CNav,
  CNavItem,
  CNavLink,
  CTabContent,
  CTabPane,
  CTabs,
} from '@coreui/react'
import CIcon from '@coreui/icons-react'
import * as loadingActions from 'src/store/modules/loading/actions';
import * as userActions from 'src/store/modules/user/actions';

const fields = ['vulnerability','result_string','url','sub_path', 'status']

const Webscan = () => {
  const dispatch = useDispatch();
  const {
    loading,
    url,
    fuzz,
    } = useSelector((state) => ({
      loading: state.loading.loading,
      url : state.user.url,
      fuzz : state.user.fuzz
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

  const urls = useRef([]);
  const messageHistory = useRef([]);

  useEffect(() => {
    if(lastMessage != null){
      const results = JSON.parse(lastMessage.data);
      if(results.urlList){
          urls.current = urls.current.concat(results.urlList)
      }
      else if(results.result){
        messageHistory.current = messageHistory.current.concat(results.result)
      }
      else if(results.message == "all good"){
        alert("스캔끝")
      }
    }
  }, [lastMessage]);
  
  useEffect(() => {
    if(connectionStatus == 'Closed'){
      dispatch(loadingActions.finishLoading());
      alert("disconnect")
    }
  }, [connectionStatus]);
      
  useEffect(() => {
    dispatch(loadingActions.finishLoading());
    dispatch(userActions.reset_msg())
  }, []);

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
    alert(e)
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
                <CCardBody style={{maxHeight:"200px",overflow: 'auto'}}>
                  <CListGroup>
                   {urls.current.map((url,idx) => (<CListGroupItem href = {url} target="_blank" key={idx}>{url}</CListGroupItem>))}
                  </CListGroup>
                </CCardBody>
              </CCard> 
            </CCol>
            <CCol>
              <CCard style={{height:"540px",overflow: 'auto'}}>
                <CCardBody>
                  <CTabs>
                      <CNav variant="tabs">
                          <CNavItem>
                          <CNavLink>
                              Request
                          </CNavLink>
                          </CNavItem>
                          <CNavItem>
                          <CNavLink>
                              Response
                          </CNavLink>
                          </CNavItem>
                      </CNav>
                      <CTabContent>
                          <CTabPane>
                            {loading ? <CSpinner
                              color="primary"
                              style={{width:'4rem', height:'4rem', marginTop:"25%",marginLeft: '45%'}}
                            />  : null}
                          </CTabPane>
                          <CTabPane>
                            {loading ? <CSpinner
                              color="primary"
                              style={{width:'4rem', height:'4rem', marginTop:"25%",marginLeft: '45%'}}
                            />  : null}
                          </CTabPane>
                      </CTabContent>
                  </CTabs>
                  </CCardBody>
              </CCard>
            </CCol>
        </CRow>
    
      
      
      <CRow>
        <CCol xs="12" md="12">
          <CCard>
              <CCardHeader>
                  Results
              </CCardHeader>
                <CCardBody>
                  <CDataTable
                  items={messageHistory.current}
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
    </>
  );
};

export default Webscan