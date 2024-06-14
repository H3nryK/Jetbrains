import React from 'react';
import { Container } from 'react-bootstrap';
import ContactForm from '../components/ContactForm';

const ContactPage = () => {
  return (
    <Container>
      <h1>Contact Us</h1>
      <ContactForm />
    </Container>
  );
}

export default ContactPage;
