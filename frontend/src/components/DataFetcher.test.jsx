Here's how you can write tests for the DataFetcher component:

```jsx
import React from 'react';
import { render, waitFor, screen } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import '@testing-library/jest-dom/extend-expect';
import DataFetcher from './DataFetcher';

jest.mock('node-fetch', () => require('fetch-mock-jest').sandbox());
const fetch = require('node-fetch');

describe('DataFetcher', () => {
  beforeEach(() => {
    fetch.reset();
  });

  it('renders without crashing', () => {
    render(<DataFetcher url="https://fakeapi.com/data" />);
  });

  it('displays loading state initially', () => {
    render(<DataFetcher url="https://fakeapi.com/data" />);
    expect(screen.getByText('Loading...')).toBeInTheDocument();
  });

  it('displays data after successful fetch', async () => {
    const mockData = { data: 'test' };
    fetch.mock('https://fakeapi.com/data', mockData);

    render(<DataFetcher url="https://fakeapi.com/data" />);
    
    await waitFor(() => expect(screen.getByText(JSON.stringify(mockData, null, 2))).toBeInTheDocument());
  });

  it('displays error message after failed fetch', async () => {
    const error = new Error('Failed to fetch');
    fetch.mock('https://fakeapi.com/data', { throws: error });

    render(<DataFetcher url="https://fakeapi.com/data" />);
    
    await waitFor(() => expect(screen.getByText(`Error: ${error.message}`)).toBeInTheDocument());
  });

  it('refetches data when url prop changes', async () => {
    const mockData1 = { data: 'test 1' };
    const mockData2 = { data: 'test 2' };
    fetch.mock('https://fakeapi.com/data1', mockData1);
    fetch.mock('https://fakeapi.com/data2', mockData2);

    const { rerender } = render(<DataFetcher url="https://fakeapi.com/data1" />);
    await waitFor(() => expect(screen.getByText(JSON.stringify(mockData1, null, 2))).toBeInTheDocument());

    rerender(<DataFetcher url="https://fakeapi.com/data2" />);
    await waitFor(() => expect(screen.getByText(JSON.stringify(mockData2, null, 2))).toBeInTheDocument());
  });
});
```

This test suite includes the following tests:
- A test to make sure the component renders without crashing.
- A test to check that the component displays a "Loading..." message initially.
- A test to check that the component displays the fetched data after a successful fetch.
- A test to check that the component displays an error message after a failed fetch.
- A test to check that the component refetches data when the `url` prop changes.

Note: This test suite uses fetch-mock to mock the Fetch API and control its behavior. This allows us to simulate different scenarios, such as a successful fetch, a failed fetch, and a fetch that returns different data when called with different arguments.