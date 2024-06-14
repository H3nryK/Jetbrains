import React, { useState, useEffect } from 'react';
import { Navbar, Nav } from 'react-bootstrap';
import styled, { keyframes } from 'styled-components';

const fadeIn = keyframes`
  0% { opacity: 0; transform: translateY(-20px); }
  100% { opacity: 1; transform: translateY(0); }
`;

const HeaderContainer = styled.div`
  background-color: #084d9c;
  animation: ${fadeIn} 1s ease-in-out;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  position: sticky;
  top: 0;
  z-index: 1000;
`;

const NavLink = styled(Nav.Link)`
  color: #bdafa6;
  font-weight: bold;
  transition: color 0.3s ease-in-out, transform 0.3s ease-in-out;

  &:hover {
    color: #96113b;
    transform: scale(1.1);
  }
`;

const Header = () => {
  const [isScrolled, setIsScrolled] = useState(false);

  useEffect(() => {
    const handleScroll = () => {
      const scrollTop = window.pageYOffset || document.documentElement.scrollTop;
      setIsScrolled(scrollTop > 0);
    };

    window.addEventListener('scroll', handleScroll);
    return () => window.removeEventListener('scroll', handleScroll);
  }, []);

  return (
    <HeaderContainer style={{ backgroundColor: isScrolled ? '#08214a' : '#084d9c' }}>
      <Navbar bg="dark" variant="dark" expand="lg" className="justify-content-center">
        <Navbar.Brand href="/" className="mr-auto">
          <img src="/logo.png" alt="IT College Logo" height="40" />
        </Navbar.Brand>
        <Navbar.Toggle aria-controls="basic-navbar-nav" />
        <Navbar.Collapse id="basic-navbar-nav">
          <Nav className="ml-auto">
            <NavLink href="/">Home</NavLink>
            <NavLink href="/about">About</NavLink>
            <NavLink href="/programs">Programs</NavLink>
            <NavLink href="/admissions">Admissions</NavLink>
            <NavLink href="/contact">Contact</NavLink>
          </Nav>
        </Navbar.Collapse>
      </Navbar>
    </HeaderContainer>
  );
};

export default Header;