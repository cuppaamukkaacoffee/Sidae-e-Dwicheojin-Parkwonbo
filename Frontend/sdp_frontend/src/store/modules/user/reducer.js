import {handleActions} from 'redux-actions';
import produce, {createDraft, finishDraft} from 'immer';
import * as USER from './actions';


const initialState = {
  id: '',
  pw: '',
  url: '',
  vul: '',
  result_string:'',
  fuzz: true,
  content:'',
  results:[],
  sidebarShow : 'responsive',
  errorMsg : '',
  errorCode : '',
}

const user = handleActions(
  {
    [USER.RESET_MSG]: (state, action) => {
      console.log('Reset state');
      return produce(state, (draft) => {
        draft.id = '';
        draft.pw = '';
        draft.url = '';
        draft.vul = '';
        draft.result_string = '';
        draft.fuzz = true;
        draft.content = '';
        draft.results = [];
        draft.errorCode = '';
        draft.errorMsg = '';
        draft.sidebarShow = 'responsive';
      })
    },
    [USER.LOGIN_SUCCESS]: (state, action) => {
      console.log('LOGIN_SUCCESS => ', action.payload);
      window.sessionStorage.setItem('id', state.id);
      window.sessionStorage.setItem('token', action.payload.JWT);
      return state;
    },
    [USER.LOGIN_FAILED]: (state, action) => {
      console.log('LOGIN_Failed => ', action.payload);
      return produce(state, (draft) => {
        draft.errorMsg = '로그인 오류';
        draft.errorCode = '404';
      })
    },
    [USER.REGISTER_SUCCESS]: (state, action) => {
      console.log('REGISTER_SUCCESS => ', action.payload);
      return state;
    },
    [USER.REGISTER_FAILED]: (state, action) => {
      console.log('REGISTER_Failed => ', action.payload);
      return produce(state, (draft) => {
        draft.errorMsg = '회원가입 오류';
        draft.errorCode = '404';
      })
    },
    [USER.SET_ID]: (state, action) => {
      return produce(state, (draft) => {
        console.log('ID in reducer => ', action.payload)
        draft.id = action.payload;
      })
    },
    [USER.SET_PW]: (state, action) => {
      return produce(state, (draft) => {
        console.log('PW in reducer => ', action.payload)
        draft.pw = action.payload;
      })
    },
    [USER.SET_URL]: (state, action) => {
      return produce(state, (draft) => {
        console.log('url in reducer => ', action.payload)
        draft.url = action.payload;
      })
    },
    [USER.SET_VUL]: (state, action) => {
      return produce(state, (draft) => {
        console.log('vul in reducer => ', action.payload)
        draft.vul = action.payload;
      })
    },
    [USER.SET_RESULT_STRING]: (state, action) => {
      return produce(state, (draft) => {
        console.log('url in result_string => ', action.payload)
        draft.result_string = action.payload;
      })
    },
    [USER.SET_FUZZ]: (state, action) => {
      return produce(state, (draft) => {
        console.log('fuzz in reducer => ', action.payload)
        if (action.payload == "false"){
          draft.fuzz = false
        }
        else{
          draft.fuzz = true
        }
      })
    },
    [USER.URL_CHECK_SUCCESS]: (state, action) => {
      console.log('URL_CHECK_SUCCESS => ', action.payload);
      return produce(state, (draft) => {
        draft.results = [];
        draft.news = [];
        draft.content = action.payload.content;
      });
    },
    [USER.URL_CHECK_FAILED]: (state, action) => {
      console.log('URL_CHECK_Failed => ', action.payload);
      return produce(state, (draft) => {
        draft.errorMsg = '탐색 오류';
        draft.errorCode = '404';
      });
    },
    [USER.RESULTS_CHECK_SUCCESS]: (state, action) => {
      console.log('RESULTS_CHECK_SUCCESS => ', action.payload);
      return produce(state, (draft) => {
        draft.results = action.payload
      });
    },
    [USER.RESULTS_CHECK_FAILED]: (state, action) => {
      console.log('RESULTS_CHECK_Failed => ', action.payload);
      return produce(state, (draft) => {
        draft.errorMsg = '오류';
        draft.errorCode = '404';
      });
    },
    [USER.RESULTS_DETAIL_CHECK_SUCCESS]: (state, action) => {
      console.log('RESULTS_DETAIL_CHECK_SUCCESS => ', action.payload);
      return produce(state, (draft) => {
        draft.content = action.payload.content
      });
    },
    [USER.RESULTS_DETAIL_CHECK_FAILED]: (state, action) => {
      console.log('RESULTS_DETAIL_CHECK_Failed => ', action.payload);
      return produce(state, (draft) => {
        draft.errorMsg = '오류';
        draft.errorCode = '404';
      });
    },
    [USER.RESULTS_DETAIL_DELETE_SUCCESS]: (state, action) => {
      console.log('RESULTS_DETAIL_DELETE_SUCCESS => ', action.payload);
      return produce(state, (draft) => {
        draft.content = action.payload
      });
    },
    [USER.RESULTS_DETAIL_DELETE_FAILED]: (state, action) => {
      console.log('RESULTS_DETAIL_DELETE_Failed => ', action.payload);
      return produce(state, (draft) => {
        draft.errorMsg = '오류';
        draft.errorCode = '404';
      });
    },
    [USER.SET_SIDEBAR]: (state, action) => {
      return produce(state, (draft) => {
        console.log('sidebarShow in reducer => ', action.payload)
        draft.sidebarShow = action.payload;
      })
    },

  },
  initialState,
);

export default user;