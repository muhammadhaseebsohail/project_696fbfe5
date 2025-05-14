Here's an example of how you could build this component using React, PropTypes, and CSS modules. 

1. The complete component code with all imports:

```jsx
import React from 'react';
import PropTypes from 'prop-types';
import styles from './Task.module.css';

/**
 * Task Component
 * @param {string} taskName - The title of the task.
 * @param {Array<string>} requirements - The requirements of the task.
 */
function Task({ taskName, requirements }) {
  return (
    <div className={styles.task}>
      <h1>{taskName}</h1>
      <ul>
        {requirements.map((requirement, index) => (
          <li key={index}>{requirement}</li>
        ))}
      </ul>
    </div>
  );
}

export default Task;
```

2. Any necessary CSS/styling:

```css
/* Task.module.css */
.task {
  border: 1px solid #ccc;
  padding: 20px;
  margin-bottom: 20px;
}

.task h1 {
  font-size: 20px;
  margin-bottom: 10px;
}
```

3. PropTypes or TypeScript interfaces:

```jsx
Task.propTypes = {
  taskName: PropTypes.string.isRequired,
  requirements: PropTypes.arrayOf(PropTypes.string).isRequired,
};
```

4. Export statements:

```jsx
export default Task;
```

This `Task` component takes in a `taskName` and an array of `requirements` as props. It then displays the task name as a heading and the requirements as a list. The `Task` component is styled using CSS modules, which allows for scoped CSS and avoids naming conflicts.