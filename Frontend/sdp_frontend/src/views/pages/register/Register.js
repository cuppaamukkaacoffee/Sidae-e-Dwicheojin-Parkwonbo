import React, { useEffect } from 'react';
import {useSelector, useDispatch} from 'react-redux';
import {useCallback} from 'react';
import * as userActions from 'src/store/modules/user/actions';
import {
  CButton,
  CCard,
  CCardBody,
  CCol,
  CContainer,
  CForm,
  CInput,
  CInputGroup,
  CInputGroupPrepend,
  CInputGroupText,
  CRow
} from '@coreui/react'
import CIcon from '@coreui/icons-react'

const Register = () => {
  const dispatch = useDispatch();
  const {id,pw,error} = useSelector(state => ({id: state.user.id, pw: state.user.pw, error: state.user.errorMsg}))
  
  useEffect(() => {
    return () => {
      dispatch(userActions.reset_msg());
    };
  }, []);

  const handleInputId = (e) => {
    dispatch(userActions.set_id(e.target.value))
  }
  
  const handleInputPass = (e) => {
    dispatch(userActions.set_pw(e.target.value))
  }

  const handleRegister = useCallback(() => {
    if(id.length > 4 && pw.length > 4){
      dispatch(userActions.register({id:id,pw:pw}))
    }
    else{
      alert('아이디 비밀번호 4자이상 입력');
    }
  }, [id, pw])

  return (
    <div className="c-app c-default-layout flex-row align-items-center">
      <CContainer>
        <CRow className="justify-content-center">
          <CCol md="9" lg="7" xl="6">
            <CCard className="mx-4">
              <CCardBody className="p-4">
                <CForm>
                  <h1>Register</h1>
                  <p className="text-muted">Create your account</p>
                  <CInputGroup className="mb-3">
                    <CInputGroupPrepend>
                      <CInputGroupText>
                        <CIcon name="cil-user" />
                      </CInputGroupText>
                    </CInputGroupPrepend>
                    <CInput type="text" placeholder="Username" autoComplete="username" onChange={handleInputId}/>
                  </CInputGroup>
                  <CInputGroup className="mb-3">
                    <CInputGroupPrepend>
                      <CInputGroupText>@</CInputGroupText>
                    </CInputGroupPrepend>
                    <CInput type="text" placeholder="Email" autoComplete="email" />
                  </CInputGroup>
                  <CInputGroup className="mb-3">
                    <CInputGroupPrepend>
                      <CInputGroupText>
                        <CIcon name="cil-lock-locked" />
                      </CInputGroupText>
                    </CInputGroupPrepend>
                    <CInput type="password" placeholder="Password" autoComplete="new-password" onChange={handleInputPass}/>
                  </CInputGroup>
                  {error}
                  <CButton color="success" block onClick = {handleRegister}>Create Account</CButton>
                </CForm>
              </CCardBody>
            </CCard>
          </CCol>
        </CRow>
      </CContainer>
    </div>
  )
}

export default Register
