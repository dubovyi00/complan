import React from 'react';
import ReactDOM from 'react-dom';

import Index from './components/index.js';

function initComponents() {

  var element = document.getElementById('react_elem');
  var c = element.getAttribute("component");
  var data = element.dataset;

  if (c === "Index") {
  	ReactDOM.render(
  		<Index />,
  		document.getElementById('react_elem')
  	);
  } 
}

// по готовности документа рендерим
$(function() { 
    initComponents();		
});

