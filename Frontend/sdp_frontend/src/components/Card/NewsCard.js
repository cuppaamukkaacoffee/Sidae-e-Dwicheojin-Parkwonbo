
const NewsCard = (props) =>{
  return (
    <>
      <h1>
        {props.title}
      </h1>
      <a href={props.link}>
        바로가기
      </a>
      <br />
      {props.description}
      <br />
      <br />
    </>
  )
}

export default NewsCard;