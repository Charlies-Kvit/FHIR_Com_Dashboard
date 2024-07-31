import { browser } from "$app/environment";

const THEME = "theme";
export type theme = "light" | "dark";

function initial_theme(): theme {
  return localStorage.getItem(THEME) as theme ??
    (window.matchMedia("(prefers-color-scheme: dark)").matches
      ? "dark" : "light") as theme
}
let _theme = $state()

export const init_theme = () => set_theme(initial_theme())

const set_theme = (value: theme) => {
  document.documentElement.dataset.theme = value;
  localStorage.setItem(THEME, value);
  _theme = value;
};

export const theme = {
  get value() { return _theme },
  toggle: () => set_theme(_theme == "light" ? "dark" : "light")
}

export type Person = { avatar_url: string, name: string, email: string, group_id: number, id?: number }
export type Dashboard = { name: string, id?: number }

let _dashboards: Dashboard[] = $state([])
export const dashboards = {
  get value() { return _dashboards },
  load: async () => {
    _dashboards = (await (await fetch('/api/groups')).json()).groups
  },
  add: function(dashboard: Dashboard) {
    fetch("/api/groups", {
      method: "POST",
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ group_name: dashboard.name })
    }).then(res => {
      this.load()
      console.log("Request complete! response:", res);
    });
  },
  update: function(dashboard_old: Dashboard, dashboard_new: Dashboard) {
    fetch("/api/groups/" + dashboard_old.id, {
      method: "PUT",
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ group_name: dashboard_new.name })
    }).then(res => {
      console.log("Request complete! response:", res);
      this.load()
    });
  },
  delete: function(dashboard: Dashboard) {
    if (_selected_dashboard == dashboard) _selected_dashboard = null
    fetch("/api/groups/" + dashboard.id, {
      method: "DELETE",
    }).then(res => {
      this.load()
      console.log("Request complete! response:", res);
    });
  }
}

let _selected_dashboard: Dashboard | null = $state(null)
export const selected_dashboard = {
  get value() { return _selected_dashboard },
  select: (dashboard: Dashboard) => { _selected_dashboard = dashboard }
}

let _persons: Person[] = $state([])
export const persons = {
  get value() { return _persons },
  for_dashboard: (id: number) => { return _persons.filter(p => p.group_id == id) },
  load: async () => {
    _persons = (await (await fetch('/api/users')).json()).users
  },
  add: function(person: Person) {
    fetch("/api/users", {
      method: "POST",
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(person)
    }).then(res => {
      console.log("Request complete! response:", res);
      this.load()
    });
  },
  update: function(person_old: Person, person_new: Person) {
    fetch("/api/users/" + person_old.id, {
      method: "PUT",
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(person_new)
    }).then(res => {
      console.log("Request complete! response:", res);
      this.load()
    });
  },
  delete: function(person: Person) {
    fetch("/api/users/" + person.id, {
      method: "DELETE",
    }).then(res => {
      console.log("Request complete! response:", res);
      this.load()
    });
  }


}

export async function initialize_store() {
  _persons = (await (await fetch('/api/users')).json()).users
  _dashboards = (await (await fetch('/api/groups')).json()).groups
  _selected_dashboard = _dashboards.length ? _dashboards[0] : null
}
