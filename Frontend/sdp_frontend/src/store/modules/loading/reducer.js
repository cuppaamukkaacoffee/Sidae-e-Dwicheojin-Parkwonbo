import {handleActions} from 'redux-actions';
import * as LOADING from './actions';

const initialState = {loading: false};

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
      [action.payload]: false,
    }),
  },
  initialState,
);

export default loading;
