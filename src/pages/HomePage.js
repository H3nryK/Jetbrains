import React, { useState } from 'react';
import { Container, Row, Col, Button, Card, Form } from 'react-bootstrap';
import { useSpring, animated } from '@react-spring/web';
import '../styles/App.css';

const courses = [
  { id: 1, title: 'Introduction to Programming', description: 'Learn the basics of programming.' },
  { id: 2, title: 'Web Development', description: 'Build modern web applications.' },
  { id: 3, title: 'Data Science', description: 'Analyze and visualize data.' },
  { id: 4, title: 'Spanish Language', description: 'Learn to speak and write in Spanish.' },
  { id: 5, title: 'French Language', description: 'Master the French language.' }
];

const HomePage = () => {
  const fade = useSpring({ from: { opacity: 0 }, to: { opacity: 1 }, config: { duration: 1000 } });
  const [searchTerm, setSearchTerm] = useState('');

  const handleSearch = (e) => {
    setSearchTerm(e.target.value);
  };

  const filteredCourses = courses.filter(course => 
    course.title.toLowerCase().includes(searchTerm.toLowerCase())
  );

  return (
    <animated.div style={fade}>
      <Container className="mt-5 text-center position-relative">
        <Row className="align-items-center mb-5">
          <Col>
            <h1 className="display-4 font-weight-bold">Welcome to Our College</h1>
            <p className="lead">We offer a variety of IT courses and foreign languages to help you excel in your career.</p>
            <Button variant="primary" size="lg" href="/courses" className="mt-3">Explore Courses</Button>
          </Col>
        </Row>
        <Row className="mt-5">
          <Col>
            <h2 className="mb-4">Popular Courses</h2>
            <Form.Control
              type="text"
              placeholder="Search for a course..."
              value={searchTerm}
              onChange={handleSearch}
              className="mb-4 p-3"
            />
          </Col>
        </Row>
        <Row>
          {filteredCourses.map(course => (
            <Col md={4} className="mb-4" key={course.id}>
              <Card className="h-100 shadow-sm border-0">
                <Card.Body>
                  <Card.Title>{course.title}</Card.Title>
                  <Card.Text>{course.description}</Card.Text>
                  <Button variant="outline-primary" href={`/courses/${course.id}`}>Learn More</Button>
                </Card.Body>
              </Card>
            </Col>
          ))}
        </Row>
      </Container>
    </animated.div>
  );
}

export default HomePage;
