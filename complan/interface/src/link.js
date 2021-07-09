import React from 'react';
import ReactDOM from 'react-dom';

import Index from './components/index.js';
//функция рендеринга компонентов на странице, свойства берутся из атрибутов data-*
function initComponents() {

  var element = document.getElementById('root');
  var c = element.getAttribute("component");
  var data = element.dataset;

  if (c === "Index") {
  	ReactDOM.render(
  		<Index />,
  		document.getElementById('root')
  	);
  } 
}

// по готовности документа рендерим
$(function() { 
    initComponents();		
});

