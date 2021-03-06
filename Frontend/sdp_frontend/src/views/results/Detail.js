import {useEffect,useState} from 'react';
import {useDispatch} from 'react-redux';
import React from 'react'
import * as userActions from 'src/store/modules/user/actions';
import {
    CCollapse,
    CCard,
    CCardBody,
    CCardHeader,
    CCardFooter,
    CButton,
} from '@coreui/react'
import CIcon from '@coreui/icons-react'
import * as content from './Detail_content';
  
  
const Detail = ({location}) => {
  const dispatch = useDispatch();
  const [Des,setDes] = useState(true);
  const [Attack,setAttack] = useState(true);
  const [Req,setReq] = useState(false);
  const [Res,setRes] = useState(false);
  const [Imp,setImp] = useState(true);
  const [Fix,setFix] = useState(true);
  const [Ref,setRef] = useState(true);
  const {rep,req,res} = location.state;
 
  useEffect(() => {
      console.log(location.state)
      return () => {
        dispatch(userActions.reset_msg());
      };
    }, []);

  const vul = (()=>{
    if(rep.vulnerability === "XSS"){
      return "Cross site scripting"
    }
    else if(rep.vulnerability === "SQL Injection"){
      return "SQL Injection"
    }
  })()

  const description = (()=>{
    if(rep.vulnerability === "XSS"){
      return content.xss_description
    }
    else if(rep.vulnerability === "SQL Injection"){
      return content.sql_description
    }
  })()

  const impact = (()=>{
    if(rep.vulnerability === "XSS"){
      return content.xss_impact
    }
    else if(rep.vulnerability === "SQL Injection"){
      return content.sql_impact
    }
  })()

  const fix = (()=>{
    if(rep.vulnerability === "XSS"){
      return content.xss_fix
    }
    else if(rep.vulnerability === "SQL Injection"){
      return content.sql_fix
    }
  })()

  const web_ref = (()=>{
    if(rep.vulnerability === "XSS"){
      return content.xss_web_reference.map((el,idx) => <li key = {idx}><a href = {el.link} target ="_blank">{el.name}</a></li>)
    }
    else if(rep.vulnerability === "SQL Injection"){
      return content.sql_web_reference.map((el,idx) => <li key = {idx}><a href = {el.link} target ="_blank">{el.name}</a></li>)
    }
  })()

  let http_req = []
  let http_res = []
  for (let [key, val] of Object.entries(res)){
      http_res.push(<p key={key}><strong>{key}</strong> : {val}</p>);
    } 
  for (let [key, val] of Object.entries(req)){
      if (key !== "id"){
          http_req.push(<p key={key}><strong>{key}</strong> : {val}</p>);
        }
    } 

  return (
    <CCard>
      <CCardHeader><h4>{vul}</h4></CCardHeader>
      <CCardBody>
        <CButton onClick={() => setDes(!Des)}>
          <span style={{fontWeight:"bold",fontSize:"15px"}}>{Des?<CIcon size="sm" name="cilChevronDoubleUp"/>:<CIcon size="sm" name="cilChevronDoubleDown"/>}Vulnerability description</span>
        </CButton>
        <hr style={{width:"100%"}}/>
        <CCollapse show={Des} style={{whiteSpace:"pre-wrap"}}>
            {description}
            <hr style={{width:"100%"}}/>
        </CCollapse>
        
        
        <CButton onClick={() => setAttack(!Attack)}>
          <span style={{fontWeight:"bold",fontSize:"15px"}}>{Attack?<CIcon size="sm" name="cilChevronDoubleUp"/>:<CIcon size="sm" name="cilChevronDoubleDown"/>}Attack Payload</span>
        </CButton>
        <hr style={{width:"100%"}}/>
        <CCollapse show={Attack}>
            <a style={{color:"red"}} href = {rep.url} target="_blank">{rep.url}</a>
            <hr style={{width:"100%"}}/>
        </CCollapse>
        
        <CButton onClick={() => setReq(!Req)}>
          <span style={{fontWeight:"bold",fontSize:"15px"}}>{Req?<CIcon size="sm" name="cilChevronDoubleUp"/>:<CIcon size="sm" name="cilChevronDoubleDown"/>}HTTP request</span>
        </CButton>
        <hr style={{width:"100%"}}/>
        <CCollapse show={Req}>
            {http_req}
            <hr style={{width:"100%"}}/>
        </CCollapse>

        <CButton onClick={() => setRes(!Res)}>
          <span style={{fontWeight:"bold",fontSize:"15px"}}>{Res?<CIcon size="sm" name="cilChevronDoubleUp"/>:<CIcon size="sm" name="cilChevronDoubleDown"/>}HTTP response</span>
        </CButton>
        <hr style={{width:"100%"}}/>
        <CCollapse show={Res}>
            {http_res}
            <hr style={{width:"100%"}}/>
        </CCollapse>

        <CButton onClick={() => setImp(!Imp)}>
          <span style={{fontWeight:"bold",fontSize:"15px"}}>{Imp?<CIcon size="sm" name="cilChevronDoubleUp"/>:<CIcon size="sm" name="cilChevronDoubleDown"/>}The impact of this vulnerability</span>
        </CButton>
        <hr style={{width:"100%"}}/>
        <CCollapse show={Imp} style={{whiteSpace:"pre-wrap"}}>
            {impact}
            <hr style={{width:"100%"}}/>
        </CCollapse>

        <CButton onClick={() => setFix(!Fix)}>
          <span style={{fontWeight:"bold",fontSize:"15px"}}>{Fix?<CIcon size="sm" name="cilChevronDoubleUp"/>:<CIcon size="sm" name="cilChevronDoubleDown"/>}How to fix this vulnerability</span>
        </CButton>
        <hr style={{width:"100%"}}/>
        <CCollapse show={Fix} style={{whiteSpace:"pre-wrap"}}>
            {fix}
            <hr style={{width:"100%"}}/>
        </CCollapse>

        <CButton onClick={() => setRef(!Ref)}>
          <span style={{fontWeight:"bold",fontSize:"15px"}}>{Ref?<CIcon size="sm" name="cilChevronDoubleUp"/>:<CIcon size="sm" name="cilChevronDoubleDown"/>}Web References</span>
        </CButton>
        <hr style={{width:"100%"}}/>
        <CCollapse show={Ref}>
            {web_ref}
            <hr style={{width:"100%"}}/>
        </CCollapse>
      </CCardBody>
    </CCard>
  )
}

export default Detail
  