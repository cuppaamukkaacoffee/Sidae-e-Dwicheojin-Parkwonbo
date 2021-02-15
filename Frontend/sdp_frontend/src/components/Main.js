import {useCallback} from 'react';
import {useSelector, useDispatch, shallowEqual} from 'react-redux';
import NewsCard from './Card/NewsCard';
import ResultsCard from './Card/ResultsCard';
import * as userActions from '../store/modules/user/actions';

function Main() {
  const dispatch = useDispatch();
  const {
      url,
      results,
  } = useSelector((state) => ({
    url: state.user.url,
    results: state.user.results,
  }), shallowEqual)
 

  const handleInputurl = (e) => {
    dispatch(userActions.set_url(e.target.value))
  }

  
  const handleSubmit_url = useCallback(() => {
      dispatch(userActions.url_check(url))
  }, [url])

  const handleSubmit_results = useCallback(() =>{
    dispatch(userActions.results_check())
  })

  return (
    <>
        
        
        <label>
          URL :
          <input type="text" name="url" onChange={handleInputurl} />
        </label>
        <button onClick={handleSubmit_url}>
          제출
        </button>
        <br/>
        <button onClick={handleSubmit_results}>
          기록
        </button>
      
    
        {
          results.map((item,index) => (
            <ResultsCard
              key={index}
              id = {item.id}
              url={item.url}
              date={item.created_at}
            />
          ))
        }
        
        <br/>
    </>
  )
}

export default Main;
