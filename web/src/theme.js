import { createTheme } from '@mui/material/styles';

const theme = createTheme({
  status: {
    danger: '#e53e3e',
  },
  palette: {
    primary: {
      main: '#FFC0CB',
      darker: '#FFC0CB',
    },
    neutral: {
      main: '#FFC0CB',
      contrastText: '#000000',
    },
  },
});

export default theme;