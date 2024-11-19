import { browser } from "$app/environment";
import { writable } from "svelte/store";

type theme = 'dark' | 'light'

const THEME = 'theme'

const get_initial_theme = (): theme => {
  const os_default: theme = matchMedia("(prefers-color-scheme: dark)").matches
    ? "dark" : "light";
  return localStorage.getItem(THEME) as theme ?? os_default
}

const createThemeStore = () => {
  const { subscribe, update } = writable<theme>(browser ? get_initial_theme() : "light")

  subscribe((theme: theme) => {
    if (browser && theme) {
      localStorage.setItem(THEME, theme)
      document.documentElement.dataset.theme = theme
    }
  })

  const toggle = () => update(t => t == 'light' ? 'dark' : 'light')

  return {
    subscribe,
    toggle,
  }
}

export const theme = createThemeStore()
