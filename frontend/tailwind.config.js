import daisyui from 'daisyui';
import themes from 'daisyui/src/theming/themes'
import typography from '@tailwindcss/typography'
import { iconsPlugin, getIconCollections } from '@egoist/tailwindcss-icons';
/** @type {import('tailwindcss').Config} */
export default {
  content: ['./src/**/*.{html,js,svelte,ts}'],
  theme: {
    extend: {

      gridRow: {
        'span-15': 'span 15 / span 15',

      }
    }
  },
  darkMode: ['selector', '[data-theme="dark"]'],
  plugins: [typography, daisyui, iconsPlugin({ collections: getIconCollections(["material-symbols"]) })],
  daisyui: {
    themes: [
      {
        'dark': {
          ...themes['dark'],
          "neutral": "#313131",
          "base-100": "#242424",
          "base-200": "#262626",
          "base-300": "#2A2A2A",

        },



      },
      {
        'light': {
          ...themes['light'],
          "neutral": "white",

        },
      },

    ]

  }
};
