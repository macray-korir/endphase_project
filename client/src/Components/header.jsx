import React from 'react';
import Container from 'react-bootstrap/Container';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';


function Header() {
  return (
    <>
      <Navbar id="nav">
        <Container>
          <Navbar.Brand href="" style={{ color: 'white' }}>
            MealBox
          </Navbar.Brand>
            <Nav className="me-auto" >
                <Nav.Link href="/homepage">Home</Nav.Link>
                <Nav.Link href="/signin">SignIn</Nav.Link>
                <Nav.Link href="/Contact">Contact Us</Nav.Link>
                {/* <Nav.Link href="/ingredient">Ingredients</Nav.Link> */}
          </Nav>
        </Container>
      </Navbar>
    </>
  );
}

export default Header;