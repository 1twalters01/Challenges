// Build a counter which increments on the click of a button using REact 16. The component should be the default export (use export default).

// 1. Create a counter
// Wrap the current counter value in a h2 element.
// Add "counter" class to the h2 element.
// Initial value of counter is set to 42.

// 2. Create a button element
// The content of the button should be "Click".
// It should have a "counter-button" class.

// 3. Users can increment the counter
// Increment the counter by 1 when user clicks the button

// Make it a class based and not function based

import React from 'react';

class Counter extends React.Component {
  constructor(props) {
    super(props);

    this.state = {
      counter: 42,
    };

    this.handleClick = this.handleClick.bind(this);
  }

  handleClick() {
    this.setState((prevState) => ({
      counter: prevState.counter + 1,
    }));
  }

  render() {
    return (
      <div>
        <h2 className="counter">{this.state.counter}</h2>
        <button className="counter-button" onClick={this.handleClick}>
          Click
        </button>
      </div>
    );
  }
}

export default Counter;