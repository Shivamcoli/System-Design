import React, { useState, useEffect } from 'react';
import { PropFunction } from './PropFunction';
export default function App() {

    
    const [count,setCount]=useState(0);
  // useEffect(()=>{
  //     setCount((count)=>{
  //        return count+1
  //     })
  // },[])

    const handlechange =()=>{
        setCount((count)=>{return count+1})
    } 
    return ( 
        <div>
            <div onClick={handlechange}>button</div>
            <PropFunction />
        </div>
    )
    
}
