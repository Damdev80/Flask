/** @type {import('tailwindcss').Config} */
import animations from '@midudev/tailwind-animations'

module.exports = {
  content: ["./app/templates/*.html"],
  theme: {
    
    extend: {
      colors: {
        morado: '#30243d',
        
      },
    },
  },
  plugins: [animations],
}

