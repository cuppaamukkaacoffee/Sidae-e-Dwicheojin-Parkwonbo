import { useRef, useState, useCallback, useEffect } from "react";
import { useSelector, useDispatch, shallowEqual } from "react-redux";
import React from "react";
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
  CSpinner,
  CPagination,
  CBadge,
  CEmbed,
  CEmbedItem,
  CCollapse,
} from "@coreui/react";
import CIcon from "@coreui/icons-react";
import * as userActions from "src/store/modules/user/actions";

const fields = [
  "target",
  "sub_path",
  "url",
  "result_string",
  "vulnerability",
  "scan_type",
  "status",
  "timestamp",
];

const Web_result = () => {
  const dispatch = useDispatch();
  const [currentPage, setCurrentPage] = useState(1);
  const [collapse, setCollapse] = useState(false);

  const {
    id,
    url,
    scan_type,
    vul,
    result_string,
    total_reports,
    requests,
    responses,
    report,
    request,
    response,
    errorMsg,
    loading,
  } = useSelector(
    (state) => ({
      id: state.user.id,
      url: state.user.url,
      scan_type: state.user.scan_type,
      vul: state.user.vul,
      result_string: state.user.result_string,
      total_reports: state.user.total_reports,
      requests: state.user.requests,
      responses: state.user.responses,
      report: state.user.report,
      request: state.user.request,
      response: state.user.response,
      errorMsg: state.user.errorMsg,
      loading: state.loading.loading,
    }),
    shallowEqual
  );

  useEffect(() => {
    return () => {
      dispatch(userActions.reset_msg());
    };
  }, []);

  useEffect(() => {
    if (total_reports.length > 0) {
      const req = requests.find((el) => el.id === total_reports[0].id);
      const res = responses.find((el) => el.id === total_reports[0].id);
      dispatch(userActions.set_request(req));
      dispatch(userActions.set_response(res));
      dispatch(userActions.set_report(total_reports[0]));
    }
  }, [total_reports]);

  const getBadge = (status) => {
    switch (status) {
      case "200":
        return "success";
      case "404":
        return "danger";
      default:
        return "primary";
    }
  };

  const handleInputid = (e) => {
    dispatch(userActions.set_id(e.target.value));
  };

  const handleInputurl = (e) => {
    dispatch(userActions.set_url(e.target.value));
  };

  const handleInputscan_type = (e) => {
    dispatch(userActions.set_scan_type(e.target.value));
  };

  const handleInputvul = (e) => {
    dispatch(userActions.set_vul(e.target.value));
  };

  const handleInputresult_string = (e) => {
    dispatch(userActions.set_result_string(e.target.value));
  };

  const handleRowclick = (e) => {
    setCollapse(false);
    dispatch(userActions.reset_r());
    const req = requests.find((el) => el.id === e.id);
    const res = responses.find((el) => el.id === e.id);
    dispatch(userActions.set_request(req));
    dispatch(userActions.set_response(res));
    dispatch(userActions.set_report(e));
  };

  const handleSubmit_results = useCallback(() => {
    if (id === sessionStorage.getItem("id")) {
      setCollapse(false);
      dispatch(userActions.reset_r());
      dispatch(
        userActions.results_check({
          id: id,
          url: url,
          scan_type: scan_type,
          vul: vul,
          result_string: result_string,
          with_headers: true,
        })
      );
    } else {
      alert("아이디를 다시 입력하세요");
    }
  }, [id, url, vul, result_string, scan_type]);

  const req = (() => {
    let req = [];
    for (let [key, val] of Object.entries(request)) {
      if (key !== "id") {
        if (key === "body") {
          if (val) {
            req.push(
              <p key={key} style={{ color: "red" }}>
                <strong>Payload</strong>
              </p>
            );
            for (let [key1, val1] of Object.entries(JSON.parse(val))) {
              req.push(
                <p key={key1}>
                  <strong>{key1}</strong> : {val1}
                </p>
              );
            }
          }
        } else {
          req.push(
            <p key={key}>
              <strong>{key}</strong> : {val}
            </p>
          );
        }
      }
    }
    return req;
  })();

  const res = (() => {
    let res = [];
    if (response.headers_string) {
      for (let [key, val] of Object.entries(
        JSON.parse(response.headers_string)
      )) {
        res.push(
          <p key={key}>
            <strong>{key}</strong> : {val}
          </p>
        );
      }
    }

    return res;
  })();

  const scan_pages = (() => {
    if (total_reports.length > 0) {
      return Math.ceil(total_reports.length / 10);
    }
  })();

  const body = (() => {
    let body = response.body;
    if (body) {
      const reactStringReplace = require("react-string-replace");

      body = reactStringReplace(body, "SIDWIPARK", (match, i) => (
        <span key={i} style={{ color: "red" }}>
          <strong>{match}</strong>
        </span>
      ));

      body = reactStringReplace(
        body,
        "<iframe/onload=alert(1)>",
        (match, i) => (
          <span id="vul" key={i} style={{ color: "red" }}>
            <strong>{match}</strong>
          </span>
        )
      );

      body = reactStringReplace(
        body,
        "<Script>alert('hi')</scripT>",
        (match, i) => (
          <span id="vul" key={i} style={{ color: "red" }}>
            <strong>{match}</strong>
          </span>
        )
      );
    }
    return body;
  })();

  return (
    <>
      <CRow>
        <CCol xs="12" md="5">
          <CCard>
            <CCardHeader>Web Scan Results</CCardHeader>
            <CCardBody>
              <CForm
                action=""
                method="post"
                encType="multipart/form-data"
                className="form-horizontal"
              >
                <CFormGroup row>
                  <CCol md="3">
                    <CLabel htmlFor="text-input">Username</CLabel>
                  </CCol>
                  <CCol xs="12" md="9">
                    <CInput
                      id="text-input"
                      name="text-input"
                      onChange={handleInputid}
                    />
                  </CCol>
                </CFormGroup>
                <CFormGroup row>
                  <CCol md="3">
                    <CLabel htmlFor="text-input">Target URL</CLabel>
                  </CCol>
                  <CCol xs="12" md="9">
                    <CInput
                      id="text-input"
                      name="text-input"
                      placeholder="URL"
                      onChange={handleInputurl}
                    />
                    <CFormText>ex) https://www.naver.com</CFormText>
                  </CCol>
                </CFormGroup>

                <CFormGroup row>
                  <CCol md="3">
                    <CLabel htmlFor="text-input">Scan type</CLabel>
                  </CCol>
                  <CCol xs="12" md="9">
                    <CSelect
                      custom
                      name="select"
                      id="select"
                      onChange={handleInputscan_type}
                    >
                      <option value="">All</option>
                      <option value="url_fuzz">Url fuzz</option>
                      <option value="form_fuzz">Form fuzz</option>
                      <option value="traversal_check">Traversal check</option>
                    </CSelect>
                  </CCol>
                </CFormGroup>

                <CFormGroup row>
                  <CCol md="3">
                    <CLabel htmlFor="select">Vunerability</CLabel>
                  </CCol>
                  <CCol xs="12" md="9">
                    <CSelect
                      custom
                      name="select"
                      id="select"
                      onChange={handleInputvul}
                    >
                      <option value="">All</option>
                      <option value="Open Redirect">Open Redirect</option>
                      <option value="SQL Injection">SQL Injection</option>
                      <option value="XSS">XSS</option>
                      <option value="Windows Directory Traversal">
                        Windows Directory Traversal
                      </option>
                      <option value="Linux Directory Traversal">
                        Linux Directory Traversal
                      </option>
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
                    <CSelect
                      custom
                      name="select"
                      id="select"
                      onChange={handleInputresult_string}
                    >
                      <option value="">All</option>
                      <option value="vulnerable">Vulnerable</option>
                      <option value="benign">Benign</option>
                    </CSelect>
                  </CCol>
                </CFormGroup>
              </CForm>
            </CCardBody>
            <CCardFooter>
              <CButton
                type="button"
                size="sm"
                color="primary"
                onClick={handleSubmit_results}
              >
                <CIcon name="cil-scrubber" /> Result
              </CButton>
              {loading && (
                <CSpinner
                  color="primary"
                  style={{
                    width: "1.5rem",
                    height: "1.5rem",
                    marginLeft: "10px",
                    marginRight: "10px",
                  }}
                />
              )}
              {errorMsg}
            </CCardFooter>
          </CCard>
        </CCol>
        <CCol xs="12" md="7">
          <CCard style={{ height: "420px", overflow: "auto" }}>
            <CCardBody>
              <CTabs>
                <CNav variant="tabs">
                  <CNavItem>
                    <CNavLink>Response</CNavLink>
                  </CNavItem>
                  <CNavItem>
                    <CNavLink>Request</CNavLink>
                  </CNavItem>
                </CNav>
                <CTabContent>
                  <CTabPane>
                    <br />
                    {report.url && (
                      <p>
                        <strong>Url</strong> :{" "}
                        <a href={report.url} target="_blank">
                          {report.url}
                        </a>
                      </p>
                    )}
                    {res}
                    {response.body && (
                      <CCard accentColor="primary">
                        <CCardHeader>
                          <strong>Body</strong>
                          <CButton
                            color="primary"
                            onClick={() => {
                              setCollapse(!collapse);
                            }}
                            style={{ float: "right" }}
                          >
                            Render
                          </CButton>
                        </CCardHeader>
                        <CCardBody
                          style={{
                            height: "350px",
                            overflow: "auto",
                            whiteSpace: "pre-wrap",
                          }}
                        >
                          <CCollapse show={collapse}>
                            {collapse && (
                              <CEmbed>
                                <CEmbedItem src={report.url} />
                              </CEmbed>
                            )}
                          </CCollapse>
                          <CCollapse show={!collapse}>{body}</CCollapse>
                        </CCardBody>
                      </CCard>
                    )}
                  </CTabPane>
                  <CTabPane>
                    <br />
                    {report.url && (
                      <p>
                        <strong>Url</strong> :{" "}
                        <a href={report.url} target="_blank">
                          {report.url}
                        </a>
                      </p>
                    )}
                    {req}
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
            <CCardBody style={{ height: "280px", overflow: "auto" }}>
              <CDataTable
                items={total_reports}
                fields={fields}
                hover
                striped
                bordered
                size="sm"
                activePage={currentPage}
                itemsPerPage={10}
                onRowClick={handleRowclick}
                scopedSlots={{
                  status: (item) => (
                    <td>
                      <CBadge color={getBadge(item.status)}>
                        {item.status}
                      </CBadge>
                    </td>
                  ),
                }}
              />
            </CCardBody>
            {scan_pages && (
              <CCardFooter>
                <CPagination
                  size="sm"
                  activePage={currentPage}
                  limit={10}
                  pages={scan_pages}
                  align="center"
                  onActivePageChange={setCurrentPage}
                />
              </CCardFooter>
            )}
          </CCard>
        </CCol>
      </CRow>
    </>
  );
};

export default Web_result;
