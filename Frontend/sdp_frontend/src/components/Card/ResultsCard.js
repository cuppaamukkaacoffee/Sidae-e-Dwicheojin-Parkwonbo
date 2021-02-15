import * as userActions from '../../store/modules/user/actions';
import {useDispatch, shallowEqual} from 'react-redux';
import {useCallback} from 'react';

const ResultsCard = (props) =>{
    const dispatch = useDispatch();

    const handleSubmit_detail = useCallback(() => {
        dispatch(userActions.results_detail_check(props.id))
      }, [props.id])

    const handleSubmit_delete = useCallback(() => {
        dispatch(userActions.results_detail_delete(props.id))
    }, [props.id])  
    
    return (
      <>
        <div>
            <br/>{props.id}. {props.date}<br/>
            {props.url} <button onClick={handleSubmit_detail}>상세</button>
            <button onClick={handleSubmit_delete}>삭제</button><br/>
        </div>
      </>
    )
  }
  
  export default ResultsCard;