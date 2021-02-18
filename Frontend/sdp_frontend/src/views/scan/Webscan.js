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
} from '@coreui/react'
import CIcon from '@coreui/icons-react'
import * as loadingActions from 'src/store/modules/loading/actions';
import * as userActions from 'src/store/modules/user/actions';

const fields = ['vulnerability','result_string','sub_path', 'url', 'status']

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
  const fieldRef = useRef(null);

  useEffect(() => {
    if(lastMessage != null){
      const results = JSON.parse(lastMessage.data);
      fieldRef.current.scrollIntoView({
        block: "end",
        behavior: "smooth",
      });
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

  return (
    <div ref={fieldRef}>
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
            </CCol>
        </CRow>
        <CRow></CRow>
      
      <CRow>
        <CCol xs="10" md="5">
        <CCard>
            <CCardHeader>
              Url List
            </CCardHeader>
            <CCardBody>
              {urls.current.map((url,idx) => (<li key={idx}>{url}</li>))}
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
                size="sm"
                
                />
              </CCardBody>
          </CCard> 
        </CCol>
      </CRow>
      {loading ? <CSpinner
        color="primary"
        style={{width:'4rem', height:'4rem', marginLeft: '50%'}}
      />  : null}
         
    </div>
  );
};

export default Webscan