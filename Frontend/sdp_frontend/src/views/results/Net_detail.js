import { useEffect, useState } from "react";
import { useSelector, useDispatch, shallowEqual } from "react-redux";
import React from "react";
import * as userActions from "src/store/modules/user/actions";
import {
  CCollapse,
  CCard,
  CCardBody,
  CCardHeader,
  CButton,
  CDataTable,
  CBadge,
} from "@coreui/react";
import CIcon from "@coreui/icons-react";
const fields = ["ip_address", "port_number", "port_protocol", "port_status"];

const Net_detail = ({ location }) => {
  const dispatch = useDispatch();

  const [whois, setWhois] = useState(false);
  const [robot, setRobot] = useState(false);
  const [ips, setIps] = useState(true);
  const [port, setPort] = useState(true);

  const { username } = location.state;
  const { scan_session_id } = location.state;
  const { target } = location.state;
  const { timestamp } = location.state;

  const { net_results } = useSelector(
    (state) => ({
      net_results: state.user.net_results,
    }),
    shallowEqual
  );

  useEffect(() => {
    console.log(location.state);
    dispatch(
      userActions.net_results_check({
        username: username,
        scan_session_id: scan_session_id,
      })
    );
    return () => {
      dispatch(userActions.reset_msg());
    };
  }, []);

  return (
    <CCard>
      <CCardHeader>
        <h4>Network Scan Report</h4>
      </CCardHeader>
      <CCardBody>
        <span style={{ fontWeight: "bold", fontSize: "15px" }}>Target</span> :{" "}
        {target}
        <br />
        <span style={{ fontWeight: "bold", fontSize: "15px" }}>
          Date
        </span> : {timestamp}
        <br />
        <br />
        <CButton onClick={() => setIps(!ips)}>
          <span style={{ fontWeight: "bold", fontSize: "18px" }}>
            {ips ? (
              <CIcon size="md" name="cilChevronDoubleUp" />
            ) : (
              <CIcon size="sm" name="cilChevronDoubleDown" />
            )}
            IP Address
          </span>
        </CButton>
        <CCollapse show={ips} style={{ marginLeft: "20px" }}>
          {net_results.ips &&
            net_results.ips.map((item, idx) => (
              <li key={idx}>{item.ip_address}</li>
            ))}
        </CCollapse>
        <hr style={{ width: "100%" }} />
        <CButton onClick={() => setPort(!port)}>
          <span style={{ fontWeight: "bold", fontSize: "18px" }}>
            {port ? (
              <CIcon size="md" name="cilChevronDoubleUp" />
            ) : (
              <CIcon size="sm" name="cilChevronDoubleDown" />
            )}
            Open Ports
          </span>
        </CButton>
        <CCollapse show={port} style={{ marginLeft: "20px" }}>
          <CDataTable
            items={net_results.ports}
            fields={fields}
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
        </CCollapse>
        <hr style={{ width: "100%" }} />
        <CButton onClick={() => setWhois(!whois)}>
          <span style={{ fontWeight: "bold", fontSize: "18px" }}>
            {whois ? (
              <CIcon size="md" name="cilChevronDoubleUp" />
            ) : (
              <CIcon size="sm" name="cilChevronDoubleDown" />
            )}
            Whois
          </span>
        </CButton>
        <CCollapse show={whois} style={{ marginLeft: "20px" }}>
          <p>
            <strong>Address</strong>
          </p>
          {net_results.whois &&
            net_results.whois.address.map((item, idx) => (
              <li key={idx}>{item}</li>
            ))}
          <br />
          <p>
            <strong>City</strong>
          </p>
          {net_results.whois &&
            net_results.whois.city.map((item, idx) => (
              <li key={idx}>{item}</li>
            ))}
          <br />
          <p>
            <strong>Country</strong>
          </p>
          {net_results.whois &&
            net_results.whois.country.map((item, idx) => (
              <li key={idx}>{item}</li>
            ))}
          <br />
          <p>
            <strong>Creation Date</strong>
          </p>
          {net_results.whois &&
            net_results.whois.creation_date.map((item, idx) => (
              <li key={idx}>{item}</li>
            ))}
          <br />
          <p>
            <strong>Dnssec</strong>
          </p>
          {net_results.whois &&
            net_results.whois.dnssec.map((item, idx) => (
              <li key={idx}>{item}</li>
            ))}
          <br />
          <p>
            <strong>Domain Name</strong>
          </p>
          {net_results.whois &&
            net_results.whois.domain_name.map((item, idx) => (
              <li key={idx}>{item}</li>
            ))}
          <br />
          <p>
            <strong>Emails</strong>
          </p>
          {net_results.whois &&
            net_results.whois.emails.map((item, idx) => (
              <li key={idx}>{item}</li>
            ))}
          <br />
          <p>
            <strong>Expiration Date</strong>
          </p>
          {net_results.whois &&
            net_results.whois.expiration_date.map((item, idx) => (
              <li key={idx}>{item}</li>
            ))}
          <br />
          <p>
            <strong>Name</strong>
          </p>
          {net_results.whois &&
            net_results.whois.name.map((item, idx) => (
              <li key={idx}>{item}</li>
            ))}
          <br />
          <p>
            <strong>Name Servers</strong>
          </p>
          {net_results.whois &&
            net_results.whois.name_servers.map((item, idx) => (
              <li key={idx}>{item}</li>
            ))}
          <br />
          <p>
            <strong>Org</strong>
          </p>
          {net_results.whois &&
            net_results.whois.org.map((item, idx) => <li key={idx}>{item}</li>)}
          <br />
          <p>
            <strong>Referral Url</strong>
          </p>
          {net_results.whois &&
            net_results.whois.referral_url.map((item, idx) => (
              <li key={idx}>{item}</li>
            ))}
          <br />
          <p>
            <strong>Registrar</strong>
          </p>
          {net_results.whois &&
            net_results.whois.registrar.map((item, idx) => (
              <li key={idx}>{item}</li>
            ))}
          <br />
          <p>
            <strong>State</strong>
          </p>
          {net_results.whois &&
            net_results.whois.state.map((item, idx) => (
              <li key={idx}>{item}</li>
            ))}
          <br />
          <p>
            <strong>Status</strong>
          </p>
          {net_results.whois &&
            net_results.whois.status.map((item, idx) => (
              <li key={idx}>{item}</li>
            ))}
          <br />
          <p>
            <strong>Updated Date</strong>
          </p>
          {net_results.whois &&
            net_results.whois.updated_date.map((item, idx) => (
              <li key={idx}>{item}</li>
            ))}
          <br />
          <p>
            <strong>Whois Server</strong>
          </p>
          {net_results.whois &&
            net_results.whois.whois_server.map((item, idx) => (
              <li key={idx}>{item}</li>
            ))}
          <br />
          <p>
            <strong>Zipcode</strong>
          </p>
          {net_results.whois &&
            net_results.whois.zipcode.map((item, idx) => (
              <li key={idx}>{item}</li>
            ))}
        </CCollapse>
        <hr style={{ width: "100%" }} />
        <CButton onClick={() => setRobot(!robot)}>
          <span style={{ fontWeight: "bold", fontSize: "18px" }}>
            {robot ? (
              <CIcon size="md" name="cilChevronDoubleUp" />
            ) : (
              <CIcon size="sm" name="cilChevronDoubleDown" />
            )}
            Robot
          </span>
        </CButton>
        <CCollapse
          show={robot}
          style={{ whiteSpace: "pre-wrap", marginLeft: "20px" }}
        >
          {net_results.robot !== undefined ? (
            net_results.robot.txt === "" ? (
              <p>No Robots.txt on {net_results.robot.target}</p>
            ) : (
              <p style={{ whiteSpace: "pre-wrap" }}>{net_results.robot.txt}</p>
            )
          ) : null}
        </CCollapse>
        <hr style={{ width: "100%" }} />
      </CCardBody>
    </CCard>
  );
};

export default Net_detail;
