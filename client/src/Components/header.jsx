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
                <Nav.Link href="/">Home</Nav.Link>
                <Nav.Link href="/meal">Meals</Nav.Link>
                <Nav.Link href="/recipe">Recipes</Nav.Link>
          </Nav>
        </Container>
      </Navbar>
    </>
  );
}

export default Header;