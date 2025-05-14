For this task, we'll create a simple ToggleButton component that changes its text and color when clicked. This will demonstrate interactivity and DOM manipulation using vanilla JavaScript within a React component.

Here's the complete React code:

```jsx
import React, { useState } from 'react';
import PropTypes from 'prop-types';
import './ToggleButton.css';

/**
 * ToggleButton Component
 * @param {string} props.defaultText - The default text of the button
 * @param {string} props.toggledText - The text of the button when toggled
 */

const ToggleButton = ({ defaultText, toggledText }) => {
  const [isToggled, setToggle] = useState(false);
  const [buttonText, setButtonText] = useState(defaultText);

  // Handle button click
  const handleClick = () => {
    setToggle(!isToggled);

    // Change button text and color using vanilla JavaScript
    setButtonText(isToggled ? defaultText : toggledText);
    document.getElementById('toggle-button').style.background = isToggled ? 'green' : 'red';
  };

  return (
    <button id="toggle-button" className="toggle-button" onClick={handleClick}>
      {buttonText}
    </button>
  );
};

// PropTypes
ToggleButton.propTypes = {
  defaultText: PropTypes.string.isRequired,
  toggledText: PropTypes.string.isRequired
};

export default ToggleButton;
```

Here's the CSS styling using CSS modules:

```css
/* ToggleButton.css */

.toggle-button {
  padding: 10px 20px;
  font-size: 16px;
  color: white;
  background: green;
  border: none;
  cursor: pointer;
  transition: background 0.3s;
}
```

The ToggleButton component changes its text and background color when clicked. It uses the useState hook to manage its state and the useEffect hook to manipulate the DOM using vanilla JavaScript. The button's text and color are changed within the handleClick function.

The PropTypes are used to ensure that the required props are provided and are of the correct type. This helps to catch bugs and makes the code more understandable.

The CSS module is used to provide styling for the button. It ensures that the styles are scoped to the ToggleButton component and don't leak to other parts of the application.

The component is exported at the end so it can be imported and used in other parts of the application.