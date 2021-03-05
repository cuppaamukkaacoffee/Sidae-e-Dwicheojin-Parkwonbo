import {useCallback, useEffect} from 'react';
import {useSelector, useDispatch, shallowEqual} from 'react-redux';
import React from 'react'
import {
  CDataTable,
} from '@coreui/react'
import * as userActions from 'src/store/modules/user/actions';
import history from "src/utils/history";

const fields = ['vulnerability','target','status','timestamp']
 

const Vulnerabilities = ({location}) => {
  const dispatch = useDispatch();

  const {
    vul_reports
    } = useSelector((state) => ({
      vul_reports: state.user.vul_reports,
    }), shallowEqual)

  useEffect(() => {
    if(location.state){
      const id = window.sessionStorage.getItem('id');
      if(location.state.vul){
        dispatch(userActions.vul_results_check({id : id, result_string : 'vulnerable',vul : location.state.vul , scan_session_id : location.state.id, with_headers : true}));
      }else{
        dispatch(userActions.vul_results_check({id : id, result_string : 'vulnerable', scan_session_id : location.state.id, with_headers : true}));
      }
      
    }else{
      const id = window.sessionStorage.getItem('id');
      dispatch(userActions.vul_results_check({id : id, result_string : 'vulnerable',with_headers : true}));
    }

    return () => {
      dispatch(userActions.reset_msg());
    };
  }, []);
  return (
    <>
      <CDataTable
                items={vul_reports}
                fields={fields}
                striped
                hover
                bordered
                size="sm"
                scopedSlots = {{
                  'target':
                    (item)=>(
                      <td style={{color: 'red'}}>
                        {item.target}
                      </td>
                    ),
                  'vulnerability':
                  (item)=>(
                    <td style={{color: 'red'}}>
                      {item.vulnerability}
                    </td>
                  ),
                }}
      />
    </>
  )
}

export default Vulnerabilities
  