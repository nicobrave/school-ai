/** @type {import('tailwindcss').Config} */
module.exports = {
    content: ['./src/**/*.{js,jsx,ts,tsx,html}'],
    theme: {
      extend: {
        colors: {
          primary: '#264653',           // Azul profesional
          secondary: '#2A9D8F',         // Verde suave
          accent: '#E9C46A',            // Amarillo arena
          background: '#F4F4F4',        // Fondo gris claro
          surface: '#FFFFFF',           // Tarjetas
          'text-primary': '#1A1A1A',    // Texto principal
          'text-secondary': '#555555',  // Texto secundario
        },
        fontFamily: {
          sans: ['Poppins', 'sans-serif'],
        },
        borderRadius: {
          xl: '1rem',
        },
        boxShadow: {
          card: '0 4px 12px rgba(0, 0, 0, 0.1)',
        },
      },
    },
    plugins: [],
  }
  