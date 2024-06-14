import React from 'react';
import styled, { keyframes } from 'styled-components';

const fadeInUp = keyframes`
  0% {
    opacity: 0;
    transform: translateY(50px);
  }
  100% {
    opacity: 1;
    transform: translateY(0);
  }
`;

const FooterContainer = styled.footer`
  background-color: #08214a;
  color: #bdafa6;
  padding: 2rem;
  animation: ${fadeInUp} 1s ease-in-out;
  box-shadow: 0 -2px 4px rgba(0, 0, 0, 0.1);
  position: relative;
`;

const FooterSection = styled.div`
  margin-bottom: 1rem;
`;

const QuickLinks = styled.ul`
  list-style: none;
  padding: 0;
  margin: 0;
`;

const QuickLink = styled.li`
  margin-bottom: 0.5rem;

  a {
    color: #bdafa6;
    text-decoration: none;
    transition: color 0.3s ease-in-out;

    &:hover {
      color: #96113b;
    }
  }
`;

const Footer = () => {
  return (
    <FooterContainer>
      <div className="container">
        <div className="row">
          <FooterSection className="col-md-4">
            <h3>IT College</h3>
            <p>Learn cutting-edge technologies and advance your career.</p>
          </FooterSection>
          <FooterSection className="col-md-4">
            <h4>Quick Links</h4>
            <QuickLinks>
              <QuickLink>
                <a href="/">Home</a>
              </QuickLink>
              <QuickLink>
                <a href="/about">About</a>
              </QuickLink>
              <QuickLink>
                <a href="/programs">Programs</a>
              </QuickLink>
              <QuickLink>
                <a href="/admissions">Admissions</a>
              </QuickLink>
              <QuickLink>
                <a href="/contact">Contact</a>
              </QuickLink>
            </QuickLinks>
          </FooterSection>
          <FooterSection className="col-md-4">
            <h4>Connect with Us</h4>
            {/* Add social media links or other information */}
          </FooterSection>
        </div>
      </div>
    </FooterContainer>
  );
};

export default Footer;