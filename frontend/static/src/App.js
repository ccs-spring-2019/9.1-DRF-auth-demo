import React, {Component} from 'react';
import axios from 'axios';
import './App.css';

axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.xsrfHeaderName = 'X-CSRFToken';

class App extends Component {

    constructor(props) {
        super(props);

        this.state = {
            todos: []
        }
    }

    componentDidMount() {
        localStorage.getItem('token') ? this.getTodos() : this.login();
    }

    login = () => {
        let user = {}

        user.username = 'admin';
        user.email = 'admin@example.com';
        user.password = 'safepass1';

        axios.post('/api/v1/rest-auth/login/', user)
            .then(response => {
                localStorage.setItem('token', response.data);
            })
            .catch(error => {
                // handle error
                console.log(error);
            })
            .finally( () => {
                // always executed
            });
    }

    getTodos = () => {
        axios.get('/api/v1/', {
            headers: {'Authorization': `Token ${localStorage.getItem('token')}`}
        })
            .then(function (response) {
                // handle success
                console.log(response);
            })
            .catch(function (error) {
                // handle error
                console.log(error);
            })
            .finally(function () {
                // always executed
            });
    }

    render() {
        return <div>I am here</div>
    }
}

export default App;
