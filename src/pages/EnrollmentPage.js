import React from 'react';
import { Container } from 'react-bootstrap';
import EnrollmentForm from '../components/EnrollmentForm';

const EnrollmentPage = () => {
  return (
    <Container>
      <h1>Enroll Now</h1>
      <EnrollmentForm />
    </Container>
  );
}

export default EnrollmentPage;
