import React, { useState } from 'react'
import PropTypes from 'prop-types'

const  SignupForm = props => {
    const [username, setUsername] = useState('')
    const [password, setPassword] = useState('')

    return (
      <form onSubmit={e => props.handleSignup(e, {username: username, password: password})}>
        <h4>Sign Up</h4>
        <label htmlFor="username">Username</label>
        <input
          type="text"
          name="username"
          value={username}
          onChange={e => setUsername(e.target.value)}
        />
        <label htmlFor="password">Password</label>
        <input
          type="password"
          name="password"
          value={password}
          onChange={e => setPassword(e.target.value)}
        />
        <input type="submit" />
      </form>
    );
}

export default SignupForm

SignupForm.propTypes = {
  handleSignup: PropTypes.func.isRequired
};