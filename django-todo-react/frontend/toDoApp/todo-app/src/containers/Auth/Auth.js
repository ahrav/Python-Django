import React, { useState, useEffect } from 'react'
import Nav from '../../components/Nav/Nav'
import axios from 'axios'
import LoginForm from '../../components/LoginForm/LoginForm'
import SignupForm from '../../components/SignUpForm/SignUpForm'
import '../../App.css'

const Auth = props => {
  const [displayedForm, setDisplayedForm] = useState('')
  const [loggedIn, setLoggedIn] = useState(window.localStorage.getItem('token') ? true : false)
  const [username, setUsername] = useState('')

  useEffect(() => {
    const token = localStorage.getItem('token')
    if (loggedIn){
      const api = 'http://localhost:8000/todo/current_user/'
      axios.get(api, { headers: {Authorization: `JWT ${token}` }})
        .then(res => setUsername(res.data.username))
        .catch(err => console.log(err))
    }
  }, [])

  const handleLogin = (e, data) => {
    e.preventDefault();
    axios.post('http://localhost:8000/token-auth/', data)
      .then(res => {
        console.log(res)
        localStorage.setItem('token', res.data.token)
        setLoggedIn(true)
        setUsername(res.data.user.username)
        setDisplayedForm('')
      })
      .catch(err => console.log(err))
    }

  const handleSignup = (e, data) => {
    e.preventDefault();
    axios.post('http://localhost:8000/todo/users/', data)
      .then(res => {
        localStorage.setItem('token', res.data.token)
        setLoggedIn(true)
        setDisplayedForm('')
        setUsername(res.data.username)
      })
  }

  const handleLogout = () => {
    localStorage.removeItem('token');
    setLoggedIn(false)
    setUsername('')
  }

  const displayForm = form => {
    setDisplayedForm(form)
  }

  let form;
  switch (displayedForm) {
    case 'login':
      form = <LoginForm handleLogin={handleLogin} />;
      break;
    case 'signup':
      form = <SignupForm handleSignup={handleSignup} />;
      break;
    default:
      form = null;
  }

    return (
      <div className="App">
        <Nav
          loggedIn={loggedIn}
          displayForm={displayForm}
          handleLogout={handleLogout}
        />
        {form}
        <h3>
          {loggedIn
            ? `Hello, ${username}`
            : 'Please Log In'}
        </h3>
      </div>
    );
}

export default Auth