import React from 'react';
import ReactDOM from 'react-dom';
import axios from 'axios';

axios.get('api/posts').then((data)=>{
  console.log(data)
})

ReactDOM.render(
  <div>hi</div>,
  document.querySelector('.root'));
