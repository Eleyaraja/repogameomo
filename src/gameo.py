// TodoItem.tsx
import React from 'react';

interface Todo {
  id: string;
  title: string;
  done: boolean;
}

interface TodoItemProps {
  todo: Todo;
  onToggleDone: (id: string) => void;
  onRemove: (id: string) => void;
}

const TodoItem: React.FC<TodoItemProps> = ({ todo, onToggleDone, onRemove }) => {
  return (
    <li>
      {todo.title}
      <input
        type="checkbox"
        checked={todo.done}
        onChange={() => onToggleDone(todo.id)}
      />
      <button onClick={() => onRemove(todo.id)}>Remove</button>
    </li>
  );
};

export default TodoItem;
