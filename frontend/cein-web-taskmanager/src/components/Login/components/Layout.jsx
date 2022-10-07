import '../styles/layout.css';

function Layout() {
  const submitHandler = (e) => {
    e.preventDefault();
  };

  return (
    <div className="container spacer wave">
      <div className="layout-login__left">
        <div className="layout-login__left__text">
          <p>
            CEIN <br /> Task Manager
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
            <input id="username" type="text" placeholder="Username" />
            <input id="password" type="password" placeholder="Password" />
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
