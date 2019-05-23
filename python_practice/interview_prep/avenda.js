/*
Implement a "ButtonGroup" component that wraps any number of "Button" components
and ensures that only 1 "Button" can be active at a time.
*/

class App extends React.Component {

    render() {
        
        return (
          <ButtonGroup />
        )

    }
}

class ButtonGroup extends React.Component {

    render() {

        return (
          <Button>Button1</Button>
          <Button>Button1</Button>
        )

    }
}

class Button extends React.Component {

    render() {

        return (
          <button>{this.children}</button>
        )
        
    }
}
