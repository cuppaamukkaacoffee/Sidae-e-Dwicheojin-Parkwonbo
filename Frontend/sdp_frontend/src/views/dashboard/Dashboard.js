import {useEffect} from 'react';
import {useSelector, useDispatch, shallowEqual} from 'react-redux';
import * as userActions from 'src/store/modules/user/actions';
import {
  CCard,
  CCardBody,
  CCardHeader,
  CWidgetDropdown,
  CDropdown,
  CDropdownMenu,
  CDropdownItem,
  CDropdownToggle,
  CRow,
  CCol,
  CWidgetProgressIcon,
  CProgress
} from '@coreui/react'
import {
  CChartBar,
  CChartDoughnut,
} from '@coreui/react-chartjs'
import CIcon from '@coreui/icons-react'

const labels = ['SQL Injection', 'XSS', 'Open Redirect', 'Windows Directory Traversal', 'Linux Directory Traversal', 'LFI Check', 'RFI Check', 'RCE Linux Check', 'SSTI Check']
const days = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]


const Dashboards = () => {
  const dispatch = useDispatch();

  const {
    db_data,
    } = useSelector((state) => ({
    db_data: state.user.db_data,
    }), shallowEqual)
 
  useEffect(() => {
    dispatch(userActions.dashboard_data_check({id:sessionStorage.getItem('id'), with_headers: false}))

    return () => {
      dispatch(userActions.reset_msg());
    };
    },[])
  
  
  const filterItems_all = (query) => {
    return db_data.filter((el) =>
      el.timestamp.includes(query) 
    );
  }
  
  const filterItems_vul = (query) => {
    return db_data.filter((el) =>
    el.result_string.includes("vulnerable") && el.timestamp.includes(query) 
    );
  }

  const filterItems_vulnerability = (query) => {
    return db_data.filter((el) =>
      el.result_string.includes("vulnerable") && el.vulnerability.includes(query)
    );
  }

  const numberPad = (n, width) => {
    n = n + '';
    return n.length >= width ? n : new Array(width - n.length + 1).join('0') + n;
  }

  const datasets_scanned = (()=>{
    let data = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    if(db_data.length > 0){
      for(let i = 0 ; i < 30 ; i++){
        if(i < 10){
          let num = numberPad(i+1,2)
          data[i] = filterItems_all(`2021-02-${num}`).length
        }else{
          data[i] = filterItems_all(`2021-02-${i+1}`).length
        }
      }

    }
    return [
      {
        data: data,
        backgroundColor: '#00D8FF',
        label: 'Scanned URL',
        barPercentage: 0.8,
      }
    ]
  })()

  const datasets_vul = (()=>{
    let data = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    if(db_data.length > 0){
      for(let i = 0 ; i < 30 ; i++){
        if(i < 10){
          let num = numberPad(i+1,2)
          data[i] = filterItems_vul(`2021-02-${num}`).length
        }else{
          data[i] = filterItems_vul(`2021-02-${i+1}`).length
        }
      }

    }
    return [
      {
        data: data,
        backgroundColor: '#DD1B16',
        label: 'vulnerable URL',
        barPercentage: 0.8,
      }
    ]
  })()

  const datasets_doughnut = (()=>{
    let data = [0,0,0,0,0,0,0,0,0]
    if(db_data.length > 0){
        for(let i = 0 ; i < 9 ; i++){
          data[i] = filterItems_vulnerability(labels[i]).length
        }
    }
    return [
      {
        data: data,
        backgroundColor: [
          '#41B883',
          '#E46651',
          '#00D8FF',
          '#DD1B16',
          '#FF4500',
          '#FF8C00',
          '#7CFC00',
          '#4169E1',
          '#4B0082'
        ],
        
      }
    ]
  })()

  return (
    <>
    <CRow>
      <CCol md="2">
        <CWidgetDropdown
          color="gradient-primary"
          header="9.823"
          text="Members online"
        >
          <CDropdown>
            <CDropdownToggle color="transparent">
              <CIcon name="cil-settings"/>
            </CDropdownToggle>
            <CDropdownMenu className="pt-0" placement="bottom-end">
              <CDropdownItem>Action</CDropdownItem>
              <CDropdownItem>Another action</CDropdownItem>
              <CDropdownItem>Something else here...</CDropdownItem>
              <CDropdownItem disabled>Disabled action</CDropdownItem>
            </CDropdownMenu>
          </CDropdown>
        </CWidgetDropdown>

        <div className="text-uppercase mb-1">
          <small><b>CPU Usage</b></small>
        </div>
        <CProgress size="xs" color="info" value={25} />
        <small className="text-muted">348 Processes. 1/4 Cores.</small>

        <div className="text-uppercase mb-1">
          <small><b>Memory Usage</b></small>
        </div>
        <CProgress size="xs" color="warning" value={70} />
        <small className="text-muted">11444GB/16384MB</small>

        <div className="text-uppercase mb-1">
          <small><b>SSD 1 Usage</b></small>
        </div>
        <CProgress size="xs" color="danger" value={90} />
        <small className="text-muted">243GB/256GB</small>

      </CCol>
      <CCol md = "4">
        <CWidgetProgressIcon
          header="385"
          text="New Clients"
          color="gradient-success"
        >
          <CIcon name="cil-userFollow" height="36"/>
        </CWidgetProgressIcon>
      </CCol>
      <CCol>
        <CCard>
          <CCardHeader>
            Scanned Vulnerability
          </CCardHeader>
          <CCardBody>
            <CChartDoughnut
                  datasets={datasets_doughnut}
                  labels={labels}
                  options={{
                    tooltips: {
                      enabled: true
                    }
                  }}
                />
          </CCardBody>
        </CCard>
      </CCol>
      </CRow>
      
      <CRow>
        <CCol>
          <CCard>
            <CCardBody>
              <CChartBar
                  datasets={datasets_scanned}
                  labels={days}
                  options={{
                    tooltips: {
                      enabled: true
                    }
                  }}
                />
            </CCardBody>
          </CCard>
        </CCol>
        <CCol>
          <CCard>
            <CCardBody>
              <CChartBar
                datasets={datasets_vul}
                labels={days}
                options={{
                  tooltips: {
                    enabled: true
                  }
                }}
              />
            </CCardBody>
          </CCard>
        </CCol>
      </CRow>
      </>
  )
}

export default Dashboards
