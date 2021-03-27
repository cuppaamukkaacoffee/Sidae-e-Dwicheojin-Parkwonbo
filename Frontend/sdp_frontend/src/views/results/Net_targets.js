import {useCallback, useEffect} from 'react';
import {useSelector, useDispatch, shallowEqual} from 'react-redux';
import React from 'react'
import {
  CDataTable,
} from '@coreui/react'
import * as userActions from 'src/store/modules/user/actions';
import history from "src/utils/history";

const fields = ['target','open_ports','timestamp']

const Net_targets = () => {
    const dispatch = useDispatch();

    const {
        net_targets
    } = useSelector((state) => ({
        net_targets : state.user.net_targets,
    }), shallowEqual)
    
    useEffect(() => {
        const id = sessionStorage.getItem("id")
        dispatch(userActions.net_targets_check({id:id}))
        return () => {
          dispatch(userActions.reset_msg());
        };
      }, []);

    const handleRowClick = (e) =>{
        history.push({
            pathname: "/netdetail",
            state: e
        });
    }
    return(
        <>
            <CDataTable
                items={net_targets}
                fields={fields}
                hover
                bordered
                striped
                size="sm"
                scopedSlots = {{
                'target':
                    (item)=>(
                    <td style={{color: 'red'}}>
                        {item.target}
                    </td>
                    ),
                }}
                onRowClick = {handleRowClick}
            />
        </>
    )
}


export default Net_targets