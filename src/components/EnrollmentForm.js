import React, { useState } from 'react';
import { Form, Button } from 'react-bootstrap';

const EnrollmentForm = () => {
  const [formData, setFormData] = useState({ name: '', email: '', course: '' });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    // Handle form submission
    console.log(formData);
  };

  return (
    <Form onSubmit={handleSubmit}>
      <Form.Group controlId="formName">
        <Form.Label>Name</Form.Label>
        <Form.Control
          type="text"
          name="name"
          value={formData.name}
          onChange={handleChange}
          placeholder="Enter your name"
          required
        />
      </Form.Group>
      <Form.Group controlId="formEmail">
        <Form.Label>Email</Form.Label>
        <Form.Control
          type="email"
          name="email"
          value={formData.email}
          onChange={handleChange}
          placeholder="Enter your email"
          required
        />
      </Form.Group>
      <Form.Group controlId="formCourse">
        <Form.Label>Course</Form.Label>
        <Form.Control
          type="text"
          name="course"
          value={formData.course}
          onChange={handleChange}
          placeholder="Enter the course you want to enroll in"
          required
        />
      </Form.Group>
      <Button variant="primary" type="submit">Enroll</Button>
    </Form>
  );
}

export default EnrollmentForm;
