import React, { Component } from 'react';
import axios from 'axios';
import Modal from './Components/Modal';
import Table from './Components/Table.js';

class App extends Component {

  constructor(props) {
    super(props);
    this.state = {
      viewCompleted: false,
      activeItem: {
        name: "",
        one: "",
        gender: "",
        age: "",
        period_of_joining: "",
        category: "",
        classes: "",
        qualification: "",
        income: "",
        levy_cash: "",
        socio_culture_caste: "",
        minority: "",
        organisation_cpm: "",
        disability: "",
        news_letter: ""
      },
      droplets: []
    };
  }

  componentDidMount() {
    this.refreshList();
  }

  refreshList = () => {
    axios.get("http://localhost:8000/member/api").then(res => this.setState({ droplets: res.data })).catch(err => console.log(err));
  };

  toggle = () => {
    this.setState({ modal: !this.state.modal });
  };

  handleSubmit = item => {
    this.toggle();
    if (item.id) {
      axios.put(`http://localhost:8000/member/api/${item.id}/`, item).then(res => this.refreshList());
      return;
    }

    axios.post("http://localhost:8000/member/api/create", item).then(res => this.refreshList());
  };

  // handleDelete = item => {
  //   axios.delete(`http://localhost:8000/member/api/${item.id}/delete`).then(res => this.refreshList());
  // };

  createItem = () => {
    const item = { name: "", one: ""};
    this.setState({ activeItem: item, modal: !this.state.modal });
  };

  renderItems = () => {
    return (
      <Table droplets={this.state.droplets} />
    );
  }

  render() {
    return (
      <div className='text-center p-2'>
        <h1 style={{ color: 'red' }} className='fs-1 fw-bolder'> இந்திய கம்யூனிஸ்ட் கட்சி (மார்க்சிஸ்ட்) </h1>
        <div style={{ color: 'red' }} className='fs-4 fw-bold'>கடலூர் மாவட்டம்</div>
        <div className='mt-2'>
          <button type="button" className="btn btn-light m-2" style={{ borderColor: 'red', backgroundColor: 'red', color: 'white' }}
            onClick={this.createItem} >Add Member
          </button>
          <button type="button" className="btn btn-light m-2" style={{ borderColor: 'red', backgroundColor: 'red', color: 'white' }}>
            Edit
          </button>
          <button type="button" className="btn btn-light m-2" style={{ borderColor: 'red', backgroundColor: 'red', color: 'white' }}>
            Delete
          </button>
        </div>
        {this.renderItems()}

        {this.state.modal ? (
          <Modal
            activeItem={this.state.activeItem}
            toggle={this.toggle}
            onSave={this.handleSubmit}
          />
        ) : null}
      </div>

    )
  }
}

export default App;