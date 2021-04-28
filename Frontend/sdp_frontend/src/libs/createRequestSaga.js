import { call, put } from "redux-saga/effects";
import { startLoading, finishLoading } from "../store/modules/loading/actions";

export const createRequestActionTypes = (type) => {
  const SUCCESS = `${type}_SUCCESS`;
  const FAILED = `${type}_FAILED`;
  return [type, SUCCESS, FAILED];
};

export default function createRequestSaga(type, request) {
  const SUCCESS = `${type}_SUCCESS`;
  const FAILED = `${type}_FAILED`;
  return function* (action) {
    yield put(startLoading(type)); // 로딩 시작
    try {
      const response = yield call(request, action.payload);
      yield put({
        type: SUCCESS,
        payload: response !== undefined ? response : action.payload,
        meta: response,
      });
    } catch (e) {
      yield put({
        type: FAILED,
        payload: e,
        error: true,
      });
    }
    yield put(finishLoading(type)); // 로딩 끝
  };
}
