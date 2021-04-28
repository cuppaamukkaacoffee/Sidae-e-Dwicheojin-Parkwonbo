import React, { useCallback, useRef, useEffect } from "react";
import { useSelector, useDispatch, shallowEqual } from "react-redux";
import useWebSocket, { ReadyState } from "react-use-websocket";
import {
  CCard,
  CCardBody,
  CDataTable,
  CSpinner,
  CRow,
  CCol,
  CCardHeader,
} from "@coreui/react";
import * as loadingActions from "src/store/modules/loading/actions";

const fields = ["vulnerability", "result_string", "sub_path", "url", "status"];

const Test = () => {
  const dispatch = useDispatch();
  const { loading } = useSelector(
    (state) => ({
      loading: state.loading.loading,
    }),
    shallowEqual
  );

  const { sendMessage, lastMessage, readyState } = useWebSocket(
    "ws://localhost:8000/ws/scan/"
  );

  const connectionStatus = {
    [ReadyState.CONNECTING]: "Connecting",
    [ReadyState.OPEN]: "Open",
    [ReadyState.CLOSING]: "Closing",
    [ReadyState.CLOSED]: "Closed",
    [ReadyState.UNINSTANTIATED]: "Uninstantiated",
  }[readyState];

  const urls = useRef([]);
  const messageHistory = useRef([]);
  const fieldRef = useRef(null);

  useEffect(() => {
    if (lastMessage != null) {
      const results = JSON.parse(lastMessage.data);
      fieldRef.current.scrollIntoView(false);
      if (results.urlList) {
        urls.current = urls.current.concat(results.urlList);
      } else if (results.result) {
        messageHistory.current = messageHistory.current.concat(results.result);
      } else if (results.message == "all good") {
        dispatch(loadingActions.finishLoading());
        alert("스캔 끝");
      }
    }
  }, [lastMessage]);

  useEffect(() => {
    if (connectionStatus == "Closed") {
      dispatch(loadingActions.finishLoading());
      alert("장고서버연결끊김");
    }
  }, [connectionStatus]);

  const handleClickSendMessage = useCallback(() => {
    dispatch(loadingActions.startLoading());
    sendMessage(
      JSON.stringify({
        token:
          "Token eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6InB1cHkwNyIsInBhc3N3b3JkIjoiYmNyeXB0X3NoYTI1NiQkMmIkMTIkL2VMZXhOUEp5R3ZQcHlIeGlxa01NdWNrLmZ0M0hYNmtpU2NkRFMvTE9BdzdwaXJVTzhwaXkiLCJleHAiOjE2MTM2MzY5NjV9.gDqkjcVVh8Kn6ZpFZmmMne-q06q1sm1r8bnJjaLHXE8",
        target: "http://testphp.vulnweb.com",
        fuzz: "True",
      })
    );
  }, []);

  return (
    <div ref={fieldRef}>
      <button
        onClick={handleClickSendMessage}
        disabled={readyState !== ReadyState.OPEN}
      >
        Click Me to send 'Hello'
      </button>
      <span>
        The WebSocket is currently
        {connectionStatus}
      </span>
      <CRow>
        <CCol xs="10" md="5">
          <CCard>
            <CCardHeader>Url List</CCardHeader>
            <CCardBody>
              {urls.current.map((url, idx) => (
                <li key={idx}>{url}</li>
              ))}
            </CCardBody>
          </CCard>
        </CCol>
      </CRow>
      <CRow>
        <CCol xs="10" md="10">
          <CCard>
            <CCardHeader>Results</CCardHeader>
            <CCardBody>
              <CDataTable
                items={messageHistory.current}
                fields={fields}
                hover
                striped
                bordered
                size="sm"
              />
            </CCardBody>
          </CCard>
        </CCol>
      </CRow>
      {loading ? (
        <CSpinner color="primary" style={{ width: "4rem", height: "4rem" }} />
      ) : null}
    </div>
  );
};

export default Test;
