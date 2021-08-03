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
      status: 1,
      rez: "",
    };
    
  }

  componentDidMount() {
      
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
                  	                fetch("/api/simple_action/"+encodeURI(e.target.value.toString().replace('/',':')))
					      .then(response => {
						if (response.status >= 400) {
						  return this.setState(() => {
						    return { status: 0 };
						  });
						}
						return response.json();
					      })
					      .then(data => {
						this.setState(() => {
						  return {
						    rez: data,
						    status: 1,
						  }
						})
					      });
					
                  	            }} 
       		>
       		
       	</input>
       	
       	{this.state.rez != undefined && this.state.rez != "" &&
       		<p>Result: {this.state.rez.response}</p>
       	}
       	{this.state.status === 0 &&
       	<p>Server error!</p>
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

