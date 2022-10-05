import { Paper, Stack } from '@mui/material';
import { Box, Container } from '@mui/system';
import { styled } from '@mui/material/styles';
import React from 'react';

function Login() {
  const Wrapper = styled(Paper)(({ theme }) => ({
    backgroundColor: theme.palette.mode === 'dark' ? '#1A2027' : '#fff',
    ...theme.typography.body2,
    padding: theme.spacing(1),
    textAlign: 'center',
    color: theme.palette.text.secondary,
  }));

  return (
    <Stack direction={{ xs: 'column', sm: 'row' }}>
      <Container
        maxWidth="sm"
        sx={{ height: '100vh', backgroundColor: '#21F44A' }}
      >
        hello
      </Container>
      <Container
        maxWidth="sm"
        sx={{ height: '100vh', backgroundColor: '#21F44A' }}
      >
        hello
      </Container>
    </Stack>
  );
}

export default Login;
