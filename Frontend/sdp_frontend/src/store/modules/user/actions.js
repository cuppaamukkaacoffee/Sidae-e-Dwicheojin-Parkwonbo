import {createAction} from 'redux-actions';
import {createRequestActionTypes} from '../../../libs/createRequestSaga';

export const RESET_MSG = 'user/RESET_MSG';
export const reset_msg = createAction(RESET_MSG);

// Redux 값을 저장할 때


export const SET_ID = 'user/SET_ID';
export const set_id = createAction(SET_ID);

export const SET_PW = 'user/SET_PW';
export const set_pw = createAction(SET_PW);

export const SET_URL = 'user/SET_URL';
export const set_url = createAction(SET_URL);

export const SET_VUL = 'user/SET_VUL';
export const set_vul = createAction(SET_VUL);

export const SET_SIDEBAR = 'user/SET_SIDEBAR';
export const set_sidebar = createAction(SET_SIDEBAR);

// API 호출 시

export const [
  LOGIN,
  LOGIN_SUCCESS,
  LOGIN_FAILED,
] = createRequestActionTypes('user/LOGIN');
export const login = createAction(LOGIN);

export const [
  REGISTER,
  REGISTER_SUCCESS,
  REGISTER_FAILED,
] = createRequestActionTypes('user/REGISTER');
export const register = createAction(REGISTER);

export const [
  URL_CHECK,
  URL_CHECK_SUCCESS,
  URL_CHECK_FAILED,
] = createRequestActionTypes('user/URL_CHECK');
export const url_check = createAction(URL_CHECK);

export const [
  RESULTS_CHECK,
  RESULTS_CHECK_SUCCESS,
  RESULTS_CHECK_FAILED,
] = createRequestActionTypes('user/RESULTS_CHECK');
export const results_check = createAction(RESULTS_CHECK);

export const [
  RESULTS_DETAIL_CHECK,
  RESULTS_DETAIL_CHECK_SUCCESS,
  RESULTS_DETAIL_CHECK_FAILED,
] = createRequestActionTypes('user/RESULTS_DETAIL_CHECK');
export const results_detail_check = createAction(RESULTS_DETAIL_CHECK);

export const [
  RESULTS_DETAIL_DELETE,
  RESULTS_DETAIL_DELETE_SUCCESS,
  RESULTS_DETAIL_DELETE_FAILED,
] = createRequestActionTypes('user/RESULTS_DETAIL_DELETE');
export const results_detail_delete = createAction(RESULTS_DETAIL_DELETE);


