import {useCallback, useEffect} from 'react';
import {useSelector, useDispatch, shallowEqual} from 'react-redux';
import React from 'react'
import {
  CCard,
  CCardBody,
  CCardHeader,
  CDataTable,
  CButton,
  CCardFooter,
  CCol,
  CForm,
  CFormGroup,
  CFormText,
  CInput,
  CLabel,
  CSelect,
  CRow,
  CNav,
  CNavItem,
  CNavLink,
  CTabContent,
  CTabPane,
  CTabs,
  CSpinner
} from '@coreui/react'
import CIcon from '@coreui/icons-react'
import * as userActions from 'src/store/modules/user/actions';

const fields = ['target','sub_path', 'url', 'result_string','vulnerability','status','timestamp']

const Result = () => {
    const dispatch = useDispatch();

    const {
    id,
    url,
    vul,
    result_string,
    reports,
    requests,
    responses,
    report,
    request,
    response,
    headers_string,
    errorMsg,
    loading
    } = useSelector((state) => ({
    id : state.user.id,
    url: state.user.url,
    vul: state.user.vul,
    result_string: state.user.result_string,
    reports: state.user.reports,
    requests: state.user.requests,
    responses: state.user.responses,
    report: state.user.report,
    request: state.user.request,
    response: state.user.response,
    headers_string: state.user.headers_string,
    errorMsg: state.user.errorMsg,
    loading: state.loading.loading
    }), shallowEqual)

    useEffect(() => {
        return () => {
            dispatch(userActions.reset_msg());
          };
      }, []);
    
    useEffect(() => {
        if(reports.length > 0){
            const req = requests.find((el) => el.id === reports[0].id);
            const res = responses.find((el) => el.id === reports[0].id);
            dispatch(userActions.set_request(req));
            dispatch(userActions.set_response(res));
            dispatch(userActions.set_report(reports[0]));
        }
      }, [reports]);
    
    const handleInputid = (e) => {
        dispatch(userActions.set_id(e.target.value))
        }
    
    const handleInputurl = (e) => {
        dispatch(userActions.set_url(e.target.value))
      }
    
    const handleInputvul = (e) => {
        dispatch(userActions.set_vul(e.target.value))
    }
    
    const handleInputresult_string = (e) => {
        dispatch(userActions.set_result_string(e.target.value))
        }

    const handleRowclick = (e) =>{
        const req = requests.find((el) => el.id === e.id);
        const res = responses.find((el) => el.id === e.id);
        dispatch(userActions.set_request(req));
        dispatch(userActions.set_response(res));
        dispatch(userActions.set_report(e));
    }
    
    
    const handleSubmit_results = useCallback(() =>{
        dispatch(userActions.reset_r())
        dispatch(userActions.results_check({id : id, url : url, vul : vul, result_string : result_string, with_headers : true}))
      }, [id ,url, vul, result_string])

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
                    Web Scan Results
                    </CCardHeader>
                    <CCardBody>
                    <CForm action="" method="post" encType="multipart/form-data" className="form-horizontal">
                        <CFormGroup row>
                            <CCol md="3">
                                <CLabel htmlFor="text-input">Username</CLabel>
                            </CCol>
                            <CCol xs="12" md="9">
                                <CInput id="text-input" name="text-input"  onChange = {handleInputid}/>
                            </CCol>
                        </CFormGroup>
                        <CFormGroup row>
                        <CCol md="3">
                            <CLabel htmlFor="text-input">Target URL</CLabel>
                        </CCol>
                        <CCol xs="12" md="9">
                            <CInput id="text-input" name="text-input" placeholder="URL" onChange = {handleInputurl}/>
                            <CFormText>ex) https://www.naver.com</CFormText>
                        </CCol>
                        </CFormGroup>
                        
                        <CFormGroup row>
                        <CCol md="3">
                            <CLabel htmlFor="select">Vunerability</CLabel>
                        </CCol>
                        <CCol xs="12" md="9">
                            <CSelect custom name="select" id="select" onChange = {handleInputvul}>
                            <option value="">All</option>
                            <option value="Open Redirect">Open Redirect</option>
                            <option value="SQL Injection">SQL Injection</option>
                            <option value="XSS">XSS</option>
                            <option value="Windows Directory Traversal">Windows Directory Traversal</option>
                            <option value="Linux Directory Traversal">Linux Directory Traversal</option>
                            <option value="LFI Check">LFI Check</option>
                            <option value="RFI Check">RFI Check</option>
                            <option value="RCE Linux Check">RCE Linux Check</option>
                            <option value="SSTI Check">SSTI Check</option>
                            </CSelect>
                        </CCol>
                        </CFormGroup>
                        <CFormGroup row>
                            <CCol md="3">
                                <CLabel htmlFor="text-input">Result_string</CLabel>
                            </CCol>
                            <CCol xs="12" md="9">
                            <CSelect custom name="select" id="select" onChange = {handleInputresult_string}>
                                <option value="">All</option>
                                <option value="vulnerable">Vulnerable</option>
                                <option value="benign">Benign</option>
                            </CSelect>
                            </CCol>
                        </CFormGroup>
                    </CForm>
                    </CCardBody>
                    <CCardFooter>
                        <CButton type="button" size="sm" color="primary" onClick={handleSubmit_results}><CIcon name="cil-scrubber" /> Result</CButton>
                        {loading && <CSpinner color="primary" style={{width:'1.5rem', height:'1.5rem'}}/>}  
                        {errorMsg}
                    </CCardFooter>
                </CCard>
            </CCol>
            <CCol xs="10" md="7">
              <CCard style={{height:"370px",overflow: 'auto'}}>
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
                            <br/>
                            {report.url? <p><strong>Url</strong> : <a href = {report.url} target="_blank">{report.url}</a></p> : null}
                            {res}
                        </CTabPane>
                        <CTabPane>
                            <br/>
                            {report.url? <p><strong>Url</strong> : <a href = {report.url} target="_blank">{report.url}</a></p> : null}
                            {req}
                        </CTabPane>
                    </CTabContent>
                </CTabs>
                </CCardBody>
              </CCard>
            </CCol>
        </CRow>
        <CRow>
            <CCol xs="10" md="12">
            <CCard style={{maxHeight:"330px",overflow: 'auto'}}>
                <CCardBody>
                <CDataTable
                items={reports}
                fields={fields}
                hover
                striped
                bordered
                size="sm"
                itemsPerPage={10}
                pagination
                onRowClick={handleRowclick}
                />
                </CCardBody>
            </CCard>
            </CCol>
        </CRow>
        
        
        </>
    )
    }

export default Result
