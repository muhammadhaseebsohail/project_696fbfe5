Sure, here is an example of how we could write unit tests for the Task component:

```jsx
import React from 'react';
import { render, cleanup, fireEvent } from '@testing-library/react';
import '@testing-library/jest-dom/extend-expect';
import Task from './Task';

afterEach(cleanup);

it('renders without crashing', () => {
  const { getByText } = render(<Task taskName="Test Task" requirements={["Requirement 1", "Requirement 2"]} />);
  expect(getByText('Test Task')).toBeInTheDocument();
});

it('renders all requirements', () => {
  const { getByText } = render(<Task taskName="Test Task" requirements={["Requirement 1", "Requirement 2"]} />);
  expect(getByText('Requirement 1')).toBeInTheDocument();
  expect(getByText('Requirement 2')).toBeInTheDocument();
});

it('does not render non-existing requirement', () => {
  const { queryByText } = render(<Task taskName="Test Task" requirements={["Requirement 1", "Requirement 2"]} />);
  expect(queryByText('Requirement 3')).toBeNull();
});

it('fails to render without required props', () => {
  console.error = jest.fn();
  render(<Task />);
  expect(console.error).toBeCalled();
});
```

Here is what each test does:

1. "renders without crashing": This test checks if the component can render without throwing an error when provided with the required props.

2. "renders all requirements": This test checks if all the requirements passed in the props are rendered.

3. "does not render non-existing requirement": This test checks if a requirement that was not passed in the props is not rendered.

4. "fails to render without required props": This test checks if an error is logged in the console when the component is rendered without the required props. This is a way to test PropTypes validation.

Note: It is recommended to mock the console.error function in the "fails to render without required props" test to prevent the error from actually logging in the console during testing.