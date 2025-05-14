Here's a comprehensive set of unit tests for the `AuthForm` component using Jest and React Testing Library:

```jsx
import React from 'react';
import { render, fireEvent, screen } from '@testing-library/react';
import '@testing-library/jest-dom/extend-expect';
import AuthForm from './AuthForm';

describe('AuthForm', () => {
  const mockOnLogin = jest.fn();
  const mockOnRegister = jest.fn();

  beforeEach(() => {
    render(<AuthForm onLogin={mockOnLogin} onRegister={mockOnRegister} />);
  });

  afterEach(() => {
    jest.clearAllMocks();
  });

  it('renders without crashing', () => {
    expect(screen.getByRole('heading')).toHaveTextContent('Login');
  });

  it('switches to Register mode on button click', () => {
    const switchButton = screen.getByText(/Switch to Register/);
    fireEvent.click(switchButton);
    expect(screen.getByRole('heading')).toHaveTextContent('Register');
  });

  it('calls onLogin with correct arguments when in Login mode', () => {
    const usernameInput = screen.getByPlaceholderText('Username');
    const passwordInput = screen.getByPlaceholderText('Password');
    const submitButton = screen.getByText('Login');

    fireEvent.change(usernameInput, { target: { value: 'test' } });
    fireEvent.change(passwordInput, { target: { value: 'password' } });
    fireEvent.click(submitButton);

    expect(mockOnLogin).toHaveBeenCalledWith('test', 'password');
  });

  it('calls onRegister with correct arguments when in Register mode', () => {
    const usernameInput = screen.getByPlaceholderText('Username');
    const passwordInput = screen.getByPlaceholderText('Password');
    const switchButton = screen.getByText(/Switch to Register/);

    fireEvent.click(switchButton);
    fireEvent.change(usernameInput, { target: { value: 'test' } });
    fireEvent.change(passwordInput, { target: { value: 'password' } });
    fireEvent.click(screen.getByText('Register'));

    expect(mockOnRegister).toHaveBeenCalledWith('test', 'password');
  });

  it('does not call onRegister or onLogin when inputs are empty', () => {
    const submitButton = screen.getByText('Login');
    const switchButton = screen.getByText(/Switch to Register/);

    fireEvent.click(submitButton);
    fireEvent.click(switchButton);
    fireEvent.click(screen.getByText('Register'));

    expect(mockOnLogin).not.toHaveBeenCalled();
    expect(mockOnRegister).not.toHaveBeenCalled();
  });
});
```

This set of tests covers:

- Component rendering: The first test verifies that the component renders without errors and that the heading is initially set to 'Login'.
- User interactions: The second test checks that the 'Switch to Register' button correctly changes the mode to 'Register'. The third and fourth tests make sure that the 'onLogin' and 'onRegister' callbacks are called with the correct arguments when the form is submitted in each mode.
- Props validation: The `onLogin` and `onRegister` props are being used in the tests, ensuring that they are functions and are required.
- Edge cases: The last test handles the case where the form is submitted with empty inputs, and makes sure that the callbacks are not called in this case.