import {handleActions} from 'redux-actions';
import * as LOADING from './actions';
import produce from 'immer';

const initialState = {
  loading: false,
  progress : 0,
  total : 1
};

const loading = handleActions(
  {
    [LOADING.START_LOADING]: (state, action) => ({
      ...state,
      loading: true,
      [action.payload]: true,
    }),
    [LOADING.FINISH_LOADING]: (state, action) => ({
      ...state,
      loading: false,
      progress : 0,
      total : 1,
      [action.payload]: false,
    }),
    [LOADING.ADD_PROGRESS]: (state, action) => {
      return produce(state, (draft) => {
       draft.progress += 1;
      })
    },
    [LOADING.ADD_TOTAL]: (state, action) => {
      return produce(state, (draft) => {
       draft.total += 1;
      })
    },
  },
  initialState,
);

export default loading;
