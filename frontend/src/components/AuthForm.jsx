1. The complete component code with all imports

```jsx
import React, { useState } from 'react';
import PropTypes from 'prop-types';
import './AuthForm.css';

const AuthForm = ({ onLogin, onRegister }) => {
    const [isLogin, setIsLogin] = useState(true);
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');

    const switchModeHandler = () => {
        setIsLogin((prevState) => !prevState);
    };

    const submitHandler = (event) => {
        event.preventDefault();
        if (isLogin) {
            onLogin(username, password);
        } else {
            onRegister(username, password);
        }
    };

    return (
        <div className="auth-form">
            <h1>{isLogin ? 'Login' : 'Register'}</h1>
            <form onSubmit={submitHandler}>
                <input type="text" placeholder="Username" value={username} onChange={(e) => setUsername(e.target.value)} required/>
                <input type="password" placeholder="Password" value={password} onChange={(e) => setPassword(e.target.value)} required/>
                <button type="submit">{isLogin ? 'Login' : 'Register'}</button>
            </form>
            <button onClick={switchModeHandler}>
                Switch to {isLogin ? 'Register' : 'Login'}
            </button>
        </div>
    );
};

export default AuthForm;
```

2. Any necessary CSS/styling

```css
/* AuthForm.css */
.auth-form {
    width: 300px;
    margin: 0 auto;
    padding: 20px;
    box-shadow: 0px 0px 10px 0px rgba(0,0,0,0.1);
}

.auth-form h1 {
    text-align: center;
    margin-bottom: 20px;
}

.auth-form form {
    display: flex;
    flex-direction: column;
}

.auth-form input {
    margin-bottom: 10px;
    padding: 10px;
    border-radius: 5px;
    border: 1px solid #ccc;
}

.auth-form button {
    padding: 10px;
    border: none;
    background-color: #007bff;
    color: white;
    cursor: pointer;
    border-radius: 5px;
}

.auth-form button:hover {
    background-color: #0056b3;
}
```

3. PropTypes

```jsx
AuthForm.propTypes = {
    onLogin: PropTypes.func.isRequired,
    onRegister: PropTypes.func.isRequired
};
```

4. Export statements

```jsx
export default AuthForm;
```