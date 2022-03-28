// frontend/src/components/Modal.js

import React, { Component } from "react";
// import Dropdown from 'react-bootstrap/Dropdown';
import * as ReactBootstrap from "react-bootstrap";
// import CustomListDropDown from './CustomListDropDown'

import DropdownButton from "react-bootstrap/DropdownButton"
import {
    Button,
    Modal,
    ModalHeader,
    ModalBody,
    ModalFooter,
    Form,
    FormGroup,
    Input,
    Label,
    Col
} from "reactstrap";
import axios from 'axios';


export default class CustomModal extends Component {
    constructor(props) {
        super(props);
        this.state = {
            activeItem: this.props.activeItem,
            dropdown: []
        };
    }

    DropDownList = () => {
        axios.get("http://localhost:8000/member/api").then(res => this.setState({ dropdown: res.data })).catch(err => console.log(err));
    };

    handleChange = e => {
        let { name, value } = e.target;
        if (e.target.type === "checkbox") {
            value = e.target.checked;
        }
        const activeItem = { ...this.state.activeItem, [name]: value };
        this.setState({ activeItem });
    };

    render() {
        const { toggle, onSave } = this.props;
        return (
            <Modal isOpen={true} toggle={toggle} size="lg" style={{ maxWidth: '1000px', width: '100%' }}>
                <ModalHeader toggle={toggle}> Add Member </ModalHeader>
                <ModalBody>
                    <Form>
                        <FormGroup row className="my-0">
                            <Col xs="4">
                                <Label for="title">Name</Label>
                                <Input
                                    type="text"
                                    name="title"
                                    value={this.state.activeItem.name}
                                    onChange={this.handleChange}
                                    placeholder="Enter Name"
                                />
                            </Col>
                            <Col xs="4">
                                <Label for="description">PM/CM/AM</Label>
                                {/* <CustomListDropDown /> */}
                            </Col>
                            <Col xs="4"><Label for="description">Gender</Label>
                                {/* <CustomListDropDown /> */}
                            </Col>
                        </FormGroup>

                        <FormGroup row className="my-0">
                            <Col xs="2">
                                <Label for="title">Age</Label>
                                <Input
                                    type="text"
                                    name="title"
                                    value={this.state.activeItem.name}
                                    onChange={this.handleChange}
                                    placeholder="Enter Name"
                                />
                            </Col>
                            <Col xs="2">
                                <Label for="description">Period of Joining</Label>
                                {/* <CustomListDropDown /> */}
                            </Col>
                            <Col xs="4"><Label for="description">Category</Label>
                                {/* <CustomListDropDown /> */}
                            </Col>
                            <Col xs="4"><Label for="description">Classes</Label>
                                {/* <CustomListDropDown /> */}
                            </Col>
                        </FormGroup>
                        <FormGroup row className="my-0">
                            <Col xs="4">
                                <Label for="title">Qualification</Label>
                                <Input
                                    type="text"
                                    name="title"
                                    value={this.state.activeItem.name}
                                    onChange={this.handleChange}
                                    placeholder="Enter Name"
                                />
                            </Col>
                            <Col xs="4">
                                <Label for="description">Income</Label>
                                {/* <CustomListDropDown /> */}
                            </Col>
                            <Col xs="4"><Label for="description">Levy Cash</Label>
                                {/* <CustomListDropDown /> */}
                            </Col>
                        </FormGroup>
                    </Form>
                </ModalBody>
                <ModalFooter>
                    <Button color="success" onClick={() => onSave(this.state.activeItem)}>
                        Save
                    </Button>
                </ModalFooter>
            </Modal>
        );
    }
}