import { useEffect } from "react";
import { useSelector, useDispatch, shallowEqual } from "react-redux";
import * as userActions from "src/store/modules/user/actions";
import {
  CCard,
  CCardBody,
  CCardHeader,
  CWidgetDropdown,
  CRow,
  CCol,
  CDataTable,
  CLink,
  CCarousel,
  CCarouselItem,
  CCarouselInner,
  CCarouselControl,
  CTabContent,
  CTabPane,
  CTabs,
  CNav,
  CNavItem,
  CNavLink,
  CButton,
} from "@coreui/react";
import { CChartBar, CChartDoughnut } from "@coreui/react-chartjs";
import CIcon from "@coreui/icons-react";
import history from "src/utils/history";

const labels = [
  "SQL Injection",
  "XSS",
  "Open Redirect",
  "Windows Directory Traversal",
  "Linux Directory Traversal",
  "LFI Check",
  "RFI Check",
  "RCE Linux Check",
  "SSTI Check",
];
const fields = ["target", "timestamp"];
const vul_field = ["vul", "num"];
const days = [
  1,
  2,
  3,
  4,
  5,
  6,
  7,
  8,
  9,
  10,
  11,
  12,
  13,
  14,
  15,
  16,
  17,
  18,
  19,
  20,
  21,
  22,
  23,
  24,
  25,
  26,
  27,
  28,
  29,
  30,
];
const backgroundColor = [
  "#41B883",
  "#E46651",
  "#00D8FF",
  "#DD1B16",
  "#FF4500",
  "#FF8C00",
  "#7CFC00",
  "#4169E1",
  "#4B0082",
];

