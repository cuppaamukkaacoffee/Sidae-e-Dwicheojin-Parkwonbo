import {takeLatest} from 'redux-saga/effects';
import createRequestSaga from '../../../libs/createRequestSaga';
import * as usersAPI from '../../../libs/api/users';
import * as USER from './actions';
import history from "../../../utils/history";


const login = createRequestSaga(USER.LOGIN, usersAPI.login_api,);

const register = createRequestSaga(USER.REGISTER, usersAPI.register_api,);

const results_check = createRequestSaga(USER.RESULTS_CHECK, usersAPI.results_api,);

const dashboard_data_check = createRequestSaga(USER.DASHBOARD_DATA_CHECK, usersAPI.results_api,);

function* goToHomeSaga() {
  history.push('/dashboard');
}

function* goToLoginSaga() {
  alert("회원가입 완료");
  history.push('/login');
}


export default function* rootSaga() {
  yield [
    yield takeLatest(USER.LOGIN, login),
    yield takeLatest(USER.LOGIN_SUCCESS, goToHomeSaga),
    yield takeLatest(USER.REGISTER, register),
    yield takeLatest(USER.REGISTER_SUCCESS, goToLoginSaga),
    yield takeLatest(USER.RESULTS_CHECK, results_check),
    yield takeLatest(USER.DASHBOARD_DATA_CHECK, dashboard_data_check),
  ];
}