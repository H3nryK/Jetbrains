import React from 'react';
import { Container, Row, Col } from 'react-bootstrap';

const HomePage = () => {
  return (
    <Container className="mt-5">
      <Row className="align-items-center">
        <Col>
          <h1>Welcome to Our College</h1>
          <p>We offer a variety of IT courses and foreign languages to help you excel in your career.</p>
        </Col>
      </Row>
    </Container>
  );
}

export default HomePage;
