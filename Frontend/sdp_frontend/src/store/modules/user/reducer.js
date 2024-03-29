import {handleActions} from 'redux-actions';
import produce from 'immer';
import * as USER from './actions';


const initialState = {
  id: '',
  pw: '',
  url: '',
  url_list:[],
  db_data:[],
  scan_type: '',
  vul: '',
  result_string:'',
  url_fuzz: true,
  traversal_check: true,
  form_fuzz: true,
  report:{},
  request:{},
  response:{},
  total_reports:[],
  vul_reports:[],
  reports:[],
  requests:[],
  responses:[],
  targets:[],
  net_targets:[],
  port_from:"",
  port_to:"",
  scan_rate:"",
  whois_flag:true,
  robot_flag:true,
  robot_results:{},
  port_results:[],
  whois_results:{},
  ip_addresses:[],
  net_results:{},
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
        draft.url_list = [];
        draft.db_data = [];
        draft.scan_type = '';
        draft.vul = '';
        draft.result_string = '';
        draft.url_fuzz = true;
        draft.traversal_check = true;
        draft.form_fuzz = true;
        draft.report = {};
        draft.request = {};
        draft.response = {};
        draft.total_reports = [];
        draft.vul_reports = [];
        draft.reports = [];
        draft.requests = [];
        draft.responses = [];
        draft.targets = [];
        draft.net_targets = [];
        draft.port_from = "";
        draft.port_to = "";
        draft.scan_rate = "";
        draft.whois_flag = true;
        draft.robot_flag = true;
        draft.robot_results = {};
        draft.port_results = [];
        draft.whois_results = {};
        draft.ip_addresses = [];
        draft.net_results = {};
        draft.errorCode = '';
        draft.errorMsg = '';
        draft.sidebarShow = 'responsive';
      })
    },
    [USER.RESET_R]: (state, action) => {
      console.log('Reset r');
      return produce(state, (draft) => {
        draft.report = {};
        draft.request = {};
        draft.response = {};
        draft.errorCode = '';
        draft.errorMsg = '';
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
    [USER.SET_PORT_FROM]: (state, action) => {
      return produce(state, (draft) => {
        console.log('port_from in reducer => ', action.payload)
        draft.port_from = action.payload;
      })
    },
    [USER.SET_PORT_TO]: (state, action) => {
      return produce(state, (draft) => {
        console.log('port_to in reducer => ', action.payload)
        draft.port_to = action.payload;
      })
    },
    [USER.SET_SCAN_RATE]: (state, action) => {
      return produce(state, (draft) => {
        console.log('scan_rate in reducer => ', action.payload)
        draft.scan_rate = action.payload;
      })
    },
    [USER.SET_URL_LIST]: (state, action) => {
      return produce(state, (draft) => {
        console.log('url_list in reducer => ', action.payload)
        draft.url_list.unshift(action.payload);
      })
    },
    [USER.SET_SCAN_TYPE]: (state, action) => {
      return produce(state, (draft) => {
        console.log('scan_type in reducer => ', action.payload)
        draft.scan_type = action.payload;
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
        console.log('result_string in reducer => ', action.payload)
        draft.result_string = action.payload;
      })
    },
    [USER.SET_RESULTS]: (state, action) => {
      return produce(state, (draft) => {
        console.log('results in reducer => ', action.payload)
        draft.reports.push(...action.payload.reports);
        draft.requests.push(...action.payload.requests);
        draft.responses.push(...action.payload.responses);
      })
    },
    [USER.SET_PORT_RESULTS]: (state, action) => {
      return produce(state, (draft) => {
        console.log('port_results in reducer => ', action.payload)
        draft.port_results.push(action.payload);
      })
    },
    [USER.SET_WHOIS_RESULTS]: (state, action) => {
      return produce(state, (draft) => {
        console.log('whois_results in reducer => ', action.payload)
        draft.whois_results = action.payload;
      })
    },
    [USER.SET_ROBOT_RESULTS]: (state, action) => {
      return produce(state, (draft) => {
        console.log('robot_results in reducer => ', action.payload)
        draft.robot_results = action.payload;
      })
    },
    [USER.SET_IP_ADDRESSES]: (state, action) => {
      return produce(state, (draft) => {
        console.log('ip_addresses in reducer => ', action.payload)
        draft.ip_addresses.push(action.payload);
      })
    },
    [USER.SET_REQUEST]: (state, action) => {
      return produce(state, (draft) => {
        console.log('request in reducer => ', action.payload)
        draft.request = action.payload;
      })
    },
    [USER.SET_RESPONSE]: (state, action) => {
      return produce(state, (draft) => {
        console.log('response in reducer => ', action.payload)
        draft.response = action.payload;
      })
    },
    [USER.SET_REPORT]: (state, action) => {
      return produce(state, (draft) => {
        console.log('report in reducer => ', action.payload)
        draft.report = action.payload;
      })
    },
    [USER.SET_URL_FUZZ]: (state, action) => {
      return produce(state, (draft) => {
        console.log('url_fuzz in reducer => ', action.payload)
        draft.url_fuzz= action.payload
      })
    },
    [USER.SET_TRAVERSAL_CHECK]: (state, action) => {
      return produce(state, (draft) => {
        console.log('traversal_check in reducer => ', action.payload)
        draft.traversal_check= action.payload
      })
    },
    [USER.SET_FORM_FUZZ]: (state, action) => {
      return produce(state, (draft) => {
        console.log('form_fuzz in reducer => ', action.payload)
        draft.form_fuzz= action.payload
      })
    },
    [USER.SET_WHOIS_FLAG]: (state, action) => {
      return produce(state, (draft) => {
        console.log('whois_flag in reducer => ', action.payload)
        draft.whois_flag= action.payload
      })
    },
    [USER.SET_ROBOT_FLAG]: (state, action) => {
      return produce(state, (draft) => {
        console.log('robot_flag in reducer => ', action.payload)
        draft.robot_flag= action.payload
      })
    },
    
    [USER.RESULTS_CHECK_SUCCESS]: (state, action) => {
      console.log('RESULTS_CHECK_SUCCESS => ', action.payload);
      return produce(state, (draft) => {
        draft.total_reports = action.payload.reports;
        draft.requests = action.payload.requests;
        draft.responses = action.payload.responses;
      });
    },
    [USER.RESULTS_CHECK_FAILED]: (state, action) => {
      console.log('RESULTS_CHECK_Failed => ', action.payload);
      return produce(state, (draft) => {
        draft.errorMsg = '오류';
        draft.errorCode = '404';
      });
    },
    [USER.VUL_RESULTS_CHECK_SUCCESS]: (state, action) => {
      console.log('VUL_RESULTS_CHECK_SUCCESS => ', action.payload);
      return produce(state, (draft) => {
        draft.vul_reports = action.payload.reports;
        draft.requests = action.payload.requests;
        draft.responses = action.payload.responses;
      });
    },
    [USER.VUL_RESULTS_CHECK_FAILED]: (state, action) => {
      console.log('VUL_RESULTS_CHECK_Failed => ', action.payload);
      return produce(state, (draft) => {
        draft.errorMsg = '오류';
        draft.errorCode = '404';
      });
    },

    [USER.DASHBOARD_DATA_CHECK_SUCCESS]: (state, action) => {
      console.log('DASHBOARD_DATA_CHECK_SUCCESS => ', action.payload);
      return produce(state, (draft) => {
        draft.db_data = action.payload.reports;
      });
    },
    [USER.DASHBOARD_DATA_CHECK_FAILED]: (state, action) => {
      console.log('DASHBOARD_DATA_CHECK_FAILED => ', action.payload);
      return produce(state, (draft) => {
        draft.errorMsg = '오류';
        draft.errorCode = '404';
      });
    },
    [USER.TARGETS_CHECK_SUCCESS]: (state, action) => {
      console.log('TARGETS_CHECK_SUCCESS => ', action.payload);
      return produce(state, (draft) => {
        draft.targets = action.payload.targets;
      });
    },
    [USER.TARGETS_CHECK_FAILED]: (state, action) => {
      console.log('TARGETS_CHECK_FAILED => ', action.payload);
      return produce(state, (draft) => {
        draft.errorMsg = '오류';
        draft.errorCode = '404';
      });
    },
    [USER.NET_TARGETS_CHECK_SUCCESS]: (state, action) => {
      console.log('NET_TARGETS_CHECK_SUCCESS => ', action.payload);
      return produce(state, (draft) => {
        draft.net_targets = action.payload.targets;
      });
    },
    [USER.NET_TARGETS_CHECK_FAILED]: (state, action) => {
      console.log('NET_TARGETS_CHECK_FAILED => ', action.payload);
      return produce(state, (draft) => {
        draft.errorMsg = '오류';
        draft.errorCode = '404';
      });
    },
    [USER.NET_RESULTS_CHECK_SUCCESS]: (state, action) => {
      console.log('NET_RESULTS_CHECK_SUCCESS => ', action.payload);
      return produce(state, (draft) => {
        draft.net_results = action.payload;
      });
    },
    [USER.NET_RESULTS_CHECK_FAILED]: (state, action) => {
      console.log('NET_RESULTS_CHECK_FAILED => ', action.payload);
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