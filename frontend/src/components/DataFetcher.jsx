Here is a simple React component that fetches data from a backend API using the Fetch API and async/await. 

```jsx
import React, { useState, useEffect } from 'react';
import PropTypes from 'prop-types';

/**
 * DataFetcher is a react component that fetches data from a given URL
 * @param {string} url The URL to fetch data from
 * @returns {object} JSX Element
 */
const DataFetcher = ({ url }) => {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  /**
   * Fetch data from API
   */
  const fetchData = async () => {
    setLoading(true);
    try {
      const response = await fetch(url);
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
      const data = await response.json();
      setData(data);
    } catch (error) {
      setError(error);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchData();
  }, [url]);

  if (loading) return <div>Loading...</div>;
  if (error) return <div>Error: {error.message}</div>;

  return (
    <div>
      <pre>{JSON.stringify(data, null, 2)}</pre>
    </div>
  );
};

DataFetcher.propTypes = {
  url: PropTypes.string.isRequired,
};

export default DataFetcher;
```

This component accepts a `url` prop, which it uses to fetch data from. It maintains three pieces of state: `data` (the data it fetched), `loading` (a boolean indicating whether it's currently fetching data), and `error` (any errors that occurred while fetching data).

When the component mounts (and whenever the `url` prop changes), it fetches data from the given URL. It sets `loading` to true before it starts fetching, and sets it to false when it's done. If an error occurs while fetching data, it sets `error` to that error.

If `loading` is true, the component renders a "Loading..." message. If `error` is not null, it renders an error message. Otherwise, it renders the fetched data as a JSON string. 

Regarding CSS/styling, you can easily add your own styling by replacing the `<div>` tags with your own styled components or CSS classes.

Finally, this component uses PropTypes to enforce that the `url` prop is a string and is required.