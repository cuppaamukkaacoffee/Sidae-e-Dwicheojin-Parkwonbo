import {useCallback} from 'react';
import {useSelector, useDispatch, shallowEqual} from 'react-redux';
import * as userActions from '../store/modules/user/actions';

function Form() {
  const dispatch = useDispatch();
  const {id,pw,error} = useSelector(state => ({id: state.user.id, pw: state.user.pw, error: state.user.errorMsg}))
  const login_id = window.sessionStorage.getItem('id');
  const token = window.sessionStorage.getItem('token');

  const handleInputId = (e) => {
    dispatch(userActions.set_id(e.target.value))
  }
  const handleInputPass = (e) => {
    dispatch(userActions.set_pw(e.target.value))
  }
  const handleLogin = useCallback(() => {
    dispatch(userActions.login({id:id,pw:pw}))
  }, [id, pw])

  const handleRegister = useCallback(() => {
    dispatch(userActions.register({id:id,pw:pw}))
  }, [id, pw])
  
  if(login_id) {
    return (
    <>
      id: {login_id}<br/>
      token: {token}
    </>
    )
  }else {
    return (
      <>  
          <label>
            ID :
            <input type="text" name="id" onChange={handleInputId} />
          </label>
          <label>
            Pass :
            <input type="text" name="pw" onChange={handleInputPass} />
          </label><br/>
          <button onClick={handleLogin}>sign in</button>
          <button onClick={handleRegister}>sign up</button>
          {error}<br/>
      </>
  )
  }

  
}

export default Form;
