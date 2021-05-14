/* eslint-disable no-unused-vars */
import React, { useEffect, useCallback } from "react";
import { Link } from "react-router-dom";
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
  CRow,
} from "@coreui/react";
import CIcon from "@coreui/icons-react";

import { useSelector, useDispatch } from "react-redux";
import * as userActions from "src/store/modules/user/actions";

const Login = () => {
  const dispatch = useDispatch();
  const { id, pw, error } = useSelector((state) => ({
    id: state.user.id,
    pw: state.user.pw,
    error: state.user.errorMsg,
  }));

  useEffect(() => {
    dispatch(userActions.reset_msg());
    return () => {
      dispatch(userActions.reset_msg());
    };
  }, []);

  const handleInputId = (e) => {
    dispatch(userActions.set_id(e.target.value));
  };

  const handleInputPass = (e) => {
    dispatch(userActions.set_pw(e.target.value));
  };

  const handleLogin = useCallback(() => {
    dispatch(userActions.login({ id, pw }));
  }, [id, pw]);

  return (
    <>
    <CButton style = {{fontSize: '25px', marginLeft: '20px'}} onClick={() => {window.location.reload()}}><strong>SDPscanner</strong></CButton>
    <div className="c-app c-default-layout flex-row align-items-center">
      <CContainer>
        <CRow className="justify-content-center">
          <CCol sm= '12' md="6">     
              <CCard className="p-4">
                <CCardBody>
                  <CForm>
                    <h1>Login</h1>
                    <p className="text-muted">Sign In to your account</p>
                    <CInputGroup className="mb-3">
                      <CInputGroupPrepend>
                        <CInputGroupText>
                          <CIcon name="cil-user" />
                        </CInputGroupText>
                      </CInputGroupPrepend>
                      <CInput
                        type="text"
                        placeholder="Username"
                        autoComplete="username"
                        onChange={handleInputId}
                      />
                    </CInputGroup>
                    <CInputGroup className="mb-4">
                      <CInputGroupPrepend>
                        <CInputGroupText>
                          <CIcon name="cil-lock-locked" />
                        </CInputGroupText>
                      </CInputGroupPrepend>
                      <CInput
                        type="password"
                        placeholder="Password"
                        autoComplete="current-password"
                        onChange={handleInputPass}
                      />
                    </CInputGroup>
                    {error}
                    <CRow>
                      <CCol xs="6">
                        <CButton
                          color="primary"
                          className="px-4"
                          onClick={handleLogin}
                        >
                          Login
                        </CButton>
                      </CCol>
                      <CCol xs="6" className="text-right">
                        <Link to="/register">
                          <CButton
                            className="mt-3"
                            active
                            tabIndex={-1}
                          >
                            Register Now!
                          </CButton>
                        </Link>
                      </CCol>
                    </CRow>
                  </CForm>
                </CCardBody>
              </CCard>
          </CCol>
        </CRow>
      </CContainer>
    </div>
    </>
  );
};

export default Login;
