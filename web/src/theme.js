import { createTheme } from '@mui/material/styles';

const theme = createTheme({
  status: {
    danger: '#e53e3e',
  },
  palette: {
    primary: {
      main: '#FFFFFF',
      darker: '#000000',
    },
    neutral: {
      main: '#ffffff',
      contrastText: '#ffffff',
    },
  },
});

export default theme;