const Dashboards = () => {
  const dispatch = useDispatch();

  const { db_data, targets, net_targets } = useSelector(
    (state) => ({
      db_data: state.user.db_data,
      targets: state.user.targets,
      net_targets: state.user.net_targets,
    }),
    shallowEqual
  );

  useEffect(() => {
    const id = sessionStorage.getItem("id");
    dispatch(userActions.dashboard_data_check({ id: id, with_headers: false }));
    dispatch(userActions.targets_check());
    dispatch(userActions.net_targets_check({ id: id }));
    return () => {
      dispatch(userActions.reset_msg());
    };
  }, []);

  const filterItems_all = (query) => {
    return db_data.filter((el) => el.timestamp.includes(query));
  };

  const filterItems_vul = (query) => {
    return db_data.filter(
      (el) =>
        el.result_string.includes("vulnerable") && el.timestamp.includes(query)
    );
  };

  const filterItems_vulnerability = (query) => {
    return db_data.filter(
      (el) =>
        el.result_string.includes("vulnerable") &&
        el.vulnerability.includes(query)
    );
  };

  const filterItems_all_vul = () => {
    return db_data.filter((el) => el.result_string.includes("vulnerable"));
  };

  const numberPad = (n, width) => {
    n = n + "";
    return n.length >= width
      ? n
      : new Array(width - n.length + 1).join("0") + n;
  };

  const num_click = (vul) => {
    history.push({
      pathname: "/vulnerabilities",
      state: { vul: vul },
    });
  };

  const datasets_scanned = (() => {
    let data = [
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
    ];
    if (db_data.length > 0) {
      for (let i = 0; i < 30; i++) {
        if (i < 10) {
          let num = numberPad(i + 1, 2);
          data[i] = filterItems_all(`2021-05-${num}`).length;
        } else {
          data[i] = filterItems_all(`2021-05-${i + 1}`).length;
        }
      }
    }
    return [
      {
        data: data,
        backgroundColor: "#00D8FF",
        label: "Scanned URL",
        barPercentage: 0.8,
      },
    ];
  })();

  const datasets_vul = (() => {
    let data = [
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
    ];
    if (db_data.length > 0) {
      for (let i = 0; i < 30; i++) {
        if (i < 10) {
          let num = numberPad(i + 1, 2);
          data[i] = filterItems_vul(`2021-05-${num}`).length;
        } else {
          data[i] = filterItems_vul(`2021-05-${i + 1}`).length;
        }
      }
    }
    return [
      {
        data: data,
        backgroundColor: "#DD1B16",
        label: "vulnerable URL",
        barPercentage: 0.8,
      },
    ];
  })();

  const datasets_doughnut = (() => {
    let data = [0, 0, 0, 0, 0, 0, 0, 0, 0];
    if (db_data.length > 0) {
      for (let i = 0; i < 9; i++) {
        data[i] = filterItems_vulnerability(labels[i]).length;
      }
    }
    return [
      {
        data: data,
        backgroundColor: backgroundColor,
      },
    ];
  })();

  const vul_length = (() => {
    let num = 0;
    if (db_data.length > 0) {
      num = filterItems_all_vul().length;
    }
    return String(num);
  })();

  const top_vul = (() => {
    let top_vul = [];
    for (let i = 0; i < 9; i++) {
      top_vul.push({
        vul: labels[i],
        num: filterItems_vulnerability(labels[i]).length,
      });
    }
    return top_vul;
  })();

  return (
    <>
      <CRow>
        <CCol xs = "12" sm="12" md="6">
          <CRow>
            <CCol xs = "4" sm="4" md="4">
              <CWidgetDropdown
                className="d-lg-none" 
                color="danger"
                header={vul_length}
                text="Vul nebilities"
              ></CWidgetDropdown>
              <CWidgetDropdown
                className="d-md-down-none" 
                color="danger"
                header={vul_length}
                text="Vulnerabilities"
                footerSlot={<CIcon name="cilBellExclamation" height="50" />}
              ></CWidgetDropdown>
            </CCol>
            <CCol xs = "4" sm="4" md="4">
              <CWidgetDropdown
                className="d-lg-none"
                color="warning"
                header={String(targets.length)}
                text="Web Scans"
              ></CWidgetDropdown>
              <CWidgetDropdown
                className="d-md-down-none" 
                color="warning"
                header={String(targets.length)}
                text="Web Scans Conducted"
                footerSlot={<CIcon name="cil-speedometer" height="50" />}
              ></CWidgetDropdown>
            </CCol>
            <CCol xs = "4" sm="4" md="4">
              <CWidgetDropdown
                className="d-lg-none"
                color="info"
                header={String(net_targets.length)}
                text="Network Scans"
              ></CWidgetDropdown>
              <CWidgetDropdown
                className="d-md-down-none" 
                color="info"
                header={String(net_targets.length)}
                text="NetworkScans"
                footerSlot={<CIcon name="cil-globe-alt" height="50" />}
              ></CWidgetDropdown>
            </CCol>
          </CRow>

          <CCard className="d-md-down-none">
            <CCardBody>
              <CChartDoughnut
                datasets={datasets_doughnut}
                labels={labels}
                options={{
                  tooltips: {
                    enabled: true,
                  },
                }}
              />
            </CCardBody>
          </CCard>

          <CCard>
            <CCardBody>
              <CCarousel animate autoSlide={3000}>
                <CCarouselInner>
                  <CCarouselItem>
                    <CChartBar
                      datasets={datasets_scanned}
                      labels={days}
                      options={{
                        tooltips: {
                          enabled: true,
                        },
                      }}
                    />
                  </CCarouselItem>
                  <CCarouselItem>
                    <CChartBar
                      datasets={datasets_vul}
                      labels={days}
                      options={{
                        tooltips: {
                          enabled: true,
                        },
                      }}
                    />
                  </CCarouselItem>
                </CCarouselInner>
                <CCarouselControl direction="prev" />
                <CCarouselControl direction="next" />
              </CCarousel>
            </CCardBody>
          </CCard>
        </CCol>
        <CCol sm="12" md="6">
          <CCard
            style={{ height: "400px", overflow: "auto" }}
            accentColor="danger"
          >
            <CTabs>
              <CNav variant="tabs">
                <CNavItem>
                  <CNavLink style={{ color: "black" }}>
                    <span className="d-lg-none">Web Target</span>
                    <span className="d-md-down-none">Recently Web Scanned Target</span>
                  </CNavLink>
                </CNavItem>
                <CNavItem>
                  <CNavLink style={{ color: "black" }}>
                    <span className="d-lg-none">Network Target</span>
                    <span className="d-md-down-none">Recently Network Scanned Target</span>
                  </CNavLink>
                </CNavItem>
              </CNav>
              <CCardBody>
                <CTabContent>
                  <CTabPane>
                    <CDataTable
                      items={targets}
                      fields={fields}
                      size="sm"
                      scopedSlots={{
                        target: (item) => (
                          <td>
                            <CLink
                              style={{ color: "red" }}
                              to={{
                                pathname: "/vulnerabilities",
                                state: { id: item.id },
                              }}
                            >
                              {item.target}
                            </CLink>
                          </td>
                        ),
                      }}
                    />
                  </CTabPane>
                  <CTabPane>
                    <CDataTable
                      items={net_targets}
                      fields={fields}
                      size="sm"
                      scopedSlots={{
                        target: (item) => (
                          <td>
                            <CLink
                              style={{ color: "red" }}
                              to={{
                                pathname: "/netdetail",
                                state: item,
                              }}
                            >
                              {item.target}
                            </CLink>
                          </td>
                        ),
                      }}
                    />
                  </CTabPane>
                </CTabContent>
              </CCardBody>
            </CTabs>
          </CCard>

          <CCard
            style={{ height: "500px", overflow: "auto" }}
            accentColor="danger"
          >
            <CCardHeader style={{ color: "black" }}>
              Top Vulnerabilities
            </CCardHeader>
            <CCardBody>
              <CDataTable
                size="sm"
                items={top_vul}
                fields={vul_field}
                header={false}
                scopedSlots={{
                  num: (item) => (
                    <td>
                      <CButton
                        onClick={() => {
                          num_click(item.vul);
                        }}
                        disabled={!item.num}
                      >
                        <strong style={{ color: "red" }}>{item.num}</strong>
                      </CButton>
                    </td>
                  ),
                }}
              />
            </CCardBody>
          </CCard>
        </CCol>
      </CRow>
    </>
  );
};

export default Dashboards;
