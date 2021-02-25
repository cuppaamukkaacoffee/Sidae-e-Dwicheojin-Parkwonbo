import {createAction} from 'redux-actions';

export const START_LOADING = 'loading/START_LOADING';
export const FINISH_LOADING = 'loading/FINISH_LOADING';

export const ADD_PROGRESS = 'loading/ADD_PROGRESS';
export const add_progress = createAction(ADD_PROGRESS);

export const ADD_TOTAL = 'loading/ADD_TOTAL';
export const add_total = createAction(ADD_TOTAL);
/*
 요청을 위한 액션 타입을 payload로 설정합니다 (예: "sample/GET_POST")
*/

export const startLoading = createAction(
  START_LOADING,
  (requestType) => requestType,
);

export const finishLoading = createAction(
  FINISH_LOADING,
  (requestType) => requestType,
);
