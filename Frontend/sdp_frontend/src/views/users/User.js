import React from "react";
import { CCard, 
        CCardBody, 
        CCardHeader, 
        CCol, 
        CRow,
        CLink,
        CButton
      } from "@coreui/react";

const User = () => {
  return (
    <CRow>
      <CCol lg={6}>
        <CCard>
          <CCardHeader>Profile</CCardHeader>
          <CCardBody>
            ID : {sessionStorage.getItem("id")} <br/><br/>
            email : <br/><br/>
            
              <CLink
                to="/login"
                onClick={() => {
                  sessionStorage.clear();
                }}
              >
                <CButton color = "dark">
                  Logout
                </CButton>
              </CLink>
          </CCardBody>
        </CCard>
      </CCol>
    </CRow>
  );
};

export default User;
