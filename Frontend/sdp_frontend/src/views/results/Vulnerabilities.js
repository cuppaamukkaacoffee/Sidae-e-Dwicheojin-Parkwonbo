import { useState, useEffect } from "react";
import { useSelector, useDispatch, shallowEqual } from "react-redux";
import React from "react";
import {
  CDataTable,
  CCard,
  CCardHeader,
  CCardBody,
  CCardFooter,
  CPagination,
  CBadge,
} from "@coreui/react";
import * as userActions from "src/store/modules/user/actions";
import history from "src/utils/history";

const fields = ["vulnerability", "target", "status", "timestamp"];

const Vulnerabilities = ({ location }) => {
  const dispatch = useDispatch();
  const [currentPage1, setCurrentPage1] = useState(1);
  const [currentPage2, setCurrentPage2] = useState(1);
  const [currentPage3, setCurrentPage3] = useState(1);

  const { requests, responses, vul_reports } = useSelector(
    (state) => ({
      requests: state.user.requests,
      responses: state.user.responses,
      vul_reports: state.user.vul_reports,
    }),
    shallowEqual
  );

  useEffect(() => {
    if (location.state) {
      const id = window.sessionStorage.getItem("id");
      if (location.state.vul) {
        dispatch(
          userActions.vul_results_check({
            id: id,
            result_string: "vulnerable",
            vul: location.state.vul,
            scan_session_id: location.state.id,
            with_headers: true,
          })
        );
      } else {
        dispatch(
          userActions.vul_results_check({
            id: id,
            result_string: "vulnerable",
            scan_session_id: location.state.id,
            with_headers: true,
          })
        );
      }
    } else {
      const id = window.sessionStorage.getItem("id");
      dispatch(
        userActions.vul_results_check({
          id: id,
          result_string: "vulnerable",
          with_headers: true,
        })
      );
    }

    return () => {
      dispatch(userActions.reset_msg());
    };
  }, []);

  const handleRowclick = (e) => {
    const req = requests.find((el) => el.id === e.id);
    const res = responses.find((el) => el.id === e.id);
    history.push({
      pathname: "/webdetail",
      state: { rep: e, req: req, res: res },
    });
  };

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

  const url_fuzz_reports = vul_reports.filter(
    (el) => el.scan_type === "url_fuzz"
  );
  const form_fuzz_reports = vul_reports.filter(
    (el) => el.scan_type === "form_fuzz"
  );
  const traversal_check_reports = vul_reports.filter(
    (el) => el.scan_type === "traversal_check"
  );

  const url_fuzz_pages = (() => {
    if (url_fuzz_reports.length > 0) {
      return Math.ceil(url_fuzz_reports.length / 10);
    }
  })();

  const form_fuzz_pages = (() => {
    if (form_fuzz_reports.length > 0) {
      return Math.ceil(form_fuzz_reports.length / 10);
    }
  })();

  const traversal_check_pages = (() => {
    if (traversal_check_reports.length > 0) {
      return Math.ceil(traversal_check_reports.length / 10);
    }
  })();

  return (
    <>
      <CCard>
        <CCardHeader>
          <h5>Url Fuzz vulnerabilities</h5>
        </CCardHeader>
        {url_fuzz_pages && (
          <>
            <CCardBody style={{ height: "280px", overflow: "auto" }}>
              <CDataTable
                items={url_fuzz_reports}
                fields={fields}
                striped
                hover
                bordered
                size="sm"
                activePage={currentPage1}
                itemsPerPage={10}
                scopedSlots={{
                  target: (item) => (
                    <td style={{ color: "red" }}>{item.target}</td>
                  ),
                  vulnerability: (item) => (
                    <td style={{ color: "red" }}>{item.vulnerability}</td>
                  ),
                  status: (item) => (
                    <td>
                      <CBadge color={getBadge(item.status)}>
                        {item.status}
                      </CBadge>
                    </td>
                  ),
                }}
                onRowClick={handleRowclick}
              />
            </CCardBody>
            <CCardFooter>
              <CPagination
                className="d-md-down-none"
                size="sm"
                activePage={currentPage1}
                limit={10}
                pages={url_fuzz_pages}
                align="center"
                onActivePageChange={setCurrentPage1}
              />
              <CPagination
                className="d-lg-none"
                size="sm"
                activePage={currentPage1}
                limit={6}
                pages={url_fuzz_pages}
                align="center"
                onActivePageChange={setCurrentPage1}
              />
            </CCardFooter>
          </>
        )}
      </CCard>
      <CCard>
        <CCardHeader>
          <h5>Form Fuzz vulnerabilities</h5>
        </CCardHeader>
        {form_fuzz_pages && (
          <>
            <CCardBody style={{ height: "280px", overflow: "auto" }}>
              <CDataTable
                items={form_fuzz_reports}
                fields={fields}
                striped
                hover
                bordered
                size="sm"
                itemsPerPage={10}
                activePage={currentPage2}
                scopedSlots={{
                  target: (item) => (
                    <td style={{ color: "red" }}>{item.target}</td>
                  ),
                  vulnerability: (item) => (
                    <td style={{ color: "red" }}>{item.vulnerability}</td>
                  ),
                  status: (item) => (
                    <td>
                      <CBadge color={getBadge(item.status)}>
                        {item.status}
                      </CBadge>
                    </td>
                  ),
                }}
                onRowClick={handleRowclick}
              />
            </CCardBody>
            <CCardFooter>
              <CPagination
                className="d-md-down-none"
                size="sm"
                activePage={currentPage2}
                limit={10}
                pages={form_fuzz_pages}
                align="center"
                onActivePageChange={(e) => setCurrentPage2(e)}
              />
              <CPagination
                className="d-lg-none"
                size="sm"
                activePage={currentPage2}
                limit={6}
                pages={form_fuzz_pages}
                align="center"
                onActivePageChange={(e) => setCurrentPage2(e)}
              />
            </CCardFooter>
          </>
        )}
      </CCard>
      <CCard>
        <CCardHeader>
          <h5>Traversal Check vulnerabilities</h5>
        </CCardHeader>
        {traversal_check_pages && (
          <>
            <CCardBody style={{ height: "280px", overflow: "auto" }}>
              <CDataTable
                items={traversal_check_reports}
                fields={fields}
                striped
                hover
                bordered
                size="sm"
                itemsPerPage={10}
                activePage={currentPage3}
                scopedSlots={{
                  target: (item) => (
                    <td style={{ color: "red" }}>{item.target}</td>
                  ),
                  vulnerability: (item) => (
                    <td style={{ color: "red" }}>{item.vulnerability}</td>
                  ),
                  status: (item) => (
                    <td>
                      <CBadge color={getBadge(item.status)}>
                        {item.status}
                      </CBadge>
                    </td>
                  ),
                }}
                onRowClick={handleRowclick}
              />
            </CCardBody>
            <CCardFooter>
              <CPagination
                className="d-md-down-none"
                size="sm"
                activePage={currentPage3}
                limit={10}
                pages={traversal_check_pages}
                align="center"
                onActivePageChange={setCurrentPage3}
              />
              <CPagination
                className="d-lg-none"
                size="sm"
                activePage={currentPage3}
                limit={10}
                pages={traversal_check_pages}
                align="center"
                onActivePageChange={setCurrentPage3}
              />
            </CCardFooter>
          </>
        )}
      </CCard>
    </>
  );
};

export default Vulnerabilities;
