import React, { Component } from 'react';
import Table from './components/Table.js';
import 'bootstrap/dist/css/bootstrap.min.css';
// import logo from './assets/DO_Logo_icon_blue.svg';
import axios from 'axios';


class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      requiredItem: 0,
      droplets: []
    }
  }

  // componentDidMount() {
  //   axios.get(`https://jsonplaceholder.typicode.com/users`)
  //     .then(res => {
  //       const persons = res.data;
  //       this.setState({ persons });
  //     })
  // }

  componentDidMount() {
    axios.get('http://127.0.0.1:8000/member/api')
      .then((res) => {
        console.log('>>>>>', res.data);
        const droplets = res.data;
        this.setState({ droplets });

      }).catch((error) => {
        console.warn('Not good man :(');
      })

    // fetch('http://127.0.0.1:8000/api/members/')
    //   .then(res => res.json())
    //   .then(json => json.droplets)
    //   .then(droplets => this.setState({ 'droplets': droplets }))
  }

  replaceModalItem() {
    console.log("Clicked add")
  }

  render() {
    return (
      <div className='text-center p-2'>
        <h1 style={{ color: 'red' }} className='fs-1 fw-bolder'> இந்திய கம்யூனிஸ்ட் கட்சி (மார்க்சிஸ்ட்) </h1>
        <div style={{ color: 'red' }} className='fs-4 fw-bold'>கடலூர் மாவட்டம்</div>
        <div className='mt-2'>
          <button type="button" class="btn btn-light m-2" style={{ borderColor: 'red', backgroundColor: 'red', color: 'white' }}
          onClick={() => this.replaceModalItem()}>Add Member
          </button>
          <button type="button" class="btn btn-light m-2" style={{ borderColor: 'red', backgroundColor: 'red', color: 'white' }}>
            Edit
          </button>
          <button type="button" class="btn btn-light m-2" style={{ borderColor: 'red', backgroundColor: 'red', color: 'white' }}>
            Delete
          </button>
        </div>
        <Table droplets={this.state.droplets} />
      </div>
    );
  }
}

export default App;