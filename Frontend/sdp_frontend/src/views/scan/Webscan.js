import React, { useCallback, useState, useEffect } from "react";
import { useSelector, useDispatch, shallowEqual } from "react-redux";
import useWebSocket, { ReadyState } from "react-use-websocket";
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
  CPagination,
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
  CToastBody,
  CSwitch,
  CBadge,
  CCollapse,
  CEmbed,
  CEmbedItem,
} from "@coreui/react";
import CIcon from "@coreui/icons-react";
import * as loadingActions from "src/store/modules/loading/actions";
import * as userActions from "src/store/modules/user/actions";

const fields = [
  "vulnerability",
  "result_string",
  "url",
  "sub_path",
  "scan_type",
  "status",
];

const Webscan = () => {
  const [toast_Active, set_toast_Active] = useState(false);
  const [first_rendering, set_first_rendering] = useState(true);
  const [currentPage, setCurrentPage] = useState(1);
  const [collapse, setCollapse] = useState(false);

  const dispatch = useDispatch();
  const {
    console,
    loading,
    url,
    url_list,
    reports,
    requests,
    responses,
    report,
    request,
    response,
    url_fuzz,
    traversal_check,
    form_fuzz,
    progress,
    total,
  } = useSelector(
    (state) => ({
      console: state.loading.console,
      loading: state.loading.loading,
      url: state.user.url,
      url_list: state.user.url_list,
      reports: state.user.reports,
      requests: state.user.requests,
      responses: state.user.responses,
      report: state.user.report,
      request: state.user.request,
      response: state.user.response,
      url_fuzz: state.user.url_fuzz,
      traversal_check: state.user.traversal_check,
      form_fuzz: state.user.form_fuzz,
      progress: state.loading.progress,
      total: state.loading.total,
    }),
    shallowEqual
  );

  const { sendMessage, lastMessage, readyState } = useWebSocket(
    "wss://sdp-test.sdp-scanner.site/ws/scan/" 
  );
  /*
    배포할때 -> "wss://sdp-test.sdp-scanner.site/ws/scan/"
  */

  const connectionStatus = {
    [ReadyState.CONNECTING]: "Connecting",
    [ReadyState.OPEN]: "Open",
    [ReadyState.CLOSING]: "Closing",
    [ReadyState.CLOSED]: "Closed",
    [ReadyState.UNINSTANTIATED]: "Uninstantiated",
  }[readyState];

  useEffect(() => {
    if (lastMessage != null) {
      const results = JSON.parse(lastMessage.data);
      if (results.urlList) {
        dispatch(userActions.set_url_list(results.urlList));
        if (url_fuzz && form_fuzz) {
          dispatch(loadingActions.add_total2());
        } else {
          dispatch(loadingActions.add_total());
        }
      } else if (results.reports) {
        dispatch(userActions.set_results(results));
        dispatch(loadingActions.add_progress());
      } else if (results.message) {
        dispatch(loadingActions.set_loading_console(results.message));
        if (results.message == "all good") {
          set_toast_Active(true);
        }
      }
    }
  }, [lastMessage]);

  useEffect(() => {
    if (reports.length > 0 && first_rendering) {
      const req = requests.find((el) => el.id === reports[0].id);
      const res = responses.find((el) => el.id === reports[0].id);
      dispatch(userActions.set_request(req));
      dispatch(userActions.set_response(res));
      dispatch(userActions.set_report(reports[0]));

      set_first_rendering(false);
    }
  }, [reports]);

  useEffect(() => {
    if (connectionStatus == "Closed") {
      dispatch(loadingActions.finishLoading());
    }
  }, [connectionStatus]);

  useEffect(() => {
    return () => {
      dispatch(loadingActions.finishLoading());
      dispatch(userActions.reset_msg());
    };
  }, []);

  useEffect(() => {
    if (toast_Active == true) {
      setTimeout(() => {
        set_toast_Active(false);
      }, 5000);
    }
  }, [toast_Active]);

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

  const handleClickSendMessage = useCallback(() => {
    if (url.length > 0) {
      const token = sessionStorage.getItem("token");
      dispatch(loadingActions.startLoading());
      dispatch(loadingActions.set_loading_console("sub domain scanning..."));
      sendMessage(
        JSON.stringify({
          token: `Token ${token}`,
          target: url,
          url_fuzz: url_fuzz,
          traversal_check: traversal_check,
          form_fuzz: form_fuzz,
        })
      );
    } else {
      alert("url제대로");
    }
  }, [url, url_fuzz, traversal_check, form_fuzz]);

  const handleInputurl = (e) => {
    dispatch(userActions.set_url(e.target.value));
  };

  const handleUrl_fuzz = (e) => {
    dispatch(userActions.set_url_fuzz(e.target.checked));
  };
  const handleTraversal_check = (e) => {
    dispatch(userActions.set_traversal_check(e.target.checked));
  };
  const handleForm_fuzz = (e) => {
    dispatch(userActions.set_form_fuzz(e.target.checked));
  };

  const handleRowclick = (e) => {
    setCollapse(false);
    const req = requests.find((el) => el.id === e.id);
    const res = responses.find((el) => el.id === e.id);
    dispatch(userActions.set_request(req));
    dispatch(userActions.set_response(res));
    dispatch(userActions.set_report(e));
  };

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
    if (reports.length > 0) {
      return Math.ceil(reports.length / 10);
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
          <CCard accentColor="primary">
            <CCardHeader>Web Scan</CCardHeader>
            <CCardBody>
              <CForm
                action=""
                method="post"
                encType="multipart/form-data"
                className="form-horizontal"
              >
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
                    <CLabel htmlFor="select">Url Fuzz</CLabel>
                  </CCol>
                  <CCol xs="12" md="9">
                    <CSwitch
                      className={"mx-1"}
                      variant={"3d"}
                      color={"primary"}
                      defaultChecked
                      onChange={handleUrl_fuzz}
                    />
                  </CCol>
                </CFormGroup>

                <CFormGroup row>
                  <CCol md="3">
                    <CLabel htmlFor="select">Form Fuzz</CLabel>
                  </CCol>
                  <CCol xs="12" md="9">
                    <CSwitch
                      className={"mx-1"}
                      variant={"3d"}
                      color={"primary"}
                      defaultChecked
                      onChange={handleForm_fuzz}
                    />
                  </CCol>
                </CFormGroup>

                <CFormGroup row>
                  <CCol md="3">
                    <CLabel htmlFor="select">Traversal Check</CLabel>
                  </CCol>
                  <CCol xs="12" md="9">
                    <CSwitch
                      className={"mx-1"}
                      variant={"3d"}
                      color={"primary"}
                      defaultChecked
                      onChange={handleTraversal_check}
                    />
                  </CCol>
                </CFormGroup>
              </CForm>
            </CCardBody>
            <CCardFooter>
              <CButton
                type="button"
                size="sm"
                color="primary"
                onClick={handleClickSendMessage}
                disabled={readyState !== ReadyState.OPEN || loading}
              >
                <CIcon name="cil-scrubber" /> Scan
              </CButton>
              {loading && (
                <span>
                  <CSpinner
                    color="primary"
                    style={{
                      width: "1.5rem",
                      height: "1.5rem",
                      marginLeft: "10px",
                      marginRight: "10px",
                    }}
                  />
                  <small style={{ color: "red" }}>{console}</small>
                </span>
              )}
            </CCardFooter>
          </CCard>
          <CCard>
            <CCardHeader>Url List</CCardHeader>
            <CCardBody style={{ maxHeight: "100px", overflow: "auto" }}>
              <ul>
                {url_list.map((url, idx) => (
                  <li key={idx}>
                    <a href={url} target="_blank">
                      {url}
                    </a>
                  </li>
                ))}
              </ul>
            </CCardBody>
          </CCard>
        </CCol>
        <CCol xs="12" md="7">
          <CCard style={{ height: "480px", overflow: "auto" }}>
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
                    {report.url ? (
                      <p>
                        <strong>Url</strong> :{" "}
                        <a href={report.url} target="_blank">
                          {report.url}
                        </a>
                      </p>
                    ) : null}
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
                            disabled={loading}
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
                    {report.url ? (
                      <p>
                        <strong>Url</strong> :{" "}
                        <a href={report.url} target="_blank">
                          {report.url}
                        </a>
                      </p>
                    ) : null}
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
          {loading && (
            <CProgress
              animated
              value={progress}
              max={total}
              showPercentage
              className="mb-3"
            />
          )}
          <CCard>
            <CCardBody style={{ height: "280px", overflow: "auto" }}>
              <CDataTable
                items={reports}
                fields={fields}
                activePage={currentPage}
                hover
                striped
                bordered
                size="sm"
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
                  className="d-md-down-none"
                  size="sm"
                  activePage={currentPage}
                  limit={10}
                  pages={scan_pages}
                  align="center"
                  onActivePageChange={setCurrentPage}
                />
                <CPagination
                  className="d-lg-none"
                  size="sm"
                  activePage={currentPage}
                  limit={6}
                  pages={scan_pages}
                  align="center"
                  onActivePageChange={setCurrentPage}
                />
              </CCardFooter>
            )}
          </CCard>
        </CCol>
      </CRow>

      <CToaster position="top-center">
        <CToast show={toast_Active} autohide={3000} fade>
          <CToastHeader>Notification</CToastHeader>
          <CToastBody>Scanned Successfully!</CToastBody>
        </CToast>
      </CToaster>
    </>
  );
};

export default Webscan;
