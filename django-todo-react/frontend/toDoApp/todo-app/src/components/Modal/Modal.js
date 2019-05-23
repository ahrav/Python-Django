import React, { useContext } from "react"
import TodoContext from '../../todo-context'
import {
  Button,
  Modal,
  ModalHeader,
  ModalBody,
  ModalFooter,
  Form,
  FormGroup,
  Input,
  Label
} from "reactstrap";

const CustomModal = props => {
  const todo = useContext(TodoContext)

  const item = {
    title: todo.title,
    description: todo.description,
    completed: todo.completed,
    todoId: todo.todoId
  }

    return (
      <Modal isOpen={true} toggle={todo.toggle}>
        <ModalHeader toggle={todo.toggle}> Todo Item </ModalHeader>
        <ModalBody>
          <Form>
            <FormGroup>
              <Label for="title">Title</Label>
              <Input
                type="text"
                name="title"
                value={todo.title}
                onChange={e => todo.setTitle(e.target.value)}
                placeholder="Enter Todo Title"
              />
            </FormGroup>
            <FormGroup>
              <Label for="description">Description</Label>
              <Input
                type="text"
                name="description"
                value={todo.description}
                onChange={e => todo.setDescription(e.target.value)}
                placeholder="Enter Todo description"
              />
            </FormGroup>
            <FormGroup check>
              <Label for="completed">
                <Input
                  type="checkbox"
                  name="completed"
                  checked={todo.completed}
                  onChange={(e) => todo.setCompleted.bind(this, e.target.value)}
                />
                Completed
              </Label>
            </FormGroup>
          </Form>
        </ModalBody>
        <ModalFooter>
          <Button color="success" onClick={() => todo.onSave({item})}>
            Save
          </Button>
        </ModalFooter>
      </Modal>
    );
}
export default CustomModal
