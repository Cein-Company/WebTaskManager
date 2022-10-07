import '../styles/layout.css';

function Layout() {
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
        <div></div>
        <div></div>
        <div></div>
        <div></div>
      </div>
    </div>
  );
}
export default Layout;
