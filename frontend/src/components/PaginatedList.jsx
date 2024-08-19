import React, { useState , useEffect} from 'react'

const PaginatedList = ({data}) => {
    const [visibleItems , setVisibleItems] = useState(5);
    const [items , setItems] = useState([]);

    useEffect(()=>{
        setItems(data.slice(0 , visibleItems));
    },[visibleItems , data]);

    const loadMoreItems = () => {
        setVisibleItems((prev)=> prev + 5);
    }

  return (
    <div>
        {items.map((item)=>{
          return (
            <div>
                {item.movie.title}
            </div>
          )   
        })}
        {visibleItems < data.length && (
            <button onClick={()=>loadMoreItems()}>Load More</button>
        )}
      
    </div>
  )
}

export default PaginatedList
