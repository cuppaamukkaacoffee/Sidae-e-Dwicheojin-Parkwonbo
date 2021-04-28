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
  CRow,
  CListGroupItem,
  CSpinner,
  CPagination,
  CBadge,
  CCollapse,
  CFade,
} from "@coreui/react";
import CIcon from "@coreui/icons-react";
import * as userActions from "src/store/modules/user/actions";

const fields = ["target", "open_ports", "timestamp"];
const fields1 = ["ip_address", "port_number", "port_protocol", "port_status"];
const Net_result = () => {
  const dispatch = useDispatch();
  const [currentPage, setCurrentPage] = useState(1);
  const [collapseMulti, setCollapseMulti] = useState([false, false, false]);
  const [col1, setCol1] = useState(true);
  const [col2, setCol2] = useState(true);
  const [col3, setCol3] = useState(true);
  const [col4, setCol4] = useState(true);
  const [col5, setCol5] = useState(true);
  const [col6, setCol6] = useState(true);
  const [col7, setCol7] = useState(true);
  const [col8, setCol8] = useState(true);
  const [col9, setCol9] = useState(true);
  const [col10, setCol10] = useState(true);
  const [col11, setCol11] = useState(true);
  const [col12, setCol12] = useState(true);
  const [col13, setCol13] = useState(true);
  const [col14, setCol14] = useState(true);
  const [col15, setCol15] = useState(true);
  const [col16, setCol16] = useState(true);
  const [col17, setCol17] = useState(true);
  const [col18, setCol18] = useState(true);

  const { id, url, net_targets, net_results, errorMsg, loading } = useSelector(
    (state) => ({
      id: state.user.id,
      url: state.user.url,
      net_targets: state.user.net_targets,
      net_results: state.user.net_results,
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

  const handleInputid = (e) => {
    dispatch(userActions.set_id(e.target.value));
  };

  const handleInputurl = (e) => {
    dispatch(userActions.set_url(e.target.value));
  };

  const handleRowclick = (e) => {
    setCollapseMulti([true, false, false]);
    dispatch(
      userActions.net_results_check({
        username: e.username,
        scan_session_id: e.scan_session_id,
      })
    );
  };

  const handleSubmit_results = useCallback(() => {
    if (id === sessionStorage.getItem("id")) {
      dispatch(userActions.net_targets_check({ id: id, url: url }));
    } else {
      alert("아이디를 다시 입력하세요");
    }
  }, [id, url]);

  const scan_pages = (() => {
    if (net_targets.length > 0) {
      return Math.ceil(net_targets.length / 10);
    }
  })();

  return (
    <>
      <CRow>
        <CCol xs="12" md="5">
          <CCard>
            <CCardHeader>Network Scan Results</CCardHeader>
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
          <CCard>
            <CCardBody style={{ height: "350px", overflow: "auto" }}>
              <CDataTable
                items={net_targets}
                fields={fields}
                hover
                striped
                bordered
                size="sm"
                activePage={currentPage}
                itemsPerPage={10}
                onRowClick={handleRowclick}
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
        <CCol xs="12" md="7">
          <CCard>
            <CCardHeader>
              <CButton
                color={collapseMulti[0] ? "dark" : null}
                onClick={() => {
                  setCollapseMulti([true, false, false]);
                }}
              >
                <strong>Whois</strong>
              </CButton>{" "}
              <CButton
                color={collapseMulti[1] ? "dark" : null}
                onClick={() => {
                  setCollapseMulti([false, true, false]);
                }}
              >
                <strong>Robot</strong>
              </CButton>{" "}
              <CButton
                color={collapseMulti[2] ? "dark" : null}
                onClick={() => {
                  setCollapseMulti([false, false, true]);
                }}
              >
                <strong>IP address / Port</strong>
              </CButton>{" "}
            </CCardHeader>
            <CCardBody style={{ height: "650px", overflow: "auto" }}>
              <CCollapse show={collapseMulti[0]}>
                <CFade timeout={300} in={collapseMulti[0]}>
                  <CButton onClick={() => setCol1(!col1)}>
                    <span style={{ fontWeight: "bold" }}>
                      {col1 ? (
                        <CIcon size="sm" name="cilChevronDoubleUp" />
                      ) : (
                        <CIcon size="sm" name="cilChevronDoubleDown" />
                      )}
                      Domain Name
                    </span>
                  </CButton>
                  <CCollapse show={col1} style={{ marginLeft: "30px" }}>
                    {net_results.whois &&
                      net_results.whois.domain_name.map((item, idx) => (
                        <li key={idx}>{item}</li>
                      ))}
                  </CCollapse>
                  <hr style={{ width: "100%" }} />

                  <CButton onClick={() => setCol2(!col2)}>
                    <span style={{ fontWeight: "bold" }}>
                      {col2 ? (
                        <CIcon size="sm" name="cilChevronDoubleUp" />
                      ) : (
                        <CIcon size="sm" name="cilChevronDoubleDown" />
                      )}
                      Registrar
                    </span>
                  </CButton>
                  <CCollapse show={col2} style={{ marginLeft: "30px" }}>
                    {net_results.whois &&
                      net_results.whois.registrar.map((item, idx) => (
                        <li key={idx}>{item}</li>
                      ))}
                  </CCollapse>
                  <hr style={{ width: "100%" }} />

                  <CButton onClick={() => setCol3(!col3)}>
                    <span style={{ fontWeight: "bold" }}>
                      {col3 ? (
                        <CIcon size="sm" name="cilChevronDoubleUp" />
                      ) : (
                        <CIcon size="sm" name="cilChevronDoubleDown" />
                      )}
                      Whois Server
                    </span>
                  </CButton>
                  <CCollapse show={col3} style={{ marginLeft: "30px" }}>
                    {net_results.whois &&
                      net_results.whois.whois_server.map((item, idx) => (
                        <li key={idx}>{item}</li>
                      ))}
                  </CCollapse>
                  <hr style={{ width: "100%" }} />

                  <CButton onClick={() => setCol4(!col4)}>
                    <span style={{ fontWeight: "bold" }}>
                      {col4 ? (
                        <CIcon size="sm" name="cilChevronDoubleUp" />
                      ) : (
                        <CIcon size="sm" name="cilChevronDoubleDown" />
                      )}
                      Referral Url
                    </span>
                  </CButton>
                  <CCollapse show={col4} style={{ marginLeft: "30px" }}>
                    {net_results.whois &&
                      net_results.whois.referral_url.map((item, idx) => (
                        <li key={idx}>{item}</li>
                      ))}
                  </CCollapse>
                  <hr style={{ width: "100%" }} />

                  <CButton onClick={() => setCol5(!col5)}>
                    <span style={{ fontWeight: "bold" }}>
                      {col5 ? (
                        <CIcon size="sm" name="cilChevronDoubleUp" />
                      ) : (
                        <CIcon size="sm" name="cilChevronDoubleDown" />
                      )}
                      Updated Date
                    </span>
                  </CButton>
                  <CCollapse show={col5} style={{ marginLeft: "30px" }}>
                    {net_results.whois &&
                      net_results.whois.updated_date.map((item, idx) => (
                        <li key={idx}>{item}</li>
                      ))}
                  </CCollapse>
                  <hr style={{ width: "100%" }} />

                  <CButton onClick={() => setCol6(!col6)}>
                    <span style={{ fontWeight: "bold" }}>
                      {col6 ? (
                        <CIcon size="sm" name="cilChevronDoubleUp" />
                      ) : (
                        <CIcon size="sm" name="cilChevronDoubleDown" />
                      )}
                      Creation Date
                    </span>
                  </CButton>
                  <CCollapse show={col6} style={{ marginLeft: "30px" }}>
                    {net_results.whois &&
                      net_results.whois.creation_date.map((item, idx) => (
                        <li key={idx}>{item}</li>
                      ))}
                  </CCollapse>
                  <hr style={{ width: "100%" }} />

                  <CButton onClick={() => setCol7(!col7)}>
                    <span style={{ fontWeight: "bold" }}>
                      {col7 ? (
                        <CIcon size="sm" name="cilChevronDoubleUp" />
                      ) : (
                        <CIcon size="sm" name="cilChevronDoubleDown" />
                      )}
                      Expiration Date
                    </span>
                  </CButton>
                  <CCollapse show={col7} style={{ marginLeft: "30px" }}>
                    {net_results.whois &&
                      net_results.whois.expiration_date.map((item, idx) => (
                        <li key={idx}>{item}</li>
                      ))}
                  </CCollapse>
                  <hr style={{ width: "100%" }} />

                  <CButton onClick={() => setCol8(!col8)}>
                    <span style={{ fontWeight: "bold" }}>
                      {col8 ? (
                        <CIcon size="sm" name="cilChevronDoubleUp" />
                      ) : (
                        <CIcon size="sm" name="cilChevronDoubleDown" />
                      )}
                      Name Servers
                    </span>
                  </CButton>
                  <CCollapse show={col8} style={{ marginLeft: "30px" }}>
                    {net_results.whois &&
                      net_results.whois.name_servers.map((item, idx) => (
                        <li key={idx}>{item}</li>
                      ))}
                  </CCollapse>
                  <hr style={{ width: "100%" }} />

                  <CButton onClick={() => setCol9(!col9)}>
                    <span style={{ fontWeight: "bold" }}>
                      {col9 ? (
                        <CIcon size="sm" name="cilChevronDoubleUp" />
                      ) : (
                        <CIcon size="sm" name="cilChevronDoubleDown" />
                      )}
                      Status
                    </span>
                  </CButton>
                  <CCollapse show={col9} style={{ marginLeft: "30px" }}>
                    {net_results.whois &&
                      net_results.whois.status.map((item, idx) => (
                        <li key={idx}>{item}</li>
                      ))}
                  </CCollapse>
                  <hr style={{ width: "100%" }} />

                  <CButton onClick={() => setCol10(!col10)}>
                    <span style={{ fontWeight: "bold" }}>
                      {col10 ? (
                        <CIcon size="sm" name="cilChevronDoubleUp" />
                      ) : (
                        <CIcon size="sm" name="cilChevronDoubleDown" />
                      )}
                      Emails
                    </span>
                  </CButton>
                  <CCollapse show={col10} style={{ marginLeft: "30px" }}>
                    {net_results.whois &&
                      net_results.whois.emails.map((item, idx) => (
                        <li key={idx}>{item}</li>
                      ))}
                  </CCollapse>
                  <hr style={{ width: "100%" }} />

                  <CButton onClick={() => setCol11(!col11)}>
                    <span style={{ fontWeight: "bold" }}>
                      {col11 ? (
                        <CIcon size="sm" name="cilChevronDoubleUp" />
                      ) : (
                        <CIcon size="sm" name="cilChevronDoubleDown" />
                      )}
                      Dnssec
                    </span>
                  </CButton>
                  <CCollapse show={col11} style={{ marginLeft: "30px" }}>
                    {net_results.whois &&
                      net_results.whois.dnssec.map((item, idx) => (
                        <li key={idx}>{item}</li>
                      ))}
                  </CCollapse>
                  <hr style={{ width: "100%" }} />

                  <CButton onClick={() => setCol12(!col12)}>
                    <span style={{ fontWeight: "bold" }}>
                      {col12 ? (
                        <CIcon size="sm" name="cilChevronDoubleUp" />
                      ) : (
                        <CIcon size="sm" name="cilChevronDoubleDown" />
                      )}
                      Name
                    </span>
                  </CButton>
                  <CCollapse show={col12} style={{ marginLeft: "30px" }}>
                    {net_results.whois &&
                      net_results.whois.name.map((item, idx) => (
                        <li key={idx}>{item}</li>
                      ))}
                  </CCollapse>
                  <hr style={{ width: "100%" }} />

                  <CButton onClick={() => setCol13(!col13)}>
                    <span style={{ fontWeight: "bold" }}>
                      {col13 ? (
                        <CIcon size="sm" name="cilChevronDoubleUp" />
                      ) : (
                        <CIcon size="sm" name="cilChevronDoubleDown" />
                      )}
                      Org
                    </span>
                  </CButton>
                  <CCollapse show={col13} style={{ marginLeft: "30px" }}>
                    {net_results.whois &&
                      net_results.whois.org.map((item, idx) => (
                        <li key={idx}>{item}</li>
                      ))}
                  </CCollapse>
                  <hr style={{ width: "100%" }} />

                  <CButton onClick={() => setCol14(!col14)}>
                    <span style={{ fontWeight: "bold" }}>
                      {col14 ? (
                        <CIcon size="sm" name="cilChevronDoubleUp" />
                      ) : (
                        <CIcon size="sm" name="cilChevronDoubleDown" />
                      )}
                      Address
                    </span>
                  </CButton>
                  <CCollapse show={col14} style={{ marginLeft: "30px" }}>
                    {net_results.whois &&
                      net_results.whois.address.map((item, idx) => (
                        <li key={idx}>{item}</li>
                      ))}
                  </CCollapse>
                  <hr style={{ width: "100%" }} />

                  <CButton onClick={() => setCol15(!col15)}>
                    <span style={{ fontWeight: "bold" }}>
                      {col15 ? (
                        <CIcon size="sm" name="cilChevronDoubleUp" />
                      ) : (
                        <CIcon size="sm" name="cilChevronDoubleDown" />
                      )}
                      City
                    </span>
                  </CButton>
                  <CCollapse show={col15} style={{ marginLeft: "30px" }}>
                    {net_results.whois &&
                      net_results.whois.city.map((item, idx) => (
                        <li key={idx}>{item}</li>
                      ))}
                  </CCollapse>
                  <hr style={{ width: "100%" }} />

                  <CButton onClick={() => setCol16(!col16)}>
                    <span style={{ fontWeight: "bold" }}>
                      {col16 ? (
                        <CIcon size="sm" name="cilChevronDoubleUp" />
                      ) : (
                        <CIcon size="sm" name="cilChevronDoubleDown" />
                      )}
                      State
                    </span>
                  </CButton>
                  <CCollapse show={col16} style={{ marginLeft: "30px" }}>
                    {net_results.whois &&
                      net_results.whois.state.map((item, idx) => (
                        <li key={idx}>{item}</li>
                      ))}
                  </CCollapse>
                  <hr style={{ width: "100%" }} />

                  <CButton onClick={() => setCol17(!col17)}>
                    <span style={{ fontWeight: "bold" }}>
                      {col17 ? (
                        <CIcon size="sm" name="cilChevronDoubleUp" />
                      ) : (
                        <CIcon size="sm" name="cilChevronDoubleDown" />
                      )}
                      Zipcode
                    </span>
                  </CButton>
                  <CCollapse show={col17} style={{ marginLeft: "30px" }}>
                    {net_results.whois &&
                      net_results.whois.zipcode.map((item, idx) => (
                        <li key={idx}>{item}</li>
                      ))}
                  </CCollapse>
                  <hr style={{ width: "100%" }} />

                  <CButton onClick={() => setCol18(!col18)}>
                    <span style={{ fontWeight: "bold" }}>
                      {col18 ? (
                        <CIcon size="sm" name="cilChevronDoubleUp" />
                      ) : (
                        <CIcon size="sm" name="cilChevronDoubleDown" />
                      )}
                      Country
                    </span>
                  </CButton>
                  <CCollapse show={col18} style={{ marginLeft: "30px" }}>
                    {net_results.whois &&
                      net_results.whois.country.map((item, idx) => (
                        <li key={idx}>{item}</li>
                      ))}
                  </CCollapse>
                  <hr style={{ width: "100%" }} />
                </CFade>
              </CCollapse>
              <CCollapse show={collapseMulti[1]}>
                <CFade timeout={300} in={collapseMulti[1]}>
                  {net_results.robot !== undefined ? (
                    net_results.robot.txt === "" ? (
                      <p>No Robots.txt on {net_results.robot.target}</p>
                    ) : (
                      <p style={{ whiteSpace: "pre-wrap" }}>
                        {net_results.robot.txt}
                      </p>
                    )
                  ) : null}
                </CFade>
              </CCollapse>
              <CCollapse show={collapseMulti[2]}>
                <CFade timeout={300} in={collapseMulti[2]}>
                  <h4>IP Address</h4>
                  {net_results.ips &&
                    net_results.ips.map((item, idx) => (
                      <CListGroupItem key={idx}>
                        {item.ip_address}
                      </CListGroupItem>
                    ))}
                  <br />
                  <h4>Open Ports</h4>
                  <CDataTable
                    items={net_results.ports}
                    fields={fields1}
                    hover
                    striped
                    bordered
                    size="sm"
                    scopedSlots={{
                      port_status: (item) => (
                        <td>
                          <CBadge color="primary">{item.port_status}</CBadge>
                        </td>
                      ),
                    }}
                  />
                </CFade>
              </CCollapse>
            </CCardBody>
          </CCard>
        </CCol>
      </CRow>
    </>
  );
};

export default Net_result;
