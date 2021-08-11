import React from 'react';
import ReactDOM from 'react-dom';


function Header(props) {
	return ( 
		<div 
			
			
			style={{
				textAlign: 'center',
				fontSize: 'large',
				background: '#40cded',
				margin: 'auto',
				width: '70%',
				boxShadow: '0 0 10px rgba(0,0,0,0.5)',
			}}>
			<br />
			<h1>Complan</h1>
			<h2>Under construction</h2>
			<br />
		</div>
	);
}

class SimpleActions extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      data: [],
      expression: "",
      status: 2,
      rez: "",
      step_list: [],
      step_list_view: (<div> Жопа</div>),
    };
    
  }

  componentDidMount() {
      
  }

  async getData(val) {
  	const response = await fetch("/api/simple_action/"+encodeURI(val));
  	console.log("Results loaded!");
  	if (response.status >= 400) {
  		return this.setState(() => {
			return { status: 0 };
		});
  	} else {
  		this.setState(() => {
			return { status: 1 };
		});
  		return await response.json();
  	}
  	
  }

  render() {
  
    return (
       <div
       style={{
       	background: '#f2fffd',
       	textAlign: 'center',
       	margin: 'auto',
		width: '70%',
		borderWidth: 'medium',
		borderColor: 'black',
		boxShadow: '0 0 10px rgba(0,0,0,0.5)',
       	
       }}>
       	<br />
       	<h2>Expression solving</h2>
       	
       	<p>Enter your expression:</p>
       	<input
       		type="text"
       		size="45" 
       		value={this.state.expression}
                  	onChange={(e) => {

                  	                this.setState({expression: e.target.value.toString()});
                  	                if (e.target.value.toString() != "") {
                  	                	this.getData(e.target.value.toString())
					      .then(data => {
					      	if (this.state.status != 0) {
					      		this.setState(() => {
							  return {
							    rez: data.response,
							    step_list: data.steps,
							    
							    status: 1,
							  }
							});
							if (data.response == "Error with brackets!") {
								this.setState(() => {
								  return {
								    
								    status: 3,
								  }
								});
							}
							console.log(data.steps);
							if (data.steps != undefined && data.steps.length != 0) {
								console.log(data.steps);
								this.setState(() => {
									return {
										step_list_view: (
										    	<div>
				       		
									       		<h3>Steps</h3>
									       		
									       		{
									       			data.steps.map((val) => (
									       			
									       				<p>{val.n}. {val.formula}</p>
									       			))
									       		}
									       	</div>
										    ),
									}
									
								})
							}
							console.log(this.state.step_list);
					      	}
						
					      });
                  	                } else {
                  	                	this.setState(() => {
							  return {
							    rez: "",
							    step_list: [],
							    
							    status: 2,
							  }
							});
                  	                }
                  	          	 
					
                  	            }} 
       		>
       		
       	</input>
       	
       	{
	       	this.state.status === 1 &&
	       	this.state.rez != undefined && this.state.rez != "" &&
	       	<p>Result: {this.state.rez}</p>
       	}
       	{
	       	this.state.status === 0 &&
	       	<p>Maybe, you haven't finished writing your expression?</p>
       	}
       	{
       		this.state.status === 1 &&
       		this.state.step_list != undefined &&
	       	this.state.step_list[0] != undefined &&
	       	this.state.step_list_view 

       	}
       	{
       		this.state.status === 3 &&
	       	<p>Brackets error!</p>

       	}
       	<br />
       	<br />
       </div>
    )

  }
}

class Index extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      data: [],
    };
    
  }

  componentDidMount() {
     
  }



  render() {
    return (
       <div>
       	<br />
       	<Header />
       	<SimpleActions />
       </div>
    )

  }
}

export default Index;

