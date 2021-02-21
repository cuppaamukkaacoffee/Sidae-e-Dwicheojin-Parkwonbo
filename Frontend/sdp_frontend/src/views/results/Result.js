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
} from '@coreui/react'
import CIcon from '@coreui/icons-react'
import * as userActions from 'src/store/modules/user/actions';

const fields = ['target','sub_path', 'url', 'result_string','vulnerability','status','timestamp']

const Result = () => {
    const dispatch = useDispatch();
    
    useEffect(() => {
        dispatch(userActions.reset_msg());
      }, []);
    
    const {
    id,
    url,
    vul,
    result_string,
    results,
    errorMsg
    } = useSelector((state) => ({
    id : state.user.id,
    url: state.user.url,
    vul: state.user.vul,
    result_string: state.user.result_string,
    results: state.user.results,
    errorMsg: state.user.errorMsg
    }), shallowEqual)

    
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
        alert(e)
    }
    
    
    const handleSubmit_results = useCallback(() =>{
        dispatch(userActions.results_check({id : id, url : url, vul : vul, result_string : result_string}))
      }, [id ,url, vul, result_string])

    
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
                {errorMsg}
                </CCardFooter>
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
                         request
                        </CTabPane>
                        <CTabPane>
                         response
                        </CTabPane>
                    </CTabContent>
                </CTabs>
                </CCardBody>
              </CCard>
            </CCol>
        </CRow>
        <CRow>
            <CCol>
            <CCard>
                <CCardBody>
                <CDataTable
                items={results}
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
