import UserSagas from "./user/sagas";
// import SignUpSagas from './signup/sagas';

import { all } from "redux-saga/effects";

export default function* rootSaga() {
  yield all([
    UserSagas(),
    // SignUpSagas(),
  ]);
}
