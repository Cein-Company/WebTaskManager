import '../styles/layout.css';
import axios from 'axios';
import { useState } from 'react';

function Layout() {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const onChangeUsernameHandler = (e) => {
    setUsername(e.target.value);
  };
  const onChangePasswordHandler = (e) => {
    setPassword(e.target.value);
  };
  const submitHandler = (e) => {
    e.preventDefault();
    const result = axios.post('http://127.0.0.1:8000/api/login', {
      username: username,
      password: password,
    });
    setUsername('');
    setPassword('');
    console.log(result); //To be completed...
  };

  return (
    <div className="container spacer wave">
      <div className="layout-login__left">
        <div className="layout-login__left__text">
          <p>
            Cein <br /> Task Manager
          </p>
          <span>Don't have an account? Sign up!</span>
        </div>
        <div className="layout-login__left__button">
          <a href="#">Register</a>
        </div>
      </div>
      <div className="layout-login__right">
        <div className="layout-login__right__text">
          <h1>Login</h1>
        </div>
        <div className="layout-login__right__inputs">
          <form onSubmit={submitHandler}>
            <input
              value={username}
              id="username"
              type="text"
              onChange={onChangeUsernameHandler}
              placeholder="Username"
            />
            <input
              value={password}
              id="password"
              type="password"
              onChange={onChangePasswordHandler}
              placeholder="Password"
            />
            <button type="submit">Submit</button>
          </form>
        </div>
        <div className="layout-login__right__forgot">
          <p>
            Forgot your password? <a href="#">Click here</a>
          </p>
        </div>
        <div className="layout-login__right__button"></div>
      </div>
    </div>
  );
}
export default Layout;
