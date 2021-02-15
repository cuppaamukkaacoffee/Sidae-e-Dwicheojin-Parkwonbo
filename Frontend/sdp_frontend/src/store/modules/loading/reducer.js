import {handleActions} from 'redux-actions';
import * as LOADING from './actions';

const initialState = {};

const loading = handleActions(
  {
    [LOADING.START_LOADING]: (state, action) => ({
      ...state,
      [action.payload]: true,
    }),
    [LOADING.FINISH_LOADING]: (state, action) => ({
      ...state,
      [action.payload]: false,
    }),
  },
  initialState,
);

export default loading;
