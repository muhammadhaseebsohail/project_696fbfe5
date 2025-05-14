Here is how you can write tests for the Layout component:

```jsx
import React from 'react';
import { render, screen } from '@testing-library/react';
import Layout from './Layout'; // assuming the component is exported from Layout.js

describe('Layout component', () => {
  it('renders correctly', () => {
    render(<Layout><p>Test Child</p></Layout>);
    
    expect(screen.getByText('My App')).toBeInTheDocument();
    expect(screen.getByText('Test Child')).toBeInTheDocument();
    expect(screen.getByText('© 2022 My App')).toBeInTheDocument();
  });
  
  it('renders children correctly', () => {
    const { container } = render(<Layout><p>Test Child</p></Layout>);
    
    expect(container.querySelector('main').textContent).toBe('Test Child');
  });

  it('throws error when no children are provided', () => {
    console.error = jest.fn(); // silence prop-types error in console
    expect(() => render(<Layout />)).toThrowError();
    expect(console.error).toHaveBeenCalled(); // check if prop-types logged an error
  });
});
```

This test suite includes the following tests:

1. **Component rendering**: This test ensures that the component renders without crashing and that it renders the expected static text ('My App' and '© 2022 My App').
2. **Props validation**: This test ensures that the `children` prop is validated correctly and that an error is thrown when no children are provided.
3. **Rendering children**: This test checks that the `children` prop is used correctly and that the child elements are rendered within the main tag.

Note: The 'User interactions' and 'Edge cases' tests are not applicable for this component as it does not handle any user interaction or have any edge cases based on the given implementation. The component is a simple layout component and does not have any click or change handlers, nor does it have any conditional rendering or other complex logic.